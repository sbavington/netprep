import os, sqlite3, hashlib, secrets, smtplib
from dotenv import load_dotenv
load_dotenv()
from datetime import datetime
from functools import wraps
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from network_content import LESSON_CONTENT as NET_CONTENT
from tp_content import LESSON_CONTENT as TP_CONTENT
from ddi_content import LESSON_CONTENT as DDI_CONTENT
from flask import (Flask, render_template, request, redirect,
                   url_for, session, jsonify, flash, g)

app = Flask(__name__)

from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(32))

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
                {"id":"1-3","title":"How data encapsulation works","type":"concept"},
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
                {"id":"3-4","title":"Spanning Tree Protocol (STP)","type":"concept"},
                {"id":"3-5","title":"Routing lab","type":"lab"},
            ]},
            {"id":4,"title":"Network Services","icon":"⚙️","hours":5,"lessons":[
                {"id":"4-1","title":"DNS — how name resolution works","type":"concept"},
                {"id":"4-2","title":"DHCP — dynamic address assignment","type":"concept"},
                {"id":"4-3","title":"NAT and PAT explained","type":"concept"},
                {"id":"4-4","title":"NTP — why time synchronisation matters","type":"concept"},
                {"id":"4-5","title":"Network services lab","type":"lab"},
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
                {"id":"6-3","title":"Wireless site survey basics","type":"concept"},
                {"id":"6-4","title":"Wireless troubleshooting","type":"lab"},
            ]},
            {"id":7,"title":"Cloud & Virtualisation","icon":"☁️","hours":4,"lessons":[
                {"id":"7-1","title":"Cloud service models — IaaS, PaaS, SaaS","type":"concept"},
                {"id":"7-2","title":"SDN and network virtualisation","type":"concept"},
                {"id":"7-3","title":"Virtual networking components","type":"concept"},
                {"id":"7-4","title":"Cloud networking lab","type":"lab"},
            ]},
            {"id":8,"title":"Troubleshooting & Diagnostics","icon":"🔬","hours":6,"lessons":[
                {"id":"8-1","title":"Troubleshooting methodology","type":"concept"},
                {"id":"8-2","title":"ping, traceroute, nslookup, netstat","type":"concept"},
                {"id":"8-3","title":"Wireshark basics — reading packet captures","type":"concept"},
                {"id":"8-4","title":"Common connectivity issues and fixes","type":"concept"},
                {"id":"8-5","title":"Network+ practice exam (50 questions)","type":"quiz"},
                {"id":"8-6","title":"Final troubleshooting lab","type":"lab"},
            ]},
        ]
    },
    'tippingpoint': {
        'id': 'tippingpoint',
        'title': 'TippingPoint IPS',
        'subtitle': 'Trend Micro · Installation & Configuration',
        'icon': '🛡️',
        'color': '#ff6b35',
        'hours': 38,
        'modules': [
            {"id":1,"title":"Introduction to TippingPoint & IPS","icon":"🛡️","hours":3,"lessons":[
                {"id":"tp-1-1","title":"What is TippingPoint? IPS vs IDS vs Firewall","type":"concept"},
                {"id":"tp-1-2","title":"TippingPoint product family overview","type":"concept"},
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
                {"id":"tp-7-2","title":"Configuring HA pairs","type":"concept"},
                {"id":"tp-7-3","title":"Testing failover and resilience","type":"concept"},
                {"id":"tp-7-4","title":"HA configuration lab","type":"lab"},
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
        'subtitle': 'Trend Micro · APT Detection & Response',
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
        course_names = ', '.join(COURSES[c]['title'] for c in course_ids if c in COURSES)
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f"You've been invited to {course_names}"
        msg['From'] = FROM_EMAIL
        msg['To'] = to_email
        text = f"""Hi {to_name},

You have been invited to the following course(s) on NetPrep:
{course_names}

Click the link below to set your password and get started:
{invite_url}

This link is unique to you — please do not share it.

NetPrep Training Platform
"""
        html = f"""<html><body style="font-family:sans-serif;background:#0a0f1e;color:#e2e8f0;padding:40px;">
<div style="max-width:500px;margin:0 auto;background:#111827;border-radius:12px;padding:32px;border:1px solid #1e293b;">
<h2 style="color:#00d4ff;margin-top:0;">You've been invited to NetPrep</h2>
<p>Hi <strong>{to_name}</strong>,</p>
<p>You have been enrolled in:</p>
<p style="font-size:18px;color:#00d4ff;font-weight:bold;">{course_names}</p>
<p>Click below to set your password and start learning:</p>
<a href="{invite_url}" style="display:inline-block;background:#00d4ff;color:#000;padding:12px 24px;border-radius:8px;text-decoration:none;font-weight:bold;margin:16px 0;">Accept Invitation →</a>
<p style="color:#64748b;font-size:12px;margin-top:24px;">This link is unique to you. If you didn't expect this email, you can ignore it.</p>
</div></body></html>"""
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

# ── Auth ──────────────────────────────────────────────────────────────────────
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
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

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email','').strip().lower()
        password = request.form.get('password','')
        db = get_db()
        user = db.execute('SELECT * FROM users WHERE email=?', (email,)).fetchone()
        if user and user['password_hash'] and check_password(user['password_hash'], password):
            session.clear()
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
        course_data.append({
            'course': COURSES[cid],
            'total': total,
            'done': done,
            'pct': int(done/total*100) if total else 0,
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
    course = COURSES[course_id]
    total = course_total(course_id)
    done_count = len(completed)
    pct = int(done_count / total * 100) if total else 0
    from flask import make_response
    resp = make_response(render_template('curriculum.html',
        course=course, modules=course['modules'],
        completed=completed, total=total,
        done_count=done_count, pct=pct,
        user_name=session['user_name'],
        lesson_content=CONTENT.get(course_id, {}),
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
@app.route('/admin')
@admin_required
def admin():
    db = get_db()
    users = db.execute('''
        SELECT u.id, u.name, u.email, u.invite_token, u.activated_at, u.created_at
        FROM users u WHERE u.is_admin=0 ORDER BY u.created_at DESC
    ''').fetchall()
    students = []
    for u in users:
        enrolments = db.execute('SELECT course_id FROM enrolments WHERE user_id=?', (u['id'],)).fetchall()
        enrolled_courses = [e['course_id'] for e in enrolments]
        total_lessons = sum(course_total(c) for c in enrolled_courses)
        done = db.execute('SELECT COUNT(*) FROM progress WHERE user_id=?', (u['id'],)).fetchone()[0]
        students.append({
            'id': u['id'], 'name': u['name'], 'email': u['email'],
            'courses': enrolled_courses,
            'lessons_done': done, 'total_lessons': total_lessons,
            'is_active': u['activated_at'] is not None,
            'invite_token': u['invite_token'],
            'created_at': u['created_at'] or '',
        })
    return render_template('admin.html', users=students, courses=COURSES)

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
    if done < total and not session.get('is_admin'):
        flash('Complete all lessons to unlock your certificate.', 'error')
        return redirect(url_for('curriculum', course_id=course_id))
    last = db.execute('''SELECT completed_at FROM progress WHERE user_id=? AND course_id=?
                         ORDER BY completed_at DESC LIMIT 1''',
                      (session['user_id'], course_id)).fetchone()
    completed_date = last['completed_at'][:10] if last else datetime.utcnow().strftime('%Y-%m-%d')
    return render_template('diploma.html',
        course=COURSES[course_id],
        user_name=session['user_name'],
        lessons_completed=done,
        completed_date=completed_date)

