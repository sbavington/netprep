import os, sqlite3, hashlib, secrets, smtplib
from dotenv import load_dotenv
load_dotenv()
from datetime import datetime
from functools import wraps
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from network_content import LESSON_CONTENT as NET_CONTENT
from exam_content import EXAM_QUESTIONS
from assessment_content import ASSESSMENT_SECTIONS, RATING_LABELS, get_competency
from tp_content import LESSON_CONTENT as TP_CONTENT
from ddi_content import LESSON_CONTENT as DDI_CONTENT
from flask import (Flask, render_template, request, redirect,
                   url_for, session, jsonify, flash, g)

app = Flask(__name__)

from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(32))
from datetime import timedelta
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=12)
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True

DATABASE = 'netprep.db'
BASE_URL  = os.environ.get('BASE_URL', 'http://localhost:5000')
SES_SMTP_HOST   = os.environ.get('SES_SMTP_HOST', '')
SES_SMTP_PORT   = int(os.environ.get('SES_SMTP_PORT', 587))
SES_SMTP_USER   = os.environ.get('SES_SMTP_USER', '')
SES_SMTP_PASS   = os.environ.get('SES_SMTP_PASS', '')
FROM_EMAIL      = os.environ.get('FROM_EMAIL', 'noreply@netprep.org')

# ── Course definitions ────────────────────────────────────────────────────────
COURSES = {
    'network': {
        'id': 'network',
        'title': 'TCP/IP Networking',
        'subtitle': 'CompTIA Network+ · N10-009',
        'icon': '🌐',
        'color': '#00d4ff',
        'hours': 40,
        'modules': [
            {"id":1,"title":"Network Fundamentals","icon":"🌐","hours":5,"lessons":[
                {"id":"1-1","title":"The OSI Model — all 7 layers explained","type":"concept"},
                {"id":"1-2","title":"TCP/IP model vs OSI model","type":"concept"},
                {"id":"1-4","title":"Network topologies and their trade-offs","type":"concept"},
                {"id":"1-5","title":"Module 1 Quiz","type":"quiz"},
            ]},
            {"id":2,"title":"IP Addressing & Subnetting","icon":"🔢","hours":6,"lessons":[
                {"id":"2-1","title":"IPv4 address structure and classes","type":"concept"},
                {"id":"2-2","title":"Subnet masks and CIDR notation","type":"concept"},
                {"id":"2-3","title":"Subnetting calculations step by step","type":"concept"},
                {"id":"2-4","title":"Private vs public IP ranges","type":"concept"},
                {"id":"2-5","title":"IPv6 addressing basics","type":"concept"},
                {"id":"2-6","title":"Subnetting practice lab","type":"lab"},
            ]},
            {"id":3,"title":"Routing & Switching","icon":"🔀","hours":5,"lessons":[
                {"id":"3-1","title":"How routers make forwarding decisions","type":"concept"},
                {"id":"3-2","title":"Static vs dynamic routing","type":"concept"},
                {"id":"3-3","title":"VLANs and inter-VLAN routing","type":"concept"},
                {"id":"3-4","title":"ICMP Protocol","type":"concept"},
                {"id":"3-5","title":"Packet Capture Lab","type":"lab"},
            ]},
            {"id":4,"title":"Network Services","icon":"⚙️","hours":5,"lessons":[
                {"id":"4-1","title":"DNS — how name resolution works","type":"concept"},
                {"id":"4-2","title":"DHCP — dynamic address assignment","type":"concept"},
                {"id":"4-3","title":"Network Inspection","type":"concept"},
                {"id":"4-4","title":"VLANs","type":"concept"},
                    ]},
            {"id":5,"title":"Network Security Fundamentals","icon":"🔒","hours":5,"lessons":[
                {"id":"5-1","title":"Firewalls — types and placement","type":"concept"},
                {"id":"5-2","title":"VPNs — IPsec and SSL/TLS","type":"concept"},
                {"id":"5-3","title":"Common network attacks","type":"concept"},
                {"id":"5-4","title":"Network Access Control (NAC)","type":"concept"},
                {"id":"5-5","title":"Security fundamentals lab","type":"lab"},
            ]},
            {"id":6,"title":"Wireless Networking","icon":"📶","hours":4,"lessons":[
                {"id":"6-1","title":"802.11 standards — a/b/g/n/ac/ax","type":"concept"},
                {"id":"6-2","title":"Wireless security — WPA2 and WPA3","type":"concept"},
                {"id":"6-3","title":"Authentication Protocols","type":"concept"},
                {"id":"6-4","title":"Wireless troubleshooting","type":"lab"},
            ]},
            {"id":7,"title":"Cloud & Virtualisation","icon":"☁️","hours":4,"lessons":[
                {"id":"7-1","title":"Troubleshooting","type":"concept"},
                {"id":"7-2","title":"CLI Tools","type":"concept"},
                {"id":"7-3","title":"Diagrams","type":"concept"},
                {"id":"7-4","title":"Network Troubleshooting","type":"lab"},
            ]},
            {"id":8,"title":"Troubleshooting & Diagnostics","icon":"🔬","hours":6,"lessons":[
                {"id":"8-1","title":"Troubleshooting methodology","type":"concept"},
                {"id":"8-2","title":"ping, traceroute, nslookup, netstat","type":"concept"},
                {"id":"8-3","title":"Wireshark basics — reading packet captures","type":"concept"},
                {"id":"8-4","title":"Common connectivity issues and fixes","type":"concept"},
                {"id":"8-5","title":"Network+ practice exam (50 questions)","type":"quiz"},
                {"id":"8-6","title":"Diagrams","type":"concept"},
            ]},
        ]
    },
    'tippingpoint': {
        'id': 'tippingpoint',
        'title': 'TippingPoint IPS',
        'subtitle': 'TrendAI · Installation & Configuration',
        'icon': '🛡️',
        'color': '#ff6b35',
        'hours': 38,
        'modules': [
            {"id":1,"title":"Introduction to TippingPoint & IPS","icon":"🛡️","hours":3,"lessons":[
                {"id":"tp-1-1","title":"What is TippingPoint? IPS vs IDS vs Firewall","type":"concept"},
                {"id":"tp-1-2","title":"TXE Series","type":"concept"},
                {"id":"tp-1-3","title":"How inline IPS works — traffic flow explained","type":"concept"},
                {"id":"tp-1-4","title":"Module 1 Quiz","type":"quiz"},
            ]},
            {"id":2,"title":"Hardware Installation & Setup","icon":"🔧","hours":4,"lessons":[
                {"id":"tp-2-1","title":"Rack mounting and cabling requirements","type":"concept"},
                {"id":"tp-2-2","title":"Segment ports and network placement","type":"concept"},
                {"id":"tp-2-3","title":"Power-on and initial boot sequence","type":"concept"},
                {"id":"tp-2-4","title":"Hardware installation lab","type":"lab"},
            ]},
            {"id":3,"title":"Initial Configuration & CLI","icon":"💻","hours":5,"lessons":[
                {"id":"tp-3-1","title":"Connecting via console and SSH","type":"concept"},
                {"id":"tp-3-2","title":"Basic CLI commands and navigation","type":"concept"},
                {"id":"tp-3-3","title":"Setting IP address, DNS and NTP","type":"concept"},
                {"id":"tp-3-4","title":"Setting up management access","type":"concept"},
                {"id":"tp-3-5","title":"CLI configuration lab","type":"lab"},
            ]},
            {"id":4,"title":"Security Management System (SMS)","icon":"🖥️","hours":5,"lessons":[
                {"id":"tp-4-1","title":"SMS architecture and components","type":"concept"},
                {"id":"tp-4-2","title":"Installing and licensing SMS","type":"concept"},
                {"id":"tp-4-3","title":"Adding devices to SMS","type":"concept"},
                {"id":"tp-4-4","title":"SMS dashboard and navigation","type":"concept"},
                {"id":"tp-4-5","title":"SMS setup lab","type":"lab"},
            ]},
            {"id":5,"title":"Security Policy Management","icon":"📋","hours":5,"lessons":[
                {"id":"tp-5-1","title":"Profiles, policies and segments explained","type":"concept"},
                {"id":"tp-5-2","title":"Creating and applying security profiles","type":"concept"},
                {"id":"tp-5-3","title":"Action sets — block, permit, rate-limit, notify","type":"concept"},
                {"id":"tp-5-4","title":"Policy exceptions and permit lists","type":"concept"},
                {"id":"tp-5-5","title":"Policy management lab","type":"lab"},
            ]},
            {"id":6,"title":"Threat Filters & Signatures","icon":"🔍","hours":5,"lessons":[
                {"id":"tp-6-1","title":"Understanding Digital Vaccine (DV) filters","type":"concept"},
                {"id":"tp-6-2","title":"Filter categories and severity levels","type":"concept"},
                {"id":"tp-6-3","title":"Customising and tuning filters","type":"concept"},
                {"id":"tp-6-4","title":"Updating Digital Vaccine packages","type":"concept"},
                {"id":"tp-6-5","title":"Filter tuning lab","type":"lab"},
            ]},
            {"id":7,"title":"High Availability & Clustering","icon":"⚡","hours":4,"lessons":[
                {"id":"tp-7-1","title":"HA modes — Layer 2 fallback and zeropower","type":"concept"},
                        {"id":"tp-7-3","title":"Testing failover and resilience","type":"concept"},
                    ]},
            {"id":8,"title":"Troubleshooting & Diagnostics","icon":"🔬","hours":4,"lessons":[
                {"id":"tp-8-1","title":"Reading and interpreting logs","type":"concept"},
                {"id":"tp-8-2","title":"Common issues and solutions","type":"concept"},
                {"id":"tp-8-3","title":"Packet capture and traffic analysis","type":"concept"},
                {"id":"tp-8-4","title":"Troubleshooting lab","type":"lab"},
            ]},
            {"id":9,"title":"SIEM Integration & Logging","icon":"📊","hours":4,"lessons":[
                {"id":"tp-9-1","title":"Syslog configuration and forwarding","type":"concept"},
                {"id":"tp-9-2","title":"SNMP monitoring setup","type":"concept"},
                {"id":"tp-9-3","title":"Integrating with Splunk and QRadar","type":"concept"},
                {"id":"tp-9-4","title":"SIEM integration lab","type":"lab"},
            ]},
        ]
    },
    'ddi': {
        'id': 'ddi',
        'title': 'Deep Discovery Inspector',
        'subtitle': 'TrendAI · APT Detection & Response',
        'icon': '🔎',
        'color': '#a855f7',
        'hours': 38,
        'modules': [
            {"id":1,"title":"Introduction to Deep Discovery Inspector","icon":"🔎","hours":3,"lessons":[
                {"id":"ddi-1-1","title":"What is DDI? APT detection vs traditional security","type":"concept"},
                {"id":"ddi-1-2","title":"DDI architecture and detection engines","type":"concept"},
                {"id":"ddi-1-3","title":"How DDI fits in your security ecosystem","type":"concept"},
                {"id":"ddi-1-4","title":"Module 1 Quiz","type":"quiz"},
            ]},
            {"id":2,"title":"Hardware Installation & Setup","icon":"🔧","hours":4,"lessons":[
                {"id":"ddi-2-1","title":"DDI hardware models and specifications","type":"concept"},
                {"id":"ddi-2-2","title":"Rack mounting, cabling and network placement","type":"concept"},
                {"id":"ddi-2-3","title":"Span port and tap configuration","type":"concept"},
                {"id":"ddi-2-4","title":"Hardware installation lab","type":"lab"},
            ]},
            {"id":3,"title":"Initial Configuration & Network Placement","icon":"🌐","hours":5,"lessons":[
                {"id":"ddi-3-1","title":"First boot and management console access","type":"concept"},
                {"id":"ddi-3-2","title":"Network interface and IP configuration","type":"concept"},
                {"id":"ddi-3-3","title":"Deployment modes — out-of-band vs inline","type":"concept"},
                {"id":"ddi-3-4","title":"NTP, DNS and proxy settings","type":"concept"},
                {"id":"ddi-3-5","title":"Initial configuration lab","type":"lab"},
            ]},
            {"id":4,"title":"Detection Policies & Threat Intelligence","icon":"🛡️","hours":5,"lessons":[
                {"id":"ddi-4-1","title":"Detection rules and pattern updates","type":"concept"},
                {"id":"ddi-4-2","title":"Threat intelligence sources and Smart Protection","type":"concept"},
                {"id":"ddi-4-3","title":"Configuring detection policies","type":"concept"},
                {"id":"ddi-4-4","title":"Exception lists and trusted sources","type":"concept"},
                {"id":"ddi-4-5","title":"Detection policy lab","type":"lab"},
            ]},
            {"id":5,"title":"Sandbox Analysis & Virtual Analyzer","icon":"🧪","hours":5,"lessons":[
                {"id":"ddi-5-1","title":"Virtual Analyzer overview and how sandboxing works","type":"concept"},
                {"id":"ddi-5-2","title":"Configuring Virtual Analyzer","type":"concept"},
                {"id":"ddi-5-3","title":"File submission and analysis workflow","type":"concept"},
                {"id":"ddi-5-4","title":"Interpreting sandbox analysis reports","type":"concept"},
                {"id":"ddi-5-5","title":"Virtual Analyzer lab","type":"lab"},
            ]},
            {"id":6,"title":"Reporting & Dashboards","icon":"📊","hours":4,"lessons":[
                {"id":"ddi-6-1","title":"DDI dashboard overview and widgets","type":"concept"},
                {"id":"ddi-6-2","title":"Threat investigation and event drill-down","type":"concept"},
                {"id":"ddi-6-3","title":"Scheduled and on-demand reports","type":"concept"},
                {"id":"ddi-6-4","title":"Reporting lab","type":"lab"},
            ]},
            {"id":7,"title":"SIEM & Syslog Integration","icon":"📡","hours":4,"lessons":[
                {"id":"ddi-7-1","title":"Syslog configuration and CEF format","type":"concept"},
                {"id":"ddi-7-2","title":"Integrating with Splunk and QRadar","type":"concept"},
                {"id":"ddi-7-3","title":"SNMP monitoring and alerts","type":"concept"},
                {"id":"ddi-7-4","title":"SIEM integration lab","type":"lab"},
            ]},
            {"id":8,"title":"High Availability & Clustering","icon":"⚡","hours":4,"lessons":[
                {"id":"ddi-8-1","title":"HA deployment options for DDI","type":"concept"},
                {"id":"ddi-8-2","title":"Configuring HA and failover","type":"concept"},
                {"id":"ddi-8-3","title":"Testing and validating HA","type":"concept"},
                {"id":"ddi-8-4","title":"HA configuration lab","type":"lab"},
            ]},
            {"id":9,"title":"Troubleshooting & Diagnostics","icon":"🔬","hours":4,"lessons":[
                {"id":"ddi-9-1","title":"Reading DDI logs and alerts","type":"concept"},
                {"id":"ddi-9-2","title":"Common issues and solutions","type":"concept"},
                {"id":"ddi-9-3","title":"Diagnostic tools and support bundles","type":"concept"},
                {"id":"ddi-9-4","title":"Troubleshooting lab","type":"lab"},
            ]},
        ]
    },
}

CONTENT = {
    'network': NET_CONTENT,
    'tippingpoint': TP_CONTENT,
    'ddi': DDI_CONTENT,
}

def course_total(course_id):
    return sum(len(m['lessons']) for m in COURSES[course_id]['modules'])

# ── DB ────────────────────────────────────────────────────────────────────────
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        db.executescript('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL DEFAULT '',
                password_hash TEXT,
                is_admin INTEGER DEFAULT 0,
                invite_token TEXT,
                invited_at TEXT,
                activated_at TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS enrolments (
                user_id INTEGER,
                course_id TEXT,
                enrolled_at TEXT DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (user_id, course_id)
            );
            CREATE TABLE IF NOT EXISTS progress (
                user_id INTEGER,
                course_id TEXT,
                lesson_id TEXT,
                completed_at TEXT,
                PRIMARY KEY (user_id, course_id, lesson_id)
            );
            CREATE TABLE IF NOT EXISTS password_reset_tokens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                token TEXT UNIQUE NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                used INTEGER DEFAULT 0
            );
            CREATE TABLE IF NOT EXISTS bookmarks (
                user_id INTEGER,
                course_id TEXT,
                lesson_id TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (user_id, course_id, lesson_id)
            );
            CREATE TABLE IF NOT EXISTS exam_attempts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                course_id TEXT NOT NULL,
                score INTEGER NOT NULL,
                total INTEGER NOT NULL,
                passed INTEGER NOT NULL DEFAULT 0,
                started_at TEXT,
                completed_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                course_id TEXT NOT NULL,
                satisfaction INTEGER NOT NULL,
                suggestions TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS assessments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                responses TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS campaigns (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL,
                report_emails TEXT NOT NULL DEFAULT '',
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS campaign_students (
                campaign_id INTEGER,
                user_id INTEGER,
                PRIMARY KEY (campaign_id, user_id)
            );
        ''')
        db.commit()
        existing = db.execute("SELECT id FROM users WHERE email='admin@netprep.org'").fetchone()
        if not existing:
            salt = secrets.token_hex(16)
            pw = f"{salt}:{hashlib.sha256((salt+'changeme123').encode()).hexdigest()}"
            db.execute("INSERT INTO users (email,name,password_hash,is_admin) VALUES (?,?,?,1)",
                       ('admin@netprep.org','Admin',pw))
            db.commit()

def hash_password(p):
    salt = secrets.token_hex(16)
    return f"{salt}:{hashlib.sha256((salt+p).encode()).hexdigest()}"

def check_password(stored, provided):
    try:
        salt, hashed = stored.split(':',1)
        return hashed == hashlib.sha256((salt+provided).encode()).hexdigest()
    except:
        return False

# ── Email ─────────────────────────────────────────────────────────────────────
def send_invite_email(to_name, to_email, course_ids, invite_url):
    if not SES_SMTP_HOST or not SES_SMTP_USER:
        app.logger.warning(f'Email not configured — invite URL: {invite_url}')
        return False
    try:
        course_order = ['network', 'tippingpoint', 'ddi']
        enrolled = [c for c in course_order if c in course_ids and c in COURSES]
        course_names = ', '.join(COURSES[c]['title'] for c in enrolled)
        course_descs = {
            'network': ('&#127760;', 'TCP/IP Networking (CompTIA Network+)', 'The foundation everything else sits on. SEs who cannot speak confidently about networking lose deals. Covers subnetting, routing, VLANs, packet capture, wireless, and CLI tools. Network+ aligned so it counts toward certification prep.'),
            'tippingpoint': ('&#128737;', 'TippingPoint IPS', 'Know the product better than the customer. Full coverage of the TippingPoint stack - hardware, CLI, Digital Vaccine, ZPHA, bypass modes, SMS, and SSL inspection. Built so you can run demos, handle PoCs, and support customers without leaning on TAC for basics.'),
            'ddi': ('&#128269;', 'Deep Discovery Inspector (DDI)', 'NDR you can actually explain. Covers deployment modes, detection engines, Vision One integration, credit billing, and how to position DDI vs VNS. Designed to make you a confident NDR voice in front of customers.'),
        }
        course_blocks_html = ''
        for cid in enrolled:
            if cid in course_descs:
                icon, title, desc = course_descs[cid]
                course_blocks_html += ('<tr><td style="padding:14px 16px;background-color:#13243a;border:1px solid #1b2a3d;border-radius:8px;">'
                    '<div style="font-size:14px;margin-bottom:6px;">' + icon + ' <span style="color:#00b4d8;font-weight:bold;">' + title + '</span></div>'
                    '<div style="color:#9fb3c8;font-size:12px;line-height:1.6;">' + desc + '</div>'
                    '</td></tr><tr><td style="height:8px;"></td></tr>')
        text = ('Hi ' + to_name + ',\n\nYou have been invited to NetPrep, Trend Micro SE Training Platform.\n\nYour enrolled courses:\n'
            + '\n'.join('- ' + COURSES[c]['title'] for c in enrolled)
            + '\n\nClick below to set your password and get started:\n' + invite_url
            + '\n\nEach course ends with a certificate of completion.\n\nThis link is unique to you.\n\nNetPrep Training Platform')
        html = ('<!DOCTYPE html><html><head><meta charset="utf-8"></head><body style="margin:0;padding:0;background-color:#0d1b2a;">'
            '<table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#0d1b2a;font-family:Arial,Helvetica,sans-serif;">'
            '<tr><td align="center" style="padding:24px 16px;">'
            '<table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;">'
            '<tr><td style="padding:0 0 18px 0;border-bottom:2px solid #00b4d8;">'
            '<span style="font-size:28px;font-weight:bold;color:#ffffff;">NET</span>'
            '<span style="font-size:28px;font-weight:bold;color:#00b4d8;">+</span>'
            '<span style="font-size:28px;font-weight:bold;color:#ffffff;">PREP</span>'
            '<div style="color:#ff6b00;font-size:12px;font-weight:bold;letter-spacing:2px;margin-top:4px;">TREND MICRO SE TRAINING PLATFORM</div>'
            '</td></tr><tr><td style="padding:24px 0 16px 0;">'
            '<p style="color:#ffffff;font-size:16px;margin:0 0 8px;">Hi <strong>' + to_name + '</strong>,</p>'
            '<p style="color:#9fb3c8;font-size:14px;line-height:1.6;margin:0 0 20px;">You have been invited to <strong style="color:#00b4d8;">NetPrep</strong>, Trend Micro SE technical training platform. Your enrollment gives you access to hands-on, self-paced courses built specifically for SEs working with our network security portfolio.</p>'
            '<div style="color:#ff6b00;font-size:11px;font-weight:bold;letter-spacing:2px;margin-bottom:14px;">YOUR COURSES</div>'
            '<table width="100%" cellpadding="0" cellspacing="0" border="0">' + course_blocks_html + '</table>'
            '<div style="margin:24px 0;text-align:center;">'
            '<a href="' + invite_url + '" style="display:inline-block;background:#00b4d8;color:#000000;font-weight:bold;font-size:15px;padding:14px 32px;border-radius:8px;text-decoration:none;">Accept Your Invitation &#8594;</a>'
            '</div>'
            '<p style="color:#9fb3c8;font-size:13px;line-height:1.6;">Each course ends with a <strong style="color:#ffffff;">certificate of completion</strong> you can add to your LinkedIn profile.</p>'
            '<p style="color:#9fb3c8;font-size:13px;">Questions? Reach out to your NDR SME.</p>'
            '</td></tr>'
            '<tr><td style="padding:16px 0;border-top:1px solid #1b2a3d;color:#5a6b7d;font-size:11px;text-align:center;">NET+PREP Training Platform &nbsp;&middot;&nbsp; This link is unique to you - please do not share it.</td></tr>'
            '</table></td></tr></table></body></html>')
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "You have been invited to NetPrep - Trend Micro SE Training"
        msg['From'] = FROM_EMAIL
        msg['To'] = to_email

        msg.attach(MIMEText(text, 'plain'))
        msg.attach(MIMEText(html, 'html'))
        with smtplib.SMTP(SES_SMTP_HOST, SES_SMTP_PORT) as server:
            server.starttls()
            server.login(SES_SMTP_USER, SES_SMTP_PASS)
            server.sendmail(FROM_EMAIL, to_email, msg.as_string())
        return True
    except Exception as e:
        app.logger.error(f'Email send failed: {e}')
        return False

def send_password_reset_email(to_name, to_email, reset_url):
    if not SES_SMTP_HOST or not SES_SMTP_USER:
        app.logger.warning(f'Email not configured — reset URL: {reset_url}')
        return False
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'NetPrep — Password Reset Request'
        msg['From'] = FROM_EMAIL
        msg['To'] = to_email
        text = (f"Hi {to_name},\n\n"
                "We received a request to reset your NetPrep password.\n\n"
                f"Click the link below to set a new password (expires in 1 hour):\n{reset_url}\n\n"
                "If you did not request this, you can safely ignore this email.\n\nNetPrep Training Platform\n")
        html = (f'<html><body style="font-family:sans-serif;background:#0a0f1e;color:#e2e8f0;padding:40px;">'
                f'<div style="max-width:500px;margin:0 auto;background:#111827;border-radius:12px;padding:32px;border:1px solid #1e293b;">'
                f'<h2 style="color:#00d4ff;margin-top:0;">Password Reset</h2>'
                f'<p>Hi <strong>{to_name}</strong>,</p>'
                f'<p>We received a request to reset your NetPrep password.</p>'
                f'<p>Click below to set a new password. This link expires in <strong>1 hour</strong>.</p>'
                f'<a href="{reset_url}" style="display:inline-block;background:#00d4ff;color:#000;padding:12px 24px;border-radius:8px;text-decoration:none;font-weight:bold;margin:16px 0;">Reset My Password</a>'
                f'<p style="color:#64748b;font-size:12px;margin-top:24px;">If you did not request this, you can safely ignore this email.</p>'
                f'</div></body></html>')
        msg.attach(MIMEText(text, 'plain'))
        msg.attach(MIMEText(html, 'html'))
        with smtplib.SMTP(SES_SMTP_HOST, SES_SMTP_PORT) as server:
            server.starttls()
            server.login(SES_SMTP_USER, SES_SMTP_PASS)
            server.sendmail(FROM_EMAIL, to_email, msg.as_string())
        return True
    except Exception as e:
        app.logger.error(f'Password reset email failed: {e}')
        return False

# ── Auth ──────────────────────────────────────────────────────────────────────
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            app.logger.error(f'login_required FAILED: path={request.path} session_keys={list(session.keys())} cookies={list(request.cookies.keys())}')
            if request.is_json or request.path.startswith('/api/'):
                return jsonify({'error': 'Not logged in'}), 401
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session or not session.get('is_admin'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

# ── Routes ────────────────────────────────────────────────────────────────────
@app.route('/')
def index():
    if 'user_id' in session:
        if session.get('is_admin'):
            return redirect(url_for('admin'))
        return redirect(url_for('my_courses'))
    return redirect(url_for('login'))

@app.route('/forgot-password', methods=['GET','POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email','').strip().lower()
        db = get_db()
        user = db.execute('SELECT * FROM users WHERE email=?', (email,)).fetchone()
        if user and user['password_hash']:
            token = secrets.token_urlsafe(32)
            db.execute('INSERT INTO password_reset_tokens (user_id, token, created_at) VALUES (?,?,?)',
                       (user['id'], token, datetime.utcnow().isoformat()))
            db.commit()
            reset_url = f"{BASE_URL}/reset-password/{token}"
            send_password_reset_email(user['name'], user['email'], reset_url)
        flash('If that email is registered, a reset link has been sent.', 'info')
        return redirect(url_for('forgot_password'))
    return render_template('forgot_password.html')

@app.route('/reset-password/<token>', methods=['GET','POST'])
def reset_password(token):
    db = get_db()
    row = db.execute('SELECT * FROM password_reset_tokens WHERE token=? AND used=0', (token,)).fetchone()
    if not row:
        flash('Invalid or expired reset link.', 'error')
        return redirect(url_for('login'))
    created = datetime.fromisoformat(row['created_at'])
    if (datetime.utcnow() - created).total_seconds() > 3600:
        flash('This reset link has expired. Please request a new one.', 'error')
        return redirect(url_for('forgot_password'))
    if request.method == 'POST':
        pw = request.form.get('password','')
        pw2 = request.form.get('password2','')
        if len(pw) < 8:
            flash('Password must be at least 8 characters.', 'error')
            return render_template('reset_password.html', token=token)
        if pw != pw2:
            flash('Passwords do not match.', 'error')
            return render_template('reset_password.html', token=token)
        db.execute('UPDATE users SET password_hash=? WHERE id=?',
                   (hash_password(pw), row['user_id']))
        db.execute('UPDATE password_reset_tokens SET used=1 WHERE token=?', (token,))
        db.commit()
        flash('Password updated successfully. Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('reset_password.html', token=token)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email','').strip().lower()
        password = request.form.get('password','')
        db = get_db()
        user = db.execute('SELECT * FROM users WHERE email=?', (email,)).fetchone()
        if user and user['password_hash'] and check_password(user['password_hash'], password):
            session.clear()
            session.permanent = True
            session['user_id']   = user['id']
            session['user_name'] = user['name']
            session['is_admin']  = bool(user['is_admin'])
            if session.get('is_admin'):
                return redirect(url_for('admin'))
            return redirect(url_for('my_courses'))
        flash('Invalid email or password.', 'error')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/change-password', methods=['GET','POST'])
@login_required
def change_password():
    if request.method == 'POST':
        current = request.form.get('current_password','')
        new_pw = request.form.get('new_password','')
        confirm = request.form.get('confirm_password','')
        db = get_db()
        user = db.execute('SELECT * FROM users WHERE id=?', (session['user_id'],)).fetchone()
        if not check_password(user['password_hash'], current):
            flash('Current password is incorrect.', 'error')
            return render_template('change_password.html')
        if len(new_pw) < 8:
            flash('New password must be at least 8 characters.', 'error')
            return render_template('change_password.html')
        if new_pw != confirm:
            flash('Passwords do not match.', 'error')
            return render_template('change_password.html')
        db.execute('UPDATE users SET password_hash=? WHERE id=?',
                   (hash_password(new_pw), session['user_id']))
        db.commit()
        flash('Password changed successfully.', 'info')
        if session.get('is_admin'):
            return redirect(url_for('admin'))
        return redirect(url_for('my_courses'))
    return render_template('change_password.html')

@app.route('/set-password', methods=['GET','POST'])
@login_required
def set_password():
    if request.method == 'POST':
        pw = request.form.get('password','')
        if len(pw) < 8:
            flash('Password must be at least 8 characters.', 'error')
            return render_template('set_password.html')
        db = get_db()
        db.execute('UPDATE users SET password_hash=? WHERE id=?',
                   (hash_password(pw), session['user_id']))
        db.commit()
        return redirect(url_for('my_courses'))
    return render_template('set_password.html')

@app.route('/invite/<token>', methods=['GET','POST'])
def accept_invite(token):
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE invite_token=?', (token,)).fetchone()
    if not user:
        return render_template('login.html', error='Invalid or expired invite link.')
    enrolments = db.execute('SELECT course_id FROM enrolments WHERE user_id=?', (user['id'],)).fetchall()
    courses = [COURSES[e['course_id']] for e in enrolments if e['course_id'] in COURSES]
    if request.method == 'POST':
        pw = request.form.get('password','')
        if len(pw) < 8:
            flash('Password must be at least 8 characters.', 'error')
            return render_template('accept_invite.html', token=token, name=user['name'],
                                   email=user['email'], courses=courses)
        db.execute('''UPDATE users SET password_hash=?, invite_token=NULL, activated_at=? WHERE id=?''',
                   (hash_password(pw), datetime.utcnow().isoformat(), user['id']))
        db.commit()
        session.clear()
        session['user_id']   = user['id']
        session['user_name'] = user['name']
        session['is_admin']  = bool(user['is_admin'])
        return redirect(url_for('my_courses'))
    return render_template('accept_invite.html', token=token, name=user['name'],
                           email=user['email'], courses=courses)

@app.route('/courses')
@login_required
def my_courses():
    db = get_db()
    enrolments = db.execute('SELECT course_id FROM enrolments WHERE user_id=?',
                            (session['user_id'],)).fetchall()
    enrolled = [e['course_id'] for e in enrolments]
    course_data = []
    for cid in enrolled:
        if cid not in COURSES:
            continue
        total = course_total(cid)
        done = db.execute('SELECT COUNT(*) FROM progress WHERE user_id=? AND course_id=?',
                          (session['user_id'], cid)).fetchone()[0]
        exam_passed = db.execute(
            'SELECT 1 FROM exam_attempts WHERE user_id=? AND course_id=? AND passed=1',
            (session['user_id'], cid)).fetchone() is not None
        course_data.append({
            'course': COURSES[cid],
            'total': total,
            'done': min(done, total),
            'pct': min(int(done/total*100), 100) if total else 0,
            'exam_passed': exam_passed,
        })
    return render_template('my_courses.html', courses=course_data, user_name=session['user_name'])

@app.route('/course/<course_id>')
@login_required
def curriculum(course_id):
    if course_id not in COURSES:
        return redirect(url_for('my_courses'))
    db = get_db()
    enrolment = db.execute('SELECT 1 FROM enrolments WHERE user_id=? AND course_id=?',
                           (session['user_id'], course_id)).fetchone()
    if not enrolment and not session.get('is_admin'):
        flash('You are not enrolled in this course.', 'error')
        return redirect(url_for('my_courses'))
    rows = db.execute('SELECT lesson_id FROM progress WHERE user_id=? AND course_id=?',
                      (session['user_id'], course_id)).fetchall()
    completed = {r['lesson_id'] for r in rows}
    bm_rows = db.execute('SELECT lesson_id FROM bookmarks WHERE user_id=? AND course_id=?',
                         (session['user_id'], course_id)).fetchall()
    bookmarked = {r['lesson_id'] for r in bm_rows}
    course = COURSES[course_id]
    total = course_total(course_id)
    done_count = len(completed)
    pct = min(int(done_count / total * 100), 100) if total else 0
    from flask import make_response
    resp = make_response(render_template('curriculum.html',
        course=course, modules=course['modules'],
        completed=completed, total=total,
        done_count=done_count, pct=pct,
        user_name=session['user_name'],
        lesson_content=CONTENT.get(course_id, {}),
        bookmarked=list(bookmarked),
        is_admin=session.get('is_admin', False)))
    resp.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    resp.headers['Pragma'] = 'no-cache'
    return resp

@app.route('/api/progress', methods=['POST'])
@login_required
def api_progress():
    data      = request.get_json()
    course_id = data.get('course_id')
    lesson_id = data.get('lesson_id')
    action    = data.get('action')
    db        = get_db()
    if action == 'complete':
        db.execute('INSERT OR IGNORE INTO progress (user_id,course_id,lesson_id,completed_at) VALUES (?,?,?,?)',
                   (session['user_id'], course_id, lesson_id, datetime.utcnow().isoformat()))
    else:
        db.execute('DELETE FROM progress WHERE user_id=? AND course_id=? AND lesson_id=?',
                   (session['user_id'], course_id, lesson_id))
    db.commit()
    total = course_total(course_id)
    count = db.execute('SELECT COUNT(*) FROM progress WHERE user_id=? AND course_id=?',
                       (session['user_id'], course_id)).fetchone()[0]
    return jsonify({'completed': count, 'total': total})

# ── Admin ─────────────────────────────────────────────────────────────────────
@app.route('/api/bookmark', methods=['POST'])
@login_required
def api_bookmark():
    data = request.get_json()
    course_id = data.get('course_id')
    lesson_id = data.get('lesson_id')
    action = data.get('action')
    db = get_db()
    if action == 'add':
        db.execute('INSERT OR IGNORE INTO bookmarks (user_id, course_id, lesson_id, created_at) VALUES (?,?,?,?)',
                   (session['user_id'], course_id, lesson_id, datetime.utcnow().isoformat()))
    else:
        db.execute('DELETE FROM bookmarks WHERE user_id=? AND course_id=? AND lesson_id=?',
                   (session['user_id'], course_id, lesson_id))
    db.commit()
    bookmarks = db.execute('SELECT lesson_id FROM bookmarks WHERE user_id=? AND course_id=?',
                           (session['user_id'], course_id)).fetchall()
    return jsonify({'bookmarks': [r['lesson_id'] for r in bookmarks]})

@app.route('/api/leave', methods=['POST'])
@login_required
def api_leave():
    db = get_db()
    db.execute('UPDATE users SET password_hash=NULL, invite_token=NULL, activated_at=NULL WHERE id=? AND is_admin=0',
               (session['user_id'],))
    db.commit()
    session.clear()
    return jsonify({'ok': True})

@app.route('/api/course/reset', methods=['POST'])
@login_required
def api_course_reset():
    data = request.get_json()
    course_id = data.get('course_id')
    if not course_id or course_id not in COURSES:
        return jsonify({'error': 'Invalid course'}), 400
    db = get_db()
    db.execute('DELETE FROM progress WHERE user_id=? AND course_id=?',
               (session['user_id'], course_id))
    db.execute('DELETE FROM bookmarks WHERE user_id=? AND course_id=?',
               (session['user_id'], course_id))
    db.commit()
    return jsonify({'ok': True})

@app.route('/admin')
@admin_required
def admin():
    db = get_db()
    users = db.execute('''
        SELECT u.id, u.name, u.email, u.invite_token, u.activated_at, u.created_at, u.password_hash
        FROM users u WHERE u.is_admin=0 ORDER BY u.created_at DESC
    ''').fetchall()
    students = []
    for u in users:
        enrolments = db.execute('SELECT course_id FROM enrolments WHERE user_id=?', (u['id'],)).fetchall()
        enrolled_courses = [e['course_id'] for e in enrolments]
        total_lessons = sum(course_total(c) for c in enrolled_courses)
        done = db.execute('SELECT COUNT(*) FROM progress WHERE user_id=?', (u['id'],)).fetchone()[0]
        left = u['activated_at'] is None and u['invite_token'] is None and u['password_hash'] is None
        students.append({
            'id': u['id'], 'name': u['name'], 'email': u['email'],
            'courses': enrolled_courses,
            'lessons_done': done, 'total_lessons': total_lessons,
            'is_active': u['activated_at'] is not None,
            'left_platform': left,
            'invite_token': u['invite_token'],
            'created_at': u['created_at'] or '',
        })
    return render_template('admin.html', users=students, courses=COURSES)

@app.route('/admin/user/<int:uid>/reinvite', methods=['POST'])
@admin_required
def admin_reinvite(uid):
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE id=? AND is_admin=0', (uid,)).fetchone()
    if not user:
        return jsonify({'error': 'User not found'}), 404
    token = secrets.token_urlsafe(32)
    db.execute('UPDATE users SET invite_token=?, invited_at=?, password_hash=NULL, activated_at=NULL WHERE id=?',
               (token, datetime.utcnow().isoformat(), uid))
    db.commit()
    enrolments = db.execute('SELECT course_id FROM enrolments WHERE user_id=?', (uid,)).fetchall()
    course_ids = [e['course_id'] for e in enrolments]
    invite_url = f"{BASE_URL}/invite/{token}"
    sent = send_invite_email(user['name'], user['email'], course_ids, invite_url)
    if sent:
        flash(f'Re-invite sent to {user["email"]}. Link: {invite_url}', 'info')
    else:
        flash(f'Re-invite link (email failed): {invite_url}', 'error')
    return redirect(url_for('admin'))

@app.route('/admin/invite', methods=['POST'])
@admin_required
def admin_invite():
    name     = request.form.get('name','').strip()
    email    = request.form.get('email','').strip().lower()
    course_ids = request.form.getlist('courses')
    if not name or not email or not course_ids:
        flash('Name, email and at least one course are required.', 'error')
        return redirect(url_for('admin'))
    db = get_db()
    existing = db.execute('SELECT id FROM users WHERE email=?', (email,)).fetchone()
    if existing:
        flash(f'{email} already has an account.', 'error')
        return redirect(url_for('admin'))
    token = secrets.token_urlsafe(32)
    db.execute('INSERT INTO users (email,name,invite_token,invited_at) VALUES (?,?,?,?)',
               (email, name, token, datetime.utcnow().isoformat()))
    db.commit()
    user = db.execute('SELECT id FROM users WHERE email=?', (email,)).fetchone()
    for cid in course_ids:
        if cid in COURSES:
            db.execute('INSERT OR IGNORE INTO enrolments (user_id,course_id) VALUES (?,?)',
                       (user['id'], cid))
    db.commit()
    invite_url = f"{BASE_URL}/invite/{token}"
    sent = send_invite_email(name, email, course_ids, invite_url)
    if sent:
        flash(f'Invite sent to {email}. Link: {invite_url}', 'info')
    else:
        flash(f'Invite link for {name}: {invite_url}', 'info')
    return redirect(url_for('admin'))

@app.route('/admin/invite/bulk', methods=['POST'])
@admin_required
def admin_invite_bulk():
    bulk = request.form.get('bulk','')
    course_ids = request.form.getlist('bulk_courses')
    if not course_ids:
        flash('Select at least one course for bulk invite.', 'error')
        return redirect(url_for('admin'))
    db = get_db()
    results = []
    for line in bulk.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        if '\t' in line:
            parts = line.split('\t', 1)
        else:
            parts = line.split(',', 1)
        if len(parts) != 2:
            results.append(f'Skipped (bad format): {line}')
            continue
        name  = parts[0].strip()
        email = parts[1].strip().lower()
        if not name or not email:
            continue
        existing = db.execute('SELECT id FROM users WHERE email=?', (email,)).fetchone()
        if existing:
            results.append(f'Already exists: {email}')
            continue
        token = secrets.token_urlsafe(32)
        db.execute('INSERT INTO users (email,name,invite_token,invited_at) VALUES (?,?,?,?)',
                   (email, name, token, datetime.utcnow().isoformat()))
        db.commit()
        user = db.execute('SELECT id FROM users WHERE email=?', (email,)).fetchone()
        for cid in course_ids:
            if cid in COURSES:
                db.execute('INSERT OR IGNORE INTO enrolments (user_id,course_id) VALUES (?,?)',
                           (user['id'], cid))
        db.commit()
        invite_url = f"{BASE_URL}/invite/{token}"
        sent = send_invite_email(name, email, course_ids, invite_url)
        status = 'emailed' if sent else 'link generated'
        results.append(f'{name} ({email}): {status} — {invite_url}')
        if sent:
            import time; time.sleep(2)
    flash('\n'.join(results), 'info')
    return redirect(url_for('admin'))

@app.route('/admin/user/<int:uid>')
@admin_required
def admin_user(uid):
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE id=?', (uid,)).fetchone()
    if not user:
        return redirect(url_for('admin'))
    enrolments = db.execute('SELECT course_id FROM enrolments WHERE user_id=?', (uid,)).fetchall()
    enrolled = [e['course_id'] for e in enrolments]
    progress = {}
    for cid in enrolled:
        done = db.execute('SELECT COUNT(*) FROM progress WHERE user_id=? AND course_id=?',
                          (uid, cid)).fetchone()[0]
        progress[cid] = {'done': done, 'total': course_total(cid)}
    invite_url = f"{BASE_URL}/invite/{user['invite_token']}" if user['invite_token'] else None
    return render_template('admin_user.html', user=user, enrolled=enrolled,
                           progress=progress, courses=COURSES, invite_url=invite_url)

@app.route('/admin/user/<int:uid>/strengths')
@admin_required
def admin_user_strengths(uid):
    import json
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE id=?', (uid,)).fetchone()
    if not user:
        return redirect(url_for('admin'))
    # Exam results
    exams = {}
    for cid, course in COURSES.items():
        attempts = db.execute(
            'SELECT score, total, passed, completed_at FROM exam_attempts WHERE user_id=? AND course_id=? ORDER BY completed_at DESC',
            (uid, cid)).fetchall()
        best = db.execute(
            'SELECT MAX(score) FROM exam_attempts WHERE user_id=? AND course_id=? AND passed=1',
            (uid, cid)).fetchone()[0]
        exams[cid] = {'attempts': attempts, 'best': best, 'course': course}
    # Assessment
    assessment = db.execute(
        'SELECT * FROM assessments WHERE user_id=? ORDER BY created_at DESC LIMIT 1',
        (uid,)).fetchone()
    assessment_data = None
    domain_scores = {}
    if assessment:
        from assessment_content import ASSESSMENT_SECTIONS, RATING_LABELS, get_competency
        responses = json.loads(assessment['responses'])
        for section in ASSESSMENT_SECTIONS:
            if section['type'] == 'rated':
                scores = []
                for q in section['questions']:
                    val = responses.get(q['id'])
                    if val and val != 'na':
                        try: scores.append(int(val))
                        except: pass
                if scores:
                    avg = round(sum(scores)/len(scores), 2)
                    domain_scores[section['title']] = {'avg': avg, 'competency': get_competency(avg)}
        assessment_data = {'responses': responses, 'completed_at': assessment['created_at'][:10]}
    # Progress
    progress = {}
    for cid in COURSES:
        done = db.execute('SELECT COUNT(*) FROM progress WHERE user_id=? AND course_id=?',
                          (uid, cid)).fetchone()[0]
        progress[cid] = {'done': done, 'total': course_total(cid)}
    return render_template('admin_user_strengths.html',
        user=user, exams=exams, domain_scores=domain_scores,
        assessment_data=assessment_data, progress=progress, courses=COURSES)

@app.route('/admin/user/<int:uid>/enrol', methods=['POST'])
@admin_required
def admin_enrol(uid):
    course_id = request.form.get('course_id')
    if course_id in COURSES:
        db = get_db()
        db.execute('INSERT OR IGNORE INTO enrolments (user_id,course_id) VALUES (?,?)', (uid, course_id))
        db.commit()
        flash(f'Enrolled in {COURSES[course_id]["title"]}.', 'info')
    return redirect(url_for('admin_user', uid=uid))

@app.route('/admin/user/<int:uid>/unenrol', methods=['POST'])
@admin_required
def admin_unenrol(uid):
    course_id = request.form.get('course_id')
    db = get_db()
    db.execute('DELETE FROM enrolments WHERE user_id=? AND course_id=?', (uid, course_id))
    db.commit()
    flash('Unenrolled.', 'info')
    return redirect(url_for('admin_user', uid=uid))

@app.route('/admin/users/bulk-delete', methods=['POST'])
@admin_required
def admin_bulk_delete():
    user_ids = request.form.getlist('user_ids')
    if not user_ids:
        flash('No students selected.', 'error')
        return redirect(url_for('admin'))
    db = get_db()
    count = 0
    for uid in user_ids:
        try:
            uid = int(uid)
            user = db.execute('SELECT id FROM users WHERE id=? AND is_admin=0', (uid,)).fetchone()
            if user:
                db.execute('DELETE FROM progress WHERE user_id=?', (uid,))
                db.execute('DELETE FROM enrolments WHERE user_id=?', (uid,))
                db.execute('DELETE FROM bookmarks WHERE user_id=?', (uid,))
                db.execute('DELETE FROM exam_attempts WHERE user_id=?', (uid,))
                db.execute('DELETE FROM feedback WHERE user_id=?', (uid,))
                db.execute('DELETE FROM campaign_students WHERE user_id=?', (uid,))
                db.execute('DELETE FROM users WHERE id=?', (uid,))
                count += 1
        except (ValueError, Exception):
            pass
    db.commit()
    flash(f'{count} student(s) deleted.', 'info')
    return redirect(url_for('admin'))

@app.route('/admin/user/<int:uid>/delete', methods=['POST'])
@admin_required
def admin_delete(uid):
    db = get_db()
    db.execute('DELETE FROM progress WHERE user_id=?', (uid,))
    db.execute('DELETE FROM enrolments WHERE user_id=?', (uid,))
    db.execute('DELETE FROM users WHERE id=?', (uid,))
    db.commit()
    flash('Student deleted.', 'info')
    return redirect(url_for('admin'))

# ── Exams ────────────────────────────────────────────────────────────────────
@app.route('/exam/<course_id>')
@login_required
def exam(course_id):
    if course_id not in COURSES:
        return redirect(url_for('my_courses'))
    db = get_db()
    enrolment = db.execute('SELECT 1 FROM enrolments WHERE user_id=? AND course_id=?',
                           (session['user_id'], course_id)).fetchone()
    if not enrolment and not session.get('is_admin'):
        return redirect(url_for('my_courses'))
    # Get attempt history
    attempts = db.execute('''SELECT score, total, passed, completed_at FROM exam_attempts
                             WHERE user_id=? AND course_id=? ORDER BY completed_at DESC''',
                          (session['user_id'], course_id)).fetchall()
    best = None
    if attempts:
        best = max(attempts, key=lambda a: a['score'])
    passed = any(a['passed'] for a in attempts)
    # Pick 25 random questions
    import random, json
    questions = EXAM_QUESTIONS.get(course_id, [])
    selected = random.sample(questions, min(25, len(questions)))
    # Shuffle options and strip answer from client-side data
    client_questions = []
    for q in selected:
        opts = q['options'][:]
        random.shuffle(opts)
        client_questions.append({
            'q': q['q'],
            'shuffled_options': opts,
            'answer': q['answer']  # needed for submit matching, stripped in template
        })
    # Strip answers for JS (keep for server-side submit)
    js_questions = [{'q': q['q'], 'shuffled_options': q['shuffled_options']} for q in client_questions]
    return render_template('exam.html',
        course=COURSES[course_id],
        questions=client_questions,
        js_questions=js_questions,
        attempts=attempts,
        best=best,
        passed=passed,
        user_name=session['user_name'],
        is_admin=session.get('is_admin', False))

@app.route('/api/exam/submit', methods=['POST'])
@login_required
def api_exam_submit():
    import json
    try:
        data = request.get_json(force=True)
    except Exception as e:
        app.logger.error(f'Exam submit JSON parse error: {e}')
        return jsonify({'error': 'Invalid JSON'}), 400
    if not data:
        app.logger.error('Exam submit: no data received')
        return jsonify({'error': 'No data'}), 400
    app.logger.info(f'Exam submit received: course={data.get("course_id")}, questions={len(data.get("questions",[]))}')
    course_id = data.get('course_id')
    answers = data.get('answers', {})
    if course_id not in COURSES:
        return jsonify({'error': 'Invalid course'}), 400
    db = get_db()
    questions = EXAM_QUESTIONS.get(course_id, [])
    selected_qs = data.get('questions', [])
    # Build answer lookup from server-side question bank
    answer_lookup = {q['q']: q['answer'] for q in EXAM_QUESTIONS.get(course_id, [])}
    score = 0
    results = []
    for q in selected_qs:
        correct = answer_lookup.get(q['q'], '')
        given = answers.get(q['q'], '')
        is_correct = given == correct
        if is_correct:
            score += 1
        results.append({'q': q['q'], 'correct': correct, 'given': given, 'is_correct': is_correct})
    total = len(selected_qs)
    passed = score >= int(total * 0.8)
    db.execute('''INSERT INTO exam_attempts (user_id, course_id, score, total, passed, started_at, completed_at)
                  VALUES (?,?,?,?,?,?,?)''',
               (session['user_id'], course_id, score, total, 1 if passed else 0,
                data.get('started_at'), datetime.utcnow().isoformat()))
    db.commit()
    return jsonify({'score': score, 'total': total, 'passed': passed, 'results': results,
                    'pct': int(score/total*100) if total else 0})

# ── Campaigns ────────────────────────────────────────────────────────────────
@app.route('/admin/campaigns')
@admin_required
def admin_campaigns():
    db = get_db()
    today = datetime.utcnow().strftime('%Y-%m-%d')
    campaigns = db.execute('SELECT * FROM campaigns ORDER BY start_date DESC').fetchall()
    camp_list = []
    for c in campaigns:
        count = db.execute('SELECT COUNT(*) FROM campaign_students WHERE campaign_id=?', (c['id'],)).fetchone()[0]
        if c['end_date'] < today:
            status = 'ended'
        elif c['start_date'] > today:
            status = 'upcoming'
        else:
            status = 'active'
        camp_list.append({
            'id': c['id'], 'name': c['name'],
            'start_date': c['start_date'], 'end_date': c['end_date'],
            'report_emails': c['report_emails'],
            'student_count': count, 'status': status,
        })
    return render_template('admin_campaigns.html', campaigns=camp_list)

@app.route('/admin/campaigns/create', methods=['POST'])
@admin_required
def admin_campaign_create():
    name = request.form.get('name','').strip()
    start_date = request.form.get('start_date','').strip()
    end_date = request.form.get('end_date','').strip()
    report_emails = request.form.get('report_emails','').strip()
    if not name or not start_date or not end_date:
        flash('Name, start date and end date are required.', 'error')
        return redirect(url_for('admin_campaigns'))
    db = get_db()
    db.execute('INSERT INTO campaigns (name, start_date, end_date, report_emails) VALUES (?,?,?,?)',
               (name, start_date, end_date, report_emails))
    db.commit()
    flash(f'Campaign "{name}" created.', 'info')
    return redirect(url_for('admin_campaigns'))

@app.route('/admin/campaigns/<int:cid>')
@admin_required
def admin_campaign_detail(cid):
    db = get_db()
    campaign = db.execute('SELECT * FROM campaigns WHERE id=?', (cid,)).fetchone()
    if not campaign:
        return redirect(url_for('admin_campaigns'))
    students = db.execute('''
        SELECT u.id, u.name, u.email, u.activated_at, u.invite_token, u.password_hash, u.created_at
        FROM users u JOIN campaign_students cs ON cs.user_id=u.id
        WHERE cs.campaign_id=? AND u.is_admin=0 ORDER BY u.name
    ''', (cid,)).fetchall()
    student_ids = [s['id'] for s in students]
    all_students = db.execute('SELECT id, name, email FROM users WHERE is_admin=0 ORDER BY name').fetchall()
    return render_template('admin_campaign_detail.html',
        campaign=campaign, students=students,
        student_ids=student_ids, all_students=all_students,
        courses=COURSES)

@app.route('/admin/campaigns/<int:cid>/bulk-invite', methods=['POST'])
@admin_required
def admin_campaign_bulk_invite(cid):
    campaign = get_db().execute('SELECT * FROM campaigns WHERE id=?', (cid,)).fetchone()
    if not campaign:
        return redirect(url_for('admin_campaigns'))
    bulk_list = request.form.get('bulk_list', '').strip()
    courses = request.form.getlist('courses')
    if not bulk_list or not courses:
        flash('Please provide students and select at least one course.', 'error')
        return redirect(url_for('admin_campaign_detail', cid=cid))
    db = get_db()
    sent = 0
    skipped = 0
    errors = []
    for line in bulk_list.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split(',', 1)]
        if len(parts) != 2:
            errors.append(f'Invalid format: {line}')
            continue
        name, email = parts
        if not name or not email or '@' not in email:
            errors.append(f'Invalid entry: {line}')
            continue
        # Check if already exists
        existing = db.execute('SELECT id FROM users WHERE email=?', (email,)).fetchone()
        if existing:
            uid = existing['id']
            # Add to campaign if not already
            already = db.execute('SELECT 1 FROM campaign_students WHERE campaign_id=? AND user_id=?',
                                 (cid, uid)).fetchone()
            if not already:
                db.execute('INSERT INTO campaign_students (campaign_id, user_id) VALUES (?,?)', (cid, uid))
            skipped += 1
            continue
        import secrets
        token = secrets.token_urlsafe(32)
        db.execute('INSERT INTO users (name, email, invite_token) VALUES (?,?,?)', (name, email, token))
        uid = db.execute('SELECT last_insert_rowid()').fetchone()[0]
        for course_id in courses:
            if course_id in COURSES:
                db.execute('INSERT OR IGNORE INTO enrolments (user_id, course_id) VALUES (?,?)', (uid, course_id))
        db.execute('INSERT OR IGNORE INTO campaign_students (campaign_id, user_id) VALUES (?,?)', (cid, uid))
        invite_url = f"{BASE_URL}/invite/{token}"
        try:
            send_invite_email(name, email, invite_url, courses)
            sent += 1
        except Exception as e:
            errors.append(f'Email failed for {email}: {e}')
    db.commit()
    msg = f'{sent} invite(s) sent.'
    if skipped:
        msg += f' {skipped} already existed (added to campaign).'
    if errors:
        msg += f' Errors: {"; ".join(errors)}'
    flash(msg, 'info')
    return redirect(url_for('admin_campaign_detail', cid=cid))

@app.route('/admin/campaigns/<int:cid>/invite', methods=['POST'])
@admin_required
def admin_campaign_invite(cid):
    db = get_db()
    campaign = db.execute('SELECT * FROM campaigns WHERE id=?', (cid,)).fetchone()
    if not campaign:
        return redirect(url_for('admin_campaigns'))
    name = request.form.get('name','').strip()
    email = request.form.get('email','').strip().lower()
    course_ids = request.form.getlist('courses')
    if not course_ids:
        course_ids = list(COURSES.keys())
    if not name or not email:
        flash('Name and email are required.', 'error')
        return redirect(url_for('admin_campaign_detail', cid=cid))
    existing = db.execute('SELECT id FROM users WHERE email=?', (email,)).fetchone()
    if existing:
        uid = existing['id']
    else:
        token = secrets.token_urlsafe(32)
        db.execute('INSERT INTO users (email,name,invite_token,invited_at) VALUES (?,?,?,?)',
                   (email, name, token, datetime.utcnow().isoformat()))
        db.commit()
        uid = db.execute('SELECT id FROM users WHERE email=?', (email,)).fetchone()['id']
        for course_id in course_ids:
            if course_id in COURSES:
                db.execute('INSERT OR IGNORE INTO enrolments (user_id,course_id) VALUES (?,?)', (uid, course_id))
        db.commit()
        invite_url = f"{BASE_URL}/invite/{token}"
        send_invite_email(name, email, course_ids, invite_url)
        flash(f'Invite sent to {email}.', 'info')
    db.execute('INSERT OR IGNORE INTO campaign_students (campaign_id, user_id) VALUES (?,?)', (cid, uid))
    db.commit()
    return redirect(url_for('admin_campaign_detail', cid=cid))

@app.route('/admin/campaigns/<int:cid>/remove_student', methods=['POST'])
@admin_required
def admin_campaign_remove_student(cid):
    uid = request.form.get('user_id')
    db = get_db()
    db.execute('DELETE FROM campaign_students WHERE campaign_id=? AND user_id=?', (cid, uid))
    db.commit()
    flash('Student removed from campaign.', 'info')
    return redirect(url_for('admin_campaign_detail', cid=cid))

@app.route('/admin/campaigns/<int:cid>/send_report', methods=['POST'])
@admin_required
def admin_campaign_send_report(cid):
    import subprocess
    subprocess.Popen(['/home/ubuntu/app/venv/bin/python3',
                      '/home/ubuntu/app/send_report.py', str(cid)])
    flash('Report is being generated and sent.', 'info')
    return redirect(url_for('admin_campaign_detail', cid=cid))

@app.route('/admin/campaigns/<int:cid>/unenrol', methods=['POST'])
@admin_required
def admin_campaign_unenrol(cid):
    uid = int(request.form.get('user_id'))
    course_id = request.form.get('course_id')
    db = get_db()
    db.execute('DELETE FROM enrolments WHERE user_id=? AND course_id=?', (uid, course_id))
    db.commit()
    flash('Student unenrolled from course.', 'info')
    return redirect(url_for('admin_campaign_detail', cid=cid))

# ── Assessment ───────────────────────────────────────────────────────────────
@app.route('/assessment', methods=['GET','POST'])
@login_required
def assessment():
    db = get_db()
    existing = db.execute('SELECT * FROM assessments WHERE user_id=? ORDER BY created_at DESC LIMIT 1',
                          (session['user_id'],)).fetchone()
    if request.method == 'POST':
        import json
        responses = {}
        for key, val in request.form.items():
            if key.startswith('s'):
                responses[key] = val
        # Handle multi-select checkboxes
        for key in request.form.keys():
            vals = request.form.getlist(key)
            if len(vals) > 1:
                responses[key] = vals
        db.execute('INSERT INTO assessments (user_id, responses) VALUES (?,?)',
                   (session['user_id'], json.dumps(responses)))
        db.commit()
        flash('Assessment submitted successfully!', 'info')
        return redirect(url_for('assessment_results'))
    return render_template('assessment.html',
        sections=ASSESSMENT_SECTIONS,
        rating_labels=RATING_LABELS,
        existing=existing,
        user_name=session['user_name'])

@app.route('/assessment/results')
@login_required
def assessment_results():
    import json
    db = get_db()
    row = db.execute('SELECT * FROM assessments WHERE user_id=? ORDER BY created_at DESC LIMIT 1',
                     (session['user_id'],)).fetchone()
    if not row:
        return redirect(url_for('assessment'))
    responses = json.loads(row['responses'])
    # Calculate domain scores
    domain_scores = {}
    for section in ASSESSMENT_SECTIONS:
        if section['type'] == 'rated':
            scores = []
            for q in section['questions']:
                val = responses.get(q['id'])
                if val and val != 'na':
                    try:
                        scores.append(int(val))
                    except ValueError:
                        pass
            if scores:
                avg = round(sum(scores) / len(scores), 2)
                domain_scores[section['title']] = {
                    'avg': avg,
                    'competency': get_competency(avg),
                    'count': len(scores)
                }
    return render_template('assessment_results.html',
        sections=ASSESSMENT_SECTIONS,
        responses=responses,
        domain_scores=domain_scores,
        rating_labels=RATING_LABELS,
        completed_at=row['created_at'][:10],
        user_name=session['user_name'])

@app.route('/admin/assessments')
@admin_required
def admin_assessments():
    import json
    db = get_db()
    rows = db.execute('''SELECT a.*, u.name, u.email FROM assessments a
                         JOIN users u ON u.id=a.user_id
                         ORDER BY a.created_at DESC''').fetchall()
    students = []
    for row in rows:
        responses = json.loads(row['responses'])
        domain_scores = {}
        for section in ASSESSMENT_SECTIONS:
            if section['type'] == 'rated':
                scores = []
                for q in section['questions']:
                    val = responses.get(q['id'])
                    if val and val != 'na':
                        try:
                            scores.append(int(val))
                        except ValueError:
                            pass
                if scores:
                    avg = round(sum(scores) / len(scores), 2)
                    domain_scores[section['title']] = {'avg': avg, 'competency': get_competency(avg)}
        students.append({
            'id': row['user_id'], 'name': row['name'], 'email': row['email'],
            'completed_at': row['created_at'][:10],
            'domain_scores': domain_scores,
            'assessment_id': row['id']
        })
    return render_template('admin_assessments.html',
        students=students,
        sections=[s for s in ASSESSMENT_SECTIONS if s['type'] == 'rated'])

@app.route('/admin/assessments/<int:assessment_id>')
@admin_required
def admin_assessment_detail(assessment_id):
    import json
    db = get_db()
    row = db.execute('''SELECT a.*, u.name, u.email FROM assessments a
                        JOIN users u ON u.id=a.user_id WHERE a.id=?''', (assessment_id,)).fetchone()
    if not row:
        return redirect(url_for('admin_assessments'))
    responses = json.loads(row['responses'])
    domain_scores = {}
    for section in ASSESSMENT_SECTIONS:
        if section['type'] == 'rated':
            scores = []
            for q in section['questions']:
                val = responses.get(q['id'])
                if val and val != 'na':
                    try:
                        scores.append(int(val))
                    except ValueError:
                        pass
            if scores:
                avg = round(sum(scores) / len(scores), 2)
                domain_scores[section['title']] = {'avg': avg, 'competency': get_competency(avg)}
    return render_template('admin_assessment_detail.html',
        student_name=row['name'], student_email=row['email'],
        sections=ASSESSMENT_SECTIONS,
        responses=responses,
        domain_scores=domain_scores,
        rating_labels=RATING_LABELS,
        completed_at=row['created_at'][:10])

# ── Feedback ─────────────────────────────────────────────────────────────────
@app.route('/feedback/<course_id>', methods=['GET','POST'])
@login_required
def feedback(course_id):
    if course_id not in COURSES:
        return redirect(url_for('my_courses'))
    db = get_db()
    # Check exam passed
    exam_pass = db.execute(
        'SELECT 1 FROM exam_attempts WHERE user_id=? AND course_id=? AND passed=1',
        (session['user_id'], course_id)).fetchone()
    if not exam_pass and not session.get('is_admin'):
        return redirect(url_for('exam', course_id=course_id))
    # Check if already submitted feedback
    existing = db.execute(
        'SELECT 1 FROM feedback WHERE user_id=? AND course_id=?',
        (session['user_id'], course_id)).fetchone()
    if request.method == 'POST':
        satisfaction = request.form.get('satisfaction', 0)
        suggestions = request.form.get('suggestions', '').strip()
        if not existing:
            db.execute('INSERT INTO feedback (user_id, course_id, satisfaction, suggestions) VALUES (?,?,?,?)',
                       (session['user_id'], course_id, satisfaction, suggestions))
            db.commit()
        return redirect(url_for('diploma', course_id=course_id))
    return render_template('feedback.html',
        course=COURSES[course_id],
        user_name=session['user_name'],
        already_submitted=bool(existing))

# ── Backup / Restore / Archive ───────────────────────────────────────────────
import shutil, glob

BACKUP_DIR = os.path.join(os.path.dirname(__file__), 'backups')
os.makedirs(BACKUP_DIR, exist_ok=True)

def get_backups():
    backups = []
    for f in sorted(glob.glob(os.path.join(BACKUP_DIR, '*.db')), reverse=True):
        fname = os.path.basename(f)
        archived = fname.startswith('archive_')
        size = os.path.getsize(f)
        mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
        backups.append({'filename': fname, 'path': f, 'archived': archived, 'size': size, 'mtime': mtime})
    return backups

def purge_old_backups():
    backups = [b for b in get_backups() if not b['archived']]
    if len(backups) > 30:
        for b in backups[30:]:
            os.remove(b['path'])

@app.route('/admin/backups')
@admin_required
def admin_backups():
    backups = get_backups()
    db_size = os.path.getsize(DATABASE)
    return render_template('admin_backups.html', backups=backups, db_size=db_size)

@app.route('/admin/backups/create', methods=['POST'])
@admin_required
def admin_backup_create():
    ts = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    dest = os.path.join(BACKUP_DIR, f'backup_{ts}.db')
    shutil.copy2(DATABASE, dest)
    purge_old_backups()
    flash(f'Backup created: backup_{ts}.db', 'info')
    return redirect(url_for('admin_backups'))

@app.route('/admin/backups/restore', methods=['POST'])
@admin_required
def admin_backup_restore():
    filename = request.form.get('filename', '')
    if not filename or '..' in filename or '/' in filename:
        flash('Invalid filename.', 'error')
        return redirect(url_for('admin_backups'))
    src = os.path.join(BACKUP_DIR, filename)
    if not os.path.exists(src):
        flash('Backup file not found.', 'error')
        return redirect(url_for('admin_backups'))
    # Backup current db before restoring
    ts = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    shutil.copy2(DATABASE, os.path.join(BACKUP_DIR, f'pre_restore_{ts}.db'))
    shutil.copy2(src, DATABASE)
    flash(f'Database restored from {filename}. Previous state saved as pre_restore_{ts}.db', 'info')
    return redirect(url_for('admin_backups'))

@app.route('/admin/backups/archive', methods=['POST'])
@admin_required
def admin_backup_archive():
    filename = request.form.get('filename', '')
    if not filename or '..' in filename or '/' in filename:
        flash('Invalid filename.', 'error')
        return redirect(url_for('admin_backups'))
    src = os.path.join(BACKUP_DIR, filename)
    if not os.path.exists(src):
        flash('Backup file not found.', 'error')
        return redirect(url_for('admin_backups'))
    if not filename.startswith('archive_'):
        new_name = 'archive_' + filename
        dest = os.path.join(BACKUP_DIR, new_name)
        os.rename(src, dest)
        flash(f'Backup archived as {new_name}', 'info')
    return redirect(url_for('admin_backups'))

@app.route('/admin/backups/delete', methods=['POST'])
@admin_required
def admin_backup_delete():
    filename = request.form.get('filename', '')
    if not filename or '..' in filename or '/' in filename:
        flash('Invalid filename.', 'error')
        return redirect(url_for('admin_backups'))
    src = os.path.join(BACKUP_DIR, filename)
    if os.path.exists(src):
        os.remove(src)
        flash(f'Backup {filename} deleted.', 'info')
    return redirect(url_for('admin_backups'))

@app.route('/admin/backups/download/<filename>')
@admin_required
def admin_backup_download(filename):
    if '..' in filename or '/' in filename:
        return 'Invalid filename', 400
    from flask import send_file
    path = os.path.join(BACKUP_DIR, filename)
    if not os.path.exists(path):
        return 'File not found', 404
    return send_file(path, as_attachment=True, download_name=filename)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

init_db()

@app.route('/diploma/<course_id>')
@login_required
def diploma(course_id):
    if course_id not in COURSES:
        return redirect(url_for('my_courses'))
    db = get_db()
    enrolment = db.execute('SELECT 1 FROM enrolments WHERE user_id=? AND course_id=?',
                           (session['user_id'], course_id)).fetchone()
    if not enrolment and not session.get('is_admin'):
        return redirect(url_for('my_courses'))
    total = course_total(course_id)
    done = db.execute('SELECT COUNT(*) FROM progress WHERE user_id=? AND course_id=?',
                      (session['user_id'], course_id)).fetchone()[0]
    # Check exam pass — exam pass is required, lesson completion is not
    exam_pass = db.execute(
        'SELECT 1 FROM exam_attempts WHERE user_id=? AND course_id=? AND passed=1',
        (session['user_id'], course_id)).fetchone()
    if not exam_pass and not session.get('is_admin'):
        flash('You must pass the course exam to unlock your certificate.', 'error')
        return redirect(url_for('exam', course_id=course_id))
    last = db.execute('''SELECT completed_at FROM progress WHERE user_id=? AND course_id=?
                         ORDER BY completed_at DESC LIMIT 1''',
                      (session['user_id'], course_id)).fetchone()
    completed_date = last['completed_at'][:10] if last else datetime.utcnow().strftime('%Y-%m-%d')
    return render_template('diploma.html',
        course=COURSES[course_id],
        user_name=session['user_name'],
        lessons_completed=total,
        completed_date=completed_date)

