# NetPrep — Security Training Platform

A self-hosted training platform for Trend Micro and networking courses. Single login, multiple course tracks, invite-based enrolment, and email notifications via AWS SES.

## Courses

| Course | Topics | Lessons | Hours |
|--------|--------|---------|-------|
| 🌐 TCP/IP Networking | OSI model, subnetting, routing, switching, security, wireless, cloud, troubleshooting | 40 | ~40h |
| 🛡️ TippingPoint IPS | Hardware install, CLI, SMS, security policies, Digital Vaccine, HA, SIEM integration | 37 | ~38h |
| 🔎 Deep Discovery Inspector | Hardware install, initial config, detection policies, Virtual Analyzer, reporting, HA, SIEM | 36 | ~38h |

## Features

- **Invite-based authentication** — admin generates invite links, students set their own password
- **Multi-course enrolment** — students can be enrolled in one or all courses from a single account
- **Progress tracking** — per-course lesson completion tracking
- **Bulk invite** — paste a list of names and emails to invite multiple students at once
- **Email notifications** — invite emails sent via AWS SES when students are invited
- **Admin dashboard** — manage students, view progress, enrol/unenrol per course
- **Lesson content** — study notes, key terms, practice questions, and resource links per lesson

## Stack

- Python 3 / Flask
- SQLite
- Gunicorn
- Nginx (reverse proxy)
- AWS SES (email)
- CloudFront + ACM (HTTPS)
- Route 53 (DNS)

## Deployment

### Prerequisites

- Ubuntu 24.04 LTS server (AWS EC2 t3.micro recommended)
- Python 3.12+
- Nginx
- Domain name pointed at server

### Install

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip python3-venv nginx unzip

cd ~
unzip netprep.zip
mv netprep app
cd app

python3 -m venv venv
source venv/bin/activate
pip install flask gunicorn python-dotenv
```

### Configure

```bash
cp .env.example .env
nano .env
```

Edit `.env`:

```env
SECRET_KEY=your_long_random_secret_key
BASE_URL=https://netprep.org

# AWS SES SMTP (leave blank to disable email)
SES_SMTP_HOST=email-smtp.us-east-1.amazonaws.com
SES_SMTP_PORT=587
SES_SMTP_USER=your_ses_smtp_username
SES_SMTP_PASS=your_ses_smtp_password
FROM_EMAIL=noreply@netprep.org
```

### Initialise database

```bash
python3 -c "from app import app, init_db; init_db(); print('OK')"
deactivate
```

### Systemd service

```bash
sudo tee /etc/systemd/system/netprep.service << 'EOF'
[Unit]
Description=NetPrep Training Platform
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/app
Environment="PATH=/home/ubuntu/app/venv/bin"
EnvironmentFile=/home/ubuntu/app/.env
ExecStart=/home/ubuntu/app/venv/bin/gunicorn -w 2 -b 127.0.0.1:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable netprep
sudo systemctl start netprep
```

### Nginx

```bash
sudo tee /etc/nginx/sites-available/netprep << 'EOF'
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        client_max_body_size 10M;
    }
}
EOF

sudo ln -s /etc/nginx/sites-available/netprep /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t && sudo systemctl restart nginx
```

## AWS SES Setup

1. Go to **SES → Verified identities → Create identity**
2. Identity type: **Domain**, enter `netprep.org`
3. Add the CNAME records to Route 53
4. Go to **SES → SMTP settings → Create SMTP credentials**
5. Copy the username and password into `.env`
6. If account is in sandbox mode, request production access

## HTTPS with CloudFront + ACM

1. **ACM (us-east-1 only)** — request a public cert for `netprep.org` and `www.netprep.org`, DNS validation, create records in Route 53
2. **Elastic IP** — allocate and associate with EC2 instance
3. **Route 53** — create A record `origin.netprep.org` → Elastic IP
4. **CloudFront** — create distribution, origin: `origin.netprep.org`, HTTP only, cache policy: CachingDisabled, alternate CNAMEs: `netprep.org` + `www.netprep.org`, SSL cert: ACM cert from us-east-1
5. **Route 53** — create A alias records for `netprep.org` and `www.netprep.org` → CloudFront distribution

## Admin Credentials

Default admin account created on first run:

- **Email:** `admin@netprep.org`
- **Password:** `changeme123`

Change the password immediately after first login.

## Troubleshooting

**Service won't start:**
```bash
sudo journalctl -u netprep -n 50 --no-pager
```

**Pattern updates / content not loading:**
```bash
sudo systemctl restart netprep
```

**Database reset:**
```bash
cd ~/app
rm netprep.db
python3 -c "from app import app, init_db; init_db()"
sudo systemctl restart netprep
```

## File Structure

```
app/
├── app.py                 # Main Flask application
├── network_content.py     # TCP/IP Networking lesson content
├── tp_content.py          # TippingPoint IPS lesson content
├── ddi_content.py         # Deep Discovery Inspector lesson content
├── templates/
│   ├── base.html          # Base template
│   ├── login.html         # Login page
│   ├── my_courses.html    # Student course selection
│   ├── curriculum.html    # Course curriculum and lessons
│   ├── admin.html         # Admin dashboard
│   ├── admin_user.html    # Student detail view
│   ├── accept_invite.html # Invite acceptance / password set
│   └── set_password.html  # Password change
├── requirements.txt
├── .env.example
└── .gitignore
```
