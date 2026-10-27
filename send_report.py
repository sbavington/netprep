#!/usr/bin/env python3
"""Daily NetPrep campaign progress report — run via cron at 8:00 ET"""

import os, sys, sqlite3, csv, io, smtplib
from datetime import datetime, date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

load_dotenv()

DB = os.path.join(os.path.dirname(__file__), 'netprep.db')
SES_SMTP_HOST = os.environ.get('SES_SMTP_HOST', '')
SES_SMTP_PORT = int(os.environ.get('SES_SMTP_PORT', 587))
SES_SMTP_USER = os.environ.get('SES_SMTP_USER', '')
SES_SMTP_PASS = os.environ.get('SES_SMTP_PASS', '')
FROM_EMAIL    = os.environ.get('FROM_EMAIL', 'noreply@netprep.org')

COURSES = {
    'network':      {'abbr': 'TCP', 'title': 'TCP/IP Networking'},
    'tippingpoint': {'abbr': 'TIP', 'title': 'TippingPoint IPS'},
    'ddi':          {'abbr': 'DDI', 'title': 'Deep Discovery Inspector'},
}
COURSE_ORDER = ['ddi', 'network', 'tippingpoint']

def get_db():
    db = sqlite3.connect(DB)
    db.row_factory = sqlite3.Row
    return db

def course_total(db, course_id):
    rows = db.execute('SELECT COUNT(*) FROM progress WHERE course_id=?', (course_id,)).fetchone()
    # Use fixed totals matching app.py
    totals = {'network': 38, 'tippingpoint': 38, 'ddi': 39}
    return totals.get(course_id, 0)

COURSE_TOTALS = {'network': 38, 'tippingpoint': 38, 'ddi': 39}

def build_report(campaign_id=None):
    db = get_db()
    today = date.today().isoformat()

    if campaign_id:
        campaigns = db.execute('SELECT * FROM campaigns WHERE id=?', (campaign_id,)).fetchall()
    else:
        campaigns = db.execute(
            'SELECT * FROM campaigns WHERE start_date <= ? AND end_date >= ?', (today, today)
        ).fetchall()

    if not campaigns:
        print('No active campaigns today.')
        return

    for campaign in campaigns:
        print(f'Processing campaign: {campaign["name"]}')

        # Get students in this campaign
        student_rows = db.execute('''
            SELECT u.id, u.name, u.email, u.activated_at, u.invite_token, u.password_hash, u.created_at
            FROM users u
            JOIN campaign_students cs ON cs.user_id = u.id
            WHERE cs.campaign_id = ? AND u.is_admin = 0
            ORDER BY u.name
        ''', (campaign['id'],)).fetchall()

        students = []
        total_possible = sum(COURSE_TOTALS.values())

        for u in student_rows:
            if u['activated_at']:
                status = 'ACTIVE'
            elif u['invite_token']:
                status = 'INVITE PENDING'
            elif not u['password_hash'] and not u['invite_token']:
                status = 'LEFT PLATFORM'
            else:
                status = 'PENDING'

            course_data = {}
            total_done = 0
            for cid in COURSE_ORDER:
                done = db.execute(
                    'SELECT COUNT(*) FROM progress WHERE user_id=? AND course_id=?',
                    (u['id'], cid)
                ).fetchone()[0]
                tot = COURSE_TOTALS[cid]
                pct = min(int(done / tot * 100), 100) if tot else 0
                exam = db.execute(
                    'SELECT score, total, passed, completed_at FROM exam_attempts WHERE user_id=? AND course_id=? ORDER BY completed_at DESC LIMIT 1',
                    (u['id'], cid)).fetchone()
                best = db.execute(
                    'SELECT MAX(score) FROM exam_attempts WHERE user_id=? AND course_id=? AND passed=1',
                    (u['id'], cid)).fetchone()[0]
                attempts = db.execute(
                    'SELECT COUNT(*) FROM exam_attempts WHERE user_id=? AND course_id=?',
                    (u['id'], cid)).fetchone()[0]
                course_data[cid] = {
                    'done': done, 'total': tot, 'pct': pct,
                    'exam_passed': bool(exam and exam['passed']),
                    'exam_score': exam['score'] if exam else None,
                    'exam_total': exam['total'] if exam else None,
                    'exam_best': best,
                    'exam_attempts': attempts,
                    'exam_date': (exam['completed_at'] or '')[:10] if exam else None,
                }
                total_done += done

            overall_pct = min(int(total_done / total_possible * 100), 100) if total_possible else 0
            exams_passed = sum(1 for cid in COURSE_ORDER if course_data[cid]['exam_passed'])
            students.append({
                'id': u['id'], 'name': u['name'], 'email': u['email'],
                'status': status, 'enrolled': (u['created_at'] or '')[:10],
                'courses': course_data,
                'total_done': total_done, 'total_possible': total_possible,
                'overall_pct': overall_pct,
                'exams_passed': exams_passed,
            })

        # Sort by overall progress desc
        students.sort(key=lambda s: s['overall_pct'], reverse=True)
        for i, s in enumerate(students):
            s['rank'] = i + 1

        active_count = sum(1 for s in students if s['status'] == 'ACTIVE')
        pending_count = sum(1 for s in students if s['status'] == 'INVITE PENDING')
        left_count = sum(1 for s in students if s['status'] == 'LEFT PLATFORM')
        all_exams_passed = sum(1 for s in students if s['exams_passed'] == 3)

        now_str = datetime.now().strftime('%Y-%m-%d')
        html = build_html(campaign, students, active_count, pending_count, left_count, all_exams_passed, now_str)
        csv_data = build_csv(students)

        recipients = [e.strip() for e in campaign['report_emails'].split(',') if e.strip()]
        if not recipients:
            print(f'  No recipients for campaign {campaign["name"]} — skipping email.')
            continue

        send_report_email(campaign['name'], recipients, html, csv_data, now_str)

def color_for_pct(pct):
    if pct == 100: return '#00c853'
    if pct >= 50:  return '#ffaa00'
    if pct > 0:    return '#ff6b00'
    return '#666666'

def build_html(campaign, students, active, pending, left, all_passed, date_str):
    total = len(students)
    rows_html = ''
    for s in students:
        status_color = {'ACTIVE': '#00c853', 'INVITE PENDING': '#ffaa00', 'LEFT PLATFORM': '#f87171'}.get(s['status'], '#666666')
        course_cells = ''
        for cid in COURSE_ORDER:
            cd = s['courses'][cid]
            c = color_for_pct(cd['pct'])
            if cd['exam_passed']:
                exam_badge = f'<br><span style="display:inline-block;background-color:#00c853;color:#000;font-weight:bold;font-size:10px;padding:2px 6px;border-radius:8px;margin-top:3px;">&#10003; PASSED {cd["exam_score"]}/{cd["exam_total"]}</span>'
            elif cd['exam_attempts'] > 0:
                exam_badge = f'<br><span style="display:inline-block;background-color:#ff6b00;color:#fff;font-weight:bold;font-size:10px;padding:2px 6px;border-radius:8px;margin-top:3px;">&#10007; {cd["exam_attempts"]} attempt{"s" if cd["exam_attempts"]!=1 else ""}</span>'
            else:
                exam_badge = '<br><span style="display:inline-block;background-color:#1b2a3d;color:#666;font-size:10px;padding:2px 6px;border-radius:8px;margin-top:3px;">No exam yet</span>'
            course_cells += f'<td align="center" style="padding:8px 6px;border-bottom:1px solid #1b2a3d;"><span style="display:inline-block;background-color:{c};color:#0d1b2a;font-weight:bold;font-size:12px;padding:3px 8px;border-radius:10px;font-family:Arial,Helvetica,sans-serif;">{cd["pct"]}% &nbsp;{cd["done"]}/{cd["total"]}</span>{exam_badge}</td>'

        bar_w = s['overall_pct']
        bar_color = color_for_pct(bar_w)
        rows_html += f'''<tr>
<td align="center" style="padding:8px 6px;border-bottom:1px solid #1b2a3d;color:#9fb3c8;font-size:13px;font-family:Arial,Helvetica,sans-serif;">{s["rank"]}</td>
<td style="padding:8px 10px;border-bottom:1px solid #1b2a3d;color:#ffffff;font-size:13px;font-weight:bold;font-family:Arial,Helvetica,sans-serif;white-space:nowrap;">{s["name"]}</td>
<td style="padding:8px 10px;border-bottom:1px solid #1b2a3d;color:#9fb3c8;font-size:12px;font-family:Arial,Helvetica,sans-serif;">{s["email"]}</td>
<td align="center" style="padding:8px 6px;border-bottom:1px solid #1b2a3d;"><span style="display:inline-block;background-color:{status_color};color:#0d1b2a;font-weight:bold;font-size:11px;padding:3px 8px;border-radius:10px;font-family:Arial,Helvetica,sans-serif;white-space:nowrap;">{s["status"]}</span></td>
{course_cells}
<td style="padding:8px 10px;border-bottom:1px solid #1b2a3d;min-width:130px;">
<table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;border-radius:7px;overflow:hidden;background-color:#1b2a3d;"><tr><td width="{bar_w}%" style="background-color:{bar_color};height:14px;line-height:14px;font-size:1px;">&nbsp;</td><td width="{100-bar_w}%" style="background-color:#1b2a3d;height:14px;">&nbsp;</td></tr></table>
<div style="color:#9fb3c8;font-size:11px;margin-top:3px;font-family:Arial,Helvetica,sans-serif;">{s["total_done"]}/{s["total_possible"]} &nbsp;·&nbsp; {s["overall_pct"]}%</div>
</td></tr>'''

    return f'''<!DOCTYPE html><html><head><meta charset="utf-8"><title>NET+PREP Admin Report {date_str}</title></head>
<body style="margin:0;padding:0;background-color:#0d1b2a;">
<table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#0d1b2a;border-collapse:collapse;font-family:Arial,Helvetica,sans-serif;"><tr><td align="center" style="padding:24px 16px;">
<table width="1080" cellpadding="0" cellspacing="0" border="0" style="max-width:1080px;border-collapse:collapse;">
<tr><td style="padding:0 0 18px 0;"><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;border-bottom:2px solid #00b4d8;"><tr>
<td style="padding:0 0 14px 0;"><span style="font-size:30px;font-weight:bold;color:#ffffff;">NET</span><span style="font-size:30px;font-weight:bold;color:#00b4d8;">+</span><span style="font-size:30px;font-weight:bold;color:#ffffff;">PREP</span>
<div style="color:#ff6b00;font-size:13px;font-weight:bold;letter-spacing:2px;margin-top:4px;">ADMIN REPORT — CONFIDENTIAL</div>
<div style="color:#9fb3c8;font-size:12px;margin-top:4px;">Campaign: {campaign["name"]}</div></td>
<td align="right" style="padding:0 0 14px 0;color:#9fb3c8;font-size:13px;vertical-align:bottom;">{date_str}</td></tr></table></td></tr>
<tr><td style="padding:0 0 16px 0;"><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;"><tr>
<td width="20%" style="padding:14px 12px;background-color:#13243a;border:1px solid #1b2a3d;border-radius:8px;"><div style="color:#00b4d8;font-size:26px;font-weight:bold;">{total}</div><div style="color:#9fb3c8;font-size:12px;text-transform:uppercase;letter-spacing:1px;margin-top:2px;">Enrolled</div></td>
<td width="12">&nbsp;</td>
<td width="20%" style="padding:14px 12px;background-color:#13243a;border:1px solid #1b2a3d;border-radius:8px;"><div style="color:#00c853;font-size:26px;font-weight:bold;">{active}</div><div style="color:#9fb3c8;font-size:12px;text-transform:uppercase;letter-spacing:1px;margin-top:2px;">Active</div></td>
<td width="12">&nbsp;</td>
<td width="20%" style="padding:14px 12px;background-color:#13243a;border:1px solid #1b2a3d;border-radius:8px;"><div style="color:#ffaa00;font-size:26px;font-weight:bold;">{pending}</div><div style="color:#9fb3c8;font-size:12px;text-transform:uppercase;letter-spacing:1px;margin-top:2px;">Invite Pending</div></td>
<td width="12">&nbsp;</td>
<td width="20%" style="padding:14px 12px;background-color:#13243a;border:1px solid #1b2a3d;border-radius:8px;"><div style="color:#f87171;font-size:26px;font-weight:bold;">{left}</div><div style="color:#9fb3c8;font-size:12px;text-transform:uppercase;letter-spacing:1px;margin-top:2px;">Left Platform</div></td>
<td width="12">&nbsp;</td>
<td width="20%" style="padding:14px 12px;background-color:#13243a;border:1px solid #1b2a3d;border-radius:8px;"><div style="color:#00c853;font-size:26px;font-weight:bold;">{all_passed}</div><div style="color:#9fb3c8;font-size:12px;text-transform:uppercase;letter-spacing:1px;margin-top:2px;">All Exams Passed</div></td>
</tr></table></td></tr>
<tr><td style="padding:0 0 16px 0;color:#9fb3c8;font-size:12px;"><span style="color:#00b4d8;font-weight:bold;">DDI</span> = Deep Discovery Inspector &nbsp;|&nbsp; <span style="color:#00b4d8;font-weight:bold;">TCP</span> = TCP/IP Networking &nbsp;|&nbsp; <span style="color:#00b4d8;font-weight:bold;">TIP</span> = TippingPoint IPS</td></tr>
<tr><td><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;background-color:#0f1f33;border:1px solid #1b2a3d;border-radius:8px;">
<tr style="background-color:#13243a;">
<th align="center" style="padding:11px 8px;color:#9fb3c8;font-size:11px;text-transform:uppercase;letter-spacing:1px;border-bottom:2px solid #1b2a3d;">#</th>
<th align="left" style="padding:11px 8px;color:#9fb3c8;font-size:11px;text-transform:uppercase;letter-spacing:1px;border-bottom:2px solid #1b2a3d;">Name</th>
<th align="left" style="padding:11px 8px;color:#9fb3c8;font-size:11px;text-transform:uppercase;letter-spacing:1px;border-bottom:2px solid #1b2a3d;">Email</th>
<th align="center" style="padding:11px 8px;color:#9fb3c8;font-size:11px;text-transform:uppercase;letter-spacing:1px;border-bottom:2px solid #1b2a3d;">Status</th>
<th align="center" style="padding:11px 8px;color:#9fb3c8;font-size:11px;text-transform:uppercase;letter-spacing:1px;border-bottom:2px solid #1b2a3d;">DDI<br><span style="color:#475569;font-size:9px;">lessons / exam</span></th>
<th align="center" style="padding:11px 8px;color:#9fb3c8;font-size:11px;text-transform:uppercase;letter-spacing:1px;border-bottom:2px solid #1b2a3d;">TCP<br><span style="color:#475569;font-size:9px;">lessons / exam</span></th>
<th align="center" style="padding:11px 8px;color:#9fb3c8;font-size:11px;text-transform:uppercase;letter-spacing:1px;border-bottom:2px solid #1b2a3d;">TIP<br><span style="color:#475569;font-size:9px;">lessons / exam</span></th>
<th align="left" style="padding:11px 8px;color:#9fb3c8;font-size:11px;text-transform:uppercase;letter-spacing:1px;border-bottom:2px solid #1b2a3d;">Overall Progress</th>
</tr>
{rows_html}
</table></td></tr>
<tr><td align="center" style="padding:22px 0 8px 0;color:#5a6b7d;font-size:12px;border-top:1px solid #1b2a3d;">NET+PREP Training Platform &nbsp;·&nbsp; Generated {date_str} &nbsp;·&nbsp; Confidential</td></tr>
</table></td></tr></table></body></html>'''

def build_csv(students):
    out = io.StringIO()
    writer = csv.writer(out)
    writer.writerow(['Rank','ID','Name','Email','Status','Enrolled',
                     'DDI Done','DDI Total','DDI %','DDI Exam Passed','DDI Exam Score','DDI Attempts',
                     'TCP Done','TCP Total','TCP %','TCP Exam Passed','TCP Exam Score','TCP Attempts',
                     'TIP Done','TIP Total','TIP %','TIP Exam Passed','TIP Exam Score','TIP Attempts',
                     'Total Lessons','Overall %','Exams Passed'])
    for s in students:
        writer.writerow([
            s['rank'], s['id'], s['name'], s['email'], s['status'], s['enrolled'],
            s['courses']['ddi']['done'], s['courses']['ddi']['total'], s['courses']['ddi']['pct'],
            'YES' if s['courses']['ddi']['exam_passed'] else 'NO',
            f"{s['courses']['ddi']['exam_score']}/{s['courses']['ddi']['exam_total']}" if s['courses']['ddi']['exam_score'] else '-',
            s['courses']['ddi']['exam_attempts'],
            s['courses']['network']['done'], s['courses']['network']['total'], s['courses']['network']['pct'],
            'YES' if s['courses']['network']['exam_passed'] else 'NO',
            f"{s['courses']['network']['exam_score']}/{s['courses']['network']['exam_total']}" if s['courses']['network']['exam_score'] else '-',
            s['courses']['network']['exam_attempts'],
            s['courses']['tippingpoint']['done'], s['courses']['tippingpoint']['total'], s['courses']['tippingpoint']['pct'],
            'YES' if s['courses']['tippingpoint']['exam_passed'] else 'NO',
            f"{s['courses']['tippingpoint']['exam_score']}/{s['courses']['tippingpoint']['exam_total']}" if s['courses']['tippingpoint']['exam_score'] else '-',
            s['courses']['tippingpoint']['exam_attempts'],
            s['total_done'], s['overall_pct'], s['exams_passed'],
        ])
    return out.getvalue()

def send_report_email(campaign_name, recipients, html, csv_data, date_str):
    if not SES_SMTP_HOST or not SES_SMTP_USER:
        print('Email not configured.')
        return
    try:
        msg = MIMEMultipart('mixed')
        msg['Subject'] = f'NetPrep Daily Report — {campaign_name} — {date_str}'
        msg['From'] = FROM_EMAIL
        msg['To'] = ', '.join(recipients)

        alt = MIMEMultipart('alternative')
        alt.attach(MIMEText('See attached HTML report.', 'plain'))
        alt.attach(MIMEText(html, 'html'))
        msg.attach(alt)

        csv_att = MIMEBase('application', 'octet-stream')
        csv_att.set_payload(csv_data.encode('utf-8'))
        encoders.encode_base64(csv_att)
        csv_att.add_header('Content-Disposition', f'attachment; filename="NETPREP_Report_{date_str}.csv"')
        msg.attach(csv_att)

        with smtplib.SMTP(SES_SMTP_HOST, SES_SMTP_PORT) as server:
            server.starttls()
            server.login(SES_SMTP_USER, SES_SMTP_PASS)
            server.sendmail(FROM_EMAIL, recipients, msg.as_string())
        print(f'  Report sent to: {", ".join(recipients)}')
    except Exception as e:
        print(f'  Email failed: {e}')

if __name__ == '__main__':
    campaign_id = int(sys.argv[1]) if len(sys.argv) > 1 else None
    build_report(campaign_id)
