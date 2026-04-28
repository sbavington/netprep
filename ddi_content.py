LESSON_CONTENT = {
    "ddi-1-1": {
        "notes": "Deep Discovery Inspector (DDI) is Trend Micro's network traffic analysis appliance designed to detect Advanced Persistent Threats (APTs) and targeted attacks that bypass traditional security controls. Traditional security — firewalls, antivirus, IPS — works well against known threats but struggles with sophisticated, customised attacks. APTs use spear phishing, zero-day exploits, and custom malware specifically crafted to evade signature-based detection.\n\nDDI operates out-of-band (passively monitoring a copy of network traffic) and uses multiple detection methods simultaneously: pattern matching against known threats, heuristic analysis for suspicious behaviour, and sandbox detonation of unknown files in an isolated virtual environment. This layered approach catches threats that each individual method would miss. DDI generates detailed threat intelligence alerts with full context — what happened, when, which systems were involved, and what data may have been accessed.",
        "terms": [
            ("DDI", "Deep Discovery Inspector — Trend Micro's network threat detection appliance for APTs and targeted attacks"),
            ("APT", "Advanced Persistent Threat — sophisticated, long-term targeted attack by skilled adversaries"),
            ("Out-of-Band", "DDI receives a copy of traffic for analysis without being in the traffic path"),
            ("Sandbox", "Isolated virtual environment where suspicious files are executed safely to observe behaviour"),
            ("Heuristic Analysis", "Detecting threats based on suspicious behaviour patterns rather than known signatures"),
            ("Targeted Attack", "Attack specifically crafted against a particular organisation, often evading generic defences"),
        ],
        "questions": [
            ("Why can't traditional security tools reliably detect APTs?", "APTs use custom malware and techniques specifically designed to evade signature-based detection used by AV and IPS"),
            ("What is the key difference between DDI and TippingPoint IPS?", "TippingPoint is inline and blocks threats; DDI is out-of-band and detects/alerts without blocking traffic"),
            ("What three detection methods does DDI use?", "Pattern matching (known threats), heuristic analysis (suspicious behaviour), and sandbox detonation (unknown files)"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Overview", "https://www.trendmicro.com/en_us/business/products/network/advanced-threat-protection.html"),
            ("Trend Micro — What is an APT?", "https://www.trendmicro.com/vinfo/us/security/definition/advanced-persistent-threat"),
            ("MITRE ATT&CK Framework", "https://attack.mitre.org/"),
        ]
    },
    "ddi-1-2": {
        "notes": "DDI uses several detection engines working together. The Network Content Inspection Engine (NCIE) examines network traffic for known malicious patterns, suspicious protocols, and command-and-control (C&C) communication. The Network Content Correlation Engine (NCCE) correlates events across time and hosts to identify multi-stage attack campaigns that no single event would reveal alone.\n\nThe Virtual Analyzer (sandbox) receives suspicious files and URLs submitted by the NCIE. It executes them in isolated Windows and other OS virtual machines and observes behaviour — does the file try to disable security software? Does it make outbound connections? Does it create registry keys for persistence? The combination of all engines produces a risk level score and detailed event information. DDI also integrates with Trend Micro's Smart Protection Network for cloud-based threat intelligence lookups.",
        "terms": [
            ("NCIE", "Network Content Inspection Engine — inspects traffic for known threats and suspicious patterns"),
            ("NCCE", "Network Content Correlation Engine — correlates events across hosts and time to find attack campaigns"),
            ("Virtual Analyzer", "DDI's built-in sandbox — executes suspicious files in isolated VMs to observe behaviour"),
            ("C&C", "Command and Control — communication between malware and the attacker's server"),
            ("Smart Protection Network", "Trend Micro's cloud threat intelligence service providing real-time lookups"),
            ("Risk Score", "DDI's rating of how dangerous a detected event is, based on combined engine analysis"),
        ],
        "questions": [
            ("What does the NCCE do that the NCIE cannot?", "The NCCE correlates events across multiple hosts and time periods to identify attack campaigns — single events may look benign but the pattern reveals an attack"),
            ("Why is sandboxing important for unknown files?", "Unknown files have no signatures to match — executing them safely in a VM reveals malicious behaviour that signatures would miss"),
            ("What is C&C traffic?", "Communication between malware installed on a victim's machine and the attacker's server — used to receive instructions and exfiltrate data"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Smart Protection Network", "https://www.trendmicro.com/en_us/business/technologies/smart-protection-network.html"),
            ("MITRE ATT&CK — C&C Techniques", "https://attack.mitre.org/tactics/TA0011/"),
        ]
    },
    "ddi-1-3": {
        "notes": "DDI is most effective as part of a layered security architecture, not as a standalone product. In a typical deployment, DDI sits alongside other controls: the firewall controls access, TippingPoint blocks known exploits inline, endpoint security protects individual machines, and DDI monitors network traffic for the sophisticated threats that bypass everything else.\n\nDDI integrates with Trend Micro's other products through the Trend Micro Control Manager (now Apex Central) for centralised management and threat sharing. When DDI detects a C&C server, it can automatically push that indicator to TippingPoint to block future connections. This automated threat sharing — sometimes called Connected Threat Defence — means your security products work together rather than in isolation. DDI also feeds into SIEM platforms via syslog for correlation with non-Trend Micro security data.",
        "terms": [
            ("Layered Security", "Using multiple security controls together — each layer catches what others miss"),
            ("Apex Central", "Trend Micro's centralised management and threat sharing platform (formerly Control Manager)"),
            ("Connected Threat Defence", "Trend Micro's framework for automatic threat intelligence sharing between products"),
            ("Indicator of Compromise (IOC)", "Evidence of a breach — malicious IPs, file hashes, domain names shared between security tools"),
            ("SIEM", "Security Information and Event Management — centralised log analysis platform"),
        ],
        "questions": [
            ("What types of threats is DDI specifically designed to catch?", "APTs, targeted attacks, zero-day malware, and C&C communications that bypass signature-based controls"),
            ("How does DDI work with TippingPoint?", "DDI detects C&C servers and shares those IPs/domains with TippingPoint, which then blocks future connections to those addresses"),
            ("What is Connected Threat Defence?", "Trend Micro's framework where products automatically share threat intelligence with each other to improve collective protection"),
        ],
        "links": [
            ("Trend Micro Connected Threat Defence", "https://www.trendmicro.com/en_us/business/technologies/connected-threat-defense.html"),
            ("Trend Micro Apex Central", "https://www.trendmicro.com/en_us/business/products/network/advanced-threat-protection.html"),
            ("MITRE ATT&CK Framework", "https://attack.mitre.org/"),
        ]
    },
    "ddi-1-4": {
        "notes": "Module 1 review quiz. Ensure you understand what DDI is, how it differs from traditional security tools, and where it fits in a security architecture before moving on to hardware installation.",
        "terms": [
            ("DDI vs IPS", "IPS is inline and blocks; DDI is out-of-band and detects/alerts"),
            ("DDI vs Firewall", "Firewall controls access by rules; DDI analyses traffic content for sophisticated threats"),
            ("DDI vs AV", "AV matches known signatures on endpoints; DDI detects unknown threats on the network using sandbox"),
        ],
        "questions": [
            ("Is DDI inline or out-of-band?", "Out-of-band — it receives a copy of traffic and does not sit in the traffic path"),
            ("What three detection engines does DDI use?", "NCIE (pattern matching), NCCE (correlation), and Virtual Analyzer (sandbox)"),
            ("What is an APT?", "Advanced Persistent Threat — a sophisticated, long-term targeted attack by skilled adversaries"),
            ("Why is DDI needed if you already have a firewall and IPS?", "Firewalls and IPS work against known threats; DDI catches sophisticated, customised attacks specifically designed to evade those controls"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Overview", "https://www.trendmicro.com/en_us/business/products/network/advanced-threat-protection.html"),
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("MITRE ATT&CK Framework", "https://attack.mitre.org/"),
        ]
    },
    "ddi-2-1": {
        "notes": "Deep Discovery Inspector is available in several hardware models designed for different network throughputs. Entry-level models handle 250Mbps-1Gbps and are suitable for small to medium organisations. Mid-range models handle 2-4Gbps for larger environments. High-end models handle 10Gbps+ for large enterprise and data centre deployments. The model number typically reflects the rated throughput — DDI 4100 handles up to 4Gbps, for example.\n\nAll models include: monitoring (capture) interfaces for receiving traffic copies, a management interface for administration, and internal storage for logs and sandbox analysis results. Higher-end models include more CPU cores, memory, and faster storage to handle the increased analysis workload. The Virtual Analyzer requires significant compute resources — sandboxing files is CPU-intensive. When selecting a model, account for both current traffic volumes and expected growth. Always size up — undersized DDI will drop packets and miss threats.",
        "terms": [
            ("Monitoring Interface", "DDI's capture interface — receives a copy of network traffic for analysis"),
            ("Management Interface", "Dedicated interface for administration — separate from monitoring interfaces"),
            ("Throughput Rating", "Maximum traffic speed the DDI model can analyse without dropping packets"),
            ("Virtual Analyzer Capacity", "Number of sandbox VMs and concurrent analysis jobs the model supports"),
            ("DDI 4100", "Example mid-range model — 4Gbps throughput; check current Trend Micro product catalogue for current models"),
        ],
        "questions": [
            ("What is the difference between monitoring and management interfaces on DDI?", "Monitoring interfaces receive traffic copies for analysis; management interface is for SSH/HTTPS administration"),
            ("What happens if DDI is undersized for the traffic volume?", "It drops packets and misses threats — always size DDI based on peak traffic, not average"),
            ("Why does Virtual Analyzer require significant compute resources?", "Executing files in sandboxed VMs is CPU-intensive — each analysis spins up one or more virtual machines"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Inspector Datasheet", "https://www.trendmicro.com/en_us/business/products/network/advanced-threat-protection.html"),
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-2-2": {
        "notes": "DDI mounts in a standard rack like any 1U or 2U appliance. The physical installation process: verify the model's U-height, attach rack ears, slide into position, and secure with screws. Connect the management interface to your management network first. Then plan your monitoring interface cabling based on your chosen deployment method.\n\nKey physical consideration: DDI monitoring interfaces are receive-only — they don't transmit. This means you need a separate mechanism to get traffic to them: either a SPAN port on a switch, or a network TAP. Cable planning is critical. For 10Gbps monitoring you need appropriate SFP+ modules and DAC cables or fibre. Label every cable before installation. Document what connects where. The management interface needs connectivity to DNS, NTP, and Trend Micro's update servers — plan firewall rules accordingly before installation day.",
        "terms": [
            ("Receive-Only Interface", "DDI monitoring ports only receive traffic — they do not transmit; purely passive"),
            ("SPAN Port", "Switch Port Analyser — copies traffic from specified switch ports to DDI's monitoring interface"),
            ("Network TAP", "Hardware device that passively copies all traffic on a link to DDI — more reliable than SPAN"),
            ("SFP+", "10Gbps transceiver module for fibre monitoring interfaces"),
            ("DAC Cable", "Direct Attach Copper — short-range 10Gbps cable; cheaper than fibre for short runs"),
        ],
        "questions": [
            ("Why are DDI's monitoring interfaces receive-only?", "DDI is purely passive — it only analyses traffic copies and never injects or modifies traffic"),
            ("What is the difference between a SPAN port and a network TAP?", "SPAN is software-configured on a switch (may drop packets under load); TAP is dedicated hardware that passively copies all traffic (more reliable)"),
            ("What network access does DDI's management interface need?", "DNS resolution, NTP time sync, and access to Trend Micro update servers for pattern updates"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Network TAP vs SPAN Explained", "https://www.garlandtechnology.com/tap-vs-span"),
        ]
    },
    "ddi-2-3": {
        "notes": "Getting traffic to DDI's monitoring interfaces requires either a SPAN port or a network TAP. SPAN ports are configured on managed switches and copy traffic from specified source ports or VLANs to a destination port connected to DDI. SPAN is convenient and free — no additional hardware needed. However, SPAN has limitations: under high load, switches may drop SPAN packets (they prioritise production traffic), and SPAN may not capture all traffic types on some switches.\n\nNetwork TAPs are purpose-built hardware devices placed inline on a network link. They passively copy all traffic to monitoring ports without affecting the production traffic path. TAPs never drop packets and capture everything. They're the gold standard for security monitoring. Passive optical TAPs have no power requirement and can't fail in a way that affects production — if the TAP fails, production traffic still flows through. Active TAPs require power but support copper links and provide more features. For critical monitoring points, always use a TAP over SPAN.",
        "terms": [
            ("SPAN", "Switch Port Analyser — copies traffic to a monitoring port; configured in switch software"),
            ("RSPAN", "Remote SPAN — copies traffic across multiple switches using a dedicated VLAN"),
            ("Passive Optical TAP", "Splits optical signal with no active components — cannot fail in a way that affects traffic"),
            ("Active TAP", "Powered TAP for copper links — copies traffic but requires power to operate"),
            ("TAP Aggregation", "Combining traffic from multiple TAPs into one monitoring port on DDI"),
            ("SPAN Limitations", "May drop packets under load; some traffic types not captured; switch CPU overhead"),
        ],
        "questions": [
            ("When should you use a TAP instead of SPAN?", "For critical monitoring points where packet loss is unacceptable, or on high-throughput links where SPAN may drop packets"),
            ("What happens to production traffic if a passive optical TAP fails?", "Production traffic continues to flow — the optical signal passes through regardless of TAP health"),
            ("What is RSPAN?", "Remote SPAN — extends SPAN across multiple switches using a dedicated VLAN to bring traffic to a central monitoring point"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Network TAP vs SPAN Explained", "https://www.garlandtechnology.com/tap-vs-span"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-2-4": {
        "notes": "Hardware installation lab. Complete these tasks in order.\n\nLab tasks: 1) Review the DDI quick start guide for your model — note the management and monitoring port locations. 2) Plan your cable layout on paper before touching any hardware. 3) Mount the appliance in the rack — attach ears, slide in, secure with screws. 4) Connect the management interface to your management switch. 5) Connect your console cable (serial or USB depending on model). 6) Plan your SPAN or TAP configuration — draw a diagram showing which switch ports will be spanned and where the monitoring cable connects to DDI. 7) Configure your SPAN port on the switch before powering on DDI. 8) Connect monitoring interface cables. 9) Connect power. 10) Power on and observe boot on console. 11) Record firmware version from boot output.",
        "terms": [
            ("Quick Start Guide", "Model-specific document with port diagrams — always read before installation"),
            ("Console Access", "Serial or USB console for out-of-band access during initial setup"),
            ("Pre-installation Planning", "Drawing cable diagrams and planning SPAN before touching hardware saves significant time"),
        ],
        "questions": [
            ("What should you do before connecting any cables?", "Plan your layout on paper — draw a diagram showing which port connects where"),
            ("Why configure the SPAN port before powering on DDI?", "So traffic starts flowing to the monitoring interface immediately on first boot, making it easier to verify the setup"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("PuTTY — Free SSH/Serial Client", "https://www.putty.org/"),
        ]
    },
    "ddi-3-1": {
        "notes": "On first boot, DDI presents a setup wizard via the console or web browser. The management interface needs an IP address before you can use HTTPS. Connect via console first: serial settings are typically 9600 8N1 (same as TippingPoint). The initial setup wizard walks you through: setting the management IP, subnet mask, and default gateway; setting the admin password; configuring basic network settings.\n\nOnce the management IP is set, you can access the DDI web console via HTTPS at https://<management-ip>. DDI uses a self-signed certificate by default — your browser will warn you. Accept the certificate or install a proper one from your internal CA. The web console is the primary management interface for DDI — unlike TippingPoint, most DDI configuration is done through the GUI rather than CLI. The CLI is available via SSH but is used mainly for diagnostics.",
        "terms": [
            ("Setup Wizard", "First-boot configuration wizard for initial DDI setup"),
            ("Web Console", "HTTPS-based management GUI — primary interface for DDI administration"),
            ("9600 8N1", "Console port settings: 9600 baud, 8 data bits, No parity, 1 stop bit"),
            ("Self-Signed Certificate", "Default HTTPS cert — replace with CA-signed cert in production"),
            ("Management IP", "IP address for administrative access to DDI web console and SSH"),
        ],
        "questions": [
            ("What is the primary management interface for DDI?", "The web console — HTTPS-based GUI accessed at https://<management-ip>"),
            ("What console settings does DDI use?", "9600 baud, 8 data bits, no parity, 1 stop bit (9600 8N1)"),
            ("Why does DDI use a web console rather than primarily CLI?", "DDI's complexity — threat dashboards, sandbox results, reports — is better suited to a graphical interface than a command line"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("PuTTY — Free SSH/Serial Client", "https://www.putty.org/"),
        ]
    },
    "ddi-3-2": {
        "notes": "DDI has multiple network interfaces serving different purposes. The management interface (eth0 or similar) handles all administrative traffic — web console, SSH, software updates, pattern downloads, and integration with other Trend Micro products. Monitoring interfaces receive traffic copies from SPAN ports or TAPs — they have no IP address and do not transmit.\n\nIP configuration: in the web console, go to Administration → Network Interface. Set the management IP, subnet mask, gateway, and DNS servers. The management interface should be on a dedicated management VLAN, separate from production traffic. Routing: DDI needs a default gateway on the management interface to reach update servers and integrate with other products. If your management network is isolated, configure explicit routes to Trend Micro's update servers. Verify connectivity with the built-in ping tool in the web console.",
        "terms": [
            ("eth0", "Typical management interface name — verify in your model's documentation"),
            ("Management VLAN", "Dedicated VLAN for administrative traffic — isolates management from production"),
            ("No-IP Monitoring Interface", "Monitoring ports have no IP address — they are purely passive capture interfaces"),
            ("DNS Configuration", "Required for DDI to resolve Trend Micro update server hostnames"),
            ("Built-in Ping", "Web console tool for testing management network connectivity"),
        ],
        "questions": [
            ("Why do monitoring interfaces have no IP address?", "They are purely passive receive-only interfaces — no IP needed because they never initiate or respond to connections"),
            ("What network access does DDI's management interface need?", "DNS, NTP, access to Trend Micro update servers, and connectivity to Apex Central if used"),
            ("Where in the DDI web console do you configure IP settings?", "Administration → Network Interface"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-3-3": {
        "notes": "DDI is designed as an out-of-band (passive) monitoring device. It receives a copy of traffic via SPAN or TAP and analyses it without affecting the production network. This is different from inline deployment where the device sits in the traffic path. Out-of-band deployment means: if DDI fails, production traffic is unaffected. DDI cannot block traffic — it only detects and alerts.\n\nPlacement decisions: where you place your SPAN or TAP determines what DDI can see. Common placements: at the internet perimeter (sees all north-south traffic), at the core switch (sees all internal traffic including east-west), or at specific high-value segments (DMZ, finance VLAN). For maximum visibility, span the core switch uplink — this captures all traffic in and out of the network. For lateral movement detection, span inter-VLAN routing interfaces. Document what each monitoring interface is capturing — critical for interpreting alerts.",
        "terms": [
            ("Out-of-Band", "Passive deployment receiving traffic copies — DDI cannot block, only detect and alert"),
            ("North-South Traffic", "Traffic flowing in and out of the network — perimeter traffic"),
            ("East-West Traffic", "Traffic flowing between internal systems — lateral movement detection"),
            ("Perimeter Placement", "SPAN/TAP at internet edge — sees external threats but misses internal lateral movement"),
            ("Core Placement", "SPAN/TAP at core switch — sees all traffic but requires high-throughput DDI model"),
            ("Segment Placement", "SPAN/TAP at specific high-value segments — targeted monitoring"),
        ],
        "questions": [
            ("What is the key limitation of out-of-band deployment?", "DDI cannot block traffic — it can only detect threats and generate alerts for human or automated response"),
            ("Why is east-west monitoring important?", "Once an attacker is inside the network, they move laterally between systems — east-west monitoring detects this internal movement"),
            ("What is the trade-off of spanning the core switch?", "Maximum visibility but requires a high-throughput DDI model to handle all internal traffic without dropping packets"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("MITRE ATT&CK — Lateral Movement", "https://attack.mitre.org/tactics/TA0008/"),
        ]
    },
    "ddi-3-4": {
        "notes": "NTP, DNS, and proxy settings are essential for DDI to function correctly. NTP: accurate time is critical for log correlation and certificate validation. Configure at least two NTP servers. In the web console: Administration → Time. DNS: DDI needs to resolve hostnames for Trend Micro update servers and Smart Protection Network queries. Configure primary and secondary DNS. Administration → Network Interface → DNS.\n\nProxy: many organisations route internet traffic through a proxy. If DDI's management interface needs to go through a proxy to reach Trend Micro update servers, configure it in Administration → Proxy. Without proxy configuration, pattern updates will fail silently. After configuring all three, use the built-in connectivity test tools to verify DDI can reach Trend Micro's servers. Also configure the SMTP settings if you want DDI to send email alerts — Administration → Notifications → SMTP. Test with a test email before relying on email alerts.",
        "terms": [
            ("NTP", "Network Time Protocol — synchronises DDI clock; critical for accurate logs"),
            ("Proxy", "HTTP proxy for outbound internet access from the management interface"),
            ("Pattern Update", "DDI's threat detection patterns downloaded from Trend Micro — must be kept current"),
            ("SMTP", "Email server settings for DDI alert notifications"),
            ("Connectivity Test", "Built-in DDI tool to verify it can reach Trend Micro update servers"),
        ],
        "questions": [
            ("Why is NTP so important for DDI?", "Log timestamps must be accurate for incident investigation and correlation with other security tools"),
            ("What happens if proxy is not configured when required?", "Pattern updates fail silently — DDI appears to be running normally but threat detection becomes outdated"),
            ("How do you verify DDI can reach Trend Micro update servers?", "Use the built-in connectivity test in the web console after configuring proxy and DNS settings"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("NTP Pool Project", "https://www.ntppool.org/"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-3-5": {
        "notes": "Initial configuration lab. Complete these tasks in sequence.\n\nLab tasks: 1) Connect to DDI web console via HTTPS at https://<management-ip>. 2) Accept the certificate warning and log in with default credentials. 3) Change the admin password immediately. 4) Go to Administration → Network Interface — verify management IP is correct. 5) Go to Administration → Time — configure two NTP servers and verify sync. 6) Go to Administration → Proxy — configure if required in your environment. 7) Go to Administration → Pattern Update — trigger a manual update and verify it succeeds. 8) Go to Administration → Notifications → SMTP — configure email server and send a test email. 9) Go to Dashboard — verify monitoring interfaces show traffic (if SPAN is configured). 10) Check Detection → Detections — note whether any initial detections have appeared. 11) Record the current pattern version for your baseline.",
        "terms": [
            ("Pattern Version", "The current threat detection pattern version — record as baseline after initial setup"),
            ("Default Credentials", "Check Trend Micro documentation for your specific model — change immediately on first login"),
            ("Manual Pattern Update", "Trigger immediately after setup to ensure DDI has current threat patterns"),
        ],
        "questions": [
            ("What should you do immediately after first login?", "Change the admin password — never leave default credentials in place"),
            ("How do you verify monitoring interfaces are receiving traffic?", "Check the Dashboard — monitoring interface traffic graphs should show traffic if SPAN is configured correctly"),
            ("Why trigger a manual pattern update immediately after setup?", "The appliance may have been built weeks or months ago — the patterns on disk may be significantly out of date"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-4-1": {
        "notes": "DDI uses multiple types of detection patterns that must be kept up to date. Pattern files are the signature database — updated daily by Trend Micro as new threats are discovered. Rule-based detection uses heuristics and behaviour patterns to detect suspicious activity even without specific signatures. The Advanced Threat Scan Engine (ATSE) combines pattern matching with machine learning to detect novel malware variants.\n\nPattern updates are pulled from Trend Micro's update servers automatically on a schedule you configure. Critical updates are pushed immediately when major threats emerge. In the web console: Administration → Pattern Update. Configure the update schedule (hourly is recommended for production), enable automatic updates, and set a rollback point in case a bad pattern causes false positives. Monitor the pattern update status regularly — a failed update means your detection is falling behind. The component status page shows the version and age of each pattern file.",
        "terms": [
            ("Pattern File", "Signature database downloaded from Trend Micro — updated daily with new threat signatures"),
            ("ATSE", "Advanced Threat Scan Engine — combines signatures with machine learning for novel threat detection"),
            ("Rule-Based Detection", "Heuristic rules detecting suspicious behaviour without requiring specific signatures"),
            ("Pattern Rollback", "Reverting to a previous pattern version if a new pattern causes false positives"),
            ("Component Status", "DDI page showing version and age of all installed pattern files"),
        ],
        "questions": [
            ("How often should DDI pattern updates be scheduled?", "Hourly in production — threat intelligence changes rapidly and daily updates leave you exposed"),
            ("What is pattern rollback used for?", "Reverting to a previous pattern version if a newly updated pattern causes excessive false positives"),
            ("Where do you check pattern update status in DDI?", "Administration → Pattern Update — shows current version, last update time, and update schedule"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Threat Encyclopedia", "https://www.trendmicro.com/vinfo/us/threat-encyclopedia/"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-4-2": {
        "notes": "The Smart Protection Network (SPN) is Trend Micro's cloud-based threat intelligence service. DDI queries SPN in real time to check file reputations, URL reputations, and IP reputations. If a file hash is known malicious, SPN returns a verdict immediately without needing sandbox analysis. URL reputation checks identify malicious websites and phishing pages. C&C callback detection uses SPN to identify known C&C server IPs and domains.\n\nSPN queries require DDI's management interface to have outbound internet access to Trend Micro's cloud servers. In air-gapped or restricted environments, the Smart Protection Server (SPS) can be deployed on-premises as a local SPN proxy. SPS caches reputation data locally and serves queries from DDI without requiring direct internet access. This is the recommended approach for high-security environments. Configure Smart Protection settings in Administration → Smart Protection.",
        "terms": [
            ("Smart Protection Network", "Trend Micro's cloud threat intelligence — file, URL, and IP reputation lookups"),
            ("File Reputation", "Cloud lookup to determine if a file hash is known malicious"),
            ("URL Reputation", "Cloud lookup to identify malicious websites and phishing pages"),
            ("C&C Callback Detection", "Identifying traffic to known command-and-control servers using cloud reputation data"),
            ("Smart Protection Server", "On-premises local SPN proxy for air-gapped environments"),
        ],
        "questions": [
            ("What does Smart Protection Network provide to DDI?", "Real-time cloud-based lookups for file reputation, URL reputation, and IP/domain reputation"),
            ("What is a Smart Protection Server?", "An on-premises appliance that proxies SPN queries locally — used when DDI cannot have direct internet access"),
            ("What happens to SPN lookups if DDI loses internet connectivity?", "Reputation checks fall back to local patterns only — protection continues but without cloud intelligence until connectivity is restored"),
        ],
        "links": [
            ("Trend Micro Smart Protection Network", "https://www.trendmicro.com/en_us/business/technologies/smart-protection-network.html"),
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-4-3": {
        "notes": "Detection policies define what DDI monitors and how it responds to detections. In the web console: Detection → Detection Policies. The default policy monitors all traffic on all monitoring interfaces. You can create custom policies for specific network segments or traffic types with different sensitivity settings.\n\nKey policy settings: detection sensitivity (high sensitivity catches more but generates more false positives), monitored protocols (HTTP, SMTP, FTP, SMB, and others), file types submitted to Virtual Analyzer (All, or specific types), and notification settings (which alerts trigger emails or SIEM events). For initial deployment, start with the default policy and medium sensitivity. After a few weeks of tuning, adjust based on your environment. Enable all protocol monitoring — attackers use every available protocol for exfiltration and C&C.",
        "terms": [
            ("Detection Policy", "Configuration defining what DDI monitors and how it handles detections"),
            ("Detection Sensitivity", "Low (fewer false positives) vs High (catches more but noisier) — tune for your environment"),
            ("Protocol Monitoring", "Which network protocols DDI analyses — enable all for maximum coverage"),
            ("File Submission Policy", "Which file types are sent to Virtual Analyzer sandbox for analysis"),
            ("Notification Settings", "Which detection types trigger alerts, emails, or syslog events"),
        ],
        "questions": [
            ("What is the recommended approach for initial policy configuration?", "Start with default policy and medium sensitivity, then tune based on your environment after observing results for a few weeks"),
            ("Why enable all protocol monitoring?", "Attackers use every available protocol — limiting monitoring to just HTTP leaves you blind to SMTP, SMB, FTP, and other exfiltration paths"),
            ("What is the trade-off of high detection sensitivity?", "Catches more threats but generates more false positives — requires more tuning and analyst time"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("MITRE ATT&CK — Exfiltration Techniques", "https://attack.mitre.org/tactics/TA0010/"),
        ]
    },
    "ddi-4-4": {
        "notes": "Exception lists (also called trusted sources) tell DDI to skip analysis of traffic from specific IPs, domains, or file hashes that are known safe. Common use cases: vulnerability scanners that trigger detections when scanning your own network, patch management servers downloading software packages, backup systems transferring large encrypted files, and known-good internal tools that match threat patterns.\n\nCreating exceptions: Detection → Exceptions. Add by IP address, CIDR range, domain name, URL, or file hash. Be as specific as possible — never add broad exceptions. Document every exception with the reason, date, and approver. Review exceptions quarterly and remove stale ones. Exceptions reduce your visibility — each one is a potential blind spot. If a vulnerability scanner is triggering too many false positives, the better solution is to schedule scans during off-hours and create a time-limited exception rather than a permanent one.",
        "terms": [
            ("Trusted Source", "IP, domain, or file hash excluded from DDI analysis"),
            ("Exception", "Rule telling DDI to skip analysis of specific traffic"),
            ("Vulnerability Scanner Exception", "Common requirement — scanners probe for vulnerabilities and trigger IDS/IPS/DDI detections"),
            ("File Hash Exception", "Excluding a specific known-good file from sandbox analysis"),
            ("Exception Review", "Quarterly audit of all exceptions to remove stale or unnecessary ones"),
        ],
        "questions": [
            ("Why should exceptions be reviewed quarterly?", "Stale exceptions are blind spots — if a trusted host is compromised, DDI won't detect malicious traffic from it"),
            ("What is better than a permanent exception for a vulnerability scanner?", "A scheduled time-limited exception during scan windows, so DDI monitors the scanner's traffic at other times"),
            ("What should always be documented when creating an exception?", "The reason for the exception, date created, who approved it, and when it should be reviewed or removed"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-4-5": {
        "notes": "Detection policy lab. Complete these tasks.\n\nLab tasks: 1) Go to Detection → Detection Policies — review the default policy settings. 2) Note which protocols are currently enabled for monitoring. 3) Enable any protocols that are not currently monitored. 4) Review file submission settings — ensure executable and document types are submitted to Virtual Analyzer. 5) Set detection sensitivity to Medium if not already. 6) Go to Administration → Pattern Update — trigger a manual update. 7) Go to Detection → Exceptions — review any existing exceptions. 8) Add an exception for your workstation IP with reason 'Lab testing'. 9) Verify the exception appears in the list. 10) Generate some test traffic (browse websites, download a file) and check Detection → Detections for any results. 11) Remove the test exception you created.",
        "terms": [
            ("Protocol Review", "Verify all relevant protocols are enabled before going live"),
            ("Test Exception", "Always remove test exceptions — never leave lab configurations in production"),
            ("Detection Verification", "After policy changes, verify detections appear as expected"),
        ],
        "questions": [
            ("After enabling a new protocol for monitoring, what should you verify?", "Check Detection → Detections for new events related to that protocol — confirm DDI is actually capturing and analysing it"),
            ("Why remove test exceptions before going live?", "Test exceptions left in production create blind spots — all exceptions must have a documented business reason"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-5-1": {
        "notes": "Virtual Analyzer is DDI's built-in sandbox — an isolated environment where suspicious files and URLs are executed safely to observe their behaviour. When DDI's inspection engine encounters a suspicious file that cannot be classified as safe or malicious by pattern matching alone, it submits it to Virtual Analyzer for deeper analysis.\n\nVirtual Analyzer runs multiple virtual machines with different OS versions (Windows 7, Windows 10, Windows Server) and applications (Office, PDF reader, browser). The suspicious file is executed in each relevant VM, and every action is recorded: file system changes, registry modifications, network connections attempted, processes created, API calls made. After analysis (typically 3-5 minutes), Virtual Analyzer produces a detailed report with a risk score. High-risk results trigger alerts. This behaviour-based approach catches zero-day malware that has no signature — even malware written specifically for your organisation.",
        "terms": [
            ("Virtual Analyzer", "DDI's built-in sandbox — executes suspicious files in isolated VMs to observe behaviour"),
            ("Sandbox VM", "Isolated virtual machine where malware runs safely without affecting real systems"),
            ("Behaviour Analysis", "Observing what a file does when executed rather than matching it to known signatures"),
            ("Risk Score", "Virtual Analyzer's rating of how dangerous the analysed sample is"),
            ("Zero-Day Detection", "Catching malware with no known signature through behaviour analysis"),
            ("Analysis Time", "Typically 3-5 minutes per sample — impacts how quickly DDI can alert on new threats"),
        ],
        "questions": [
            ("Why is sandboxing necessary for zero-day malware?", "Zero-day malware has no signatures — only by executing it and observing behaviour can DDI determine if it's malicious"),
            ("What does Virtual Analyzer record during analysis?", "File system changes, registry modifications, network connections, processes created, and API calls made by the sample"),
            ("Why does Virtual Analyzer use multiple OS versions?", "Malware often targets specific OS versions — testing in multiple environments catches samples that only detonate on certain systems"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Virtual Analyzer Overview", "https://www.trendmicro.com/en_us/business/products/network/advanced-threat-protection.html"),
            ("MITRE ATT&CK — Defense Evasion", "https://attack.mitre.org/tactics/TA0005/"),
        ]
    },
    "ddi-5-2": {
        "notes": "Configuring Virtual Analyzer involves setting up the analysis VMs and configuring submission policies. In the web console: Virtual Analyzer → Settings. Key configuration: VM images (which OS versions to use for analysis), network settings for VMs (usually isolated with no real internet — use a simulated internet environment), submission settings (which file types trigger sandbox analysis), and capacity settings (how many concurrent analyses to run).\n\nVM images must be representative of your environment — if your users run Windows 10 with Office 365, configure VMs to match. Malware authors sometimes check the OS version before detonating. Custom VM images can be created with your specific software stack for maximum fidelity. Network settings in VMs: connecting sandbox VMs to the real internet allows malware to complete its C&C communication — useful for observing full behaviour but requires careful network isolation to prevent actual damage. Most organisations use a simulated internet environment instead.",
        "terms": [
            ("VM Image", "Virtual machine template used for sandbox analysis — configure to match your user environment"),
            ("Simulated Internet", "Fake internet environment for sandbox VMs — captures network behaviour without real internet risk"),
            ("Submission Policy", "Configuration defining which file types are automatically submitted to Virtual Analyzer"),
            ("Concurrent Analysis", "Number of simultaneous sandbox analyses — limited by DDI hardware capacity"),
            ("Custom VM Image", "VM built with your specific software stack for maximum analysis fidelity"),
        ],
        "questions": [
            ("Why should sandbox VMs match your user environment?", "Sophisticated malware checks the OS and application versions before detonating — mismatched VMs may not trigger the malicious behaviour"),
            ("What is the risk of connecting sandbox VMs to the real internet?", "Malware could complete C&C communication, receive additional payloads, or potentially exfiltrate data from the sandbox VM"),
            ("What is a simulated internet environment?", "A fake DNS/HTTP/SMTP environment that satisfies malware's network requests without real internet connectivity"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-5-3": {
        "notes": "File submission to Virtual Analyzer happens automatically based on your submission policy, but you can also submit files manually for investigation. Automatic submission: DDI's inspection engine extracts files from network traffic (email attachments, web downloads, FTP transfers) and submits them to Virtual Analyzer based on file type and risk indicators. The submission queue is visible in Virtual Analyzer → Submissions.\n\nManual submission: useful when investigating a suspected incident. Upload a suspicious file directly to Virtual Analyzer via the web console. You can also submit file hashes for reputation checks without re-analysis. URL submission: DDI can submit suspicious URLs to Virtual Analyzer, which opens them in a sandboxed browser and observes behaviour — useful for detecting drive-by download sites and phishing pages. The submission queue shows pending, in-progress, and completed analyses. Monitor queue depth — a consistently full queue means DDI is overwhelmed and may be dropping submissions.",
        "terms": [
            ("Submission Queue", "List of files and URLs pending or in Virtual Analyzer analysis"),
            ("Automatic Submission", "DDI automatically submits suspicious files based on the submission policy"),
            ("Manual Submission", "Directly uploading a file to Virtual Analyzer for investigation"),
            ("URL Submission", "Opening suspicious URLs in a sandboxed browser to detect malicious web content"),
            ("Queue Depth", "Number of pending analyses — if consistently full, DDI capacity may be insufficient"),
        ],
        "questions": [
            ("What does a consistently full submission queue indicate?", "DDI's Virtual Analyzer capacity is insufficient for the volume of suspicious files — may need hardware upgrade or tuning of submission policy"),
            ("When would you manually submit a file?", "During incident investigation when you have a specific suspicious file from an endpoint or email that you want to analyse"),
            ("What does URL submission detect?", "Drive-by download sites, phishing pages, and malicious redirects by opening URLs in a sandboxed browser"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-5-4": {
        "notes": "Virtual Analyzer produces detailed analysis reports for each submitted sample. The report includes: risk score (0-100, with 100 being most dangerous), threat classification (Trojan, Ransomware, Backdoor, etc.), MITRE ATT&CK techniques observed, detailed behaviour log (every file created, registry key modified, network connection attempted), network IOCs (IPs and domains contacted), and file IOCs (file hashes created).\n\nInterpreting the report: start with the risk score and classification. Then review the network behaviour section — C&C connections are the most critical finding. Review file creation — did it drop additional malware? Check persistence mechanisms — registry run keys, scheduled tasks, services created. The MITRE ATT&CK mapping shows exactly which attack techniques the malware uses, which helps defenders understand the full threat scope. Export the IOCs and share them with your SIEM and TippingPoint for automated blocking.",
        "terms": [
            ("Risk Score", "0-100 rating of sample danger — 70+ typically indicates high-confidence malware"),
            ("IOC", "Indicator of Compromise — file hashes, IPs, domains extracted from analysis for defensive use"),
            ("MITRE ATT&CK Mapping", "Virtual Analyzer maps observed behaviours to ATT&CK techniques for context"),
            ("Persistence Mechanism", "How malware survives reboots — registry keys, scheduled tasks, services"),
            ("C&C Connection", "Network connection to attacker's server — most critical finding in a sandbox report"),
        ],
        "questions": [
            ("What is the most critical finding in a Virtual Analyzer report?", "C&C connections — they reveal the attacker's infrastructure and confirm active compromise"),
            ("What should you do with IOCs from a Virtual Analyzer report?", "Share them with your SIEM for correlation and with TippingPoint/firewall for blocking"),
            ("What does the MITRE ATT&CK mapping in a report show?", "Which specific attack techniques the malware uses, helping defenders understand the threat scope and prioritise response"),
        ],
        "links": [
            ("MITRE ATT&CK Framework", "https://attack.mitre.org/"),
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Threat Encyclopedia", "https://www.trendmicro.com/vinfo/us/threat-encyclopedia/"),
        ]
    },
    "ddi-5-5": {
        "notes": "Virtual Analyzer lab. Complete these tasks.\n\nLab tasks: 1) Go to Virtual Analyzer → Settings — review VM image configuration. 2) Note which OS versions are configured. 3) Check submission policy — verify executable and document file types are enabled. 4) Go to Virtual Analyzer → Submissions — review the queue status. 5) Download the EICAR test file (safe AV test file) from eicar.org. 6) Submit it manually to Virtual Analyzer. 7) Monitor the submission queue and wait for analysis to complete. 8) Review the analysis report — note the risk score and findings. 9) Go to Detection → Detections — find the EICAR-related detection. 10) Click on a detection to view the full details. 11) Practice exporting IOCs from a detection report.",
        "terms": [
            ("EICAR Test File", "Safe standardised test file for verifying AV and security tool detection — not real malware"),
            ("Manual Submission Steps", "Virtual Analyzer → Submit File → Browse → Submit → Monitor queue → View report"),
            ("IOC Export", "Downloading file hashes, IPs, and domains from a report for use in other security tools"),
        ],
        "questions": [
            ("What is the EICAR test file?", "A standardised safe test file that triggers security tools without being real malware — used to verify detection is working"),
            ("Where do you monitor the status of submitted files?", "Virtual Analyzer → Submissions — shows pending, in-progress, and completed analyses"),
        ],
        "links": [
            ("EICAR Test File — Safe Download", "https://www.eicar.org/download-anti-malware-testfile/"),
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-6-1": {
        "notes": "The DDI web console dashboard provides an at-a-glance view of your security posture. Key dashboard widgets: Detections Over Time (trend graph of detections by severity), Top Threats (most frequently detected threat families), Affected Hosts (internal hosts generating the most alerts), C&C Callback Attempts (hosts attempting to communicate with known C&C servers), and Network Traffic (volume on monitoring interfaces).\n\nCustomise the dashboard by adding, removing, and rearranging widgets. Create multiple dashboard views for different audiences — a NOC dashboard showing volume and trends, an executive dashboard showing risk summary, and an analyst dashboard with full technical detail. The C&C Callback Attempts widget is often the highest-priority item — any internal host making C&C connections indicates active compromise and requires immediate investigation. Configure the dashboard refresh interval based on your monitoring needs.",
        "terms": [
            ("Dashboard Widget", "Individual panel on the DDI dashboard showing specific data or metrics"),
            ("Detections Over Time", "Trend graph showing detection volume — useful for spotting attack campaigns"),
            ("Affected Hosts", "Internal hosts with the most detections — prioritise investigation here"),
            ("C&C Callback", "Internal host communicating with a known attacker server — indicates active compromise"),
            ("Dashboard Refresh", "How often the dashboard data updates — configurable based on monitoring needs"),
        ],
        "questions": [
            ("Which dashboard widget should be your highest priority?", "C&C Callback Attempts — any internal host making C&C connections indicates active compromise requiring immediate response"),
            ("What does the Detections Over Time graph help you identify?", "Attack campaigns — a sudden spike in detections often indicates an active attack or new malware spreading"),
            ("Why create multiple dashboard views?", "Different audiences need different information — NOC needs volume/trends, executives need risk summary, analysts need technical detail"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-6-2": {
        "notes": "Threat investigation in DDI starts at the detection list and drills down into full event detail. Detection → Detections shows all events with filters for time range, severity, detection type, and affected hosts. Click any detection to see: the full event details (what was detected, when, which hosts), the network traffic that triggered the detection (source and destination IPs, ports, protocol), the file or URL involved, the Virtual Analyzer report if a sandbox analysis was performed, and the MITRE ATT&CK technique mapping.\n\nHost-centric investigation: click on an affected host IP to see all detections involving that host — this builds a timeline of activity for a potentially compromised system. Detection → Affected Hosts shows hosts ranked by risk score. The investigation workflow: start with high-severity detections, identify affected hosts, build a timeline, extract IOCs, and hand off to incident response with full context. DDI's investigation data should be your starting point for any suspected APT incident.",
        "terms": [
            ("Detection List", "All DDI detections with filtering by time, severity, type, and host"),
            ("Event Drill-Down", "Clicking a detection to view full technical details including traffic and sandbox results"),
            ("Host-Centric View", "Viewing all detections for a specific internal host to build an activity timeline"),
            ("IOC Extraction", "Pulling file hashes, IPs, and domains from detections for incident response use"),
            ("Incident Timeline", "Chronological view of all detections for an affected host — shows attack progression"),
        ],
        "questions": [
            ("What is the first step when investigating a high-severity detection?", "Click on the detection to view full details — understand what was detected, which hosts are involved, and what the Virtual Analyzer found"),
            ("How do you build a timeline for a potentially compromised host?", "Click on the host's IP in DDI to see all detections involving that host in chronological order"),
            ("What should you extract from DDI before handing off to incident response?", "IOCs (file hashes, IPs, domains), affected host list, timeline of events, and Virtual Analyzer reports"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("MITRE ATT&CK Framework", "https://attack.mitre.org/"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-6-3": {
        "notes": "DDI generates scheduled and on-demand reports for tracking security posture over time. Built-in report types: Executive Summary (high-level overview for management), Threat Analysis (detailed technical breakdown of detections), Top Threats (most active threat families), Affected Hosts (hosts with most detections), and Compliance Reports (for regulatory requirements).\n\nScheduled reports: configure DDI to automatically generate and email reports on a daily, weekly, or monthly schedule. Useful for regular management briefings and compliance evidence. On-demand reports: generate for specific time ranges during incident investigations. Custom reports: combine multiple data sources into tailored reports for your organisation's specific needs. Reports can be exported as PDF or CSV. For compliance: schedule monthly executive summaries and quarterly threat analysis reports. Store report PDFs in your document management system as evidence for audits.",
        "terms": [
            ("Executive Summary", "High-level report for management showing overall threat posture without technical detail"),
            ("Threat Analysis Report", "Detailed technical report breaking down detection types, volumes, and affected systems"),
            ("Scheduled Report", "Automatically generated report emailed on a configured schedule"),
            ("On-Demand Report", "Report generated manually for a specific time range — used during investigations"),
            ("Compliance Report", "Report formatted to meet regulatory evidence requirements"),
        ],
        "questions": [
            ("What report type is appropriate for monthly management briefings?", "Executive Summary — high-level overview of threats detected without technical detail"),
            ("When would you generate an on-demand report?", "During incident investigation to document the detection timeline and threat activity for a specific period"),
            ("Why store scheduled reports in a document management system?", "As evidence for compliance audits — regulators may require proof of regular security monitoring"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-6-4": {
        "notes": "Reporting lab. Complete these tasks.\n\nLab tasks: 1) Go to Reports in the DDI web console. 2) Review available built-in report types. 3) Generate an on-demand Executive Summary for the last 7 days. 4) Review the generated report — note what information is included. 5) Generate an on-demand Threat Analysis report for the same period. 6) Compare the two reports — note the difference in detail level. 7) Configure a scheduled weekly Executive Summary to be emailed to an administrator address. 8) Verify the schedule is saved correctly. 9) Go to Detection → Detections — practice filtering by severity, time range, and detection type. 10) Click on a detection and practice the drill-down workflow. 11) Practice identifying an affected host and viewing all its detections.",
        "terms": [
            ("Report Generation", "Reports → Generate Report → Select type → Set time range → Generate"),
            ("Scheduled Report Configuration", "Reports → Scheduled Reports → Add → Configure type, frequency, and recipients"),
            ("Detection Filtering", "Use time range, severity, type, and host filters to narrow the detection list"),
        ],
        "questions": [
            ("What is the difference between Executive Summary and Threat Analysis reports?", "Executive Summary is high-level for management; Threat Analysis is detailed technical data for security teams"),
            ("How do you investigate all detections for a specific internal host?", "Filter the detection list by the host's IP address, or click the host in the Affected Hosts view"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-7-1": {
        "notes": "DDI can forward security events to external syslog servers for centralised log management and SIEM correlation. Configure syslog in Administration → Syslog. Settings: syslog server IP, port (UDP 514 default, TCP 514 for reliable delivery), and format. CEF (Common Event Format) is the recommended format — it's supported natively by Splunk, QRadar, ArcSight, and most other SIEMs.\n\nWhat DDI sends via syslog: detection events (threat name, severity, affected hosts, detection method), Virtual Analyzer results (sandbox risk score and findings), system events (pattern updates, connectivity issues), and audit events (administrative actions). Configure which event types to forward in the syslog settings — typically send all detections and VA results, but be selective about system events to avoid flooding your SIEM. Test with a test event before relying on syslog for production monitoring.",
        "terms": [
            ("Syslog", "Protocol for forwarding DDI events to a central log server; UDP 514 default"),
            ("CEF", "Common Event Format — standardised format supported by most SIEMs"),
            ("Detection Event", "Syslog message for each threat DDI detects — includes threat name, hosts, and severity"),
            ("VA Result", "Syslog message with Virtual Analyzer sandbox findings"),
            ("Syslog Test", "DDI feature to send a test message — verify reception before relying on it"),
        ],
        "questions": [
            ("What syslog format should you use for SIEM integration?", "CEF — Common Event Format, supported natively by Splunk, QRadar, ArcSight, and most SIEMs"),
            ("Why use TCP syslog instead of UDP?", "TCP syslog is reliable — UDP can drop messages under load, causing security events to be lost"),
            ("What DDI event types should be forwarded to SIEM?", "All detection events and Virtual Analyzer results — be selective with system events to avoid noise"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Graylog — Free SIEM/Log Management", "https://graylog.org/products/open-source/"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-7-2": {
        "notes": "Splunk and QRadar are the most common SIEM platforms in enterprise environments. For Splunk: install the Trend Micro Deep Discovery add-on from Splunkbase. Configure DDI syslog to point to your Splunk indexer or heavy forwarder. The add-on provides pre-built field extractions, dashboards, and correlation searches for DDI data. Key Splunk searches: `sourcetype=trend_ddi severity=high` for high-severity detections, and `sourcetype=trend_ddi detection_type=*c2*` for C&C callbacks.\n\nFor QRadar: DDI has a pre-built DSM (Device Support Module). Add DDI as a log source in QRadar pointing to your syslog output. QRadar automatically parses and maps DDI events to its taxonomy. The real power comes from cross-source correlation: correlate DDI C&C callback detections with firewall allow logs (did the firewall actually allow the connection?) and endpoint alerts (is the affected host showing other signs of compromise?). This multi-source correlation is what distinguishes a SIEM from simple log collection.",
        "terms": [
            ("Splunk Add-on", "Trend Micro DDI app from Splunkbase providing field extractions and dashboards"),
            ("QRadar DSM", "Device Support Module — pre-built parser for DDI logs in QRadar"),
            ("Cross-Source Correlation", "Combining DDI events with firewall, endpoint, and other logs for full incident context"),
            ("Splunkbase", "Splunk's app marketplace — search 'Deep Discovery' for the official add-on"),
            ("Log Source", "QRadar term for a device sending logs — add DDI as a log source in QRadar"),
        ],
        "questions": [
            ("What Splunk component is needed for DDI integration?", "The Trend Micro Deep Discovery add-on from Splunkbase"),
            ("What is cross-source correlation?", "Combining DDI detections with data from other sources (firewall, endpoint, DNS) to build a complete picture of an incident"),
            ("Why is a SIEM more powerful than DDI alone for investigation?", "A SIEM correlates DDI events with all other security data — you can see if the firewall allowed a C&C connection that DDI detected"),
        ],
        "links": [
            ("Splunkbase — Search Deep Discovery", "https://splunkbase.splunk.com/"),
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-7-3": {
        "notes": "SNMP allows your network management system (NMS) to monitor DDI appliance health — CPU, memory, disk usage, and interface status. Always use SNMPv3 for authentication and encryption. Configure SNMP in Administration → SNMP.\n\nSNMP traps are the most useful SNMP feature for DDI monitoring: configure traps for high-CPU events (DDI overwhelmed), disk full warnings (log storage full — old logs being overwritten), pattern update failures (threat detection becoming outdated), and connectivity failures (DDI can no longer reach update servers). These operational alerts ensure DDI is functioning correctly — a DDI with full disks or failed pattern updates provides degraded protection. Import DDI's MIB files into your NMS for human-readable metric names. Monitor DDI health alongside your other network devices in the same NMS for a unified operational view.",
        "terms": [
            ("SNMPv3", "Secure SNMP with authentication and encryption — always use over v2c"),
            ("SNMP Trap", "Unsolicited alert sent from DDI to NMS when a significant operational event occurs"),
            ("Disk Full Warning", "Critical alert — full disk means old logs are overwritten and pattern updates may fail"),
            ("Pattern Update Failure Trap", "Alert indicating DDI cannot reach update servers — protection becoming outdated"),
            ("MIB File", "Management Information Base — defines DDI's SNMP metrics for import into your NMS"),
        ],
        "questions": [
            ("Why is the disk full SNMP trap critical?", "Full disk means old logs are overwritten (losing evidence) and pattern updates may fail (losing protection)"),
            ("What operational traps should you configure for DDI?", "High CPU, disk full warning, pattern update failure, and management network connectivity failure"),
            ("Where do you get DDI's MIB files?", "From Trend Micro support portal — import into your NMS for human-readable metric descriptions"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("PRTG — Free Network Monitor (up to 100 sensors)", "https://www.paessler.com/prtg"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-7-4": {
        "notes": "SIEM integration lab.\n\nLab tasks: 1) Go to Administration → Syslog in DDI. 2) Add a syslog destination — your lab syslog server, port 514, CEF format. 3) Enable Detection Events and Virtual Analyzer Results for forwarding. 4) Click Send Test Message and verify receipt on your syslog server. 5) Configure SNMPv3: Administration → SNMP → add v3 user with SHA/AES. 6) Add your NMS as an SNMP trap destination. 7) Verify SNMP polling returns DDI CPU and memory OIDs. 8) If Splunk available: install Deep Discovery add-on from Splunkbase. 9) Configure Splunk to receive syslog from DDI. 10) Trigger a test detection (browse to a test threat URL if available) and verify it appears in Splunk. 11) Build a simple Splunk search showing detections by severity for the last 24 hours.",
        "terms": [
            ("CEF Test Message", "Verify format and connectivity before relying on it for production monitoring"),
            ("Splunk Search Example", "index=main sourcetype=trend_ddi | stats count by severity"),
            ("SNMP Verification", "snmpwalk -v3 <ddi-ip> to verify OIDs return values"),
        ],
        "questions": [
            ("After configuring syslog, what must you verify?", "Send a test message and confirm it arrives correctly formatted in your syslog server/SIEM"),
            ("What Splunk search shows DDI detections by severity?", "index=main sourcetype=trend_ddi | stats count by severity"),
        ],
        "links": [
            ("Splunkbase — Search Deep Discovery", "https://splunkbase.splunk.com/"),
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Graylog — Free SIEM/Log Management", "https://graylog.org/products/open-source/"),
        ]
    },
    "ddi-8-1": {
        "notes": "High Availability for DDI ensures continuous monitoring even during device failure. Unlike TippingPoint (which is inline), DDI is out-of-band — if DDI fails, production traffic continues unaffected but you lose visibility. HA for DDI is about maintaining monitoring continuity, not preventing network outages.\n\nDDI HA options: Active/Passive clustering where two DDI appliances share a virtual IP, with the passive taking over if the active fails. Both appliances receive the same traffic (both connected to the same SPAN/TAP) — only one analyses at a time. Configuration is synchronised between members. Alternatively, some organisations deploy multiple DDI appliances monitoring different segments independently — not HA in the traditional sense, but provides redundancy through coverage overlap. For maximum resilience, combine HA clustering with TAP-based traffic feeds (TAPs are more reliable than SPAN for consistent traffic delivery to both HA members).",
        "terms": [
            ("Active/Passive HA", "Two DDI appliances sharing a virtual IP — passive takes over if active fails"),
            ("Virtual IP", "Shared IP address used by the active DDI member — clients always connect to this IP"),
            ("Configuration Sync", "HA members automatically synchronise configuration changes"),
            ("Monitoring Continuity", "DDI HA goal — maintain threat visibility even during device failure"),
            ("TAP for HA", "TAPs provide more reliable traffic feed to both HA members than SPAN ports"),
        ],
        "questions": [
            ("What is the impact if DDI fails without HA?", "Production traffic continues unaffected but you lose threat visibility — attacks may go undetected during the outage"),
            ("How does Active/Passive HA work for DDI?", "Both appliances connect to the same traffic feed; only the active analyses traffic. If it fails, the passive takes over and begins analysing"),
            ("Why use TAPs instead of SPAN for HA deployments?", "TAPs reliably deliver traffic copies to both HA members simultaneously; SPAN may inconsistently deliver to multiple destinations"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Network TAP vs SPAN Explained", "https://www.garlandtechnology.com/tap-vs-span"),
        ]
    },
    "ddi-8-2": {
        "notes": "Configuring DDI HA requires two identical appliances running the same firmware version. Setup process: 1) Configure both appliances with management IPs on the same subnet. 2) In the primary appliance web console, go to Administration → High Availability. 3) Enable HA and configure the virtual IP (the shared management IP that clients will use). 4) Set this appliance as Primary. 5) On the secondary appliance, enable HA and point it to the primary. 6) The appliances pair and synchronise configuration automatically.\n\nAfter pairing, all management access should use the virtual IP — not the individual appliance IPs. Configuration changes made through the virtual IP are automatically synchronised to both members. The HA status page shows current Active/Passive state, last synchronisation time, and health of both members. Both appliances must be connected to the same traffic feeds — verify both monitoring interfaces show traffic after HA is configured.",
        "terms": [
            ("Virtual IP (VIP)", "Shared management IP address — always use this for DDI management, not individual IPs"),
            ("HA Pairing", "Process of connecting two DDI appliances into an HA cluster"),
            ("Configuration Synchronisation", "Changes made on active are automatically pushed to passive member"),
            ("HA Status Page", "Administration → High Availability — shows member roles, sync status, and health"),
            ("Same Firmware Requirement", "Both HA members must run identical firmware — verify before pairing"),
        ],
        "questions": [
            ("Why should you always use the virtual IP for DDI management?", "Individual appliance IPs change role after failover — the VIP always points to the active member regardless of which physical appliance is active"),
            ("What happens to configuration changes after HA is set up?", "Changes are automatically synchronised from the active to the passive member"),
            ("What must you verify after HA pairing?", "Both appliances show traffic on monitoring interfaces and HA status shows Active/Passive with successful synchronisation"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-8-3": {
        "notes": "Testing DDI HA failover before relying on it is essential. Testing procedure: 1) Verify HA status shows Active/Passive with green health indicators. 2) Note the current Active member's physical management IP. 3) Generate continuous test traffic and verify detections are appearing. 4) Simulate failure: power off or disconnect the active appliance. 5) Observe: the passive should become active within 30-60 seconds. 6) Verify the virtual IP is now responding and detections continue appearing. 7) Restore the failed appliance. 8) Verify it comes up as Passive and synchronises. 9) Document the failover time (your RTO).\n\nCommon HA issues: split-brain (both members think they're active) — caused by HA link failure; requires careful physical redundancy for the HA communication link. Sync failures — usually caused by firmware version mismatch or network connectivity issues between members. After any firmware upgrade, verify HA sync is working before considering the upgrade complete.",
        "terms": [
            ("Failover Time", "Time for passive to become active after active failure — measure during testing"),
            ("Split-Brain", "Both HA members become active simultaneously — caused by HA link failure"),
            ("HA Link", "Network connection between HA members for health monitoring and synchronisation"),
            ("RTO", "Recovery Time Objective — maximum acceptable failover time; measure during testing"),
            ("Post-Upgrade HA Verification", "After firmware upgrades, always verify HA sync is working before declaring success"),
        ],
        "questions": [
            ("What is split-brain in an HA context?", "Both members think they are active simultaneously — usually caused by failure of the HA communication link"),
            ("How do you prevent split-brain?", "Use redundant HA links — if one link fails, the other maintains HA communication"),
            ("What should you verify after restoring a failed HA member?", "That it comes up as Passive (not Active), successfully synchronises configuration from the Active, and monitoring interfaces show traffic"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-8-4": {
        "notes": "HA configuration lab.\n\nLab tasks: 1) Go to Administration → High Availability — review current HA status. 2) If HA is configured: note which member is Active and which is Passive. 3) Note the virtual IP address. 4) Check that both members show healthy status. 5) Review the last synchronisation time. 6) Simulate a failover: shut down the active member (or use the failover button if available). 7) Measure the time until the passive becomes active. 8) Verify detections continue appearing during and after failover. 9) Restore the original active — verify it comes up as Passive. 10) Record failover time as your measured RTO. 11) If HA is not configured: document the steps you would follow based on this module to set it up.",
        "terms": [
            ("Failover Button", "Some DDI versions support manual failover trigger from web console — check your version"),
            ("Failover Measurement", "Use a stopwatch — time from active going down to detections resuming on passive"),
            ("RTO Documentation", "Record measured RTO in your runbook — update after each test"),
        ],
        "questions": [
            ("What does a successful HA failover test verify?", "That the passive can take over, the virtual IP remains accessible, and detections continue without manual intervention"),
            ("How frequently should HA failover be tested?", "At least annually and after any firmware upgrade or significant configuration change"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-9-1": {
        "notes": "DDI generates several types of logs accessible from the web console. Detection logs: every threat detection with full details — available in Detection → Detections. System logs: operational events including pattern updates, connectivity changes, and service restarts — Administration → System Log. Audit logs: all administrative actions with user and timestamp — Administration → Audit Log. Virtual Analyzer logs: sandbox analysis results — Virtual Analyzer → Analysis Results.\n\nLog retention: DDI stores logs locally on its hard drive. Retention period depends on detection volume and disk size — configure log cleanup settings to prevent disk full conditions. Always export logs to an external syslog server or SIEM for long-term retention. Compliance requirements (PCI DSS, HIPAA, SOX) often mandate 1-3 years of log retention — local DDI storage alone is insufficient. The system log is your first place to look when DDI is behaving unexpectedly — it shows connectivity failures, service restarts, and pattern update errors.",
        "terms": [
            ("Detection Log", "Record of every threat DDI detects — full event detail with host, threat, and context"),
            ("System Log", "Operational events — pattern updates, connectivity, service health"),
            ("Audit Log", "Administrative actions log — who did what and when in the DDI web console"),
            ("Log Retention", "How long logs are kept — local retention is limited; use SIEM for long-term storage"),
            ("Log Cleanup", "Automatic removal of old logs to prevent disk full conditions"),
        ],
        "questions": [
            ("Where do you look first when DDI is behaving unexpectedly?", "Administration → System Log — shows connectivity failures, service restarts, and pattern update errors"),
            ("Why is local log storage insufficient for compliance?", "DDI's disk fills up and old logs are overwritten — compliance requirements for 1-3 year retention require external SIEM storage"),
            ("What is in the Audit Log?", "All administrative actions in the DDI web console — who logged in, what settings were changed, when"),
        ],
        "links": [
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-9-2": {
        "notes": "Common DDI issues and solutions. Issue 1: No detections appearing. Check: is the SPAN port configured correctly? (verify traffic is reaching the monitoring interface — check interface traffic counters). Are detection policies enabled? Is the pattern current? Issue 2: Pattern update failing. Check: can DDI reach update servers? (test connectivity from web console). Is proxy configured correctly? Is the licence valid?\n\nIssue 3: Virtual Analyzer not analysing files. Check: is Virtual Analyzer enabled? Are VM images properly configured? Is disk space available? Issue 4: High disk usage. Check: log cleanup settings — reduce retention period or increase SIEM forwarding. Issue 5: DDI web console unreachable. Check: is the management interface up? (check from console). Has the management IP changed? Is the web service running? (SSH in and check service status). Issue 6: False positives flooding detection list. Check: review exception list and add specific exceptions for known-good sources. Adjust detection sensitivity if needed.",
        "terms": [
            ("Interface Traffic Counter", "Verify SPAN is working by checking monitoring interface receives non-zero traffic"),
            ("Connectivity Test", "Built-in DDI tool to test management network and update server reachability"),
            ("Licence Check", "Administration → Licence — verify DDI and component licences are valid"),
            ("Web Service Restart", "SSH to DDI and restart web management service if console is unreachable"),
            ("Sensitivity Adjustment", "Reduce detection sensitivity to decrease false positive volume"),
        ],
        "questions": [
            ("DDI shows no detections despite traffic flowing through the network. What do you check first?", "Verify the monitoring interface is receiving traffic — check interface traffic counters in the web console"),
            ("Pattern updates are failing. What are the three things to check?", "Proxy configuration, DNS resolution of update servers, and licence validity"),
            ("The DDI web console is unreachable. What is your first step?", "Connect via console port or SSH — check if the management interface is up and the web service is running"),
        ],
        "links": [
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/"),
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
        ]
    },
    "ddi-9-3": {
        "notes": "DDI provides several built-in diagnostic tools accessible from the web console and CLI. Web console diagnostics: Administration → Diagnostics. Tools include ping (test management connectivity), traceroute (trace path to update servers), DNS lookup (test name resolution), and port connectivity test (verify specific ports are reachable). Pattern update test (verify update server connectivity). These cover most common connectivity issues.\n\nCLI diagnostics: SSH to the management IP and log in. The DDI CLI is Linux-based. Key commands: `ifconfig` or `ip addr` to check interface status, `ping` for connectivity, `netstat -an` to check listening services, `df -h` for disk space, `top` for CPU and memory. Support bundle: when Trend Micro support needs diagnostic data, generate a support bundle from Administration → Diagnostics → Support Bundle. This creates a compressed file containing logs, configuration, and system information. Download and upload to the Trend Micro support portal.",
        "terms": [
            ("Diagnostics Page", "Administration → Diagnostics — built-in web console tools for connectivity testing"),
            ("Support Bundle", "Compressed diagnostic package for Trend Micro support — generated from web console"),
            ("df -h", "Linux command showing disk space usage — check for full disks"),
            ("netstat -an", "Shows listening services and active connections on DDI"),
            ("ifconfig/ip addr", "Shows network interface status and IP addresses on DDI"),
        ],
        "questions": [
            ("Where are the built-in diagnostic tools in DDI?", "Administration → Diagnostics — includes ping, traceroute, DNS lookup, and connectivity tests"),
            ("When do you generate a support bundle?", "When Trend Micro support requests diagnostic data to investigate a complex issue"),
            ("What Linux command shows disk space on DDI?", "df -h — shows all filesystems and their usage percentage"),
        ],
        "links": [
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/"),
        ]
    },
    "ddi-9-4": {
        "notes": "Troubleshooting lab. Work through this simulated troubleshooting scenario.\n\nLab tasks: 1) Go to Administration → System Log — review entries from the last 24 hours. 2) Identify any errors or warnings. 3) Go to Administration → Diagnostics — run a ping to 8.8.8.8 and note the result. 4) Run a DNS lookup for update.activeupdate.trendmicro.com — verify it resolves. 5) Run the pattern update connectivity test. 6) Go to Administration → Pattern Update — check current pattern version and last update time. 7) Trigger a manual pattern update and observe the process. 8) Go to Virtual Analyzer → Settings — verify VM images are configured. 9) Check disk space from Diagnostics or SSH (df -h). 10) Generate a support bundle: Administration → Diagnostics → Support Bundle → Generate. 11) Download the bundle and note its contents (do not upload to Trend Micro without a support case).",
        "terms": [
            ("System Log Review", "First step in any DDI troubleshooting — look for errors and warnings"),
            ("Pattern Update Connectivity", "Test at Administration → Diagnostics → Pattern Update Test"),
            ("Manual Pattern Update", "Administration → Pattern Update → Update Now"),
        ],
        "questions": [
            ("What is the first action in any DDI troubleshooting workflow?", "Check Administration → System Log for errors and warnings that reveal what went wrong"),
            ("How do you verify DDI can reach Trend Micro update servers?", "Administration → Diagnostics → run the pattern update connectivity test"),
        ],
        "links": [
            ("Trend Micro Support Portal", "https://success.trendmicro.com/"),
            ("Trend Micro Deep Discovery Documentation", "https://docs.trendmicro.com/en-us/enterprise/deep-discovery-inspector.aspx"),
            ("Trend Micro Knowledge Base", "https://success.trendmicro.com/"),
        ]
    },
}
