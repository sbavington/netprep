LESSON_CONTENT = {
    "1-1": {
        "notes": "TippingPoint is an Intrusion Prevention System (IPS) made by Trend Micro. Unlike a firewall, which controls access based on rules about who can connect where, an IPS inspects the actual content of network traffic and blocks attacks in real time. Unlike an IDS (Intrusion Detection System), which only alerts you when it sees something suspicious, an IPS sits inline in the network and actively drops malicious packets before they reach their destination.\n\nThink of it this way: a firewall is a bouncer checking IDs at the door, an IDS is a security camera that records incidents, and an IPS is a guard that physically stops attacks as they happen. TippingPoint combines deep packet inspection with a continuously updated threat intelligence database (Digital Vaccine) to stop exploits, malware, and attacks across thousands of known vulnerabilities — without requiring you to manually write rules for each one.",
        "terms": [
            ("IPS", "Intrusion Prevention System — inline device that inspects and blocks malicious traffic in real time"),
            ("IDS", "Intrusion Detection System — monitors traffic and generates alerts but does not block"),
            ("Inline Mode", "Device sits directly in the traffic path; can drop packets before they reach the destination"),
            ("Deep Packet Inspection", "Examining packet payloads (not just headers) to identify threats and attacks"),
            ("TippingPoint", "Trend Micro's IPS product line, formerly owned by 3Com and HP"),
            ("Digital Vaccine (DV)", "TippingPoint's threat intelligence filter package, updated regularly by Trend Micro"),
        ],
        "questions": [
            ("What is the key difference between an IPS and an IDS?", "An IPS actively blocks threats inline; an IDS only detects and alerts without blocking"),
            ("Why is TippingPoint placed inline in the network?", "So it can inspect and drop malicious packets before they reach their destination"),
            ("What is the Digital Vaccine?", "TippingPoint's regularly updated filter package containing signatures and rules for thousands of known threats"),
        ],
        "links": [
            ("Trend Micro TippingPoint Overview", "https://www.trendmicro.com/en_us/business/products/network/intrusion-prevention.html"),
            ("Cloudflare — What is an IPS?", "https://www.cloudflare.com/learning/security/glossary/intrusion-detection-prevention/"),
            ("NIST — IPS Guide", "https://csrc.nist.gov/publications/detail/sp/800-94/final"),
        ]
    },
    "1-2": {
        "notes": "The TippingPoint product family includes several hardware appliances designed for different network speeds and deployment scenarios. The TPS (Threat Protection System) series is the current generation, available in models ranging from 100Mbps to 100Gbps throughput. The older IPS series (2500N, 5100N, 8200ZX etc.) is still widely deployed. The Virtual TPS (vTPS) runs as a virtual machine for cloud and virtualised environments.\n\nAll TippingPoint devices share the same core architecture: high-speed custom ASICs for packet processing, a management plane running Linux, and the SMS (Security Management System) for centralised management of multiple devices. The TX Series represents the latest generation with enhanced performance and cloud integration. Understanding which platform you're working with matters because CLI commands, hardware ports, and capabilities differ between generations.",
        "terms": [
            ("TPS", "Threat Protection System — current generation TippingPoint hardware appliances"),
            ("vTPS", "Virtual TippingPoint — software IPS for virtualised and cloud environments"),
            ("SMS", "Security Management System — centralised management console for TippingPoint devices"),
            ("ASIC", "Application-Specific Integrated Circuit — custom hardware enabling line-rate packet inspection"),
            ("Throughput", "The maximum traffic speed the device can inspect; e.g. 1Gbps, 10Gbps"),
            ("TX Series", "Latest generation TippingPoint appliances with enhanced performance"),
        ],
        "questions": [
            ("What is the SMS?", "Security Management System — the centralised console used to manage multiple TippingPoint devices from one place"),
            ("What is vTPS?", "Virtual TippingPoint — a software version of the IPS that runs in virtual and cloud environments"),
            ("Why does TippingPoint use custom ASICs?", "To perform deep packet inspection at line rate without introducing significant latency"),
        ],
        "links": [
            ("Trend Micro TippingPoint Datasheet", "https://www.trendmicro.com/en_us/business/products/network/intrusion-prevention.html"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
        ]
    },
    "1-3": {
        "notes": "TippingPoint operates in Layer 2 bridge mode — it is completely transparent to the network. Traffic flows into one segment port and out another, and the device is invisible to everything around it (no IP address on the data path interfaces). This means you can insert TippingPoint into an existing network without changing IP addresses, routing, or any other configuration on surrounding devices.\n\nWhen a packet arrives, TippingPoint's inspection engine checks it against all active Digital Vaccine filters simultaneously using parallel processing. If the packet matches a threat filter with a Block action set, it is dropped and a log entry is created. If it matches a Rate Limit filter, bandwidth is restricted. If no filter matches, or if the filter action is Permit, the packet passes through unmodified. The entire process happens in microseconds. Understanding this traffic flow is essential for placement decisions and troubleshooting.",
        "terms": [
            ("Layer 2 Bridge", "TippingPoint's transparent inline mode — no IP on data interfaces, invisible to network"),
            ("Segment Port", "Physical port pair on TippingPoint that traffic flows through; one in, one out"),
            ("Inspection Engine", "The component that matches packets against Digital Vaccine filters"),
            ("Action Set", "The response to a filter match: Block, Permit, Rate Limit, or Notify"),
            ("Transparent Mode", "Device passes traffic without modifying it or requiring network reconfiguration"),
            ("Latency", "Delay introduced by inspection — TippingPoint is designed to minimise this"),
        ],
        "questions": [
            ("Why is TippingPoint called 'transparent'?", "Because it operates as a Layer 2 bridge with no IP on data interfaces — surrounding devices don't know it's there"),
            ("What happens to a packet that matches a Block action set?", "It is dropped and a log entry is created; it never reaches its destination"),
            ("What is a segment port?", "A physical port pair on TippingPoint through which traffic flows — one port receives traffic, the other sends it onward"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Cloudflare — What is Deep Packet Inspection?", "https://www.cloudflare.com/learning/network-layer/what-is-deep-packet-inspection/"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
        ]
    },
    "1-4": {
        "notes": "Module 1 review quiz. Make sure you can clearly explain what TippingPoint does, how it differs from a firewall and IDS, and the basic traffic flow through an inline IPS before moving on to hardware installation.",
        "terms": [
            ("IPS vs Firewall", "Firewall controls access by rules; IPS inspects content and blocks attacks"),
            ("IPS vs IDS", "IPS is inline and blocks; IDS is passive and only alerts"),
            ("Inline", "Device sits in the traffic path and can actively drop packets"),
        ],
        "questions": [
            ("What are the three possible actions TippingPoint can take on a packet?", "Block (drop it), Permit (allow it), or Rate Limit (restrict bandwidth)"),
            ("Can TippingPoint be inserted into a network without changing IP addresses?", "Yes — it operates as a transparent Layer 2 bridge"),
            ("What is the Digital Vaccine?", "Trend Micro's regularly updated filter package with signatures for thousands of known threats"),
            ("At which OSI layer does TippingPoint primarily operate?", "Layer 2 (bridge) for placement, but it inspects up to Layer 7 (application layer) for content"),
        ],
        "links": [
            ("Trend Micro TippingPoint Overview", "https://www.trendmicro.com/en_us/business/products/network/intrusion-prevention.html"),
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
        ]
    },
    "2-1": {
        "notes": "TippingPoint appliances are designed for standard 1U or 2U rack mounting. Before installation, plan your cabling carefully — the device has separate management ports and segment (data) ports. The management port connects to your management network and is used for SSH, HTTPS, and SMS communication. Segment ports connect inline in your traffic path.\n\nPhysical requirements: adequate rack space (measure U-height for your model), power (check whether the model requires redundant PSUs), and proper grounding. Cable management matters — label every cable before installation. Copper segment ports use standard Cat6 cables; fibre segment ports require the appropriate SFP modules (check whether single-mode or multimode fibre is needed for your environment). Always power down properly — never hard-power a TippingPoint device as the database may corrupt.",
        "terms": [
            ("Management Port", "Dedicated Ethernet port for SSH, HTTPS, and SMS management traffic — not in the data path"),
            ("Segment Port", "Inline data port pair through which production traffic flows"),
            ("SFP", "Small Form-factor Pluggable — transceiver module for fibre segment ports"),
            ("1U/2U", "Rack unit height measurement; 1U = 1.75 inches"),
            ("Redundant PSU", "Dual power supplies for high availability; some models support hot-swap"),
            ("Grounding", "Proper electrical grounding is required before powering on network hardware"),
        ],
        "questions": [
            ("What is the difference between a management port and a segment port on TippingPoint?", "Management port is for administration (SSH/HTTPS/SMS); segment ports carry production traffic inline"),
            ("Why should you never hard-power off a TippingPoint device?", "The internal database may corrupt, requiring a factory reset or recovery procedure"),
            ("What must you check before ordering fibre SFP modules?", "Whether the fibre runs are single-mode or multimode, and the required distance/wavelength"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Rack Unit Calculator", "https://www.racksolutions.com/news/data-center-hardware/rack-unit-explained/"),
        ]
    },
    "2-2": {
        "notes": "Network placement is one of the most important decisions when deploying TippingPoint. The device must be placed inline in the traffic path you want to protect. Common placements: between the internet router and the core switch (protects all traffic), between the DMZ and internal network (protects servers), or between network segments (east-west protection).\n\nEach physical segment port pair represents one network segment. A single TippingPoint appliance can protect multiple segments simultaneously — check your model's segment count. When planning, consider: which traffic flows need inspection, what throughput each segment carries (don't exceed the device's rated capacity), and whether you need bypass capability during maintenance. Virtual segments allow you to logically divide a physical segment and apply different policies to different traffic types.",
        "terms": [
            ("Network Segment", "A traffic flow that TippingPoint inspects inline between two network points"),
            ("Bypass Mode", "Allows traffic to pass through uninspected during maintenance or device failure"),
            ("East-West Traffic", "Traffic flowing between internal systems (vs north-south which is in/out of the network)"),
            ("Virtual Segment", "Logical subdivision of a physical segment allowing different policies per traffic type"),
            ("DMZ", "Demilitarised Zone — network segment containing publicly accessible servers"),
            ("Throughput Planning", "Ensuring the device's rated capacity exceeds the peak traffic on each segment"),
        ],
        "questions": [
            ("What is the most common placement for a TippingPoint IPS?", "Between the internet router and the core switch, or between the firewall and internal network"),
            ("What is bypass mode?", "A mode where traffic passes through the device uninspected, used during maintenance or device failure"),
            ("Why is throughput planning important?", "If traffic exceeds the device's rated capacity, the IPS may drop packets or fail to inspect all traffic"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Cloudflare — DMZ Explained", "https://www.cloudflare.com/learning/security/glossary/dmz-network/"),
        ]
    },
    "2-3": {
        "notes": "When you first power on a TippingPoint device, it goes through a POST (Power-On Self Test) and then boots its operating system. The console port (serial, RJ45 or DB9 depending on model) provides access during initial setup before network connectivity is configured. Console settings: 9600 baud, 8 data bits, no parity, 1 stop bit (9600 8N1).\n\nThe initial boot takes 2-5 minutes. You'll see boot messages on the console, then a login prompt. Default credentials vary by firmware version — check the quick start guide for your specific model. The first login typically forces a password change. After logging in via console, your first task is to configure the management IP address so you can switch to SSH or HTTPS management. The system will display the current software version during boot — record this for support purposes.",
        "terms": [
            ("POST", "Power-On Self Test — hardware diagnostics run at startup"),
            ("Console Port", "Serial port for out-of-band management access during initial setup"),
            ("9600 8N1", "Console port settings: 9600 baud, 8 data bits, No parity, 1 stop bit"),
            ("Out-of-Band Management", "Management access via a separate path from production traffic"),
            ("Boot Sequence", "The startup process: POST, BIOS, OS load, application start"),
            ("Management IP", "IP address assigned to the management interface for SSH/HTTPS access"),
        ],
        "questions": [
            ("What are the console port settings for TippingPoint?", "9600 baud, 8 data bits, no parity, 1 stop bit (9600 8N1)"),
            ("What is the purpose of the console port?", "Out-of-band management access, especially during initial setup before network access is configured"),
            ("What should you do after the first login?", "Change the default password and configure the management IP address"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("PuTTY — Free SSH/Serial Client", "https://www.putty.org/"),
        ]
    },
    "2-4": {
        "notes": "This lab covers the physical installation of a TippingPoint appliance. If you have access to a physical unit, follow the steps in order. If working in a lab environment, document each step as if performing the installation.\n\nLab steps: 1) Verify physical condition of the appliance on receipt. 2) Mount in rack — attach rack ears, slide in, secure with screws. 3) Connect console cable to your laptop (use PuTTY or screen on Linux). 4) Connect management port to management switch. 5) Plan segment port cabling — draw a diagram showing what connects where. 6) Connect power — do NOT power on yet. 7) Verify all connections. 8) Power on and observe boot sequence on console. 9) Record the firmware version displayed during boot. 10) Verify login prompt appears.",
        "terms": [
            ("Rack Ears", "Metal brackets attached to the appliance sides for rack mounting"),
            ("Cable Documentation", "Recording what is connected to each port — essential for troubleshooting"),
            ("Boot Observation", "Watching console output during startup to identify errors"),
            ("Firmware Version", "The software version running on the device — record for support and upgrade planning"),
        ],
        "questions": [
            ("What should you do before powering on a newly racked appliance?", "Verify all connections are secure, power cables are connected, and console access is ready to observe the boot"),
            ("Why document your cabling before and after installation?", "For troubleshooting, audits, and future maintenance — you must know what is connected where"),
            ("What tool do you need for console access on Windows?", "PuTTY (or similar serial terminal emulator) configured for 9600 8N1"),
        ],
        "links": [
            ("PuTTY — Free SSH/Serial Client", "https://www.putty.org/"),
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
        ]
    },
    "3-1": {
        "notes": "Once the management IP is configured, you have two ways to access TippingPoint: SSH for CLI access and HTTPS for the web-based Local Security Manager (LSM). SSH is the primary tool for initial configuration and troubleshooting. To connect: ssh admin@<management-ip>. The default SSH port is 22.\n\nThe LSM (Local Security Manager) is a web interface running on the device itself — not to be confused with SMS, which is the centralised management system for multiple devices. The LSM is useful for initial setup and when SMS is unavailable. In production environments, most administration is done through SMS. For console access during the initial setup phase before network is configured, connect your serial cable and use a terminal emulator (PuTTY on Windows, screen or minicom on Linux/Mac).",
        "terms": [
            ("SSH", "Secure Shell — encrypted remote CLI access; connect with ssh admin@<ip>"),
            ("LSM", "Local Security Manager — web-based management interface on the device itself"),
            ("SMS", "Security Management System — centralised management for multiple TippingPoint devices"),
            ("Management IP", "IP address on the management interface used for all administrative access"),
            ("Terminal Emulator", "Software for console/serial access (PuTTY, minicom, screen)"),
            ("Port 22", "Default SSH port"),
        ],
        "questions": [
            ("What is the difference between LSM and SMS?", "LSM is the local web interface on a single device; SMS is the centralised system for managing multiple devices"),
            ("How do you connect to TippingPoint via SSH?", "ssh admin@<management-ip-address>"),
            ("When would you use console access instead of SSH?", "During initial setup before the management IP is configured, or when network access is lost"),
        ],
        "links": [
            ("PuTTY — Free SSH/Serial Client", "https://www.putty.org/"),
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
        ]
    },
    "3-2": {
        "notes": "The TippingPoint CLI uses a hierarchical command structure similar to Cisco IOS. Key commands to know: `show version` displays firmware version and system info. `show system` shows CPU, memory, and uptime. `show interface` shows interface status and statistics. `show segment` displays segment configuration and traffic counters. `show filter` lists active filters and their states.\n\nConfiguration commands require you to enter configuration mode: `conf t` (or `configure terminal`). Changes take effect immediately but must be saved with `write memory` (or `copy running startup`). The `show log` command displays system and security event logs. `ping <ip>` tests management connectivity. `traceroute <ip>` traces the management path. The `debug` commands provide detailed troubleshooting output but should be used carefully in production as they can impact performance.",
        "terms": [
            ("show version", "Displays firmware version, serial number, uptime, and hardware info"),
            ("show system", "Shows CPU usage, memory usage, and system health"),
            ("show segment", "Displays segment port status, configuration, and traffic statistics"),
            ("conf t", "Enters configuration mode (configure terminal)"),
            ("write memory", "Saves running configuration to startup configuration"),
            ("show log", "Displays system and security event logs"),
        ],
        "questions": [
            ("What command shows the firmware version on TippingPoint?", "show version"),
            ("How do you save configuration changes so they persist after a reboot?", "write memory (or copy running startup)"),
            ("What command shows segment port status and traffic statistics?", "show segment"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/dcx/s/search#t=All&f:Product=[TippingPoint]"),
        ]
    },
    "3-3": {
        "notes": "Setting the management IP, DNS, and NTP are the three critical initial configuration tasks. Management IP: in configuration mode, use `ip address <ip> <mask>` on the management interface, then set the default gateway with `ip default-gateway <ip>`. Verify with `show interface management`.\n\nDNS configuration: `dns server <primary-ip> <secondary-ip>`. NTP is critical — TippingPoint's log timestamps and certificate validation depend on accurate time. Configure with `ntp server <ip>`. Verify time sync with `show ntp`. The hostname can be set with `hostname <name>` — use something descriptive like the device's physical location. After setting these, test connectivity: `ping 8.8.8.8` for internet, `ping <dns-server>` for DNS, and verify `show ntp` shows the clock is synchronised.",
        "terms": [
            ("Management Interface", "The dedicated interface for administrative traffic, separate from data segment ports"),
            ("Default Gateway", "Router IP the management interface uses to reach other networks"),
            ("NTP", "Network Time Protocol — synchronises the device clock; critical for accurate logs"),
            ("DNS", "Domain Name System — allows the device to resolve hostnames"),
            ("hostname", "Command to set the device's name, shown in CLI prompt and logs"),
            ("show ntp", "Displays NTP synchronisation status and current time source"),
        ],
        "questions": [
            ("Why is NTP configuration so important on TippingPoint?", "Log timestamps must be accurate for incident investigation, and certificate validation requires correct time"),
            ("What command verifies the management IP is configured correctly?", "show interface management"),
            ("After configuring DNS, how do you test it works?", "ping a hostname (e.g. ping updates.trendmicro.com) — if it resolves and responds, DNS is working"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("NTP Pool Project", "https://www.ntppool.org/"),
        ]
    },
    "3-4": {
        "notes": "Management access control is critical for security. By default, TippingPoint allows SSH and HTTPS access from any IP on the management network. In production, restrict this using access control lists (ACLs) to only allow connections from specific management hosts or subnets.\n\nUser accounts: TippingPoint supports role-based access control with SuperUser, Administrator, and Operator roles. SuperUser has full access. Administrator can manage security policies but not system config. Operator can view but not change. Create separate accounts for each administrator — never share credentials. RADIUS authentication can be configured for centralised user management. HTTPS certificate: replace the self-signed certificate with a proper one signed by your internal CA to eliminate browser warnings and improve security. Always disable Telnet if it's enabled — only SSH should be used.",
        "terms": [
            ("RBAC", "Role-Based Access Control — different permission levels for different user roles"),
            ("SuperUser", "Highest privilege level — full system and security policy access"),
            ("ACL", "Access Control List — restricts which IPs can connect to management interfaces"),
            ("RADIUS", "Centralised authentication — allows TippingPoint to authenticate users against a RADIUS server"),
            ("Self-Signed Certificate", "Default HTTPS cert — browsers warn about it; replace with CA-signed cert in production"),
            ("Telnet", "Unencrypted remote access — must be disabled; use SSH only"),
        ],
        "questions": [
            ("Why should you create individual accounts for each administrator?", "Accountability — if something is changed, you need to know which account made the change"),
            ("What is the difference between Administrator and Operator roles?", "Administrator can manage security policies; Operator can view but not modify configuration"),
            ("How do you restrict which hosts can access TippingPoint management?", "Configure ACLs on the management interface to only allow specific IP addresses or subnets"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("NIST — Access Control Guide", "https://csrc.nist.gov/publications/detail/sp/800-162/final"),
        ]
    },
    "3-5": {
        "notes": "This lab covers initial CLI configuration of a TippingPoint device. Work through these tasks in order, verifying each step before moving on.\n\nLab tasks: 1) Connect via SSH: `ssh admin@<ip>`. 2) Run `show version` — record firmware version. 3) Run `show system` — note CPU and memory. 4) Run `show interface` — verify management interface is up. 5) Enter config mode: `conf t`. 6) Set hostname: `hostname LAB-TPS-01`. 7) Configure NTP: `ntp server 216.239.35.0`. 8) Configure DNS: `dns server 8.8.8.8 8.8.4.4`. 9) Save: `write memory`. 10) Verify NTP: `show ntp`. 11) Run `show segment` — note segment status. 12) Create a test user with Operator role. 13) Log out and log back in as the new user to verify access.",
        "terms": [
            ("SSH Verification", "Always run show version after connecting to confirm you're on the right device"),
            ("Incremental Save", "Save with write memory after each significant change, not just at the end"),
            ("User Testing", "Always test new accounts by logging in as that user before finishing"),
        ],
        "questions": [
            ("What is the first command you should run after SSH-ing into a device?", "show version — to confirm you're on the correct device and record the firmware version"),
            ("Why save with write memory after each major change?", "So if the device unexpectedly reboots, you don't lose your configuration changes"),
            ("How do you verify NTP is synchronised?", "show ntp — look for a * or + next to the NTP server indicating it's the active time source"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("PuTTY — Free SSH/Serial Client", "https://www.putty.org/"),
        ]
    },
    "4-1": {
        "notes": "The Security Management System (SMS) is the centralised management platform for TippingPoint. Instead of logging into each IPS device individually, SMS provides a single pane of glass for managing security policies, distributing Digital Vaccine updates, monitoring events, and generating reports across your entire TippingPoint deployment.\n\nSMS runs on a dedicated server — either a physical SMS appliance or as a virtual machine (vSMS) on VMware or Hyper-V. The SMS server communicates with each managed TippingPoint device over an encrypted channel on TCP port 9898. Key SMS components: the SMS application (web-based GUI), the database (stores events, configuration, and policies), and the device management service (handles communication with IPS devices). SMS uses a client-server model — administrators connect to SMS, not directly to individual IPS devices.",
        "terms": [
            ("SMS", "Security Management System — centralised management for all TippingPoint IPS devices"),
            ("vSMS", "Virtual SMS — SMS running as a VM on VMware or Hyper-V"),
            ("Port 9898", "TCP port used for communication between SMS and managed TippingPoint devices"),
            ("Single Pane of Glass", "Managing all devices from one central interface"),
            ("SMS Database", "Stores events, configuration, policies, and reports for all managed devices"),
            ("Device Management Service", "SMS component that handles encrypted communication with IPS devices"),
        ],
        "questions": [
            ("What port does SMS use to communicate with TippingPoint devices?", "TCP port 9898"),
            ("What is the advantage of using SMS over managing each device individually?", "Centralised management, consistent policy deployment, unified event monitoring, and easier Digital Vaccine distribution"),
            ("Can SMS run as a virtual machine?", "Yes — vSMS runs on VMware or Hyper-V and has the same functionality as the physical appliance"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro SMS Overview", "https://www.trendmicro.com/en_us/business/products/network/intrusion-prevention.html"),
        ]
    },
    "4-2": {
        "notes": "Installing SMS requires a dedicated server meeting minimum hardware requirements: typically 8+ CPU cores, 16GB+ RAM, 500GB+ storage (more for large deployments with high event volumes). The SMS software is installed on Windows Server or as a pre-built virtual appliance.\n\nLicensing: TippingPoint uses a subscription-based licensing model. You need a licence for SMS itself and separate licences for Digital Vaccine (threat filter updates). Licences are managed through the Trend Micro licencing portal and imported into SMS. Without a valid DV licence, the device cannot receive new threat filter updates — the existing filters remain active but won't be updated. After installing SMS, import your licence file via the SMS GUI: Administration → Licenses → Import. Then configure the Digital Vaccine download schedule to automatically fetch updates from Trend Micro.",
        "terms": [
            ("SMS Licence", "Required for SMS functionality and Digital Vaccine update access"),
            ("Digital Vaccine Licence", "Subscription for receiving updated threat filter packages"),
            ("Licence Import", "Process of loading licence files into SMS via Administration → Licenses"),
            ("DV Schedule", "Automated schedule for SMS to download and distribute Digital Vaccine updates"),
            ("Windows Server", "Supported OS for SMS installation (check current version requirements)"),
            ("Virtual Appliance", "Pre-built VM image with SMS pre-installed — simplest deployment option"),
        ],
        "questions": [
            ("What happens if the Digital Vaccine licence expires?", "Existing filters remain active but no new updates are received — protection against new threats degrades over time"),
            ("Where do you import licences in SMS?", "Administration → Licenses → Import"),
            ("What is the recommended way to deploy SMS in a new environment?", "Using the virtual appliance image — it simplifies installation and is easier to back up and restore"),
        ],
        "links": [
            ("Trend Micro Licensing Portal", "https://clp.trendmicro.com/"),
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
        ]
    },
    "4-3": {
        "notes": "Adding a TippingPoint device to SMS is called 'registering' the device. The process: 1) In SMS, go to Devices → Add Device. 2) Enter the device's management IP address. 3) SMS connects to the device over port 9898 and verifies the connection. 4) Accept the device's SSL certificate. 5) Enter the device's admin credentials. 6) SMS retrieves the device's configuration and registers it.\n\nPrerequisites: the IPS device must have its management IP configured and must be reachable from the SMS server. Port 9898 must be open between SMS and all managed devices (check firewall rules). Once registered, SMS takes over policy management — you should no longer make policy changes via LSM. System configuration (IP, NTP, DNS) can still be done via CLI or LSM. Best practice: create a dedicated SMS-managed account on each device rather than using the admin account.",
        "terms": [
            ("Device Registration", "Process of adding a TippingPoint IPS to SMS management"),
            ("Port 9898", "Must be open between SMS server and all managed TippingPoint devices"),
            ("SSL Certificate Acceptance", "During registration, verify and accept the device's SSL certificate"),
            ("LSM vs SMS", "After SMS registration, policy changes should only be made in SMS, not LSM"),
            ("Managed Device", "A TippingPoint IPS that has been registered and is controlled by SMS"),
        ],
        "questions": [
            ("What port must be open for SMS to communicate with managed devices?", "TCP port 9898"),
            ("After registering a device in SMS, where should policy changes be made?", "In SMS only — making changes via LSM after SMS registration can cause conflicts"),
            ("What is the first thing to verify before attempting to register a device?", "That the device management IP is reachable from the SMS server (ping the device from the SMS server)"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/dcx/s/search#t=All&f:Product=[TippingPoint]"),
        ]
    },
    "4-4": {
        "notes": "The SMS dashboard provides an overview of your entire TippingPoint deployment. Key areas: the Device Summary panel shows all registered devices and their status (green = online and healthy, yellow = warning, red = error or offline). The Events panel shows recent security events across all devices. The DV Status panel shows the current Digital Vaccine version installed on each device.\n\nNavigation: Devices → [device name] drills into a specific device. Events → Event Log shows all security events with filtering by severity, device, filter name, and time range. Reports → Generate creates scheduled or on-demand reports. Policies → Security Profiles manages your security configurations. Understanding the dashboard layout is essential — in a real incident, you need to navigate quickly to find the relevant events and understand what's being blocked.",
        "terms": [
            ("Device Summary", "SMS dashboard panel showing all devices and their health status"),
            ("Event Log", "SMS view of all security events across all managed devices"),
            ("DV Status", "Shows which Digital Vaccine version is running on each device"),
            ("Security Profile", "A named collection of filter settings that can be applied to devices"),
            ("Dashboard", "SMS home screen with overview of device health, events, and DV status"),
        ],
        "questions": [
            ("What does a red status indicator mean on the SMS device summary?", "The device is in an error state or offline — requires immediate investigation"),
            ("Where in SMS do you view security events from all devices?", "Events → Event Log"),
            ("What is a Security Profile in SMS?", "A named collection of Digital Vaccine filter settings that can be applied to one or more devices"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro SMS Overview", "https://www.trendmicro.com/en_us/business/products/network/intrusion-prevention.html"),
        ]
    },
    "4-5": {
        "notes": "SMS setup lab. Work through these tasks using your SMS instance.\n\nLab tasks: 1) Log into SMS via HTTPS. 2) Navigate the dashboard — identify Device Summary, Event Log, and DV Status panels. 3) Go to Devices → Add Device and register your TippingPoint appliance. 4) Verify the device shows as green/online in the dashboard. 5) Navigate to the registered device and review its configuration. 6) Check Administration → Licenses — verify DV licence is valid. 7) Go to Digital Vaccine → Download/Install — note the current DV version. 8) Create a test user account in SMS with Administrator role. 9) Log out and log back in as the test user. 10) Generate a test report from Reports → Device Summary.",
        "terms": [
            ("HTTPS Access", "SMS is accessed via web browser over HTTPS — accept the certificate warning on first access"),
            ("License Verification", "Always verify licence validity immediately after SMS installation"),
            ("DV Version", "Record the current DV version — this is your baseline for update tracking"),
        ],
        "questions": [
            ("After registering a device, what should you immediately verify?", "That the device shows as green/online in the SMS dashboard and that the DV version displayed is current"),
            ("What should you do if the SMS licence shows as expired?", "Contact Trend Micro or your reseller to renew — then re-import the new licence file via Administration → Licenses"),
            ("Why create separate SMS user accounts for each administrator?", "Accountability and audit trail — each action in SMS is logged against the user account that performed it"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Licensing Portal", "https://clp.trendmicro.com/"),
        ]
    },
    "5-1": {
        "notes": "TippingPoint's security policy has three key concepts: Profiles, Segments, and Policies. A Security Profile is a collection of filter settings — which Digital Vaccine filters are active, and what action each filter takes. A Segment is a physical port pair on the device through which traffic flows. A Policy connects a profile to a segment — it defines which security profile applies to which network segment.\n\nThis separation is powerful: you can create different profiles for different traffic types (e.g. a strict profile for internet-facing traffic, a less strict profile for internal traffic) and apply them to the appropriate segments. Changes to a profile automatically apply to all segments using that profile. The default profile is a starting point, but you should create custom profiles for your environment rather than modifying the default.",
        "terms": [
            ("Security Profile", "A named set of filter configurations defining which filters are active and their actions"),
            ("Segment", "A physical port pair through which traffic flows and to which a policy is applied"),
            ("Policy", "The connection between a security profile and a network segment"),
            ("Default Profile", "Pre-configured starting profile — copy and customise rather than modifying directly"),
            ("Filter Action", "What TippingPoint does when a filter matches: Block, Permit, Rate Limit, or Notify"),
        ],
        "questions": [
            ("What is the relationship between a Profile, Segment, and Policy?", "A Policy applies a Profile to a Segment — it defines which filter settings apply to which traffic flow"),
            ("Why should you copy the default profile rather than modify it?", "The default profile is a known good baseline — if you modify it directly, you lose the reference point"),
            ("Can the same profile be applied to multiple segments?", "Yes — one profile can be applied to many segments, and changes to the profile affect all segments using it"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/dcx/s/search#t=All&f:Product=[TippingPoint]"),
        ]
    },
    "5-2": {
        "notes": "Creating a security profile in SMS: navigate to Policies → Security Profiles → New. Give it a descriptive name (e.g. INTERNET-INBOUND-STRICT). Select the base filters to include — typically start with all Critical and High severity filters set to Block, Medium filters set to Block or Notify, and Low filters set to Permit or Notify.\n\nApplying a profile: once created, go to the device, select the target segment, and set the policy to use your new profile. Click Distribute to push the policy to the device — this is the step that actually sends the configuration to the IPS hardware. Always verify distribution completed successfully. Test the profile: generate some known benign traffic and verify it passes, then check the Event Log for any unexpected blocks. The Audit Trail in SMS records every policy change with timestamp and user — use this to track changes.",
        "terms": [
            ("Distribute", "The SMS action that pushes policy changes to the physical TippingPoint device"),
            ("Audit Trail", "SMS log of all policy changes with user, timestamp, and details"),
            ("Severity Levels", "Critical, High, Medium, Low, Informational — indicate threat seriousness"),
            ("Profile Distribution", "Process of sending a configured profile from SMS to managed devices"),
            ("Test Traffic", "Generating known-good traffic after policy changes to verify nothing legitimate is blocked"),
        ],
        "questions": [
            ("What does 'Distribute' do in SMS?", "Pushes the policy configuration from SMS to the physical TippingPoint device — without this, changes in SMS don't take effect"),
            ("What filters should typically be set to Block in a new profile?", "Critical and High severity filters — these represent the most serious threats"),
            ("How do you track who made policy changes in SMS?", "The Audit Trail logs every change with the user account, timestamp, and details of what changed"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/dcx/s/search#t=All&f:Product=[TippingPoint]"),
        ]
    },
    "5-3": {
        "notes": "Action Sets define what TippingPoint does when a filter matches. The four action types are Block (drop the packet and log), Permit (allow and optionally log), Rate Limit (restrict bandwidth for matching traffic), and Notify (allow but send an alert/notification). You can also combine actions — e.g. Block + Notify sends an email or SNMP trap when a filter fires.\n\nCustom action sets are powerful: create an action set that blocks traffic AND sends an email to the security team AND logs to syslog. Or create a rate-limit action set for bandwidth-heavy but not malicious traffic (e.g. P2P). Action sets are reusable — one action set can be assigned to hundreds of filters. Best practice: create a small number of well-named action sets (BLOCK-AND-ALERT, PERMIT-AND-LOG, RATE-LIMIT-1MBPS) rather than creating custom ones for every filter.",
        "terms": [
            ("Block", "Action that drops the matching packet and creates a log entry"),
            ("Permit", "Action that allows the matching packet through (optionally logged)"),
            ("Rate Limit", "Action that restricts bandwidth for matching traffic to a configured rate"),
            ("Notify", "Action that sends an alert (email, SNMP trap, syslog) when a filter matches"),
            ("Action Set", "A reusable named configuration of one or more actions applied when a filter matches"),
            ("Compound Action", "Combining multiple actions — e.g. Block + Notify + Syslog"),
        ],
        "questions": [
            ("What is the difference between Block and Notify action sets?", "Block drops the packet; Notify allows it through but sends an alert"),
            ("When would you use Rate Limit instead of Block?", "For traffic that is not a direct threat but consumes excessive bandwidth — you want to control it, not stop it entirely"),
            ("Why use reusable action sets rather than creating new ones for each filter?", "Consistency and easier management — changing one action set updates all filters that use it"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/dcx/s/search#t=All&f:Product=[TippingPoint]"),
        ]
    },
    "5-4": {
        "notes": "Even with excellent threat filters, legitimate traffic sometimes triggers false positives — a filter fires on traffic that is not actually malicious. Policy exceptions (also called Permit Lists or Exemptions) allow you to exclude specific traffic from specific filters. Common use case: a vulnerability scanner triggering attack signatures when it scans your own network, or a legacy application using protocols that trigger filters.\n\nCreating an exception: in SMS, go to the filter that's causing the false positive, add an exception for the specific source IP, destination IP, or traffic pattern. Be precise — never create a blanket 'Permit All' exception; always be as specific as possible. Document every exception with the reason and date. Review exceptions quarterly and remove any that are no longer needed. Exceptions are a security risk — each one is a hole in your protection.",
        "terms": [
            ("False Positive", "A filter firing on legitimate traffic that is not actually a threat"),
            ("Policy Exception", "A rule that exempts specific traffic from a specific filter"),
            ("Permit List", "Another term for exceptions/exemptions — traffic that is always allowed"),
            ("Vulnerability Scanner", "Security tool that often triggers IPS filters when scanning your own network"),
            ("Exception Review", "Regular process of auditing exceptions to remove those no longer needed"),
        ],
        "questions": [
            ("What is a false positive in an IPS context?", "A filter firing on legitimate traffic that is not actually malicious"),
            ("How specific should exceptions be?", "As specific as possible — limit by source IP, destination IP, and specific filter, never create blanket exceptions"),
            ("Why should exceptions be reviewed regularly?", "Exceptions are security gaps — old exceptions that are no longer needed should be removed to maintain protection"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/dcx/s/search#t=All&f:Product=[TippingPoint]"),
        ]
    },
    "5-5": {
        "notes": "Policy management lab. Complete these tasks in your SMS environment.\n\nLab tasks: 1) Create a new Security Profile named LAB-PROFILE-01. 2) Set all Critical filters to Block action set. 3) Set all High filters to Block action set. 4) Set all Medium filters to Notify action set. 5) Create a custom action set named BLOCK-AND-LOG with Block + Syslog actions. 6) Apply BLOCK-AND-LOG to three Critical filters of your choice. 7) Apply LAB-PROFILE-01 to a segment on your device. 8) Click Distribute and verify it completes successfully. 9) Check the Event Log for any immediate filter activity. 10) Create a test exception for your workstation IP on one filter. 11) Document the exception with reason and date in the exception comments field. 12) Review the Audit Trail to see your changes recorded.",
        "terms": [
            ("Profile Creation Checklist", "Name, base filter settings, custom action sets, exceptions, distribution, verification"),
            ("Distribution Verification", "Confirm the device shows the new profile version in SMS after distributing"),
            ("Audit Trail Review", "Verify your changes appear correctly in the SMS audit log"),
        ],
        "questions": [
            ("After distributing a policy, how do you verify it was applied successfully?", "Check the device in SMS shows the new policy version, and review the Event Log for any distribution errors"),
            ("What should you always include when creating a policy exception?", "The reason for the exception, the date it was created, and who approved it"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/dcx/s/search#t=All&f:Product=[TippingPoint]"),
        ]
    },
    "6-1": {
        "notes": "The Digital Vaccine (DV) is TippingPoint's core threat intelligence. It's a regularly updated package of filters developed by Trend Micro's TippingPoint DVLabs team. Each DV package contains thousands of filters covering exploits, malware, protocol anomalies, and policy violations.\n\nDV filters are different from traditional AV signatures — instead of matching known malware files, they protect at the vulnerability level. A single DV filter can block all exploits targeting a specific vulnerability, even zero-day variants, because it targets the vulnerable code path rather than specific malware samples. DVLabs releases emergency DV packages (called Digital Vaccine Advisories or DVAs) for critical vulnerabilities like major zero-days, sometimes before vendors release patches. This is TippingPoint's strongest value proposition: protection before patches.",
        "terms": [
            ("Digital Vaccine (DV)", "TippingPoint's threat filter package — thousands of filters updated regularly by DVLabs"),
            ("DVLabs", "Trend Micro's research team that creates and maintains Digital Vaccine filters"),
            ("Vulnerability-Based Filter", "Filter that blocks all exploits targeting a vulnerability, not just known samples"),
            ("DVA", "Digital Vaccine Advisory — emergency DV package for critical zero-day vulnerabilities"),
            ("Zero-Day", "Vulnerability exploited before a vendor patch is available"),
            ("Pre-Patch Protection", "TippingPoint's ability to block zero-day exploits before the vendor releases a fix"),
        ],
        "questions": [
            ("How is a Digital Vaccine filter different from an antivirus signature?", "AV signatures match known malware files; DV filters target vulnerabilities — blocking all exploits of that vulnerability including unknown variants"),
            ("What is a Digital Vaccine Advisory (DVA)?", "An emergency DV package released for critical vulnerabilities, sometimes before vendor patches are available"),
            ("What is meant by pre-patch protection?", "TippingPoint can block exploitation of a vulnerability before the software vendor releases a patch to fix it"),
        ],
        "links": [
            ("Trend Micro DVLabs", "https://www.trendmicro.com/en_us/research.html"),
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Threat Encyclopedia", "https://www.trendmicro.com/vinfo/us/threat-encyclopedia/"),
        ]
    },
    "6-2": {
        "notes": "DV filters are organised into categories and assigned severity levels. Categories include: Exploits (targeting specific vulnerabilities), Reconnaissance (scanning and probing), DoS (denial of service attacks), Backdoors (remote access trojans), Spyware (data-stealing malware), P2P (peer-to-peer applications), IM (instant messaging), and Policy (traffic that violates acceptable use policies).\n\nSeverity levels: Critical (immediate system compromise possible), High (significant risk), Medium (moderate risk or policy violation), Low (informational or minor risk), Informational (logging only, no blocking). In a default deployment, Critical and High should always be Block, Medium depends on your environment, and Low/Informational are typically Permit or Notify. The CVE number (Common Vulnerabilities and Exposures) is often referenced in filter descriptions — you can look these up at cve.mitre.org to understand exactly what vulnerability each filter protects against.",
        "terms": [
            ("Filter Category", "Classification of what type of threat the filter addresses (Exploit, DoS, Spyware, etc.)"),
            ("Critical Severity", "Highest risk — filters for threats that can immediately compromise systems; always Block"),
            ("High Severity", "Significant risk — should be Block in most environments"),
            ("CVE", "Common Vulnerabilities and Exposures — standard identifier for known vulnerabilities"),
            ("Reconnaissance", "Scanning and probing activity — often detected by TippingPoint before attacks begin"),
            ("Informational", "Lowest severity — used for logging traffic patterns without blocking"),
        ],
        "questions": [
            ("What severity level should always be set to Block?", "Critical — these filters protect against threats that can immediately compromise systems"),
            ("What is a CVE number?", "A standardised identifier for a specific known vulnerability — look up CVE details at cve.mitre.org"),
            ("When might you set Medium severity filters to Permit instead of Block?", "In environments with legacy applications that might trigger false positives, or when tuning a new deployment"),
        ],
        "links": [
            ("CVE Database — MITRE", "https://cve.mitre.org/"),
            ("NVD — NIST Vulnerability Database", "https://nvd.nist.gov/"),
            ("Trend Micro Threat Encyclopedia", "https://www.trendmicro.com/vinfo/us/threat-encyclopedia/"),
        ]
    },
    "6-3": {
        "notes": "Filter tuning is the ongoing process of optimising your TippingPoint deployment to minimise false positives while maintaining security. The process: 1) Review the Event Log for high-volume filter hits. 2) Investigate each high-volume filter — is it a real threat or a false positive? 3) For false positives: create a specific exception (not a blanket disable). 4) For real threats being blocked: verify the block action is correct and no exceptions are needed.\n\nIn SMS, the Filter Search feature lets you find filters by CVE, name, or keyword. Click any filter to see its description, affected systems, and recommended action. The Reputation filter category uses Trend Micro's cloud-based threat intelligence to block traffic from known malicious IPs — keep this enabled. Adaptive Filter (AFS) automatically adjusts filter sensitivity based on traffic patterns — useful for reducing false positives in complex environments. Never disable a Critical filter without a very strong reason and management approval.",
        "terms": [
            ("Filter Tuning", "Ongoing process of optimising filters to reduce false positives while maintaining security"),
            ("Adaptive Filter (AFS)", "Feature that automatically adjusts filter sensitivity based on observed traffic"),
            ("Reputation Filter", "Uses cloud threat intelligence to block traffic from known malicious IPs"),
            ("Filter Search", "SMS feature to find filters by CVE number, name, or keyword"),
            ("High-Volume Hits", "Filters firing frequently — may indicate attacks or false positives needing investigation"),
        ],
        "questions": [
            ("What is the correct way to handle a false positive — a Critical filter blocking legitimate traffic?", "Create a specific exception for that traffic, not disable the filter. Document the exception with reason and date"),
            ("What does Adaptive Filter (AFS) do?", "Automatically adjusts filter sensitivity based on observed traffic patterns to reduce false positives"),
            ("What should you never do without management approval?", "Disable a Critical severity filter"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("CVE Database — MITRE", "https://cve.mitre.org/"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
        ]
    },
    "6-4": {
        "notes": "Digital Vaccine updates must be applied regularly to maintain protection against new threats. Trend Micro releases weekly DV updates and emergency DVA packages for critical vulnerabilities. In SMS, configure automatic DV download and distribution: go to Digital Vaccine → Schedule, set download frequency (weekly minimum, daily recommended), and enable automatic distribution to all managed devices.\n\nThe DV update process: SMS downloads the new package from Trend Micro's update servers, verifies the digital signature, and then distributes it to all managed devices. Devices apply the new filters without requiring a reboot or interrupting traffic. Monitor the DV Status panel in SMS to verify all devices are running the same (latest) DV version. If a device shows a different version, trigger a manual distribution. Maintain a change log for all DV updates — required for compliance audits.",
        "terms": [
            ("DV Schedule", "Automated configuration for downloading and distributing DV updates"),
            ("Digital Signature", "Cryptographic verification ensuring the DV package is genuine and unmodified"),
            ("DV Distribution", "Process of SMS pushing a new DV package to managed devices"),
            ("DV Status Panel", "SMS dashboard showing current DV version on each managed device"),
            ("DVA", "Emergency DV package for critical zero-days — apply immediately when released"),
            ("Change Log", "Record of all DV updates applied — required for compliance audits"),
        ],
        "questions": [
            ("How often should DV updates be applied at minimum?", "Weekly — daily is recommended. Emergency DVAs should be applied immediately when released"),
            ("Does applying a DV update require a device reboot?", "No — DV updates are applied without interrupting traffic or requiring a reboot"),
            ("What should you do if one device shows an older DV version than others?", "Trigger a manual DV distribution from SMS to that device, then verify the version updates"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Threat Encyclopedia", "https://www.trendmicro.com/vinfo/us/threat-encyclopedia/"),
        ]
    },
    "6-5": {
        "notes": "Filter tuning lab. Work through these tasks to develop hands-on filter management skills.\n\nLab tasks: 1) In SMS, navigate to Policies → Security Profiles → your profile. 2) Use Filter Search to find the filter for CVE-2021-44228 (Log4Shell) — note its severity and current action. 3) Find all Critical filters currently set to Permit — change them to Block. 4) Review the Event Log for the last 24 hours — identify the top 5 most triggered filters. 5) For each high-volume filter, investigate whether it's a real threat or false positive. 6) Create an appropriate exception for any confirmed false positives. 7) In Digital Vaccine → Schedule, verify auto-update is configured for weekly download. 8) Manually trigger a DV update check. 9) Verify all devices show the same DV version in the DV Status panel. 10) Document your findings and any changes made.",
        "terms": [
            ("Log4Shell", "CVE-2021-44228 — critical Apache Log4j vulnerability; all TippingPoint should have this filter active"),
            ("Top Triggered Filters", "Reviewing frequently-firing filters is the starting point for tuning"),
            ("Manual DV Trigger", "In SMS: Digital Vaccine → Check for Updates → Download and Distribute"),
        ],
        "questions": [
            ("Where in SMS do you check for DV updates manually?", "Digital Vaccine → Check for Updates"),
            ("What does finding a Critical filter set to Permit indicate?", "A misconfiguration or deliberate exception — investigate immediately and change to Block unless there is a documented reason"),
        ],
        "links": [
            ("CVE-2021-44228 — Log4Shell Detail", "https://nvd.nist.gov/vuln/detail/CVE-2021-44228"),
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
        ]
    },
    "7-1": {
        "notes": "High Availability (HA) ensures TippingPoint continues to function even if a device fails or needs maintenance. TippingPoint supports two key HA features: Zero Power HA (ZPHA) and Layer 2 Fallback.\n\nZero Power HA (ZPHA) uses a hardware bypass mechanism — if the TippingPoint device loses power or fails completely, the segment ports physically connect together using relays, allowing traffic to pass through uninspected. This prevents a device failure from taking down the network, at the cost of temporarily losing IPS protection. Layer 2 Fallback is a software mechanism — if the inspection engine becomes overloaded or a software issue occurs, traffic passes through in bypass mode while the device is still powered on. For full HA with continuous protection, deploy two TippingPoint devices in an Active/Standby pair — if the active device fails, the standby takes over inspection.",
        "terms": [
            ("ZPHA", "Zero Power HA — hardware bypass that passes traffic if device loses power"),
            ("Layer 2 Fallback", "Software bypass mode activated when inspection engine is overloaded"),
            ("Active/Standby", "HA pair where one device inspects traffic; the other takes over if the active device fails"),
            ("Hardware Bypass", "Physical relay that connects segment ports together, allowing uninspected traffic flow"),
            ("Bypass Mode", "State where traffic passes through without inspection — network stays up but unprotected"),
            ("Heartbeat", "Signal exchanged between HA pair members to detect device failure"),
        ],
        "questions": [
            ("What is the difference between ZPHA and Layer 2 Fallback?", "ZPHA is hardware-based and activates on power loss; Layer 2 Fallback is software-based and activates on inspection engine issues"),
            ("What is the trade-off of ZPHA?", "Network stays up during device failure but traffic is no longer inspected — you have availability but lose security"),
            ("When is an Active/Standby pair needed?", "When you need continuous IPS protection even during a device failure — ZPHA and Layer 2 Fallback allow traffic but without inspection"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/dcx/s/search#t=All&f:Product=[TippingPoint]"),
        ]
    },
    "7-2": {
        "notes": "Configuring an HA pair requires two identical TippingPoint appliances (same model, same firmware version). The HA link is a dedicated Ethernet connection between the two devices used for heartbeat and state synchronisation. Setup process: 1) Configure both devices with the same firmware version. 2) Connect the HA link between the two devices. 3) On the primary device, enable HA and configure the HA IP address. 4) On the secondary device, enable HA and point it to the primary. 5) Verify the HA status shows Active (primary) and Standby (secondary).\n\nSMS manages HA pairs as a single logical device — policy changes are pushed to both devices simultaneously. The HA state is shown in the SMS device summary. Both devices share the same security policy but maintain separate management IPs. Firmware upgrades on an HA pair should be done in a specific sequence to avoid downtime.",
        "terms": [
            ("HA Link", "Dedicated Ethernet cable between HA pair members for heartbeat and synchronisation"),
            ("Primary/Secondary", "Roles in an HA pair — primary is Active, secondary is Standby"),
            ("HA IP", "IP address used for HA communication between pair members"),
            ("State Synchronisation", "Keeping connection tables and configuration identical between HA pair members"),
            ("HA Firmware Upgrade", "Specific sequence required to upgrade firmware on an HA pair without losing protection"),
        ],
        "questions": [
            ("What physical connection is required between HA pair members?", "A dedicated Ethernet HA link cable — this carries heartbeat and state synchronisation traffic"),
            ("Must both devices in an HA pair run the same firmware version?", "Yes — mismatched firmware versions can cause HA instability or failure"),
            ("How does SMS handle an HA pair?", "As a single logical device — policy changes are distributed to both members simultaneously"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/dcx/s/search#t=All&f:Product=[TippingPoint]"),
        ]
    },
    "7-3": {
        "notes": "Testing HA failover before relying on it in production is essential — never assume HA works until you've tested it. Testing procedure: 1) Verify HA is in normal state (Active + Standby showing green). 2) Generate continuous traffic through the device (ping flood, or use a traffic generator). 3) Simulate failure on the active device: either unplug power or use the CLI command to force failover. 4) Observe: traffic should continue flowing with a brief interruption (typically <1 second for planned failover). 5) Verify the standby device is now Active in SMS. 6) Restore the original active device. 7) Verify it comes up as Standby. 8) Force failback if desired.\n\nDocument the failover time — this is your RTO (Recovery Time Objective) for this component. Schedule HA testing at least annually, and after any firmware upgrades. A failover event is also logged in SMS — check the event log for HA state changes.",
        "terms": [
            ("Failover", "The process of the Standby device taking over from the failed Active device"),
            ("Failback", "Returning to the original Active/Standby state after the failed device is restored"),
            ("RTO", "Recovery Time Objective — maximum acceptable time for failover to complete"),
            ("Planned Failover", "Deliberately triggering failover for testing or maintenance — faster than unplanned"),
            ("Unplanned Failover", "Failover triggered by an actual device failure"),
        ],
        "questions": [
            ("Why must you test HA failover before relying on it?", "To verify it actually works, measure the failover time, and identify any configuration issues before a real failure occurs"),
            ("What is RTO in the context of HA testing?", "Recovery Time Objective — the maximum acceptable time for the standby to take over, measured during testing"),
            ("How often should HA failover be tested?", "At least annually, and after any firmware upgrades or significant configuration changes"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/dcx/s/search#t=All&f:Product=[TippingPoint]"),
        ]
    },
    "7-4": {
        "notes": "HA configuration lab.\n\nLab tasks: 1) Verify current HA status: `show ha` on CLI. 2) In SMS, view the HA pair status in the device summary. 3) Document which device is currently Active and which is Standby. 4) Generate continuous ping traffic through the segment. 5) Force a failover using the CLI: `ha force-failover`. 6) Observe the failover — note how long traffic interruption lasts. 7) Verify the secondary is now Active in SMS. 8) Check the SMS Event Log for the HA state change event. 9) Allow the original primary to come up as Standby. 10) Force failback: `ha force-failover` on the new Active to return to original state. 11) Record the failover time in your lab notes as the measured RTO.",
        "terms": [
            ("show ha", "CLI command to display HA status, role, and health"),
            ("ha force-failover", "CLI command to manually trigger an HA failover for testing"),
            ("HA State Change Event", "SMS event log entry recording when HA state changed and why"),
        ],
        "questions": [
            ("What CLI command shows HA status?", "show ha"),
            ("What should you observe during a failover test?", "Traffic interruption duration, which device becomes Active in SMS, and the HA state change event in the event log"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/dcx/s/search#t=All&f:Product=[TippingPoint]"),
        ]
    },
    "8-1": {
        "notes": "TippingPoint generates several types of logs. Security Event logs record filter matches — every time a filter fires, a log entry is created with: timestamp, filter name, filter ID, source IP, destination IP, source port, destination port, protocol, action taken, and segment. System logs record device health events: reboots, HA state changes, DV updates, configuration changes. Audit logs record all administrative actions.\n\nIn SMS, the Event Log viewer provides powerful filtering: filter by device, time range, severity, filter category, source/destination IP, and action. The Drill-Down feature lets you click on any event to see full details including the raw packet data (if packet capture is enabled). Understanding how to read and filter security events is the most important day-to-day skill for a TippingPoint administrator — it's how you distinguish real attacks from false positives and track threat patterns over time.",
        "terms": [
            ("Security Event Log", "Record of every filter match including source/dest IP, ports, action, and filter details"),
            ("System Log", "Record of device health events: reboots, HA changes, DV updates, config changes"),
            ("Audit Log", "Record of all administrative actions in SMS with user, timestamp, and details"),
            ("Event Drill-Down", "Clicking an event in SMS to see full details including raw packet data"),
            ("Log Filtering", "Using SMS to narrow event view by time, severity, device, IP, or filter name"),
        ],
        "questions": [
            ("What information is in a TippingPoint security event log entry?", "Timestamp, filter name/ID, source IP, destination IP, ports, protocol, action taken, and segment"),
            ("What is the Audit Log used for?", "Tracking all administrative changes in SMS — who did what and when"),
            ("How do you investigate a specific security event in SMS?", "Find it in the Event Log, apply filters to narrow results, then click the event to drill down into full details"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/dcx/s/search#t=All&f:Product=[TippingPoint]"),
        ]
    },
    "8-2": {
        "notes": "Common TippingPoint issues and their solutions. Issue 1: Device shows offline in SMS. Check: is the management IP reachable? (ping from SMS server). Is port 9898 open? (telnet <device-ip> 9898). Did the device reboot? (check system log). Issue 2: High CPU on device. Check: is traffic volume within rated capacity? Are there high-volume filters firing? Consider enabling Adaptive Filter. Issue 3: Legitimate traffic being blocked. Check: which filter is blocking it? Is it a false positive? Add a specific exception. Issue 4: DV update failing. Check: can the SMS server reach updates.trendmicro.com? (proxy settings?). Is the DV licence valid?\n\nIssue 5: HA not failing over. Check: is the HA link cable connected? Are both devices running the same firmware? Is the heartbeat IP reachable? Issue 6: Event Log shows no events. Check: is the profile distributed to the device? Are filters set to log? Is the device sending events to SMS (port 9898 open)? Issue 7: Segment shows as down. Check: is the connected switch port up? Is the cable good? Try swapping the cable.",
        "terms": [
            ("Port 9898", "Test with telnet <ip> 9898 — if it fails, check firewall rules between SMS and device"),
            ("Adaptive Filter", "Enable to reduce CPU load from high-volume traffic"),
            ("DV Licence Check", "Administration → Licenses in SMS — verify expiry date"),
            ("Segment Down", "Physical layer problem — check cables and connected switch ports first"),
            ("Proxy Settings", "SMS may need proxy configured to reach Trend Micro update servers"),
        ],
        "questions": [
            ("A device shows offline in SMS. What is your first troubleshooting step?", "Ping the device management IP from the SMS server — determine if it's a connectivity issue or an SMS communication issue"),
            ("What command tests whether port 9898 is reachable?", "telnet <device-management-ip> 9898 — if it connects, the port is open"),
            ("High CPU on a TippingPoint device — what should you check?", "Traffic volume vs rated capacity, number of high-volume filter hits, and whether Adaptive Filter is enabled"),
        ],
        "links": [
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/dcx/s/search#t=All&f:Product=[TippingPoint]"),
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
        ]
    },
    "8-3": {
        "notes": "Packet capture on TippingPoint allows you to capture the actual packets that triggered a security event. This is invaluable for investigating false positives and confirming real attacks. Enable packet capture in SMS: go to the security profile, enable 'Packet Trace' for specific filters or globally. Captured packets are stored on the device and viewable in SMS — you can download them as .pcap files and open them in Wireshark.\n\nCLI diagnostics: `show interface` shows port statistics including error counts — high error rates indicate physical layer problems. `show segment stats` shows per-segment traffic counters and drop counts. `debug traffic` captures traffic at the CLI level (use carefully — high overhead). `show cpu` monitors processor usage. `show memory` shows memory utilisation. For serious issues, Trend Micro support may request a `support bundle` — generate with `support bundle generate` and upload to the support portal.",
        "terms": [
            ("Packet Trace", "TippingPoint feature that captures packets matching specific filters for analysis"),
            ("pcap", "Packet capture file format — open with Wireshark for analysis"),
            ("show segment stats", "CLI command showing per-segment traffic, drop, and error counters"),
            ("Support Bundle", "Diagnostic package generated by TippingPoint for Trend Micro support analysis"),
            ("debug traffic", "CLI command for packet-level debugging — high overhead, use briefly"),
            ("show cpu", "CLI command showing current and historical CPU utilisation"),
        ],
        "questions": [
            ("How do you capture packets for a specific filter in TippingPoint?", "Enable Packet Trace on that filter in the security profile in SMS, then reproduce the traffic — captured packets appear in the event details"),
            ("What format are captured packets saved in?", "pcap format — can be downloaded from SMS and opened in Wireshark"),
            ("When would you generate a support bundle?", "When Trend Micro support requests diagnostic information to investigate a complex issue"),
        ],
        "links": [
            ("Wireshark — Free Download", "https://www.wireshark.org/download.html"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/dcx/s/search#t=All&f:Product=[TippingPoint]"),
        ]
    },
    "8-4": {
        "notes": "Troubleshooting lab. Work through a simulated troubleshooting scenario.\n\nLab tasks: 1) Run `show system` — note CPU, memory, and uptime. 2) Run `show interface` — check for any error counters. 3) Run `show segment stats` — note traffic counters and any drops. 4) In SMS, filter the Event Log to show only Critical events in the last 24 hours. 5) Identify the top 3 most triggered Critical filters. 6) For each, determine if it's a real threat or false positive. 7) Check the DV Status panel — verify all devices are on the same version. 8) Navigate to a device in SMS — check the last heartbeat time. 9) Generate a support bundle: `support bundle generate`. 10) Simulate a segment issue by disconnecting one cable — observe the segment status change in SMS. 11) Reconnect and verify the segment returns to up state.",
        "terms": [
            ("Error Counters", "Non-zero values in show interface output indicate physical layer problems"),
            ("Last Heartbeat", "SMS shows when it last received a heartbeat from each device — long gaps indicate connectivity issues"),
            ("Segment Status Change", "SMS updates segment status when a port goes up or down — verify this works"),
        ],
        "questions": [
            ("What does a high drop count in show segment stats indicate?", "The device may be overwhelmed with traffic, or there is a filter blocking high volumes of traffic"),
            ("If show interface shows high error counts on a segment port, what should you check?", "The physical cable and the connected switch port — high error rates are usually a Layer 1 problem"),
        ],
        "links": [
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Wireshark — Free Download", "https://www.wireshark.org/download.html"),
        ]
    },
    "9-1": {
        "notes": "Syslog integration sends TippingPoint security events to an external log management system in real time. This is essential for compliance (PCI DSS, HIPAA, ISO 27001 all require centralised logging), incident response (correlate IPS events with other data sources), and long-term retention (TippingPoint's internal log storage is limited).\n\nConfiguring syslog in SMS: go to Administration → Notifications → Syslog. Add your syslog server IP, port (UDP 514 by default, TCP 514 or 6514 for reliable/encrypted), and select the message format (CEF is recommended for compatibility with most SIEMs). Choose which event types to forward: Security Events, System Events, Audit Events. Test the configuration by clicking 'Send Test Message' — verify it appears in your syslog server. CEF (Common Event Format) is preferred over the legacy TippingPoint format as it's supported by Splunk, QRadar, ArcSight, and others natively.",
        "terms": [
            ("Syslog", "Protocol for forwarding log messages to a central log server; UDP 514 by default"),
            ("CEF", "Common Event Format — standardised log format supported by most SIEMs"),
            ("SIEM", "Security Information and Event Management — centralised security log management and analysis"),
            ("TCP Syslog", "Reliable syslog using TCP instead of UDP — prevents log loss on busy networks"),
            ("Log Retention", "Storing logs for a defined period — compliance requirements vary (PCI DSS: 1 year minimum)"),
            ("Test Message", "SMS feature to send a test syslog entry — verify integration is working"),
        ],
        "questions": [
            ("Why is centralised syslog important?", "Compliance requirements, longer retention than on-device storage, and correlation with other security data sources"),
            ("What log format should you use for SIEM integration?", "CEF (Common Event Format) — supported natively by Splunk, QRadar, ArcSight, and most other SIEMs"),
            ("What port does syslog use by default?", "UDP 514 — use TCP 514 or 6514 for reliable delivery or encrypted transport"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Graylog — Free SIEM/Log Management", "https://graylog.org/products/open-source/"),
        ]
    },
    "9-2": {
        "notes": "SNMP (Simple Network Management Protocol) allows your network management system (NMS) to monitor TippingPoint device health — CPU, memory, interface status, and system alarms. TippingPoint supports SNMPv2c and SNMPv3. Always use SNMPv3 — it provides authentication and encryption unlike v2c which sends community strings in plaintext.\n\nConfiguration in SMS: Administration → SNMP. Configure SNMP v3 with: username, authentication protocol (SHA recommended), authentication password, privacy protocol (AES recommended), privacy password, and the IP of your SNMP manager. Also configure SNMP traps — these are alerts sent from TippingPoint to your NMS when significant events occur (device offline, high CPU, HA state change, DV update). Test by forcing a trap condition and verifying receipt in your NMS. TippingPoint's MIB files are available from Trend Micro support — import them into your NMS for proper OID descriptions.",
        "terms": [
            ("SNMP", "Simple Network Management Protocol — monitors device health via polling and traps"),
            ("SNMPv3", "Secure SNMP with authentication and encryption — always prefer over v2c"),
            ("SNMP Trap", "Unsolicited alert sent from device to NMS when a significant event occurs"),
            ("Community String", "SNMPv2c authentication — sent in plaintext; never use v2c in production"),
            ("MIB", "Management Information Base — defines the OIDs (metrics) available via SNMP"),
            ("NMS", "Network Management System — software that receives SNMP data (Nagios, PRTG, Zabbix)"),
        ],
        "questions": [
            ("Why should you use SNMPv3 instead of SNMPv2c?", "SNMPv3 provides authentication and encryption; SNMPv2c sends community strings in plaintext"),
            ("What is an SNMP trap?", "An unsolicited alert sent from TippingPoint to the NMS when a significant event occurs — like a device going offline"),
            ("What are MIB files used for?", "Importing into your NMS to get human-readable descriptions of TippingPoint's SNMP metrics"),
        ],
        "links": [
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("PRTG — Free Network Monitor (up to 100 sensors)", "https://www.paessler.com/prtg"),
        ]
    },
    "9-3": {
        "notes": "Splunk and IBM QRadar are the two most common SIEMs in enterprise environments. Both support TippingPoint integration via syslog in CEF format. For Splunk: install the Trend Micro TippingPoint Add-on from Splunkbase — this provides pre-built field extractions, dashboards, and alert rules for TippingPoint data. Configure TippingPoint SMS to send syslog to your Splunk indexer or heavy forwarder on UDP/TCP 514.\n\nFor QRadar: TippingPoint uses a pre-built Device Support Module (DSM) in QRadar. Configure the log source in QRadar pointing to the SMS syslog output. QRadar will automatically parse TippingPoint events and map them to the QRadar taxonomy. Key dashboards to build in your SIEM: Top Blocked Sources (which IPs are being blocked most), Top Triggered Filters (which threats are most active), Geo-map of blocked sources, and Trend over time charts. Correlate TippingPoint block events with firewall and endpoint data for full incident context.",
        "terms": [
            ("Splunk", "Leading SIEM and log analysis platform; TippingPoint add-on available on Splunkbase"),
            ("QRadar", "IBM SIEM platform; pre-built TippingPoint DSM for automatic event parsing"),
            ("DSM", "Device Support Module — QRadar component for parsing a specific log source"),
            ("Splunkbase", "Splunk's app marketplace — search 'TippingPoint' for official add-on"),
            ("Correlation", "Combining events from multiple sources (IPS, firewall, endpoint) to build full incident picture"),
            ("CEF", "Common Event Format — the recommended format for TippingPoint syslog to SIEM"),
        ],
        "questions": [
            ("What Splunk component do you need for TippingPoint integration?", "The Trend Micro TippingPoint Add-on from Splunkbase — provides field extractions and dashboards"),
            ("What is a QRadar DSM?", "Device Support Module — pre-built parser that automatically extracts fields from TippingPoint log entries"),
            ("Name three useful SIEM dashboards for TippingPoint data.", "Top Blocked Sources, Top Triggered Filters, Geographic map of blocked IPs, Trend over time charts"),
        ],
        "links": [
            ("Splunk — TippingPoint Add-on (Splunkbase)", "https://splunkbase.splunk.com/app/4077/"),
            ("Trend Micro TippingPoint Documentation", "https://docs.trendmicro.com/en-us/enterprise/tippingpoint.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
        ]
    },
    "9-4": {
        "notes": "SIEM integration lab.\n\nLab tasks: 1) In SMS, go to Administration → Notifications → Syslog. 2) Add a syslog destination — use your lab syslog server IP, port 514, format CEF. 3) Enable forwarding of Security Events and System Events. 4) Click 'Send Test Message' and verify it arrives at your syslog server. 5) Configure SNMPv3: Administration → SNMP. Set up a v3 user with SHA auth and AES encryption. 6) Configure your NMS to poll TippingPoint via SNMP. 7) Verify CPU and memory OIDs return values. 8) Configure an SNMP trap destination. 9) Trigger a test trap and verify receipt. 10) If Splunk is available: install the TippingPoint add-on, configure the log source, and verify events appear. 11) Build a simple search showing top 10 blocked source IPs from the last 7 days.",
        "terms": [
            ("CEF Test Message", "Verify format and connectivity before relying on it for production monitoring"),
            ("SNMP Poll Test", "Use snmpwalk or your NMS to verify OIDs return correct values"),
            ("Splunk Search", "index=main sourcetype=tippingpoint action=Block | top src_ip"),
        ],
        "questions": [
            ("What Splunk search shows the top blocked source IPs?", "index=main sourcetype=tippingpoint action=Block | top src_ip"),
            ("After configuring syslog, what should you always do before considering the integration complete?", "Send a test message and verify it arrives correctly formatted in the SIEM"),
        ],
        "links": [
            ("Splunk — TippingPoint Add-on (Splunkbase)", "https://splunkbase.splunk.com/app/4077/"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Graylog — Free SIEM/Log Management", "https://graylog.org/products/open-source/"),
        ]
    },
}
