LESSON_CONTENT = {'1-1': {'links': [('Professor Messer — Network+ Course (Free)',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                   ('Cloudflare — OSI Model Explained',
                    'https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/'),
                   ('TryHackMe — Free Networking Rooms',
                    'https://tryhackme.com/hacktivities?tab=practice')],
         'notes': 'The OSI (Open Systems Interconnection) model is a 7-layer framework that '
                  'describes how data travels from one device to another across a network. Each '
                  'layer has a specific job and communicates with the layers above and below it. '
                  'From top to bottom: Application (layer 7) is where user-facing software lives; '
                  'Presentation (6) handles data formatting and encryption; Session (5) manages '
                  'connections; Transport (4) handles reliable delivery with TCP/UDP; Network (3) '
                  'handles IP addressing and routing; Data Link (2) handles MAC addresses and '
                  'switches; Physical (1) is the actual cables and signals.\n'
                  '\n'
                  'The OSI model is critical for the Network+ exam and for troubleshooting. When '
                  'something goes wrong, you work from layer 1 upward — is the cable plugged in? '
                  'Is the IP address correct? Is the application configured properly? Every '
                  'networking concept maps to a specific OSI layer.',
         'questions': [('At which OSI layer do routers operate?',
                        'Layer 3 — Network layer (routers forward packets based on IP addresses)'),
                       ('At which OSI layer do switches operate?',
                        'Layer 2 — Data Link layer (switches forward frames based on MAC '
                        'addresses)'),
                       ('Which layer is responsible for encryption and data formatting?',
                        'Layer 6 — Presentation layer')],
         'diagram': '<svg viewBox="0 0 500 380" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:500px;display:block;margin:0 auto;"><defs><style>.ll{font-family:JetBrains Mono,monospace;font-size:11px;fill:#0a0f1e;font-weight:700;}.ln{font-family:JetBrains Mono,monospace;font-size:18px;fill:#0a0f1e;font-weight:900;}.lp{font-family:Arial,sans-serif;font-size:10px;fill:#0a0f1e;opacity:0.85;}.tt{font-family:JetBrains Mono,monospace;font-size:13px;fill:#00d4ff;letter-spacing:2px;}</style></defs><text x="250" y="22" text-anchor="middle" class="tt">OSI MODEL - 7 LAYERS</text><rect x="60" y="35" width="380" height="44" rx="4" fill="#00c853"/><text x="85" y="63" class="ln">7</text><text x="115" y="58" class="ll">APPLICATION</text><text x="115" y="72" class="lp">HTTP - HTTPS - FTP - DNS - SMTP - SSH</text><rect x="60" y="83" width="380" height="44" rx="4" fill="#34d399"/><text x="85" y="111" class="ln">6</text><text x="115" y="106" class="ll">PRESENTATION</text><text x="115" y="120" class="lp">SSL/TLS - Encryption - Data Formatting - Compression</text><rect x="60" y="131" width="380" height="44" rx="4" fill="#6ee7b7"/><text x="85" y="159" class="ln">5</text><text x="115" y="154" class="ll">SESSION</text><text x="115" y="168" class="lp">NetBIOS - RPC - Session Establishment and Teardown</text><rect x="60" y="179" width="380" height="44" rx="4" fill="#00b4d8"/><text x="85" y="207" class="ln">4</text><text x="115" y="202" class="ll">TRANSPORT</text><text x="115" y="216" class="lp">TCP - UDP - Ports - Segmentation - Flow Control</text><rect x="60" y="227" width="380" height="44" rx="4" fill="#0096c7"/><text x="85" y="255" class="ln">3</text><text x="115" y="250" class="ll">NETWORK</text><text x="115" y="264" class="lp">IP - ICMP - Routers - Routing - Logical Addressing</text><rect x="60" y="275" width="380" height="44" rx="4" fill="#f59e0b"/><text x="85" y="303" class="ln">2</text><text x="115" y="298" class="ll">DATA LINK</text><text x="115" y="312" class="lp">MAC - Ethernet - Switches - Frames - ARP</text><rect x="60" y="323" width="380" height="44" rx="4" fill="#ef4444"/><text x="85" y="351" class="ln">1</text><text x="115" y="346" class="ll">PHYSICAL</text><text x="115" y="360" class="lp">Cables - Hubs - NIC - Signals - Bits - Fiber - Wi-Fi</text></svg>',
         'terms': [('OSI Model',
                    'A 7-layer conceptual framework describing how network communication works'),
                   ('Layer 1 — Physical', 'Cables, signals, network interface cards, hubs'),
                   ('Layer 2 — Data Link', 'MAC addresses, switches, frames, error detection'),
                   ('Layer 3 — Network', 'IP addresses, routers, packets, routing'),
                   ('Layer 4 — Transport', 'TCP/UDP, ports, segmentation, reliable delivery'),
                   ('Layer 7 — Application', 'HTTP, FTP, DNS, SMTP — user-facing protocols')]},
 '1-2': {'links': [('Professor Messer — Network+ Course (Free)',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                   ('Cloudflare Learning Center', 'https://www.cloudflare.com/learning/'),
                   ('CompTIA Network+ Exam Objectives',
                    'https://www.comptia.org/training/resources/exam-objectives')],
         'notes': 'While the OSI model has 7 layers, the TCP/IP model is the practical framework '
                  'that the internet actually uses, with 4 layers. The Application layer maps to '
                  'OSI layers 5-7 and handles protocols like HTTP, DNS, and SMTP. The Transport '
                  'layer (same as OSI layer 4) handles TCP and UDP. The Internet layer maps to OSI '
                  'layer 3 and handles IP addressing. The Network Access layer maps to OSI layers '
                  '1-2 and handles physical transmission.\n'
                  '\n'
                  "The TCP/IP model is what you'll use day-to-day in real networking. The OSI "
                  'model is more of a teaching tool and troubleshooting reference. The Network+ '
                  'exam tests both — you need to know which OSI layers map to which TCP/IP layers '
                  'and what protocols live at each layer of both models.',
         'questions': [('How many layers does the TCP/IP model have?',
                        '4 layers: Application, Transport, Internet, Network Access'),
                       ('Which TCP/IP layer corresponds to OSI layers 5, 6, and 7?',
                        'The Application layer'),
                       ('What is the main difference between OSI and TCP/IP models?',
                        'OSI has 7 layers and is a conceptual reference model; TCP/IP has 4 layers '
                        'and is the practical model the internet uses')],
                  'diagram': '<svg width="100%" viewBox="0 0 680 420" xmlns="http://www.w3.org/2000/svg"><defs><style>.th{font-family:Arial,sans-serif;font-size:13px;font-weight:700;}.ts{font-family:Arial,sans-serif;font-size:11px;}.tt{font-family:JetBrains Mono,monospace;font-size:12px;fill:#00d4ff;letter-spacing:2px;}</style></defs><text class="tt" x="340" y="22" text-anchor="middle">TCP/IP MODEL vs OSI MODEL</text><text class="th" x="175" y="44" text-anchor="middle" fill="#e2e8f0">TCP/IP</text><text class="th" x="505" y="44" text-anchor="middle" fill="#e2e8f0">OSI</text><rect x="50" y="55" width="250" height="115" rx="8" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="175" y="105" text-anchor="middle" fill="#ffffff">Application</text><text class="ts" x="175" y="125" text-anchor="middle" fill="#e2e8f0">HTTP - DNS - FTP - SMTP - SSH</text><rect x="50" y="178" width="250" height="56" rx="8" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="th" x="175" y="200" text-anchor="middle" fill="#ffffff">Transport</text><text class="ts" x="175" y="218" text-anchor="middle" fill="#e2e8f0">TCP - UDP - Ports</text><rect x="50" y="242" width="250" height="56" rx="8" fill="#ba7517" stroke="#fac775" stroke-width="1"/><text class="th" x="175" y="264" text-anchor="middle" fill="#ffffff">Internet</text><text class="ts" x="175" y="282" text-anchor="middle" fill="#e2e8f0">IP - ICMP - Routing</text><rect x="50" y="306" width="250" height="56" rx="8" fill="#993c1d" stroke="#f0997b" stroke-width="1"/><text class="th" x="175" y="328" text-anchor="middle" fill="#ffffff">Network Access</text><text class="ts" x="175" y="346" text-anchor="middle" fill="#e2e8f0">Ethernet - MAC - Physical</text><rect x="380" y="55" width="250" height="38" rx="6" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="505" y="74" text-anchor="middle" fill="#ffffff">7 - Application</text><rect x="380" y="97" width="250" height="38" rx="6" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="505" y="116" text-anchor="middle" fill="#ffffff">6 - Presentation</text><rect x="380" y="139" width="250" height="38" rx="6" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="505" y="158" text-anchor="middle" fill="#ffffff">5 - Session</text><rect x="380" y="178" width="250" height="56" rx="6" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="th" x="505" y="206" text-anchor="middle" fill="#ffffff">4 - Transport</text><rect x="380" y="242" width="250" height="56" rx="6" fill="#ba7517" stroke="#fac775" stroke-width="1"/><text class="th" x="505" y="270" text-anchor="middle" fill="#ffffff">3 - Network</text><rect x="380" y="306" width="250" height="28" rx="6" fill="#993c1d" stroke="#f0997b" stroke-width="1"/><text class="th" x="505" y="320" text-anchor="middle" fill="#ffffff">2 - Data Link</text><rect x="380" y="338" width="250" height="24" rx="6" fill="#993c1d" stroke="#f0997b" stroke-width="1"/><text class="th" x="505" y="350" text-anchor="middle" fill="#ffffff">1 - Physical</text><line x1="300" y1="112" x2="378" y2="74" stroke="#64748b" stroke-width="0.5" stroke-dasharray="4 3"/><line x1="300" y1="112" x2="378" y2="116" stroke="#64748b" stroke-width="0.5" stroke-dasharray="4 3"/><line x1="300" y1="112" x2="378" y2="158" stroke="#64748b" stroke-width="0.5" stroke-dasharray="4 3"/><line x1="300" y1="206" x2="378" y2="206" stroke="#64748b" stroke-width="0.5" stroke-dasharray="4 3"/><line x1="300" y1="270" x2="378" y2="270" stroke="#64748b" stroke-width="0.5" stroke-dasharray="4 3"/><line x1="300" y1="334" x2="378" y2="320" stroke="#64748b" stroke-width="0.5" stroke-dasharray="4 3"/><line x1="300" y1="334" x2="378" y2="350" stroke="#64748b" stroke-width="0.5" stroke-dasharray="4 3"/><text class="ts" x="340" y="395" text-anchor="middle" fill="#64748b">Matching colors show which layers correspond</text></svg>',
         'terms': [('Star Topology',
                    'All devices connect to a central switch; most common modern topology'),
                   ('Bus Topology',
                    'All devices share a single cable backbone; a break affects the whole network'),
                   ('Ring Topology',
                    'Devices connected in a circle; data travels in one direction'),
                   ('Mesh Topology', 'Every device connects to every other; maximum redundancy'),
                   ('Topology',
                    'The arrangement or layout of devices and connections in a network')]},
 '1-4': {'diagram': '<svg width="100%" viewBox="0 0 680 420" xmlns="http://www.w3.org/2000/svg"><defs><style>.th{font-family:Arial,sans-serif;font-size:12px;font-weight:700;}.ts{font-family:Arial,sans-serif;font-size:10px;}.tt{font-family:JetBrains Mono,monospace;font-size:11px;fill:#00d4ff;letter-spacing:2px;}</style></defs><text class="tt" x="340" y="20" text-anchor="middle">NETWORK TOPOLOGIES</text><text class="th" x="115" y="42" text-anchor="middle" fill="#e2e8f0">Bus</text><line x1="40" y1="75" x2="190" y2="75" stroke="#185fa5" stroke-width="3"/><circle cx="65" cy="75" r="10" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><circle cx="100" cy="75" r="10" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><circle cx="135" cy="75" r="10" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><circle cx="170" cy="75" r="10" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="ts" x="115" y="100" text-anchor="middle" fill="#64748b">Single shared cable</text><text class="ts" x="115" y="112" text-anchor="middle" fill="#ef4444">Single point of failure</text><text class="th" x="340" y="42" text-anchor="middle" fill="#e2e8f0">Star</text><circle cx="340" cy="75" r="14" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="ts" x="340" y="79" text-anchor="middle" fill="#ffffff">SW</text><circle cx="295" cy="52" r="9" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><circle cx="385" cy="52" r="9" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><circle cx="295" cy="98" r="9" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><circle cx="385" cy="98" r="9" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><circle cx="265" cy="75" r="9" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><circle cx="415" cy="75" r="9" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><line x1="326" y1="65" x2="304" y2="57" stroke="#94a3b8" stroke-width="1"/><line x1="354" y1="65" x2="376" y2="57" stroke="#94a3b8" stroke-width="1"/><line x1="326" y1="85" x2="304" y2="93" stroke="#94a3b8" stroke-width="1"/><line x1="354" y1="85" x2="376" y2="93" stroke="#94a3b8" stroke-width="1"/><line x1="326" y1="75" x2="274" y2="75" stroke="#94a3b8" stroke-width="1"/><line x1="354" y1="75" x2="406" y2="75" stroke="#94a3b8" stroke-width="1"/><text class="ts" x="340" y="120" text-anchor="middle" fill="#00c853">Most common today</text><text class="ts" x="340" y="132" text-anchor="middle" fill="#ef4444">Switch = single point</text><text class="th" x="565" y="42" text-anchor="middle" fill="#e2e8f0">Ring</text><circle cx="565" cy="75" r="35" fill="none" stroke="#ba7517" stroke-width="2" stroke-dasharray="3 2"/><circle cx="565" cy="40" r="9" fill="#ba7517" stroke="#fac775" stroke-width="1"/><circle cx="600" cy="75" r="9" fill="#ba7517" stroke="#fac775" stroke-width="1"/><circle cx="565" cy="110" r="9" fill="#ba7517" stroke="#fac775" stroke-width="1"/><circle cx="530" cy="75" r="9" fill="#ba7517" stroke="#fac775" stroke-width="1"/><text class="ts" x="565" y="132" text-anchor="middle" fill="#64748b">Token passing</text><text class="ts" x="565" y="144" text-anchor="middle" fill="#ef4444">One break = failure</text><line x1="40" y1="155" x2="640" y2="155" stroke="#1e293b" stroke-width="0.5"/><line x1="230" y1="30" x2="230" y2="150" stroke="#1e293b" stroke-width="0.5"/><line x1="455" y1="30" x2="455" y2="150" stroke="#1e293b" stroke-width="0.5"/><text class="th" x="115" y="178" text-anchor="middle" fill="#e2e8f0">Partial mesh</text><circle cx="80" cy="230" r="9" fill="#993c1d" stroke="#f0997b" stroke-width="1"/><circle cx="150" cy="210" r="9" fill="#993c1d" stroke="#f0997b" stroke-width="1"/><circle cx="150" cy="255" r="9" fill="#993c1d" stroke="#f0997b" stroke-width="1"/><circle cx="80" cy="275" r="9" fill="#993c1d" stroke="#f0997b" stroke-width="1"/><line x1="89" y1="230" x2="141" y2="215" stroke="#f0997b" stroke-width="1"/><line x1="89" y1="232" x2="141" y2="250" stroke="#f0997b" stroke-width="1"/><line x1="89" y1="275" x2="141" y2="260" stroke="#f0997b" stroke-width="1"/><line x1="150" y1="219" x2="150" y2="246" stroke="#f0997b" stroke-width="1"/><text class="ts" x="115" y="305" text-anchor="middle" fill="#64748b">Some redundant paths</text><text class="ts" x="115" y="317" text-anchor="middle" fill="#00c853">WAN / internet core</text><text class="th" x="340" y="178" text-anchor="middle" fill="#e2e8f0">Full mesh</text><circle cx="340" cy="210" r="9" fill="#534ab7" stroke="#7f77dd" stroke-width="1"/><circle cx="375" cy="235" r="9" fill="#534ab7" stroke="#7f77dd" stroke-width="1"/><circle cx="360" cy="268" r="9" fill="#534ab7" stroke="#7f77dd" stroke-width="1"/><circle cx="320" cy="268" r="9" fill="#534ab7" stroke="#7f77dd" stroke-width="1"/><circle cx="305" cy="235" r="9" fill="#534ab7" stroke="#7f77dd" stroke-width="1"/><line x1="349" y1="210" x2="366" y2="226" stroke="#7f77dd" stroke-width="1"/><line x1="348" y1="214" x2="357" y2="259" stroke="#7f77dd" stroke-width="1"/><line x1="344" y1="219" x2="326" y2="259" stroke="#7f77dd" stroke-width="1"/><line x1="331" y1="213" x2="314" y2="227" stroke="#7f77dd" stroke-width="1"/><line x1="375" y1="244" x2="367" y2="259" stroke="#7f77dd" stroke-width="1"/><line x1="371" y1="243" x2="328" y2="260" stroke="#7f77dd" stroke-width="1"/><line x1="366" y1="238" x2="314" y2="238" stroke="#7f77dd" stroke-width="1"/><line x1="351" y1="268" x2="329" y2="268" stroke="#7f77dd" stroke-width="1"/><line x1="311" y1="243" x2="321" y2="260" stroke="#7f77dd" stroke-width="1"/><text class="ts" x="340" y="296" text-anchor="middle" fill="#00c853">Maximum redundancy</text><text class="ts" x="340" y="308" text-anchor="middle" fill="#ef4444">Very expensive</text><text class="th" x="565" y="178" text-anchor="middle" fill="#e2e8f0">Hybrid</text><circle cx="565" cy="222" r="14" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="ts" x="565" y="226" text-anchor="middle" fill="#ffffff">SW</text><circle cx="520" cy="198" r="8" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><circle cx="610" cy="198" r="8" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><circle cx="520" cy="248" r="8" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><circle cx="610" cy="248" r="8" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><line x1="551" y1="212" x2="528" y2="203" stroke="#94a3b8" stroke-width="1"/><line x1="579" y1="212" x2="602" y2="203" stroke="#94a3b8" stroke-width="1"/><line x1="551" y1="232" x2="528" y2="243" stroke="#94a3b8" stroke-width="1"/><line x1="579" y1="232" x2="602" y2="243" stroke="#94a3b8" stroke-width="1"/><line x1="520" y1="206" x2="520" y2="240" stroke="#94a3b8" stroke-width="1"/><line x1="610" y1="206" x2="610" y2="240" stroke="#94a3b8" stroke-width="1"/><text class="ts" x="565" y="276" text-anchor="middle" fill="#00c853">Most enterprise networks</text><text class="ts" x="565" y="288" text-anchor="middle" fill="#64748b">Combines topologies</text><line x1="230" y1="165" x2="230" y2="330" stroke="#1e293b" stroke-width="0.5"/><line x1="455" y1="165" x2="455" y2="330" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="340" y="360" text-anchor="middle" fill="#64748b">Green = advantage  |  Red = disadvantage</text></svg>',
         'links': [('Professor Messer — Network+ Course (Free)',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                   ('Cloudflare Learning Center',
                    'https://www.cloudflare.com/learning/')],
         'notes': 'Network topology refers to the physical or logical arrangement of devices and connections in a network. Understanding topologies helps you design resilient networks and troubleshoot failures.\n\nBus topology uses a single shared cable — all devices tap into the same medium. Simple and cheap but a break anywhere kills the whole network. Largely obsolete.\n\nStar topology connects every device to a central switch. This is the standard for modern LANs — easy to manage, isolates failures to individual links, but the switch itself becomes a single point of failure.\n\nRing topology passes a token around a loop — only the device holding the token can transmit. Deterministic but fragile — one break disrupts the whole ring. Used in legacy Token Ring and SONET/SDH.\n\nMesh topology provides redundant paths between devices. Partial mesh connects only some devices with redundant links — used in WAN and internet core routing. Full mesh connects every device to every other device — maximum redundancy but expensive and complex. Used in critical infrastructure.\n\nHybrid topology combines two or more topologies — for example, a star of stars in a hierarchical enterprise network. Most real networks are hybrids.',
         'questions': [('What is the main advantage of star topology over bus topology?',
                        'Star topology isolates failures — a broken cable only affects one device, not the entire network'),
                       ('Why is full mesh topology rarely used for large networks?',
                        'The number of connections grows exponentially — N devices require N*(N-1)/2 links, making it very expensive'),
                       ('What is the difference between physical and logical topology?',
                        'Physical topology is the actual cable layout; logical topology is how data flows — a hub-based star is physically star but logically bus')],
         'terms': [('Bus topology', 'All devices share a single cable; a break affects the entire network'),
                   ('Star topology', 'All devices connect to a central switch; most common modern LAN design'),
                   ('Ring topology', 'Devices connected in a loop; token passing controls transmission'),
                   ('Mesh topology', 'Redundant paths between devices; partial mesh for WANs, full mesh for critical links'),
                   ('Hybrid topology', 'Combination of two or more topologies; used in most enterprise networks')]},
  '1-5': {'links': [('Professor Messer — Free Practice Exams',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                   ('ExamCompass — Free Network+ Quizzes',
                    'https://www.comptia.org/training/certmaster-practice/network'),
                   ('CompTIA CertMaster Learn (Official)',
                    'https://www.comptia.org/training/certmaster-learn/network')],
         'notes': 'This is a review quiz for Module 1. Test your understanding of network types, '
                  'topologies, and the OSI and TCP/IP models before moving on. These concepts '
                  'underpin everything in the rest of the course — if any answers are unclear, '
                  'review the relevant lesson before continuing.\n'
                  '\n'
                  'Tip for the exam: OSI layer numbers and what operates at each layer is one of '
                  'the most frequently tested topics on Network+. Make sure you can name all 7 '
                  'layers in order and give an example of a protocol or device at each one.',
         'questions': [('Name the 7 OSI layers in order from layer 1 to layer 7.',
                        'Physical, Data Link, Network, Transport, Session, Presentation, '
                        'Application'),
                       ('What type of network covers a single building?',
                        'LAN — Local Area Network'),
                       ('Which topology provides the most redundancy?', 'Mesh topology'),
                       ('At which OSI layer does IP addressing occur?', 'Layer 3 — Network layer'),
                       ('What are the 4 layers of the TCP/IP model?',
                        'Network Access, Internet, Transport, Application')],
         'terms': [('Mnemonic for OSI layers (top to bottom)',
                    'All People Seem To Need Data Processing — Application, Presentation, Session, '
                    'Transport, Network, Data Link, Physical'),
                   ('Mnemonic (bottom to top)', 'Please Do Not Throw Sausage Pizza Away')]},
 '2-1': {'links': [('Professor Messer — Network+ Course (Free)',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                   ('Subnet Calculator', 'https://www.subnet-calculator.com'),
                   ('CIDR.xyz — Visual Subnet Tool', 'https://cidr.xyz')],
         'notes': 'An IPv4 address is a 32-bit number written as four octets in dotted decimal '
                  'notation (e.g. 192.168.1.1). Each octet is 8 bits and can range from 0 to 255. '
                  'IPv4 addresses were originally divided into classes: Class A (1-126 in first '
                  'octet) for large networks with millions of hosts; Class B (128-191) for medium '
                  'networks; Class C (192-223) for small networks up to 254 hosts. Class D '
                  '(224-239) is used for multicast and Class E (240-255) is reserved.\n'
                  '\n'
                  'Classful addressing is largely obsolete — replaced by CIDR — but Network+ still '
                  'tests it. The address 127.x.x.x is always the loopback range (127.0.0.1 = '
                  "localhost). The address 0.0.0.0 means 'this network'. Understanding the "
                  'structure of IP addresses is the foundation for subnetting.',
         'questions': [('What class is the IP address 172.16.5.10?',
                        'Class B (first octet 128-191)'),
                       ('How many bits are in an IPv4 address?', '32 bits'),
                       ('What is the loopback address?', '127.0.0.1'),
                       ('What is the maximum value of any single octet?', '255')],
                  'diagram': '<svg width="100%" viewBox="0 0 680 380" xmlns="http://www.w3.org/2000/svg"><defs><style>.th{font-family:Arial,sans-serif;font-size:13px;font-weight:700;}.ts{font-family:Arial,sans-serif;font-size:11px;}.tm{font-family:JetBrains Mono,monospace;font-size:13px;font-weight:700;}.tt{font-family:JetBrains Mono,monospace;font-size:11px;fill:#00d4ff;letter-spacing:2px;}</style></defs><text class="tt" x="340" y="22" text-anchor="middle">IPv4 ADDRESS STRUCTURE</text><text class="tm" x="340" y="58" text-anchor="middle" fill="#00d4ff">192 . 168 . 1 . 100</text><rect x="60" y="72" width="130" height="44" rx="6" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="th" x="125" y="90" text-anchor="middle" fill="#ffffff">Octet 1</text><text class="tm" x="125" y="108" text-anchor="middle" fill="#e2e8f0">192</text><rect x="205" y="72" width="130" height="44" rx="6" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="th" x="270" y="90" text-anchor="middle" fill="#ffffff">Octet 2</text><text class="tm" x="270" y="108" text-anchor="middle" fill="#e2e8f0">168</text><rect x="350" y="72" width="130" height="44" rx="6" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="th" x="415" y="90" text-anchor="middle" fill="#ffffff">Octet 3</text><text class="tm" x="415" y="108" text-anchor="middle" fill="#e2e8f0">1</text><rect x="495" y="72" width="130" height="44" rx="6" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="th" x="560" y="90" text-anchor="middle" fill="#ffffff">Octet 4</text><text class="tm" x="560" y="108" text-anchor="middle" fill="#e2e8f0">100</text><text class="ts" x="340" y="138" text-anchor="middle" fill="#64748b">In binary (32 bits total):</text><rect x="40" y="148" width="600" height="32" rx="4" fill="#0a0f1e" stroke="#1e293b" stroke-width="1"/><text class="tm" x="340" y="170" text-anchor="middle" fill="#00c853" style="font-size:12px;">11000000 . 10101000 . 00000001 . 01100100</text><text class="ts" x="125" y="198" text-anchor="middle" fill="#64748b">8 bits</text><text class="ts" x="270" y="198" text-anchor="middle" fill="#64748b">8 bits</text><text class="ts" x="415" y="198" text-anchor="middle" fill="#64748b">8 bits</text><text class="ts" x="560" y="198" text-anchor="middle" fill="#64748b">8 bits</text><text class="ts" x="340" y="212" text-anchor="middle" fill="#64748b">= 32 bits total</text><line x1="40" y1="225" x2="640" y2="225" stroke="#1e293b" stroke-width="0.5"/><text class="tt" x="340" y="244" text-anchor="middle">ADDRESS CLASSES</text><rect x="40" y="254" width="115" height="48" rx="6" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="97" y="273" text-anchor="middle" fill="#ffffff">Class A</text><text class="ts" x="97" y="290" text-anchor="middle" fill="#e2e8f0">1.0 to 126.x</text><text class="ts" x="97" y="303" text-anchor="middle" fill="#e2e8f0">16M hosts</text><rect x="165" y="254" width="115" height="48" rx="6" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="th" x="222" y="273" text-anchor="middle" fill="#ffffff">Class B</text><text class="ts" x="222" y="290" text-anchor="middle" fill="#e2e8f0">128.0 to 191.x</text><text class="ts" x="222" y="303" text-anchor="middle" fill="#e2e8f0">65K hosts</text><rect x="290" y="254" width="115" height="48" rx="6" fill="#ba7517" stroke="#fac775" stroke-width="1"/><text class="th" x="347" y="273" text-anchor="middle" fill="#ffffff">Class C</text><text class="ts" x="347" y="290" text-anchor="middle" fill="#e2e8f0">192.0 to 223.x</text><text class="ts" x="347" y="303" text-anchor="middle" fill="#e2e8f0">254 hosts</text><rect x="415" y="254" width="115" height="48" rx="6" fill="#993c1d" stroke="#f0997b" stroke-width="1"/><text class="th" x="472" y="273" text-anchor="middle" fill="#ffffff">Class D</text><text class="ts" x="472" y="290" text-anchor="middle" fill="#e2e8f0">224.0 to 239.x</text><text class="ts" x="472" y="303" text-anchor="middle" fill="#e2e8f0">Multicast</text><rect x="540" y="254" width="100" height="48" rx="6" fill="#475569" stroke="#94a3b8" stroke-width="1"/><text class="th" x="590" y="273" text-anchor="middle" fill="#ffffff">Class E</text><text class="ts" x="590" y="290" text-anchor="middle" fill="#e2e8f0">240.0 to 255.x</text><text class="ts" x="590" y="303" text-anchor="middle" fill="#e2e8f0">Reserved</text><text class="ts" x="340" y="340" text-anchor="middle" fill="#64748b">Each octet ranges from 0 to 255 (2 to the power of 8 = 256 values)</text><text class="ts" x="340" y="356" text-anchor="middle" fill="#64748b">Total IPv4 address space = 2 to the power of 32 = approximately 4.3 billion addresses</text></svg>',
'terms': [('IPv4', '32-bit IP address written as four decimal octets, e.g. 192.168.1.1'),
                   ('Octet', '8-bit section of an IP address; values range from 0-255'),
                   ('Class A', 'First octet 1-126; default mask /8; supports ~16 million hosts'),
                   ('Class B', 'First octet 128-191; default mask /16; supports ~65,000 hosts'),
                   ('Class C', 'First octet 192-223; default mask /24; supports 254 hosts'),
                   ('Loopback', '127.0.0.1 — the address a device uses to refer to itself')]},
 '2-2': {'links': [('Subnet Calculator', 'https://www.subnet-calculator.com'),
                   ('CIDR.xyz — Visual Subnet Tool', 'https://cidr.xyz'),
                   ('Subnetting Practice', 'https://subnettingpractice.com')],
         'notes': 'A subnet mask defines which part of an IP address is the network portion and '
                  'which part identifies the host. Written in dotted decimal (255.255.255.0) or '
                  'CIDR notation (/24), it works by masking the network bits with 1s and host bits '
                  'with 0s. A /24 mask means 24 bits are network, 8 bits are host — giving 256 '
                  'addresses (254 usable, minus network and broadcast addresses).\n'
                  '\n'
                  'CIDR (Classless Inter-Domain Routing) replaced classful addressing and allows '
                  'flexible subnet sizes. A /30 gives 4 addresses (2 usable) — perfect for '
                  'point-to-point links. A /16 gives 65,536 addresses. The formula for usable '
                  'hosts is 2^(host bits) - 2. You must be fast with these calculations for the '
                  'Network+ exam.',
         'questions': [('How many usable hosts does a /24 subnet provide?',
                        '254 (2^8 = 256, minus 2 for network and broadcast)'),
                       ('What is the subnet mask for a /24 in dotted decimal?', '255.255.255.0'),
                       ('How many usable hosts does a /30 subnet provide?', '2 (2^2 = 4, minus 2)'),
                       ('In CIDR notation, what does the number after the slash represent?',
                        'The number of bits used for the network portion')],
         'terms': [('Subnet Mask',
                    '32-bit number that separates network and host portions of an IP address'),
                   ('CIDR Notation',
                    'Slash notation indicating how many bits are the network portion, e.g. /24'),
                   ('Network Address',
                    'First address in a subnet — identifies the network itself, not usable for '
                    'hosts'),
                   ('Broadcast Address',
                    'Last address in a subnet — sent to all hosts, not usable for individual '
                    'hosts'),
                   ('Usable Hosts',
                    'Total addresses minus 2 (network + broadcast) = 2^host bits - 2')]},
 '2-3': {'links': [('Subnetting Practice — Free Drill Tool', 'https://subnettingpractice.com'),
                   ('Subnet Calculator', 'https://www.subnet-calculator.com'),
                   ('CIDR.xyz — Visual Subnet Tool', 'https://cidr.xyz')],
         'notes': 'Subnetting divides a large network into smaller sub-networks. The process: 1) '
                  'Convert the IP and mask to binary. 2) Determine how many subnets or hosts you '
                  'need. 3) Borrow bits from the host portion to create subnets. Each bit borrowed '
                  'doubles the number of subnets but halves the hosts per subnet.\n'
                  '\n'
                  "The quick method: identify the 'interesting octet' (where the subnet mask isn't "
                  '255 or 0). The block size = 256 minus the mask value in that octet. Subnets '
                  'increment by the block size. For example, /26 = 255.255.255.192 — block size is '
                  "256-192=64. Subnets are .0, .64, .128, .192. Practice this daily until it's "
                  'automatic — it comes up on every Network+ exam.',
         'questions': [('What is the block size for a /26 subnet?', '64 (256 - 192 = 64)'),
                       ('For 192.168.1.0/26, what are the four subnet addresses?',
                        '.0, .64, .128, .192'),
                       ('How many hosts can a /26 subnet support?',
                        '62 usable hosts (2^6 = 64, minus 2)'),
                       ('You need 30 hosts per subnet. What prefix length should you use?',
                        '/27 — provides 30 usable hosts (2^5=32, minus 2)')],
                  'diagram': '<svg width="100%" viewBox="0 0 680 440" xmlns="http://www.w3.org/2000/svg"><defs><style>.th{font-family:Arial,sans-serif;font-size:13px;font-weight:700;}.ts{font-family:Arial,sans-serif;font-size:11px;}.tt{font-family:JetBrains Mono,monospace;font-size:12px;fill:#00d4ff;letter-spacing:2px;}</style></defs><text class="tt" x="340" y="22" text-anchor="middle">SUBNETTING 192.168.1.0/24 INTO /26 SUBNETS</text><rect x="190" y="35" width="300" height="50" rx="8" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="th" x="340" y="56" text-anchor="middle" fill="#ffffff">192.168.1.0 /24</text><text class="ts" x="340" y="74" text-anchor="middle" fill="#e2e8f0">256 addresses - 254 usable hosts</text><line x1="260" y1="85" x2="135" y2="135" stroke="#64748b" stroke-width="1"/><line x1="310" y1="85" x2="260" y2="135" stroke="#64748b" stroke-width="1"/><line x1="370" y1="85" x2="420" y2="135" stroke="#64748b" stroke-width="1"/><line x1="420" y1="85" x2="545" y2="135" stroke="#64748b" stroke-width="1"/><rect x="45" y="138" width="145" height="60" rx="8" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="117" y="158" text-anchor="middle" fill="#ffffff">Subnet 1</text><text class="ts" x="117" y="174" text-anchor="middle" fill="#e2e8f0">192.168.1.0/26</text><text class="ts" x="117" y="188" text-anchor="middle" fill="#e2e8f0">.0 to .63</text><rect x="200" y="138" width="145" height="60" rx="8" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="272" y="158" text-anchor="middle" fill="#ffffff">Subnet 2</text><text class="ts" x="272" y="174" text-anchor="middle" fill="#e2e8f0">192.168.1.64/26</text><text class="ts" x="272" y="188" text-anchor="middle" fill="#e2e8f0">.64 to .127</text><rect x="355" y="138" width="155" height="60" rx="8" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="432" y="158" text-anchor="middle" fill="#ffffff">Subnet 3</text><text class="ts" x="432" y="174" text-anchor="middle" fill="#e2e8f0">192.168.1.128/26</text><text class="ts" x="432" y="188" text-anchor="middle" fill="#e2e8f0">.128 to .191</text><rect x="520" y="138" width="155" height="60" rx="8" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="597" y="158" text-anchor="middle" fill="#ffffff">Subnet 4</text><text class="ts" x="597" y="174" text-anchor="middle" fill="#e2e8f0">192.168.1.192/26</text><text class="ts" x="597" y="188" text-anchor="middle" fill="#e2e8f0">.192 to .255</text><rect x="40" y="225" width="600" height="170" rx="8" fill="#111827" stroke="#1e293b" stroke-width="1" stroke-dasharray="4 3"/><text class="th" x="340" y="248" text-anchor="middle" fill="#00d4ff">The maths</text><text class="ts" x="60" y="272" fill="#94a3b8">Borrowing 2 bits from host portion: 2 squared = 4 subnets</text><text class="ts" x="60" y="295" fill="#94a3b8">Each /26 subnet = 64 addresses (2 to the power of 6 = 64)</text><text class="ts" x="60" y="318" fill="#94a3b8">Usable hosts per subnet = 64 - 2 = 62 (network + broadcast reserved)</text><text class="ts" x="60" y="341" fill="#94a3b8">Subnet increment = 256 - 192 = 64 (256 minus the mask octet value)</text><text class="ts" x="60" y="364" fill="#94a3b8">Mask: 255.255.255.192 = /26</text></svg>',
         'terms': [('Private IP',
                    'Non-routable IP ranges for internal use: 10.x, 172.16-31.x, 192.168.x'),
                   ('Public IP', 'Globally routable IP address assigned by ISPs'),
                   ('NAT',
                    'Network Address Translation — maps private IPs to public IPs for internet '
                    'access'),
                   ('PAT',
                    'Port Address Translation — many private IPs share one public IP using port '
                    'numbers'),
                   ('RFC 1918', 'The standard defining private IPv4 address ranges')]},
 '2-4': {'diagram': '<svg width="100%" viewBox="0 0 680 380" xmlns="http://www.w3.org/2000/svg"><defs><style>.th{font-family:Arial,sans-serif;font-size:13px;font-weight:700;}.ts{font-family:Arial,sans-serif;font-size:11px;}.tm{font-family:JetBrains Mono,monospace;font-size:12px;}.tt{font-family:JetBrains Mono,monospace;font-size:11px;fill:#00d4ff;letter-spacing:2px;}</style></defs><text class="tt" x="340" y="22" text-anchor="middle">PRIVATE vs PUBLIC IP RANGES</text><text class="th" x="170" y="48" text-anchor="middle" fill="#6ee7b7">Private Ranges (RFC 1918)</text><rect x="30" y="58" width="290" height="180" rx="8" fill="#111827" stroke="#1d9e75" stroke-width="1"/><rect x="50" y="74" width="250" height="42" rx="6" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="tm" x="175" y="92" text-anchor="middle" fill="#ffffff">10.0.0.0 /8</text><text class="ts" x="175" y="108" text-anchor="middle" fill="#e2e8f0">10.0.0.0 to 10.255.255.255 - 16.7M addresses</text><rect x="50" y="122" width="250" height="42" rx="6" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="tm" x="175" y="140" text-anchor="middle" fill="#ffffff">172.16.0.0 /12</text><text class="ts" x="175" y="156" text-anchor="middle" fill="#e2e8f0">172.16.0.0 to 172.31.255.255 - 1M addresses</text><rect x="50" y="170" width="250" height="42" rx="6" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="tm" x="175" y="188" text-anchor="middle" fill="#ffffff">192.168.0.0 /16</text><text class="ts" x="175" y="204" text-anchor="middle" fill="#e2e8f0">192.168.0.0 to 192.168.255.255 - 65K addresses</text><text class="th" x="510" y="48" text-anchor="middle" fill="#f0997b">Public Ranges</text><rect x="360" y="58" width="290" height="180" rx="8" fill="#111827" stroke="#993c1d" stroke-width="1"/><rect x="380" y="74" width="250" height="42" rx="6" fill="#993c1d" stroke="#f0997b" stroke-width="1"/><text class="tm" x="505" y="92" text-anchor="middle" fill="#ffffff">1.0.0.0 to 9.255.255.255</text><text class="ts" x="505" y="108" text-anchor="middle" fill="#e2e8f0">Class A public (excl. 10.x.x.x)</text><rect x="380" y="122" width="250" height="42" rx="6" fill="#993c1d" stroke="#f0997b" stroke-width="1"/><text class="tm" x="505" y="140" text-anchor="middle" fill="#ffffff">11.0.0.0 to 172.15.255.255</text><text class="ts" x="505" y="156" text-anchor="middle" fill="#e2e8f0">Public ranges between private blocks</text><rect x="380" y="170" width="250" height="42" rx="6" fill="#993c1d" stroke="#f0997b" stroke-width="1"/><text class="tm" x="505" y="188" text-anchor="middle" fill="#ffffff">192.169.0.0 to 223.255.255.255</text><text class="ts" x="505" y="204" text-anchor="middle" fill="#e2e8f0">Class C public (excl. 192.168.x.x)</text><line x1="40" y1="258" x2="640" y2="258" stroke="#1e293b" stroke-width="0.5"/><text class="tt" x="340" y="276" text-anchor="middle" style="font-size:10px;">HOW NAT BRIDGES PRIVATE AND PUBLIC</text><rect x="40" y="288" width="110" height="44" rx="6" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="th" x="95" y="308" text-anchor="middle" fill="#fff">Private LAN</text><text class="ts" x="95" y="324" text-anchor="middle" fill="#e2e8f0">192.168.1.x</text><rect x="280" y="288" width="120" height="44" rx="6" fill="#ba7517" stroke="#fac775" stroke-width="1"/><text class="th" x="340" y="308" text-anchor="middle" fill="#fff">Router / NAT</text><text class="ts" x="340" y="324" text-anchor="middle" fill="#e2e8f0">Translates addresses</text><rect x="530" y="288" width="110" height="44" rx="6" fill="#993c1d" stroke="#f0997b" stroke-width="1"/><text class="th" x="585" y="308" text-anchor="middle" fill="#fff">Internet</text><text class="ts" x="585" y="324" text-anchor="middle" fill="#e2e8f0">203.0.113.x</text><line x1="150" y1="310" x2="278" y2="310" stroke="#94a3b8" stroke-width="1.5"/><line x1="400" y1="310" x2="528" y2="310" stroke="#94a3b8" stroke-width="1.5"/><text class="ts" x="214" y="304" text-anchor="middle" fill="#64748b">private</text><text class="ts" x="464" y="304" text-anchor="middle" fill="#64748b">public</text></svg>',
         'links': [('IANA — IPv4 Special Purpose Registry', 'https://www.iana.org/assignments/iana-ipv4-special-registry/'),
                   ('RFC 1918 — Address Allocation for Private Internets', 'https://tools.ietf.org/html/rfc1918')],
         'notes': 'IPv4 addresses are divided into public and private ranges. Private addresses are defined in RFC 1918 and are not routable on the internet — they are used inside homes, offices, and data centres. Three private ranges exist: 10.0.0.0/8 (Class A, ~16 million addresses), 172.16.0.0/12 (Class B, ~1 million addresses), and 192.168.0.0/16 (Class C, 65,536 addresses).\n\nPublic IP addresses are globally routable on the internet and must be unique worldwide. They are assigned by IANA and regional registries (ARIN, RIPE, APNIC). Public IPv4 space is nearly exhausted — this is the primary driver of IPv6 adoption.\n\nNAT (Network Address Translation) allows many devices with private addresses to share a single public IP. The router tracks outbound connections and rewrites source addresses. This is how almost every home and office network connects to the internet today.\n\nOther special ranges include 127.0.0.0/8 (loopback, 127.0.0.1 is localhost), 169.254.0.0/16 (APIPA, self-assigned when DHCP fails), and 100.64.0.0/10 (carrier-grade NAT used by ISPs).',
         'questions': [('What are the three RFC 1918 private IP ranges?',
                        '10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16'),
                       ('Why are private IP addresses not routable on the internet?',
                        'Routers on the internet are configured to drop packets with private source or destination addresses — they are reserved for internal use only'),
                       ('What does NAT do?',
                        'Translates private IP addresses to a public IP address for internet-bound traffic, allowing many devices to share one public IP')],
         'terms': [('Private IP', 'Non-routable address from RFC 1918 ranges used inside networks'),
                   ('Public IP', 'Globally unique, internet-routable address assigned by IANA'),
                   ('NAT', 'Network Address Translation — maps private IPs to public IPs at the router'),
                   ('RFC 1918', 'Standard defining the three private IPv4 address ranges'),
                   ('APIPA', 'Automatic Private IP Addressing — 169.254.x.x self-assigned when DHCP fails')]},
  '2-5': {'links': [('Cloudflare — What is IPv6?',
                    'https://www.cloudflare.com/learning/network-layer/what-is-ipv6/'),
                   ('Professor Messer — Network+ Course (Free)',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                   ('Hurricane Electric IPv6 Certification (Free)',
                    'https://ipv6.he.net/certification/')],
                  'diagram': '<svg width="100%" viewBox="0 0 680 380" xmlns="http://www.w3.org/2000/svg"><defs><style>.th{font-family:Arial,sans-serif;font-size:13px;font-weight:700;}.ts{font-family:Arial,sans-serif;font-size:11px;}.tm{font-family:JetBrains Mono,monospace;font-size:12px;font-weight:700;}.tt{font-family:JetBrains Mono,monospace;font-size:11px;fill:#00d4ff;letter-spacing:2px;}</style></defs><text class="tt" x="340" y="22" text-anchor="middle">IPv6 ADDRESSING BASICS</text><text class="ts" x="340" y="48" text-anchor="middle" fill="#64748b">Full IPv6 address (128 bits = 8 groups of 16 bits each):</text><rect x="40" y="56" width="600" height="32" rx="4" fill="#0a0f1e" stroke="#1e293b" stroke-width="1"/><text class="tm" x="340" y="78" text-anchor="middle" fill="#00d4ff" style="font-size:13px;">2001:0db8:0000:0000:0000:ff00:0042:8329</text><text class="ts" x="340" y="108" text-anchor="middle" fill="#64748b">Abbreviated (leading zeros dropped, consecutive zero groups = ::):</text><rect x="40" y="116" width="600" height="32" rx="4" fill="#0a0f1e" stroke="#1e293b" stroke-width="1"/><text class="tm" x="340" y="138" text-anchor="middle" fill="#00c853" style="font-size:13px;">2001:db8::ff00:42:8329</text><text class="ts" x="340" y="168" text-anchor="middle" fill="#64748b">Address structure for a /64 network:</text><rect x="40" y="178" width="300" height="44" rx="6" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="th" x="190" y="197" text-anchor="middle" fill="#ffffff">Network prefix (64 bits)</text><text class="ts" x="190" y="213" text-anchor="middle" fill="#e2e8f0">2001:db8:1:1 - assigned by ISP</text><rect x="344" y="178" width="296" height="44" rx="6" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="492" y="197" text-anchor="middle" fill="#ffffff">Interface ID (64 bits)</text><text class="ts" x="492" y="213" text-anchor="middle" fill="#e2e8f0">::1 to ::ffff - device address</text><line x1="40" y1="240" x2="640" y2="240" stroke="#1e293b" stroke-width="0.5"/><text class="tt" x="340" y="260" text-anchor="middle" style="font-size:10px;">COMMON ADDRESS TYPES</text><rect x="40" y="270" width="180" height="52" rx="6" fill="#534ab7" stroke="#7f77dd" stroke-width="1"/><text class="th" x="130" y="290" text-anchor="middle" fill="#fff">Global unicast</text><text class="ts" x="130" y="306" text-anchor="middle" fill="#e2e8f0">2000::/3</text><text class="ts" x="130" y="318" text-anchor="middle" fill="#e2e8f0">Public routable</text><rect x="230" y="270" width="200" height="52" rx="6" fill="#ba7517" stroke="#fac775" stroke-width="1"/><text class="th" x="330" y="290" text-anchor="middle" fill="#fff">Link-local</text><text class="ts" x="330" y="306" text-anchor="middle" fill="#e2e8f0">fe80::/10</text><text class="ts" x="330" y="318" text-anchor="middle" fill="#e2e8f0">Auto-assigned, LAN only</text><rect x="440" y="270" width="200" height="52" rx="6" fill="#475569" stroke="#94a3b8" stroke-width="1"/><text class="th" x="540" y="290" text-anchor="middle" fill="#fff">Loopback</text><text class="ts" x="540" y="306" text-anchor="middle" fill="#e2e8f0">::1/128</text><text class="ts" x="540" y="318" text-anchor="middle" fill="#e2e8f0">Equiv. to 127.0.0.1</text><text class="ts" x="340" y="348" text-anchor="middle" fill="#64748b">IPv6 has 340 undecillion addresses - enough for every grain of sand on Earth to have trillions</text><text class="ts" x="340" y="363" text-anchor="middle" fill="#64748b">No broadcast in IPv6 - replaced by multicast and anycast</text></svg>',
'notes': 'IPv6 was created to solve IPv4 address exhaustion. It uses 128-bit addresses '
                  'written as eight groups of four hexadecimal digits separated by colons: '
                  '2001:0db8:85a3:0000:0000:8a2e:0370:7334. Leading zeros in a group can be '
                  'omitted, and consecutive groups of zeros can be replaced with :: (but only once '
                  'per address). IPv6 provides 340 undecillion addresses — essentially unlimited.\n'
                  '\n'
                  'Key IPv6 address types: unicast (one-to-one), multicast (one-to-many), anycast '
                  '(one-to-nearest). There is no broadcast in IPv6. The loopback address is ::1. '
                  'Link-local addresses start with fe80:: and are automatically assigned. Global '
                  'unicast addresses (2000::/3) are the public internet addresses. IPv6 also has '
                  'built-in IPsec support and simplified headers for faster routing.',
         'questions': [('How many bits are in an IPv6 address?', '128 bits'),
                       ('What does :: represent in an IPv6 address?',
                        'One or more consecutive groups of zeros (can only be used once per '
                        'address)'),
                       ('What is the IPv6 loopback address?', '::1'),
                       ('Does IPv6 use broadcast?',
                        'No — IPv6 uses multicast and anycast instead of broadcast')],
         'terms': [('IPv6', '128-bit addressing scheme providing ~340 undecillion addresses'),
                   ('Link-Local',
                    'fe80::/10 — automatically assigned, only valid on local network segment'),
                   ('Global Unicast', '2000::/3 — publicly routable IPv6 addresses'),
                   (':: Notation',
                    'Shorthand replacing one or more consecutive groups of all-zero hextets'),
                   ('Loopback (IPv6)', '::1 — equivalent to 127.0.0.1 in IPv4')]},
 '2-6': {'links': [('Subnetting Practice — Free Drill Tool', 'https://subnettingpractice.com'),
                   ('Subnet Calculator', 'https://www.subnet-calculator.com'),
                   ('CIDR.xyz — Visual Subnet Tool', 'https://cidr.xyz')],
         'notes': 'This lab focuses on hands-on subnetting practice. Subnetting is the single most '
                  'important skill for the Network+ exam — questions appear in multiple domains '
                  'and performance-based questions will test it directly. Use the block size '
                  'method: find the interesting octet, calculate block size (256 - mask value), '
                  'and count up by that block size to find all subnets.\n'
                  '\n'
                  'For speed: memorize the common prefix lengths and their properties. /24=254 '
                  'hosts, /25=126, /26=62, /27=30, /28=14, /29=6, /30=2. Practice at '
                  'subnettingpractice.com until you can answer in under 30 seconds. In the real '
                  'exam you have 90 questions in 90 minutes — you cannot afford to spend 5 minutes '
                  'on a subnetting question.',
         'questions': [('A host has IP 192.168.10.130/26. What subnet is it on?',
                        '192.168.10.128/26 (block size 64: subnets at .0, .64, .128, .192)'),
                       ('How many usable hosts does a /29 provide?', '6 hosts (2^3=8, minus 2)'),
                       ('You need 50 hosts per subnet. What is the smallest prefix that works?',
                        '/26 — provides 62 usable hosts')],
         'terms': [('/25', '255.255.255.128 — 2 subnets, 126 hosts each'),
                   ('/26', '255.255.255.192 — 4 subnets, 62 hosts each'),
                   ('/27', '255.255.255.224 — 8 subnets, 30 hosts each'),
                   ('/28', '255.255.255.240 — 16 subnets, 14 hosts each'),
                   ('/29', '255.255.255.248 — 32 subnets, 6 hosts each'),
                   ('/30', '255.255.255.252 — 64 subnets, 2 hosts each (point-to-point links)')]},
 '3-1': {'links': [('Cloudflare — What is a Router?',
                    'https://www.cloudflare.com/learning/network-layer/what-is-a-router/'),
                   ('Professor Messer — Network+ Course (Free)',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                   ('Packet Tracer — Free Cisco Network Simulator',
                    'https://www.netacad.com/courses/packet-tracer')],
                  'diagram': '<svg width="100%" viewBox="0 0 680 360" xmlns="http://www.w3.org/2000/svg"><defs><style>.th{font-family:Arial,sans-serif;font-size:13px;font-weight:700;}.ts{font-family:Arial,sans-serif;font-size:11px;}.tm{font-family:JetBrains Mono,monospace;font-size:12px;}.tt{font-family:JetBrains Mono,monospace;font-size:11px;fill:#00d4ff;letter-spacing:2px;}</style><marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs><text class="tt" x="340" y="22" text-anchor="middle">HOW ROUTERS MAKE FORWARDING DECISIONS</text><rect x="30" y="80" width="90" height="44" rx="6" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="th" x="75" y="100" text-anchor="middle" fill="#ffffff">PC</text><text class="ts" x="75" y="116" text-anchor="middle" fill="#e2e8f0">10.0.1.10</text><line x1="120" y1="102" x2="158" y2="102" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#arr)"/><rect x="160" y="70" width="110" height="64" rx="8" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="215" y="92" text-anchor="middle" fill="#ffffff">Router</text><text class="ts" x="215" y="108" text-anchor="middle" fill="#e2e8f0">Checks routing</text><text class="ts" x="215" y="122" text-anchor="middle" fill="#e2e8f0">table for dest.</text><rect x="320" y="40" width="320" height="150" rx="8" fill="#111827" stroke="#1e293b" stroke-width="1"/><text class="tt" x="480" y="62" text-anchor="middle" style="font-size:10px;">ROUTING TABLE</text><line x1="320" y1="70" x2="640" y2="70" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="340" y="85" fill="#64748b">Destination</text><text class="ts" x="490" y="85" fill="#64748b">Next Hop</text><text class="ts" x="590" y="85" fill="#64748b">Interface</text><line x1="320" y1="90" x2="640" y2="90" stroke="#1e293b" stroke-width="0.5"/><text class="tm" x="340" y="107" fill="#e2e8f0">10.0.1.0/24</text><text class="tm" x="490" y="107" fill="#e2e8f0">Connected</text><text class="tm" x="590" y="107" fill="#e2e8f0">Gi0/0</text><text class="tm" x="340" y="125" fill="#00c853">192.168.1.0/24</text><text class="tm" x="490" y="125" fill="#00c853">10.0.2.1</text><text class="tm" x="590" y="125" fill="#00c853">Gi0/1</text><text class="tm" x="340" y="143" fill="#e2e8f0">0.0.0.0/0</text><text class="tm" x="490" y="143" fill="#e2e8f0">203.0.113.1</text><text class="tm" x="590" y="143" fill="#e2e8f0">Gi0/2</text><text class="ts" x="340" y="178" fill="#64748b">Default route (0.0.0.0/0) = gateway of last resort</text><line x1="270" y1="90" x2="318" y2="90" stroke="#00c853" stroke-width="1" stroke-dasharray="4 2" marker-end="url(#arr)"/><rect x="160" y="220" width="110" height="44" rx="6" fill="#ba7517" stroke="#fac775" stroke-width="1"/><text class="th" x="215" y="240" text-anchor="middle" fill="#ffffff">192.168.1.0/24</text><text class="ts" x="215" y="256" text-anchor="middle" fill="#e2e8f0">via 10.0.2.1</text><rect x="30" y="220" width="110" height="44" rx="6" fill="#993c1d" stroke="#f0997b" stroke-width="1"/><text class="th" x="85" y="240" text-anchor="middle" fill="#ffffff">Internet</text><text class="ts" x="85" y="256" text-anchor="middle" fill="#e2e8f0">via 203.0.113.1</text><line x1="180" y1="134" x2="180" y2="218" stroke="#fac775" stroke-width="1" stroke-dasharray="3 2" marker-end="url(#arr)"/><line x1="195" y1="134" x2="85" y2="218" stroke="#f0997b" stroke-width="1" stroke-dasharray="3 2" marker-end="url(#arr)"/><rect x="30" y="300" width="620" height="40" rx="6" fill="none" stroke="#1e293b" stroke-width="0.5" stroke-dasharray="4 3"/><text class="ts" x="340" y="316" text-anchor="middle" fill="#64748b">Longest prefix match wins - router picks the most specific route matching the destination</text><text class="ts" x="340" y="332" text-anchor="middle" fill="#64748b">If no specific match, falls back to default route (0.0.0.0/0)</text></svg>',
'notes': 'A router is a Layer 3 device that forwards packets between different networks '
                  'based on IP addresses. Where a switch connects devices within the same network, '
                  'a router connects different networks together. Routers maintain a routing table '
                  '— a list of known networks and the best path to reach them. When a packet '
                  'arrives, the router looks up the destination IP in its routing table and '
                  'forwards the packet out the appropriate interface.\n'
                  '\n'
                  'Routing can be static (manually configured routes) or dynamic (routes learned '
                  'automatically via protocols like OSPF, EIGRP, or BGP). The default gateway on '
                  "any device is the router's IP address — it's where traffic is sent when the "
                  'destination is not on the local network. Every time traffic crosses from one '
                  'network to another, it passes through at least one router.',
         'questions': [('At which OSI layer do routers operate?', 'Layer 3 — Network layer'),
                       ('What is a default gateway?',
                        'The IP address of the router that a host sends traffic to for '
                        'destinations outside its subnet'),
                       ('What is the difference between a router and a switch?',
                        'A switch forwards frames within a network using MAC addresses (L2); a '
                        'router forwards packets between networks using IP addresses (L3)')],
         'terms': [('Router',
                    'Layer 3 device that forwards packets between networks based on IP addresses'),
                   ('Routing Table',
                    'List of networks and next-hop addresses a router uses to forward traffic'),
                   ('Default Gateway',
                    'The router IP address that a host sends traffic to when the destination is '
                    'off-network'),
                   ('Static Route', "Manually configured route that doesn't change automatically"),
                   ('Dynamic Routing',
                    'Routes learned automatically via protocols like OSPF, EIGRP, BGP')]},
 '3-3': {'links': [('Professor Messer — Network+ Course (Free)',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                   ('Packet Tracer — Free Cisco Network Simulator',
                    'https://www.netacad.com/courses/packet-tracer'),
                   ('Cloudflare Learning Center', 'https://www.cloudflare.com/learning/')],
         'notes': 'A VLAN (Virtual LAN) logically segments a physical network into separate '
                  'broadcast domains without requiring separate physical switches. Ports on a '
                  'switch are assigned to VLANs — devices in VLAN 10 cannot communicate directly '
                  'with devices in VLAN 20 without going through a router (or Layer 3 switch). '
                  'This improves security, reduces broadcast traffic, and enables logical grouping '
                  'of users regardless of physical location.\n'
                  '\n'
                  'Trunk ports carry traffic for multiple VLANs between switches using 802.1Q '
                  'tagging — a 4-byte tag is added to the frame header identifying which VLAN it '
                  'belongs to. Access ports connect to end devices and carry only one VLAN. '
                  'Inter-VLAN routing requires a router or Layer 3 switch. VLANs are essential for '
                  'network segmentation — separating staff from guests, or finance from IT.',
         'questions': [('Can two devices on different VLANs communicate without a router?',
                        'No — VLANs are separate broadcast domains; a router or L3 switch is '
                        'required'),
                       ('What standard is used for VLAN tagging on trunk links?', 'IEEE 802.1Q'),
                       ('What is the difference between a trunk port and an access port?',
                        'Trunk port carries multiple VLANs (tagged); access port carries one VLAN '
                        '(untagged) for end devices')],
                  'diagram': '<svg width="100%" viewBox="0 0 680 400" xmlns="http://www.w3.org/2000/svg"><defs><style>.th{font-family:Arial,sans-serif;font-size:13px;font-weight:700;}.ts{font-family:Arial,sans-serif;font-size:11px;}.tt{font-family:JetBrains Mono,monospace;font-size:12px;fill:#00d4ff;letter-spacing:2px;}</style></defs><text class="tt" x="340" y="22" text-anchor="middle">VLANs AND INTER-VLAN ROUTING</text><rect x="265" y="35" width="150" height="48" rx="8" fill="#475569" stroke="#94a3b8" stroke-width="1"/><text class="th" x="340" y="55" text-anchor="middle" fill="#ffffff">Router</text><text class="ts" x="340" y="72" text-anchor="middle" fill="#e2e8f0">Inter-VLAN routing</text><text class="ts" x="392" y="104" fill="#64748b">Trunk (802.1Q)</text><line x1="340" y1="83" x2="340" y2="143" stroke="#94a3b8" stroke-width="2"/><rect x="185" y="145" width="310" height="48" rx="8" fill="#475569" stroke="#94a3b8" stroke-width="1"/><text class="th" x="340" y="165" text-anchor="middle" fill="#ffffff">Managed switch</text><text class="ts" x="340" y="182" text-anchor="middle" fill="#e2e8f0">VLAN 10 + VLAN 20 configured</text><line x1="230" y1="193" x2="160" y2="248" stroke="#94a3b8" stroke-width="1"/><line x1="270" y1="193" x2="270" y2="248" stroke="#94a3b8" stroke-width="1"/><line x1="410" y1="193" x2="410" y2="248" stroke="#94a3b8" stroke-width="1"/><line x1="450" y1="193" x2="520" y2="248" stroke="#94a3b8" stroke-width="1"/><rect x="60" y="250" width="240" height="75" rx="8" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="th" x="180" y="272" text-anchor="middle" fill="#ffffff">VLAN 10 - Finance</text><text class="ts" x="180" y="290" text-anchor="middle" fill="#e2e8f0">192.168.10.0/24</text><text class="ts" x="180" y="308" text-anchor="middle" fill="#e2e8f0">PC1 (.10) - PC2 (.11)</text><rect x="370" y="250" width="250" height="75" rx="8" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="495" y="272" text-anchor="middle" fill="#ffffff">VLAN 20 - IT</text><text class="ts" x="495" y="290" text-anchor="middle" fill="#e2e8f0">192.168.20.0/24</text><text class="ts" x="495" y="308" text-anchor="middle" fill="#e2e8f0">PC3 (.10) - PC4 (.11)</text><line x1="300" y1="288" x2="368" y2="288" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4 3"/><text class="ts" x="334" y="280" text-anchor="middle" fill="#ef4444">no direct</text><rect x="40" y="348" width="600" height="35" rx="6" fill="none" stroke="#1e293b" stroke-width="1" stroke-dasharray="4 3"/><text class="ts" x="340" y="360" text-anchor="middle" fill="#64748b">Devices in different VLANs cannot communicate without the router</text><text class="ts" x="340" y="376" text-anchor="middle" fill="#64748b">Trunk port carries tagged 802.1Q frames for both VLANs</text></svg>',
         'terms': [('ICMP',
                    'Internet Control Message Protocol — used for diagnostics and error reporting, '
                    'Layer 3'),
                   ('Ping',
                    'Uses ICMP Echo Request/Reply to test host reachability and measure latency'),
                   ('Traceroute',
                    'Maps the path to a destination by sending packets with incrementing TTL '
                    'values'),
                   ('TTL',
                    'Time to Live — decrements at each router hop; packet discarded when it '
                    'reaches 0'),
                   ('Echo Request/Reply',
                    'ICMP message types used by ping (type 8 = request, type 0 = reply)')]},
 '3-4': {'diagram': '<svg width="100%" viewBox="0 0 680 400" xmlns="http://www.w3.org/2000/svg"><defs><style>.th{font-family:Arial,sans-serif;font-size:13px;font-weight:700;}.ts{font-family:Arial,sans-serif;font-size:11px;}.tm{font-family:JetBrains Mono,monospace;font-size:12px;}.tt{font-family:JetBrains Mono,monospace;font-size:11px;fill:#00d4ff;letter-spacing:2px;}</style><marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs><text class="tt" x="340" y="22" text-anchor="middle">ICMP PROTOCOL - PING AND TRACEROUTE</text><text class="th" x="340" y="50" text-anchor="middle" fill="#00d4ff">How ping works</text><rect x="40" y="62" width="100" height="44" rx="6" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="th" x="90" y="82" text-anchor="middle" fill="#fff">Host A</text><text class="ts" x="90" y="98" text-anchor="middle" fill="#e2e8f0">10.0.0.1</text><rect x="540" y="62" width="100" height="44" rx="6" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="590" y="82" text-anchor="middle" fill="#fff">Host B</text><text class="ts" x="590" y="98" text-anchor="middle" fill="#e2e8f0">10.0.0.2</text><line x1="140" y1="78" x2="538" y2="78" stroke="#00b4d8" stroke-width="1.5" marker-end="url(#arr)"/><text class="ts" x="340" y="72" text-anchor="middle" fill="#00b4d8">ICMP Echo Request (type 8)</text><line x1="538" y1="92" x2="140" y2="92" stroke="#00c853" stroke-width="1.5" marker-end="url(#arr)"/><text class="ts" x="340" y="106" text-anchor="middle" fill="#00c853">ICMP Echo Reply (type 0)</text><line x1="40" y1="130" x2="640" y2="130" stroke="#1e293b" stroke-width="0.5"/><text class="th" x="340" y="150" text-anchor="middle" fill="#00d4ff">How traceroute works (TTL incrementing)</text><rect x="30" y="162" width="80" height="36" rx="6" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="th" x="70" y="185" text-anchor="middle" fill="#fff">Source</text><rect x="190" y="162" width="80" height="36" rx="6" fill="#475569" stroke="#94a3b8" stroke-width="1"/><text class="th" x="230" y="185" text-anchor="middle" fill="#fff">Router 1</text><rect x="350" y="162" width="80" height="36" rx="6" fill="#475569" stroke="#94a3b8" stroke-width="1"/><text class="th" x="390" y="185" text-anchor="middle" fill="#fff">Router 2</text><rect x="510" y="162" width="100" height="36" rx="6" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="560" y="185" text-anchor="middle" fill="#fff">Destination</text><line x1="110" y1="175" x2="188" y2="175" stroke="#fac775" stroke-width="1.5" marker-end="url(#arr)"/><text class="ts" x="150" y="169" text-anchor="middle" fill="#fac775">TTL=1</text><line x1="188" y1="188" x2="110" y2="188" stroke="#ef4444" stroke-width="1" stroke-dasharray="4 2" marker-end="url(#arr)"/><text class="ts" x="150" y="202" text-anchor="middle" fill="#ef4444">TTL exceeded</text><line x1="110" y1="218" x2="348" y2="218" stroke="#fac775" stroke-width="1.5" marker-end="url(#arr)"/><text class="ts" x="229" y="212" text-anchor="middle" fill="#fac775">TTL=2</text><line x1="348" y1="230" x2="110" y2="230" stroke="#ef4444" stroke-width="1" stroke-dasharray="4 2" marker-end="url(#arr)"/><text class="ts" x="229" y="244" text-anchor="middle" fill="#ef4444">TTL exceeded</text><line x1="110" y1="258" x2="508" y2="258" stroke="#fac775" stroke-width="1.5" marker-end="url(#arr)"/><text class="ts" x="309" y="252" text-anchor="middle" fill="#fac775">TTL=3</text><line x1="508" y1="268" x2="110" y2="268" stroke="#00c853" stroke-width="1.5" marker-end="url(#arr)"/><text class="ts" x="309" y="282" text-anchor="middle" fill="#00c853">Echo Reply - destination reached!</text><line x1="40" y1="300" x2="640" y2="300" stroke="#1e293b" stroke-width="0.5"/><text class="tt" x="340" y="318" text-anchor="middle" style="font-size:10px;">KEY ICMP MESSAGE TYPES</text><rect x="40" y="328" width="130" height="44" rx="6" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="th" x="105" y="348" text-anchor="middle" fill="#fff">Type 0 / 8</text><text class="ts" x="105" y="364" text-anchor="middle" fill="#e2e8f0">Echo Reply/Request</text><rect x="185" y="328" width="130" height="44" rx="6" fill="#993c1d" stroke="#f0997b" stroke-width="1"/><text class="th" x="250" y="348" text-anchor="middle" fill="#fff">Type 3</text><text class="ts" x="250" y="364" text-anchor="middle" fill="#e2e8f0">Dest. Unreachable</text><rect x="330" y="328" width="130" height="44" rx="6" fill="#ba7517" stroke="#fac775" stroke-width="1"/><text class="th" x="395" y="348" text-anchor="middle" fill="#fff">Type 11</text><text class="ts" x="395" y="364" text-anchor="middle" fill="#e2e8f0">TTL Exceeded</text><rect x="475" y="328" width="165" height="44" rx="6" fill="#534ab7" stroke="#7f77dd" stroke-width="1"/><text class="th" x="557" y="348" text-anchor="middle" fill="#fff">Type 5</text><text class="ts" x="557" y="364" text-anchor="middle" fill="#e2e8f0">Redirect (reroute)</text></svg>',
         'links': [('Cloudflare - What is ICMP?', 'https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/'),
                   ('Professor Messer - Network+ Course (Free)', 'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/')],
         'notes': 'ICMP (Internet Control Message Protocol) is a Layer 3 protocol used for network diagnostics and error reporting. Unlike TCP and UDP, ICMP does not carry application data — it carries control messages between network devices.\n\nPing uses ICMP Echo Request (type 8) and Echo Reply (type 0) to test connectivity and measure round-trip time. When you ping a host, your machine sends an Echo Request and waits for an Echo Reply.\n\nTraceroute uses ICMP TTL (Time to Live) expiry to map the path to a destination. It sends packets with TTL=1, 2, 3... Each router decrements TTL by 1 and when TTL reaches 0, returns an ICMP Time Exceeded message (type 11). This reveals each hop along the path.\n\nOther important ICMP types include Type 3 (Destination Unreachable — host or port not reachable), Type 5 (Redirect — tells a host to use a better route), and Type 9/10 (Router Advertisement/Solicitation).\n\nICMP is frequently blocked by firewalls since it can be used for reconnaissance and attacks like ping floods and Smurf attacks. However, blocking all ICMP breaks path MTU discovery and other useful network functions.',
         'questions': [('What ICMP types does ping use?',
                        'Type 8 (Echo Request) sent to the destination, Type 0 (Echo Reply) returned by the destination'),
                       ('How does traceroute use ICMP to map network paths?',
                        'It sends packets with increasing TTL values - each router that drops a packet returns an ICMP Type 11 Time Exceeded message revealing its address'),
                       ('What does ICMP Type 3 mean?',
                        'Destination Unreachable - the packet could not be delivered, with a code indicating why (host unreachable, port unreachable, etc.)')],
         'terms': [('ICMP', 'Internet Control Message Protocol - Layer 3 protocol for diagnostics and error reporting'),
                   ('Echo Request/Reply', 'ICMP types 8 and 0 used by ping to test host reachability'),
                   ('TTL', 'Time to Live - decremented by each router; when it reaches 0 an ICMP Time Exceeded is returned'),
                   ('Traceroute', 'Tool that maps network path by exploiting TTL expiry to identify each hop'),
                   ('Destination Unreachable', 'ICMP type 3 - sent when a packet cannot reach its destination')]},
  '3-5': {'links': [('Wireshark — Free Download', 'https://www.wireshark.org/download.html'),
                   ('Wireshark User Guide', 'https://www.wireshark.org/docs/wsug_html_chunked/'),
                   ('Wireshark Display Filter Reference', 'https://www.wireshark.org/docs/dfref/')],
         'notes': 'Wireshark is the industry-standard free packet analyser. It captures all '
                  'network traffic passing through a network interface and displays it in a '
                  'human-readable format. You can filter by protocol (tcp, udp, icmp, dns, http), '
                  'by IP address (ip.addr == 192.168.1.1), or by port (tcp.port == 443). Wireshark '
                  'is essential for troubleshooting and understanding how protocols actually work '
                  'in practice.\n'
                  '\n'
                  'For this lab: install Wireshark from wireshark.org, start a capture on your '
                  'network interface, then open a browser or run ping. Watch the packets appear. '
                  "Try filtering for 'icmp' and run a ping — you'll see the Echo Request and Reply "
                  "packets. Try 'dns' and browse to a website — you'll see the DNS query and "
                  'response. This hands-on practice cements the theory in a way reading never can.',
         'questions': [('What Wireshark filter shows only ICMP traffic?', 'icmp'),
                       ('What Wireshark filter shows traffic to/from a specific IP?',
                        'ip.addr == x.x.x.x'),
                       ('What Wireshark filter shows only DNS traffic?', 'dns or udp.port == 53')],
         'terms': [('Packet Capture', 'Recording network traffic for analysis; also called a pcap'),
                   ('Display Filter',
                    "Wireshark filter to show only specific traffic, e.g. 'tcp.port == 80'"),
                   ('Promiscuous Mode',
                    'NIC mode that captures all packets, not just those addressed to it'),
                   ('Follow TCP Stream',
                    'Wireshark feature to reconstruct and read an entire TCP conversation'),
                   ('.pcap file', 'Standard file format for saved packet captures')]},
 '4-1': {'links': [('Cloudflare — How DNS Works',
                    'https://www.cloudflare.com/learning/dns/what-is-dns/'),
                   ('Cloudflare — DNS Record Types',
                    'https://www.cloudflare.com/learning/dns/dns-records/'),
                   ('Professor Messer — Network+ Course (Free)',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/')],
                  'diagram': '<svg width="100%" viewBox="0 0 680 360" xmlns="http://www.w3.org/2000/svg"><defs><style>.th{font-family:Arial,sans-serif;font-size:13px;font-weight:700;}.ts{font-family:Arial,sans-serif;font-size:11px;}.tm{font-family:JetBrains Mono,monospace;font-size:11px;}.tt{font-family:JetBrains Mono,monospace;font-size:11px;fill:#00d4ff;letter-spacing:2px;}</style><marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs><text class="tt" x="340" y="22" text-anchor="middle">DNS NAME RESOLUTION PROCESS</text><rect x="30" y="60" width="90" height="50" rx="6" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="th" x="75" y="82" text-anchor="middle" fill="#fff">Client</text><text class="ts" x="75" y="98" text-anchor="middle" fill="#e2e8f0">Browser</text><rect x="175" y="60" width="110" height="50" rx="6" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="230" y="82" text-anchor="middle" fill="#fff">Local resolver</text><text class="ts" x="230" y="98" text-anchor="middle" fill="#e2e8f0">ISP / corp DNS</text><rect x="340" y="40" width="100" height="50" rx="6" fill="#ba7517" stroke="#fac775" stroke-width="1"/><text class="th" x="390" y="62" text-anchor="middle" fill="#fff">Root server</text><text class="ts" x="390" y="78" text-anchor="middle" fill="#e2e8f0">13 root zones</text><rect x="460" y="60" width="100" height="50" rx="6" fill="#993c1d" stroke="#f0997b" stroke-width="1"/><text class="th" x="510" y="82" text-anchor="middle" fill="#fff">TLD server</text><text class="ts" x="510" y="98" text-anchor="middle" fill="#e2e8f0">.com / .org</text><rect x="570" y="80" width="100" height="50" rx="6" fill="#534ab7" stroke="#7f77dd" stroke-width="1"/><text class="th" x="620" y="100" text-anchor="middle" fill="#fff">Authoritative</text><text class="ts" x="620" y="116" text-anchor="middle" fill="#e2e8f0">example.com</text><line x1="120" y1="82" x2="173" y2="82" stroke="#00b4d8" stroke-width="1.5" marker-end="url(#arr)"/><text class="ts" x="148" y="76" text-anchor="middle" fill="#00b4d8">1</text><line x1="285" y1="75" x2="338" y2="68" stroke="#fac775" stroke-width="1.5" marker-end="url(#arr)"/><text class="ts" x="310" y="64" text-anchor="middle" fill="#fac775">2</text><line x1="390" y1="90" x2="390" y2="108" stroke="#fac775" stroke-width="1"/><line x1="390" y1="108" x2="458" y2="95" stroke="#f0997b" stroke-width="1.5" marker-end="url(#arr)"/><text class="ts" x="430" y="96" text-anchor="middle" fill="#f0997b">3</text><line x1="560" y1="90" x2="572" y2="94" stroke="#7f77dd" stroke-width="1.5" marker-end="url(#arr)"/><text class="ts" x="570" y="84" text-anchor="middle" fill="#7f77dd">4</text><path d="M620 132 Q620 160 340 170 Q120 178 75 132" fill="none" stroke="#00c853" stroke-width="1.5" stroke-dasharray="5 3" marker-end="url(#arr)"/><text class="ts" x="340" y="190" text-anchor="middle" fill="#00c853">5. IP address returned to client (e.g. 93.184.216.34)</text><rect x="30" y="210" width="620" height="120" rx="8" fill="#111827" stroke="#1e293b" stroke-width="1"/><text class="ts" x="50" y="230" fill="#94a3b8">1. Client asks local resolver: "What is the IP for www.example.com?"</text><text class="ts" x="50" y="250" fill="#94a3b8">2. Resolver checks cache (miss) - asks root server which TLD server handles .com</text><text class="ts" x="50" y="270" fill="#94a3b8">3. Root replies with TLD server address - resolver asks TLD for example.com nameserver</text><text class="ts" x="50" y="290" fill="#94a3b8">4. TLD replies with authoritative nameserver - resolver asks it for the A record</text><text class="ts" x="50" y="310" fill="#00c853">5. Authoritative server returns 93.184.216.34 - resolver caches it and returns to client</text></svg>',
'notes': 'DNS (Domain Name System) translates human-readable domain names into IP '
                  'addresses. When you type google.com, your device sends a DNS query to a '
                  'resolver (usually your ISP or a public resolver like 8.8.8.8). The resolver '
                  'checks its cache, then queries root servers, then TLD servers (.com), then the '
                  'authoritative name server for google.com, which returns the IP address.\n'
                  '\n'
                  'This hierarchical process is called recursive resolution. The result is cached '
                  'at multiple levels to speed up future queries — TTL (Time to Live) in the DNS '
                  "record controls how long it's cached. DNS operates on port 53 and uses UDP for "
                  'queries (fast) and TCP for zone transfers (reliable). Understanding DNS is '
                  "critical for troubleshooting connectivity issues — 'it's always DNS' is a "
                  'famous sysadmin joke because DNS failures cause so many apparent outages.',
         'questions': [('What port does DNS use?',
                        'Port 53 (UDP for queries, TCP for zone transfers)'),
                       ('What is the role of an authoritative name server?',
                        'It holds the actual DNS records for a domain and answers queries about it '
                        'definitively'),
                       ('Why does DNS caching matter?',
                        'It speeds up resolution by avoiding repeated queries and reduces load on '
                        'DNS servers')],
         'terms': [('DNS', 'Domain Name System — translates domain names to IP addresses'),
                   ('Resolver', 'The DNS server your device queries; usually your ISP or 8.8.8.8'),
                   ('Authoritative Name Server',
                    'The server that holds the actual DNS records for a domain'),
                   ('Root Server',
                    'Top of the DNS hierarchy; 13 sets worldwide; knows where TLD servers are'),
                   ('DNS Cache',
                    'Temporary storage of DNS query results to speed up future lookups'),
                   ('TTL',
                    'Time to Live — how long a DNS record is cached before being refreshed')]},
 '4-2': {'links': [('Cloudflare — What is DHCP?',
                    'https://www.cloudflare.com/learning/network-layer/what-is-dhcp/'),
                   ('Professor Messer — Network+ Course (Free)',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                   ('Packet Tracer — Free Cisco Network Simulator',
                    'https://www.netacad.com/courses/packet-tracer')],
                  'diagram': '<svg width="100%" viewBox="0 0 680 380" xmlns="http://www.w3.org/2000/svg"><defs><style>.th{font-family:Arial,sans-serif;font-size:13px;font-weight:700;}.ts{font-family:Arial,sans-serif;font-size:11px;}.tm{font-family:JetBrains Mono,monospace;font-size:12px;}.tt{font-family:JetBrains Mono,monospace;font-size:11px;fill:#00d4ff;letter-spacing:2px;}</style><marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs><text class="tt" x="340" y="22" text-anchor="middle">DHCP DORA PROCESS</text><rect x="40" y="45" width="120" height="50" rx="6" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="th" x="100" y="68" text-anchor="middle" fill="#fff">DHCP Client</text><text class="ts" x="100" y="85" text-anchor="middle" fill="#e2e8f0">No IP yet</text><rect x="520" y="45" width="120" height="50" rx="6" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="580" y="68" text-anchor="middle" fill="#fff">DHCP Server</text><text class="ts" x="580" y="85" text-anchor="middle" fill="#e2e8f0">IP pool: 192.168.1.x</text><line x1="100" y1="95" x2="100" y2="340" stroke="#00b4d8" stroke-width="0.5" stroke-dasharray="3 3"/><line x1="580" y1="95" x2="580" y2="340" stroke="#00c853" stroke-width="0.5" stroke-dasharray="3 3"/><rect x="30" y="108" width="50" height="28" rx="4" fill="#185fa5" stroke="#00b4d8" stroke-width="0.5"/><text class="ts" x="55" y="126" text-anchor="middle" fill="#fff">1</text><line x1="100" y1="122" x2="578" y2="122" stroke="#00b4d8" stroke-width="1.5" marker-end="url(#arr)"/><rect x="190" y="108" width="300" height="28" rx="4" fill="#0a0f1e" stroke="#1e293b" stroke-width="0.5"/><text class="th" x="340" y="126" text-anchor="middle" fill="#00b4d8">DISCOVER</text><text class="ts" x="600" y="118" fill="#64748b">Broadcast</text><text class="ts" x="600" y="130" fill="#64748b">src: 0.0.0.0</text><text class="ts" x="340" y="154" text-anchor="middle" fill="#64748b">I need an IP address - is there a DHCP server?</text><rect x="600" y="168" width="50" height="28" rx="4" fill="#1d9e75" stroke="#00c853" stroke-width="0.5"/><text class="ts" x="625" y="186" text-anchor="middle" fill="#fff">2</text><line x1="578" y1="182" x2="102" y2="182" stroke="#00c853" stroke-width="1.5" marker-end="url(#arr)"/><rect x="190" y="168" width="300" height="28" rx="4" fill="#0a0f1e" stroke="#1e293b" stroke-width="0.5"/><text class="th" x="340" y="186" text-anchor="middle" fill="#00c853">OFFER</text><text class="ts" x="340" y="210" text-anchor="middle" fill="#64748b">Here, use 192.168.1.50 - lease 24 hours, gateway .1, DNS .1</text><rect x="30" y="224" width="50" height="28" rx="4" fill="#185fa5" stroke="#00b4d8" stroke-width="0.5"/><text class="ts" x="55" y="242" text-anchor="middle" fill="#fff">3</text><line x1="100" y1="238" x2="578" y2="238" stroke="#ba7517" stroke-width="1.5" marker-end="url(#arr)"/><rect x="190" y="224" width="300" height="28" rx="4" fill="#0a0f1e" stroke="#1e293b" stroke-width="0.5"/><text class="th" x="340" y="242" text-anchor="middle" fill="#fac775">REQUEST</text><text class="ts" x="340" y="266" text-anchor="middle" fill="#64748b">I accept 192.168.1.50 - please confirm (still broadcast)</text><rect x="600" y="280" width="50" height="28" rx="4" fill="#1d9e75" stroke="#00c853" stroke-width="0.5"/><text class="ts" x="625" y="298" text-anchor="middle" fill="#fff">4</text><line x1="578" y1="294" x2="102" y2="294" stroke="#534ab7" stroke-width="1.5" marker-end="url(#arr)"/><rect x="190" y="280" width="300" height="28" rx="4" fill="#0a0f1e" stroke="#1e293b" stroke-width="0.5"/><text class="th" x="340" y="298" text-anchor="middle" fill="#7f77dd">ACKNOWLEDGE</text><text class="ts" x="340" y="322" text-anchor="middle" fill="#64748b">Confirmed - 192.168.1.50 is yours for 24 hours</text><rect x="190" y="340" width="300" height="28" rx="6" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="340" y="358" text-anchor="middle" fill="#fff">Client now has IP, mask, gateway, DNS</text></svg>',
'notes': 'DHCP (Dynamic Host Configuration Protocol) automatically assigns IP addresses '
                  'and network configuration to devices. Without DHCP, every device would need a '
                  'manually configured IP, subnet mask, default gateway, and DNS server. DHCP uses '
                  'a four-step process called DORA: Discover (client broadcasts looking for a DHCP '
                  'server), Offer (server offers an IP address), Request (client requests the '
                  'offered address), Acknowledge (server confirms the lease).\n'
                  '\n'
                  'DHCP leases are temporary — devices must renew them periodically. A DHCP scope '
                  'defines the range of addresses the server can assign. DHCP can also assign '
                  'options: default gateway, DNS servers, domain name, NTP server. DHCP Relay (ip '
                  'helper-address on Cisco) forwards DHCP broadcasts across routers so one DHCP '
                  'server can serve multiple subnets. DHCP uses UDP ports 67 (server) and 68 '
                  '(client).',
         'questions': [('What does DORA stand for?', 'Discover, Offer, Request, Acknowledge'),
                       ('What ports does DHCP use?', 'UDP 67 (server) and UDP 68 (client)'),
                       ('What is a DHCP scope?',
                        'The range of IP addresses a DHCP server is configured to assign'),
                       ('Why is DHCP Relay needed?',
                        "DHCP uses broadcasts which don't cross routers; relay forwards DHCP "
                        'messages across subnets')],
         'terms': [('DHCP',
                    'Dynamic Host Configuration Protocol — automatically assigns IP configuration '
                    'to hosts'),
                   ('DORA', 'Discover, Offer, Request, Acknowledge — the four steps of DHCP'),
                   ('DHCP Lease', 'Temporary assignment of an IP address; must be renewed'),
                   ('DHCP Scope', 'The pool of IP addresses a DHCP server can assign'),
                   ('DHCP Relay', 'Forwards DHCP broadcasts across routers (ip helper-address)'),
                   ('Ports 67/68', 'DHCP server listens on 67; client on 68; both use UDP')]},
 '4-3': {'links': [('Cloudflare — What is a Firewall?',
                    'https://www.cloudflare.com/learning/security/what-is-a-firewall/'),
                   ('Cloudflare — IDS vs IPS',
                    'https://www.cloudflare.com/learning/security/glossary/intrusion-detection-prevention/'),
                   ('Professor Messer — Network+ Course (Free)',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/')],
         'notes': 'A firewall filters traffic based on rules, blocking unauthorised access while '
                  'allowing legitimate traffic. Stateful firewalls track the state of connections '
                  '— they know whether an incoming packet is part of an established connection or '
                  'a new unsolicited one. Next-gen firewalls (NGFW) add deep packet inspection, '
                  'application awareness, and intrusion prevention.\n'
                  '\n'
                  'An IDS (Intrusion Detection System) monitors traffic and alerts on suspicious '
                  "activity but doesn't block it. An IPS (Intrusion Prevention System) actively "
                  'blocks threats in real time — it sits inline in the network path. A load '
                  'balancer distributes incoming traffic across multiple servers to prevent '
                  'overload and provide redundancy. These devices all appear in the Network+ '
                  "exam's security and infrastructure domains.",
         'questions': [('What is the difference between an IDS and an IPS?',
                        'IDS detects and alerts (passive); IPS detects and blocks (active, '
                        'inline)'),
                       ('What makes a stateful firewall different from a simple packet filter?',
                        'A stateful firewall tracks connection state so it can distinguish '
                        'established traffic from new unsolicited connections'),
                       ('What does a load balancer do?',
                        'Distributes incoming connections across multiple servers to balance load '
                        'and provide redundancy')],
         'terms': [('Firewall',
                    'Filters network traffic based on rules; blocks unauthorised access'),
                   ('Stateful Firewall',
                    'Tracks connection state; knows if traffic is part of an established session'),
                   ('IDS',
                    'Intrusion Detection System — monitors and alerts on suspicious traffic; '
                    'passive'),
                   ('IPS',
                    'Intrusion Prevention System — monitors and actively blocks threats; inline'),
                   ('Load Balancer',
                    'Distributes traffic across multiple servers for performance and redundancy')]},
 '5-2': {'links': [('Cloudflare — TLS Explained',
                    'https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/'),
                   ('Cloudflare — What is a VPN?',
                    'https://www.cloudflare.com/learning/access-management/what-is-a-vpn/'),
                   ('Professor Messer — Network+ Course (Free)',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/')],
                  'diagram': '<svg width="100%" viewBox="0 0 680 400" xmlns="http://www.w3.org/2000/svg"><defs><style>.th{font-family:Arial,sans-serif;font-size:13px;font-weight:700;}.ts{font-family:Arial,sans-serif;font-size:11px;}.tt{font-family:JetBrains Mono,monospace;font-size:11px;fill:#00d4ff;letter-spacing:2px;}</style><marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs><text class="tt" x="340" y="22" text-anchor="middle">VPNs - IPsec AND SSL/TLS</text><text class="th" x="340" y="48" text-anchor="middle" fill="#fac775">Site-to-site IPsec VPN</text><rect x="30" y="58" width="130" height="70" rx="6" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="th" x="95" y="80" text-anchor="middle" fill="#fff">Site A</text><text class="ts" x="95" y="96" text-anchor="middle" fill="#e2e8f0">10.0.1.0/24</text><text class="ts" x="95" y="112" text-anchor="middle" fill="#e2e8f0">VPN gateway</text><text class="ts" x="95" y="124" text-anchor="middle" fill="#e2e8f0">203.0.113.1</text><rect x="520" y="58" width="130" height="70" rx="6" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="585" y="80" text-anchor="middle" fill="#fff">Site B</text><text class="ts" x="585" y="96" text-anchor="middle" fill="#e2e8f0">10.0.2.0/24</text><text class="ts" x="585" y="112" text-anchor="middle" fill="#e2e8f0">VPN gateway</text><text class="ts" x="585" y="124" text-anchor="middle" fill="#e2e8f0">203.0.113.2</text><rect x="160" y="75" width="360" height="36" rx="18" fill="#534ab7" stroke="#7f77dd" stroke-width="1.5"/><text class="th" x="340" y="97" text-anchor="middle" fill="#fff">Encrypted IPsec tunnel over internet</text><text class="ts" x="340" y="130" text-anchor="middle" fill="#64748b">ESP encapsulates original packet - outer header has public IPs, inner has private IPs</text><line x1="40" y1="150" x2="640" y2="150" stroke="#1e293b" stroke-width="0.5"/><text class="th" x="340" y="172" text-anchor="middle" fill="#6ee7b7">Remote access SSL/TLS VPN</text><rect x="30" y="184" width="110" height="60" rx="6" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="th" x="85" y="207" text-anchor="middle" fill="#fff">Remote user</text><text class="ts" x="85" y="223" text-anchor="middle" fill="#e2e8f0">Laptop/phone</text><text class="ts" x="85" y="237" text-anchor="middle" fill="#e2e8f0">Any internet</text><rect x="285" y="184" width="110" height="60" rx="6" fill="#ba7517" stroke="#fac775" stroke-width="1"/><text class="th" x="340" y="207" text-anchor="middle" fill="#fff">VPN gateway</text><text class="ts" x="340" y="223" text-anchor="middle" fill="#e2e8f0">SSL termination</text><text class="ts" x="340" y="237" text-anchor="middle" fill="#e2e8f0">Auth + tunnel</text><rect x="540" y="184" width="110" height="60" rx="6" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="595" y="207" text-anchor="middle" fill="#fff">Corp network</text><text class="ts" x="595" y="223" text-anchor="middle" fill="#e2e8f0">10.0.0.0/8</text><text class="ts" x="595" y="237" text-anchor="middle" fill="#e2e8f0">Internal resources</text><line x1="140" y1="214" x2="283" y2="214" stroke="#7f77dd" stroke-width="1.5" marker-end="url(#arr)"/><text class="ts" x="212" y="208" text-anchor="middle" fill="#7f77dd">HTTPS/443</text><line x1="395" y1="214" x2="538" y2="214" stroke="#00c853" stroke-width="1.5" marker-end="url(#arr)"/><line x1="40" y1="265" x2="640" y2="265" stroke="#1e293b" stroke-width="0.5"/><text class="tt" x="340" y="283" text-anchor="middle" style="font-size:10px;">IPsec vs SSL/TLS COMPARISON</text><rect x="40" y="293" width="290" height="88" rx="6" fill="#111827" stroke="#534ab7" stroke-width="1"/><text class="th" x="185" y="313" text-anchor="middle" fill="#7f77dd">IPsec</text><text class="ts" x="55" y="330" fill="#94a3b8">Layer 3 - tunnels entire IP packets</text><text class="ts" x="55" y="346" fill="#94a3b8">Site-to-site and remote access</text><text class="ts" x="55" y="362" fill="#94a3b8">Requires VPN client software</text><text class="ts" x="55" y="378" fill="#94a3b8">IKE negotiation + ESP encryption</text><rect x="350" y="293" width="290" height="88" rx="6" fill="#111827" stroke="#1d9e75" stroke-width="1"/><text class="th" x="495" y="313" text-anchor="middle" fill="#00c853">SSL/TLS VPN</text><text class="ts" x="365" y="330" fill="#94a3b8">Layer 4-7 - tunnels over HTTPS</text><text class="ts" x="365" y="346" fill="#94a3b8">Primarily remote access</text><text class="ts" x="365" y="362" fill="#94a3b8">Browser-based or thin client</text><text class="ts" x="365" y="378" fill="#94a3b8">Easier to deploy through firewalls</text></svg>',
'notes': 'Encryption protects data in transit from eavesdropping. TLS (Transport Layer '
                  'Security) is the current standard for encrypting web traffic — HTTPS is HTTP '
                  'over TLS. TLS uses a handshake to negotiate encryption algorithms and exchange '
                  'keys before data is transmitted. SSL is the predecessor to TLS and is now '
                  "deprecated and insecure — but the term 'SSL' is still commonly (incorrectly) "
                  'used to mean TLS.\n'
                  '\n'
                  'A VPN (Virtual Private Network) creates an encrypted tunnel across an untrusted '
                  'network (like the internet). Site-to-site VPNs connect entire offices. Client '
                  'VPNs let remote workers securely access company resources. IPsec is a suite of '
                  'protocols for encrypting IP traffic — used heavily in VPNs. It operates in '
                  'tunnel mode (encrypts the entire packet) or transport mode (encrypts just the '
                  'payload). OpenVPN and WireGuard are popular open-source VPN protocols.',
         'questions': [('What is the difference between SSL and TLS?',
                        'SSL is deprecated and insecure; TLS is its secure successor. Most '
                        "references to 'SSL' today actually mean TLS"),
                       ('What port does HTTPS use?', '443'),
                       ('What is the difference between site-to-site and client VPN?',
                        'Site-to-site connects two networks permanently; client VPN connects an '
                        "individual user's device to a network")],
         'terms': [('TLS', 'Transport Layer Security — encrypts data in transit; successor to SSL'),
                   ('HTTPS', 'HTTP over TLS — encrypted web browsing on port 443'),
                   ('VPN', 'Virtual Private Network — encrypted tunnel over an untrusted network'),
                   ('IPsec',
                    'IP Security — suite of protocols for encrypting IP traffic, used in VPNs'),
                   ('Tunnel Mode',
                    'IPsec mode that encrypts the entire IP packet including headers'),
                   ('SSL',
                    'Secure Sockets Layer — deprecated predecessor to TLS; no longer secure')]},
 '5-3': {'links': [('Cloudflare — DDoS Explained',
                    'https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/'),
                   ('Cloudflare — What is a MITM Attack?',
                    'https://www.cloudflare.com/learning/security/threats/man-in-the-middle-attack/'),
                   ('Professor Messer — Network+ Course (Free)',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/')],
         'notes': 'Common network attacks you must know for Network+: A Man-in-the-Middle (MITM) '
                  'attack intercepts communication between two parties — the attacker secretly '
                  'relays and potentially alters messages. ARP Spoofing/Poisoning sends fake ARP '
                  "replies to associate the attacker's MAC with a legitimate IP, enabling MITM on "
                  'local networks. A DoS (Denial of Service) attack floods a target with traffic '
                  'to overwhelm it; a DDoS uses many compromised systems simultaneously.\n'
                  '\n'
                  'Other attacks: VLAN Hopping allows an attacker to send traffic to a different '
                  'VLAN by exploiting trunk ports. DNS Spoofing/Poisoning inserts false DNS '
                  'records to redirect users to malicious sites. A Rogue DHCP server gives clients '
                  'incorrect network configuration. Recognising these attacks and knowing their '
                  'mitigations is a significant portion of the Network+ security domain.',
         'questions': [('How does ARP spoofing enable a MITM attack?',
                        'The attacker sends fake ARP replies mapping their MAC to a legitimate IP, '
                        'so traffic intended for that IP goes to the attacker instead'),
                       ('What is the difference between DoS and DDoS?',
                        'DoS is from one source; DDoS uses many compromised systems (botnet) to '
                        'overwhelm the target'),
                       ('What mitigation prevents rogue DHCP servers?',
                        'DHCP snooping on switches — only trusted ports can send DHCP offers')],
         'terms': [('MITM',
                    'Man-in-the-Middle — attacker intercepts communication between two parties'),
                   ('ARP Spoofing',
                    "Sending fake ARP replies to associate attacker's MAC with a legitimate IP"),
                   ('DoS', 'Denial of Service — flooding a target to make it unavailable'),
                   ('DDoS', 'Distributed DoS — DoS using many compromised systems simultaneously'),
                   ('VLAN Hopping',
                    'Exploiting trunk port configuration to send traffic to another VLAN'),
                   ('Rogue DHCP',
                    'Unauthorised DHCP server giving clients incorrect network configuration')]},
 '5-4': {'links': [('Professor Messer — Network+ Course (Free)',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                   ('Cloudflare — What is 802.1X?',
                    'https://www.cloudflare.com/learning/access-management/what-is-802.1x/'),
                   ('ExamCompass — Free Network+ Practice',
                    'https://www.comptia.org/training/certmaster-practice/network')],
         'notes': 'Authentication protocols verify the identity of users and devices trying to '
                  'access a network. RADIUS (Remote Authentication Dial-In User Service) is a '
                  'centralised AAA (Authentication, Authorisation, Accounting) protocol. When a '
                  'user tries to connect to a network, the authenticator (e.g. a switch or VPN '
                  'server) forwards credentials to the RADIUS server, which approves or denies '
                  'access. RADIUS uses UDP ports 1812/1813.\n'
                  '\n'
                  'TACACS+ (Terminal Access Controller Access-Control System Plus) is a Cisco '
                  'proprietary AAA protocol that encrypts the entire payload (RADIUS only encrypts '
                  'the password). TACACS+ uses TCP port 49 and separates authentication, '
                  'authorisation, and accounting into separate functions. RADIUS is typically used '
                  'for network access (Wi-Fi, VPN); TACACS+ is used for device administration '
                  '(router/switch login). 802.1X is a port-based access control standard that uses '
                  "RADIUS for authenticating devices before they're allowed network access.",
         'questions': [('What ports does RADIUS use?',
                        'UDP 1812 (authentication) and 1813 (accounting)'),
                       ('What is the key security difference between RADIUS and TACACS+?',
                        'TACACS+ encrypts the entire packet; RADIUS only encrypts the password'),
                       ('What does AAA stand for?', 'Authentication, Authorisation, Accounting'),
                       ('What protocol is used with 802.1X?', 'RADIUS')],
         'terms': [('RADIUS',
                    'Remote Authentication Dial-In User Service — centralised AAA; UDP 1812/1813'),
                   ('TACACS+', 'Cisco AAA protocol; encrypts full payload; TCP port 49'),
                   ('AAA',
                    'Authentication (who are you?), Authorisation (what can you do?), Accounting '
                    '(what did you do?)'),
                   ('802.1X',
                    'Port-based network access control; uses RADIUS to authenticate devices before '
                    'network access'),
                   ('Authenticator',
                    'The device (switch, AP) that forwards credentials to the RADIUS server')]},
 '5-5': {'links': [('Professor Messer — Free Practice Exams',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                   ('ExamCompass — Free Network+ Quizzes',
                    'https://www.comptia.org/training/certmaster-practice/network'),
                   ('CompTIA Network+ Exam Objectives (Free PDF)',
                    'https://www.comptia.org/training/resources/exam-objectives')],
         'notes': 'This is a review quiz for Module 6 — Network Security. Security is one of the '
                  'most heavily weighted domains on the Network+ exam. Make sure you can identify '
                  'attack types, explain mitigation strategies, distinguish encryption protocols, '
                  'and understand authentication frameworks.\n'
                  '\n'
                  'Key areas to be solid on: port numbers for security protocols (SSH=22, '
                  'HTTPS=443, RADIUS=1812), the difference between IDS and IPS, WPA2 vs WPA3, '
                  'RADIUS vs TACACS+, and common network attacks with their mitigations.',
         'questions': [('What port does SSH use?', '22'),
                       ('Why is Telnet insecure?',
                        'Telnet transmits data including passwords in plaintext — anyone on the '
                        'network can intercept it'),
                       ('What is the difference between IDS and IPS?',
                        'IDS detects and alerts (passive); IPS detects and blocks (active/inline)'),
                       ('Which wireless security protocol should be used on enterprise networks?',
                        'WPA2-Enterprise or WPA3-Enterprise with 802.1X authentication'),
                       ('What does DHCP snooping prevent?',
                        'Rogue DHCP servers — only trusted ports can send DHCP offers')],
         'terms': [('SSH',
                    'Secure Shell — encrypted remote access; port 22; replacement for Telnet'),
                   ('Telnet',
                    'Unencrypted remote access; port 23; never use on production networks'),
                   ('SNMP',
                    'Simple Network Management Protocol — network monitoring; port 161 (UDP)'),
                   ('Syslog', 'Standard for sending log messages; UDP port 514')]},
 '6-2': {'links': [('Wi-Fi Alliance — Security Overview',
                    'https://www.wi-fi.org/discover-wi-fi/security'),
                   ('Cloudflare — WPA3 Explained',
                    'https://www.cloudflare.com/learning/network-layer/what-is-wpa3/'),
                   ('Professor Messer — Network+ Course (Free)',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/')],
         'notes': 'Wireless security has evolved significantly. WEP (Wired Equivalent Privacy) was '
                  'the original standard but is completely broken and should never be used. WPA '
                  '(Wi-Fi Protected Access) improved on WEP but also has vulnerabilities. WPA2 '
                  'uses AES encryption and is the current standard for home and business networks '
                  '— WPA2-Personal uses a pre-shared key (PSK); WPA2-Enterprise uses 802.1X with '
                  'RADIUS for per-user authentication.\n'
                  '\n'
                  'WPA3 is the latest standard with stronger encryption and protection against '
                  'offline dictionary attacks. It uses SAE (Simultaneous Authentication of Equals) '
                  'instead of PSK. For enterprise networks, WPA2/WPA3-Enterprise with 802.1X is '
                  'the gold standard — each user authenticates individually and a compromised '
                  'password only affects one account. Common wireless attacks include evil twin '
                  '(rogue AP), deauth attacks, and WPS brute-forcing (disable WPS on all '
                  'networks).',
         'questions': [('Why should WEP never be used?',
                        "WEP's encryption is completely broken and can be cracked in minutes with "
                        'freely available tools'),
                       ('What is the difference between WPA2-Personal and WPA2-Enterprise?',
                        'Personal uses a shared passphrase; Enterprise uses 802.1X with individual '
                        'user credentials via RADIUS'),
                       ("What attack does WPA3 protect against that WPA2 doesn't?",
                        "Offline dictionary attacks — WPA3's SAE handshake doesn't allow captured "
                        'handshakes to be brute-forced offline')],
         'terms': [('WEP',
                    'Wired Equivalent Privacy — original wireless security; completely broken; '
                    'never use'),
                   ('WPA2-Personal',
                    'Uses a pre-shared key (PSK/passphrase); suitable for home networks'),
                   ('WPA2-Enterprise',
                    'Uses 802.1X and RADIUS for individual user authentication; business standard'),
                   ('WPA3',
                    'Latest Wi-Fi security standard; SAE handshake; resistant to offline attacks'),
                   ('Evil Twin',
                    'Rogue access point mimicking a legitimate one to capture traffic'),
                   ('SAE',
                    'Simultaneous Authentication of Equals — WPA3 handshake replacing PSK')]},
 '6-5': {'links': [('Professor Messer — Free Practice Exams',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                   ('ExamCompass — Free Network+ Quizzes',
                    'https://www.comptia.org/training/certmaster-practice/network'),
                   ('CompTIA Network+ Exam Objectives (Free PDF)',
                    'https://www.comptia.org/training/resources/exam-objectives')],
         'notes': 'This is a review quiz for Module 6 — Network Security. Security is one of the '
                  'most heavily weighted domains on the Network+ exam. Make sure you can identify '
                  'attack types, explain mitigation strategies, distinguish encryption protocols, '
                  'and understand authentication frameworks.\n'
                  '\n'
                  'Key areas to be solid on: port numbers for security protocols (SSH=22, '
                  'HTTPS=443, RADIUS=1812), the difference between IDS and IPS, WPA2 vs WPA3, '
                  'RADIUS vs TACACS+, and common network attacks with their mitigations.',
         'questions': [('What port does SSH use?', '22'),
                       ('Why is Telnet insecure?',
                        'Telnet transmits data including passwords in plaintext — anyone on the '
                        'network can intercept it'),
                       ('What is the difference between IDS and IPS?',
                        'IDS detects and alerts (passive); IPS detects and blocks (active/inline)'),
                       ('Which wireless security protocol should be used on enterprise networks?',
                        'WPA2-Enterprise or WPA3-Enterprise with 802.1X authentication'),
                       ('What does DHCP snooping prevent?',
                        'Rogue DHCP servers — only trusted ports can send DHCP offers')],
         'terms': [('SSH',
                    'Secure Shell — encrypted remote access; port 22; replacement for Telnet'),
                   ('Telnet',
                    'Unencrypted remote access; port 23; never use on production networks'),
                   ('SNMP',
                    'Simple Network Management Protocol — network monitoring; port 161 (UDP)'),
                   ('Syslog', 'Standard for sending log messages; UDP port 514')]},
 '7-1': {'links': [('Professor Messer — Network+ Course (Free)',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                   ('CompTIA Network+ Exam Objectives (Free PDF)',
                    'https://www.comptia.org/training/resources/exam-objectives'),
                   ('ExamCompass — Free Network+ Practice',
                    'https://www.comptia.org/training/certmaster-practice/network')],
         'notes': "CompTIA's official troubleshooting methodology has seven steps: 1) Identify the "
                  'problem — gather information and symptoms. 2) Establish a theory of probable '
                  'cause — what do you think is wrong? 3) Test the theory — confirm or deny your '
                  'hypothesis. 4) Establish a plan of action — how will you fix it with minimal '
                  'disruption? 5) Implement the solution — make the change. 6) Verify full '
                  'functionality — confirm the fix worked and nothing else broke. 7) Document '
                  'findings — record what happened and how you fixed it.\n'
                  '\n'
                  'In practice, experienced engineers often jump to step 2 based on intuition — '
                  'but the methodology exists to avoid missing obvious causes. Always start at '
                  'Layer 1 (is the cable plugged in?) and work up. The OSI model is your '
                  'troubleshooting map: Physical → Data Link → Network → Transport → Application.',
         'questions': [("What is the first step in CompTIA's troubleshooting methodology?",
                        'Identify the problem — gather information, question users, observe '
                        'symptoms'),
                       ('Why is documentation the final step?',
                        'To create a record for future reference, track recurring issues, and help '
                        'other engineers'),
                       ('If a user can ping by IP but not by name, which layer/service is the '
                        'problem?',
                        'DNS — name resolution failure (application layer service)')],
         'terms': [('Troubleshooting Methodology',
                    "CompTIA's 7-step process: Identify, Theory, Test, Plan, Implement, Verify, "
                    'Document'),
                   ('Bottom-Up Approach',
                    'Start troubleshooting at Layer 1 (physical) and work up through OSI layers'),
                   ('Top-Down Approach',
                    'Start at Layer 7 (application) and work down — used when software issues are '
                    'suspected'),
                   ('Divide and Conquer',
                    'Start at Layer 3 (network) and work up or down based on test results'),
                   ('Documentation',
                    'Recording the problem, cause, and solution — essential for future '
                    'reference')]},
 '7-2': {'links': [('SS64 — Windows Command Reference', 'https://ss64.com/nt/'),
                   ('SS64 — Linux Command Reference', 'https://ss64.com/bash/'),
                   ('MXToolbox — Network Tools', 'https://mxtoolbox.com/NetworkTools.aspx')],
         'notes': 'Essential CLI tools for every network engineer. ping tests basic connectivity — '
                  'if it fails, work down the OSI model. tracert (Windows) / traceroute (Linux) '
                  'shows the path to a destination and identifies where failures or latency occur. '
                  'netstat shows active connections, listening ports, and network statistics — '
                  "useful for finding what's using a port or how many connections exist. arp -a "
                  'shows the ARP cache; arp -d clears it.\n'
                  '\n'
                  'route print (Windows) / ip route (Linux) shows the routing table — essential '
                  'for diagnosing routing issues. nslookup and dig diagnose DNS. netstat -an shows '
                  'all connections and listening ports numerically. On Cisco devices: show ip '
                  'interface brief, show ip route, show mac address-table, show vlan brief, and '
                  'show running-config are the essential show commands. Practice all of these '
                  "until they're instinctive.",
         'questions': [('A user can ping 8.8.8.8 but not google.com. What is likely wrong?',
                        'DNS resolution is failing — the IP stack works but name resolution '
                        "doesn't"),
                       ('What command shows which ports are listening on a Windows machine?',
                        'netstat -an'),
                       ('What does traceroute help you identify?',
                        'The path packets take and where failures or high latency occur along the '
                        'route')],
         'terms': [('ping', 'Tests ICMP reachability; measures round-trip time'),
                   ('tracert/traceroute', 'Maps the path to a destination hop by hop'),
                   ('netstat', 'Shows active connections and listening ports'),
                   ('netstat -an',
                    'Shows all connections and ports numerically (no DNS resolution)'),
                   ('route print', 'Shows the Windows routing table (ip route on Linux)'),
                   ('arp -a', 'Displays the ARP cache — IP to MAC address mappings')]},
 '7-3': {'links': [('draw.io — Free Network Diagram Tool', 'https://app.diagrams.net'),
                   ('Lucidchart — Network Diagram Tool',
                    'https://www.lucidchart.com/pages/network-diagram'),
                   ('Packet Tracer — Free Cisco Network Simulator',
                    'https://www.netacad.com/courses/packet-tracer')],
                  'diagram': '<svg width="100%" viewBox="0 0 680 440" xmlns="http://www.w3.org/2000/svg"><defs><style>.th{font-family:Arial,sans-serif;font-size:12px;font-weight:700;}.ts{font-family:Arial,sans-serif;font-size:10px;}.tt{font-family:JetBrains Mono,monospace;font-size:11px;fill:#00d4ff;letter-spacing:2px;}</style><marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs><text class="tt" x="340" y="22" text-anchor="middle">SAMPLE LOGICAL NETWORK DIAGRAM</text><text class="ts" x="340" y="38" text-anchor="middle" fill="#64748b">Inline IPS in traffic path - IDS/DDI passive via SPAN from core switch</text><ellipse cx="50" cy="110" rx="38" ry="24" fill="#1e293b" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3 2"/><text class="ts" x="50" y="114" text-anchor="middle" fill="#94a3b8">Internet</text><line x1="88" y1="110" x2="112" y2="110" stroke="#94a3b8" stroke-width="1.5"/><rect x="114" y="94" width="56" height="32" rx="2" fill="none" stroke="#ef4444" stroke-width="1.5"/><line x1="114" y1="103" x2="170" y2="103" stroke="#ef4444" stroke-width="0.8"/><line x1="114" y1="110" x2="170" y2="110" stroke="#ef4444" stroke-width="0.8"/><line x1="114" y1="117" x2="170" y2="117" stroke="#ef4444" stroke-width="0.8"/><rect x="122" y="94" width="7" height="9" rx="1" fill="#ef4444"/><rect x="135" y="94" width="7" height="9" rx="1" fill="#ef4444"/><rect x="148" y="94" width="7" height="9" rx="1" fill="#ef4444"/><rect x="122" y="117" width="7" height="9" rx="1" fill="#ef4444"/><rect x="135" y="117" width="7" height="9" rx="1" fill="#ef4444"/><rect x="148" y="117" width="7" height="9" rx="1" fill="#ef4444"/><text class="ts" x="142" y="140" text-anchor="middle" fill="#f87171">Perimeter FW</text><line x1="170" y1="110" x2="196" y2="110" stroke="#94a3b8" stroke-width="1.5"/><rect x="198" y="94" width="66" height="32" rx="6" fill="#534ab7" stroke="#7f77dd" stroke-width="1.5"/><text class="th" x="231" y="112" text-anchor="middle" fill="#fff">IPS</text><text class="ts" x="231" y="122" text-anchor="middle" fill="#ddd">Inline</text><text class="ts" x="231" y="140" text-anchor="middle" fill="#7f77dd">TippingPoint</text><line x1="264" y1="110" x2="292" y2="110" stroke="#94a3b8" stroke-width="1.5"/><circle cx="312" cy="110" r="20" fill="none" stroke="#ba7517" stroke-width="1.5"/><line x1="292" y1="110" x2="332" y2="110" stroke="#ba7517" stroke-width="1"/><line x1="312" y1="90" x2="312" y2="130" stroke="#ba7517" stroke-width="1"/><path d="M298 100 L312 90 L326 100" fill="none" stroke="#ba7517" stroke-width="1"/><path d="M326 120 L312 130 L298 120" fill="none" stroke="#ba7517" stroke-width="1"/><text class="ts" x="312" y="148" text-anchor="middle" fill="#e2e8f0">RTR-01</text><line x1="332" y1="110" x2="358" y2="110" stroke="#94a3b8" stroke-width="1.5"/><rect x="360" y="90" width="90" height="40" rx="4" fill="#185fa5" stroke="#00b4d8" stroke-width="2"/><line x1="375" y1="102" x2="375" y2="118" stroke="#00b4d8" stroke-width="1"/><line x1="388" y1="98" x2="388" y2="122" stroke="#00b4d8" stroke-width="1"/><line x1="401" y1="102" x2="401" y2="118" stroke="#00b4d8" stroke-width="1"/><line x1="414" y1="98" x2="414" y2="122" stroke="#00b4d8" stroke-width="1"/><line x1="427" y1="102" x2="427" y2="118" stroke="#00b4d8" stroke-width="1"/><line x1="368" y1="110" x2="442" y2="110" stroke="#00b4d8" stroke-width="1.5"/><text class="ts" x="405" y="146" text-anchor="middle" fill="#e2e8f0">SW-CORE</text><line x1="450" y1="110" x2="510" y2="110" stroke="#00c853" stroke-width="1.5" stroke-dasharray="5 3" marker-end="url(#arr)"/><text class="ts" x="480" y="104" text-anchor="middle" fill="#00c853">SPAN</text><rect x="512" y="94" width="78" height="32" rx="6" fill="#1d9e75" stroke="#00c853" stroke-width="1.5"/><text class="th" x="551" y="112" text-anchor="middle" fill="#fff">IDS / DDI</text><text class="ts" x="551" y="122" text-anchor="middle" fill="#e2e8f0">Out-of-band</text><text class="ts" x="551" y="146" text-anchor="middle" fill="#64748b">Passive - detect only</text><line x1="390" y1="130" x2="310" y2="200" stroke="#94a3b8" stroke-width="1"/><line x1="405" y1="130" x2="510" y2="200" stroke="#94a3b8" stroke-width="1"/><rect x="260" y="202" width="80" height="28" rx="4" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="ts" x="300" y="220" text-anchor="middle" fill="#fff">SW-A1</text><text class="ts" x="300" y="244" text-anchor="middle" fill="#64748b">VLAN 10 - Users</text><text class="ts" x="300" y="256" text-anchor="middle" fill="#64748b">192.168.10.0/24</text><rect x="460" y="202" width="80" height="28" rx="4" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="ts" x="500" y="220" text-anchor="middle" fill="#fff">SW-A2</text><text class="ts" x="500" y="244" text-anchor="middle" fill="#64748b">VLAN 20 - Servers</text><text class="ts" x="500" y="256" text-anchor="middle" fill="#64748b">192.168.20.0/24</text><line x1="290" y1="230" x2="255" y2="278" stroke="#94a3b8" stroke-width="0.8"/><line x1="310" y1="230" x2="345" y2="278" stroke="#94a3b8" stroke-width="0.8"/><rect x="220" y="280" width="60" height="22" rx="3" fill="#475569" stroke="#94a3b8" stroke-width="0.5"/><text class="ts" x="250" y="295" text-anchor="middle" fill="#e2e8f0">PC-01</text><rect x="315" y="280" width="60" height="22" rx="3" fill="#475569" stroke="#94a3b8" stroke-width="0.5"/><text class="ts" x="345" y="295" text-anchor="middle" fill="#e2e8f0">PC-02</text><line x1="490" y1="230" x2="455" y2="278" stroke="#94a3b8" stroke-width="0.8"/><line x1="510" y1="230" x2="545" y2="278" stroke="#94a3b8" stroke-width="0.8"/><rect x="420" y="280" width="60" height="22" rx="3" fill="#1d9e75" stroke="#00c853" stroke-width="0.5"/><text class="ts" x="450" y="295" text-anchor="middle" fill="#fff">SRV-01</text><rect x="515" y="280" width="60" height="22" rx="3" fill="#1d9e75" stroke="#00c853" stroke-width="0.5"/><text class="ts" x="545" y="295" text-anchor="middle" fill="#fff">SRV-02</text><rect x="40" y="322" width="600" height="96" rx="8" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="th" x="340" y="340" text-anchor="middle" fill="#00d4ff">Key design points</text><text class="ts" x="60" y="358" fill="#7f77dd">IPS (inline)</text><text class="ts" x="130" y="358" fill="#94a3b8">- sits in the traffic path between FW and router, can block threats in real time</text><text class="ts" x="60" y="374" fill="#00c853">IDS/DDI (out-of-band)</text><text class="ts" x="190" y="374" fill="#94a3b8">- receives mirrored traffic via SPAN port from SW-CORE, passively detects</text><text class="ts" x="60" y="390" fill="#94a3b8">Dashed green line = SPAN mirror - copy of all traffic, no impact on forwarding</text><text class="ts" x="60" y="406" fill="#94a3b8">Solid lines = data path  |  Labels show VLAN and subnet per segment</text></svg>',
'notes': 'Network diagrams visually represent the layout of a network. A physical diagram '
                  'shows actual hardware locations, cable runs, and rack layouts. A logical '
                  'diagram shows IP addressing, VLANs, routing, and how traffic flows — regardless '
                  'of physical location. Both types appear in Network+ performance-based '
                  'questions.\n'
                  '\n'
                  'Standard symbols: clouds represent the internet or an ISP, cylinders represent '
                  'servers, rectangles are switches, the routing symbol is a circle with arrows, '
                  'firewalls are represented by brick wall icons (varies by tool). Cisco uses '
                  'specific icons for its devices. Being able to read and draw network diagrams is '
                  'essential for planning, documentation, and troubleshooting. Tools like draw.io '
                  '(free) or Lucidchart are commonly used.',
         'questions': [('What is the difference between a physical and logical network diagram?',
                        'Physical shows actual hardware and cables; logical shows IP addressing '
                        'and traffic flow'),
                       ('Why are network diagrams important for troubleshooting?',
                        'They provide a reference for understanding how the network is connected, '
                        'making it faster to identify where a failure might be')],
         'terms': [('Physical Diagram', 'Shows actual hardware, locations, and cable connections'),
                   ('Logical Diagram',
                    'Shows IP addressing, VLANs, and traffic flow regardless of physical layout'),
                   ('Network Topology', 'The arrangement of network components shown in a diagram'),
                   ('Rack Diagram',
                    'Shows equipment installed in server racks with U-space measurements'),
                   ('draw.io', 'Free online tool for creating network diagrams')]},
 '7-4': {'links': [('Professor Messer — Network+ Course (Free)',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                   ('ExamCompass — Free Network+ Practice',
                    'https://www.comptia.org/training/certmaster-practice/network'),
                   ('Packet Tracer — Free Cisco Network Simulator',
                    'https://www.netacad.com/courses/packet-tracer')],
         'notes': 'Troubleshooting scenarios test your ability to apply methodology and tools to '
                  'realistic problems. Common scenarios: 1) Duplicate IP address — two devices '
                  'share an IP; symptoms are intermittent connectivity for both. Fix: use arp -a '
                  "to find the conflict, assign a unique IP. 2) Wrong subnet mask — device can't "
                  'reach some hosts but not others. Fix: ipconfig /all to verify mask. 3) Default '
                  'gateway missing — device can reach local network but not the internet. Fix: '
                  'verify gateway config. 4) DNS failure — can ping IPs but not names. Fix: '
                  'nslookup to test, check DNS server assignment.\n'
                  '\n'
                  '5) Switching loop — broadcast storm, all ports at 100%, network unusable. Fix: '
                  'STP should prevent this; check for disabled STP or non-managed switches. 6) '
                  "VLAN mismatch — devices on the wrong VLAN can't communicate. Fix: verify "
                  "switchport access vlan on Cisco. Practice recognising these patterns — they're "
                  'exactly what appears in Network+ performance-based questions.',
         'questions': [('A device gets a 169.254.x.x address. What does this indicate?',
                        'APIPA — the device failed to get a DHCP lease; check DHCP server and '
                        'connectivity'),
                       ('A user can reach local servers but not the internet. What should you '
                        'check first?',
                        'The default gateway — it may be missing, wrong, or the router may be '
                        'down'),
                       ('What protocol prevents switching loops?',
                        'STP — Spanning Tree Protocol (or RSTP, the faster version)')],
         'terms': [('Duplicate IP',
                    'Two devices with the same IP; causes intermittent connectivity for both'),
                   ('Broadcast Storm',
                    'Network flooding caused by a switching loop; STP prevents this'),
                   ('STP',
                    'Spanning Tree Protocol — prevents switching loops by blocking redundant '
                    'paths'),
                   ('APIPA',
                    '169.254.x.x — automatic address assigned when DHCP fails; indicates DHCP '
                    'problem'),
                   ('Default Gateway',
                    'Missing or wrong gateway = can reach local network but not internet')]},
 '8-5': {'links': [('Professor Messer — Free Practice Exams',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                   ('ExamCompass — Free Network+ Quizzes',
                    'https://www.comptia.org/training/certmaster-practice/network'),
                   ('CompTIA CertMaster Practice (Official)',
                    'https://www.comptia.org/training/certmaster-practice/network')],
         'notes': 'This is your full timed practice exam. Set a timer for 90 minutes and attempt '
                  'all questions without looking anything up. Treat it exactly like the real exam. '
                  'When you finish, review every wrong answer — not just the right answer, but why '
                  'the other options were wrong. This is how you learn the most.\n'
                  '\n'
                  'After the practice exam, identify your weak domains and return to those '
                  'modules. Aim for 80%+ on practice exams before sitting the real thing. '
                  "Professor Messer's practice exams and ExamCompass are excellent free resources. "
                  "Jason Dion's Udemy course includes high-quality practice exams. Remember: the "
                  'real exam has scenario-based questions that test application, not just '
                  'memorisation.',
         'questions': [('What score should you aim for on practice exams before sitting the real '
                        'test?',
                        '80% or higher consistently across multiple practice exams'),
                       ('What should you do after reviewing wrong answers?',
                        'Understand WHY each wrong answer was wrong, not just what the right '
                        'answer is — this prevents the same mistake twice')],
         'terms': [('Process of Elimination',
                    'On tricky questions, eliminate obviously wrong answers first to improve odds'),
                   ('Keyword Analysis',
                    "Read questions carefully for words like 'MOST', 'BEST', 'LEAST', 'NOT' — they "
                    'change the answer'),
                   ('Flag and Return',
                    "Flag uncertain questions and return to them — don't spend too long on any "
                    'single question')]},
 '3-2': {         'diagram': '<svg width="100%" viewBox="0 0 680 340" xmlns="http://www.w3.org/2000/svg"><defs><style>.th{font-family:Arial,sans-serif;font-size:13px;font-weight:700;}.ts{font-family:Arial,sans-serif;font-size:11px;}.tt{font-family:JetBrains Mono,monospace;font-size:11px;fill:#00d4ff;letter-spacing:2px;}</style></defs><text class="tt" x="340" y="22" text-anchor="middle">STATIC vs DYNAMIC ROUTING</text><line x1="340" y1="35" x2="340" y2="310" stroke="#1e293b" stroke-width="1"/><text class="th" x="170" y="50" text-anchor="middle" fill="#fac775">Static Routing</text><rect x="30" y="62" width="290" height="220" rx="8" fill="#111827" stroke="#ba7517" stroke-width="1"/><rect x="50" y="80" width="70" height="36" rx="6" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="th" x="85" y="102" text-anchor="middle" fill="#fff">R1</text><rect x="230" y="80" width="70" height="36" rx="6" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="th" x="265" y="102" text-anchor="middle" fill="#fff">R2</text><line x1="120" y1="98" x2="228" y2="98" stroke="#ba7517" stroke-width="2"/><text class="ts" x="175" y="92" text-anchor="middle" fill="#fac775">fixed path</text><text class="ts" x="85" y="138" text-anchor="middle" fill="#64748b">ip route 192.168.2.0</text><text class="ts" x="85" y="152" text-anchor="middle" fill="#64748b">255.255.255.0 10.0.0.2</text><rect x="50" y="168" width="250" height="96" rx="6" fill="#0a0f1e" stroke="#1e293b" stroke-width="1"/><text class="ts" x="175" y="185" text-anchor="middle" fill="#00c853">+ Predictable, low overhead</text><text class="ts" x="175" y="200" text-anchor="middle" fill="#00c853">+ Good for small networks</text><text class="ts" x="175" y="215" text-anchor="middle" fill="#00c853">+ No routing protocol needed</text><text class="ts" x="175" y="232" text-anchor="middle" fill="#ef4444">- Manual config, no failover</text><text class="ts" x="175" y="247" text-anchor="middle" fill="#ef4444">- Does not adapt to failures</text><text class="th" x="510" y="50" text-anchor="middle" fill="#6ee7b7">Dynamic Routing</text><rect x="360" y="62" width="290" height="220" rx="8" fill="#111827" stroke="#1d9e75" stroke-width="1"/><rect x="375" y="80" width="60" height="36" rx="6" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="405" y="102" text-anchor="middle" fill="#fff">R1</text><rect x="590" y="80" width="60" height="36" rx="6" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="620" y="102" text-anchor="middle" fill="#fff">R3</text><rect x="480" y="80" width="60" height="36" rx="6" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="510" y="102" text-anchor="middle" fill="#fff">R2</text><line x1="435" y1="98" x2="478" y2="98" stroke="#00c853" stroke-width="1.5"/><line x1="540" y1="98" x2="588" y2="98" stroke="#00c853" stroke-width="1.5"/><line x1="435" y1="108" x2="595" y2="130" stroke="#00c853" stroke-width="1" stroke-dasharray="3 2"/><text class="ts" x="510" y="148" text-anchor="middle" fill="#00c853">OSPF/BGP auto-learns</text><rect x="375" y="168" width="260" height="96" rx="6" fill="#0a0f1e" stroke="#1e293b" stroke-width="1"/><text class="ts" x="505" y="185" text-anchor="middle" fill="#00c853">+ Auto-discovers routes</text><text class="ts" x="505" y="200" text-anchor="middle" fill="#00c853">+ Adapts to failures</text><text class="ts" x="505" y="215" text-anchor="middle" fill="#00c853">+ Scales to large networks</text><text class="ts" x="505" y="232" text-anchor="middle" fill="#ef4444">- More CPU/bandwidth overhead</text><text class="ts" x="505" y="247" text-anchor="middle" fill="#ef4444">- More complex to configure</text><text class="ts" x="340" y="305" text-anchor="middle" fill="#64748b">Most networks use both - static for default routes and specific paths, dynamic for the rest</text></svg>',
'notes': 'Static routing means an administrator manually configures each route in the '
                  'routing table; the routes never change unless edited by hand. It is '
                  'predictable, uses no CPU or bandwidth for route exchange, and is ideal for '
                  'small or stub networks. Its weakness is scale: every topology change requires '
                  'manual updates, and there is no automatic failover. Dynamic routing uses '
                  'protocols (OSPF, EIGRP, RIP, BGP) so routers learn routes from each other and '
                  'recalculate paths automatically when links go up or down. Dynamic routing '
                  'scales well and self-heals, at the cost of CPU, memory, bandwidth, and added '
                  'complexity. Distance-vector protocols (RIP) choose paths by hop count; '
                  'link-state protocols (OSPF) build a full map of the network and run '
                  'shortest-path-first. A default route (0.0.0.0/0) is a special static route used '
                  'as a last resort when no more specific route matches.',
         'links': [('Cisco - Static vs Dynamic Routing',
                    'https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html'),
                   ('Cloudflare - What is Routing?',
                    'https://www.cloudflare.com/learning/network-layer/what-is-routing/'),
                   ('Professor Messer - Routing Technologies',
                    'https://www.professormesser.com/network-plus/n10-008/n10-008-training-course/')],
         'terms': [('Static route',
                    'A route manually entered by an administrator that does not change '
                    'automatically.'),
                   ('Dynamic route',
                    'A route learned and maintained automatically by a routing protocol.'),
                   ('Default route',
                    'The 0.0.0.0/0 route of last resort used when no more specific route matches.'),
                   ('Distance-vector',
                    'A protocol family (e.g. RIP) that selects routes based on hop count.'),
                   ('Link-state',
                    'A protocol family (e.g. OSPF) that builds a full topology map and runs SPF.'),
                   ('Administrative distance',
                    'A trust ranking used to choose between routes learned from different '
                    'sources.')],
         'questions': [('When is static routing usually preferred over dynamic routing?',
                        'On small, stable, or stub networks where routes rarely change and '
                        'predictability matters.'),
                       ('What is the main advantage of dynamic routing?',
                        'It learns routes automatically and reroutes around failures without '
                        'manual intervention.'),
                       ('What does a default route (0.0.0.0/0) do?',
                        'It forwards traffic that matches no more specific route, acting as the '
                        'route of last resort.'),
                       ('How does a distance-vector protocol differ from a link-state protocol?',
                        'Distance-vector picks paths by hop count; link-state builds a full '
                        'topology map and runs shortest-path-first.')]},
 '4-4': {'notes': 'A VLAN (Virtual LAN) logically segments a single physical switch into multiple '
                  'broadcast domains, so devices can be grouped by function instead of physical '
                  'location. Each VLAN is its own broadcast domain, which reduces broadcast '
                  'traffic and improves security by isolating groups (for example separating '
                  'staff, guests, and VoIP). An access port belongs to a single VLAN and connects '
                  'to an end device. A trunk port carries traffic for multiple VLANs between '
                  'switches and tags each frame using the 802.1Q standard, which inserts a 4-byte '
                  'tag containing the VLAN ID (12 bits, so 1-4094 usable). Devices in different '
                  'VLANs cannot talk directly; inter-VLAN routing through a router or a Layer 3 '
                  "switch (often a 'router on a stick' with subinterfaces) is required. The native "
                  'VLAN on a trunk carries untagged frames and should be changed from the default '
                  'VLAN 1 as a security best practice.',
         'links': [('Cisco - VLANs Explained',
                    'https://www.cisco.com/c/en/us/support/docs/lan-switching/vlan/10023-3.html'),
                   ('Cloudflare - What is a VLAN?',
                    'https://www.cloudflare.com/learning/network-layer/what-is-a-vlan/'),
                   ('Professor Messer - VLANs and Trunking',
                    'https://www.professormesser.com/network-plus/n10-008/n10-008-training-course/')],
         'terms': [('VLAN',
                    'A logical broadcast domain created on a switch to group devices independent '
                    'of location.'),
                   ('Access port',
                    'A switch port that belongs to a single VLAN and connects to an end device.'),
                   ('Trunk port',
                    'A switch port that carries multiple VLANs between switches, tagging frames '
                    'with 802.1Q.'),
                   ('802.1Q',
                    'The IEEE standard that tags Ethernet frames with a VLAN ID using a 4-byte '
                    'tag.'),
                   ('Native VLAN',
                    'The VLAN whose frames are sent untagged on a trunk; should be changed from '
                    'default VLAN 1.'),
                   ('Inter-VLAN routing',
                    'Routing traffic between VLANs using a router or a Layer 3 switch.')],
         'questions': [('Can two devices on different VLANs communicate without a router?',
                        'No - VLANs are separate broadcast domains; a router or Layer 3 switch is '
                        'required.'),
                       ('What is the difference between an access port and a trunk port?',
                        'A trunk port carries multiple VLANs (tagged with 802.1Q); an access port '
                        'carries a single VLAN.'),
                       ('What standard is used to tag frames on a trunk?',
                        '802.1Q, which inserts a 4-byte VLAN tag into the Ethernet frame.'),
                       ('Why segment a network into VLANs?',
                        'To reduce broadcast domains, improve performance, and isolate groups for '
                        'security.')]},
 '5-1': {         'diagram': '<svg width="100%" viewBox="0 0 680 360" xmlns="http://www.w3.org/2000/svg"><defs><style>.th{font-family:Arial,sans-serif;font-size:12px;font-weight:700;}.ts{font-family:Arial,sans-serif;font-size:10px;}.tt{font-family:JetBrains Mono,monospace;font-size:11px;fill:#00d4ff;letter-spacing:2px;}</style></defs><text class="tt" x="340" y="22" text-anchor="middle">FIREWALL TYPES AND PLACEMENT</text><rect x="20" y="140" width="80" height="44" rx="6" fill="#ef4444" stroke="#fca5a5" stroke-width="1"/><text class="th" x="60" y="160" text-anchor="middle" fill="#fff">Internet</text><text class="ts" x="60" y="176" text-anchor="middle" fill="#fee2e2">Untrusted</text><line x1="100" y1="162" x2="130" y2="162" stroke="#94a3b8" stroke-width="1.5"/><rect x="132" y="128" width="100" height="68" rx="6" fill="#ba7517" stroke="#fac775" stroke-width="1"/><text class="th" x="182" y="148" text-anchor="middle" fill="#fff">Perimeter FW</text><text class="ts" x="182" y="163" text-anchor="middle" fill="#e2e8f0">Stateful + NAT</text><text class="ts" x="182" y="176" text-anchor="middle" fill="#e2e8f0">Port filtering</text><text class="ts" x="182" y="189" text-anchor="middle" fill="#fac700">Zone 1</text><line x1="232" y1="162" x2="262" y2="162" stroke="#94a3b8" stroke-width="1.5"/><rect x="264" y="60" width="120" height="200" rx="6" fill="none" stroke="#00d4ff" stroke-width="1" stroke-dasharray="5 3"/><text class="ts" x="324" y="80" text-anchor="middle" fill="#00d4ff">DMZ</text><rect x="274" y="88" width="100" height="28" rx="4" fill="#475569" stroke="#94a3b8" stroke-width="0.5"/><text class="th" x="324" y="106" text-anchor="middle" fill="#fff">Web server</text><rect x="274" y="122" width="100" height="28" rx="4" fill="#475569" stroke="#94a3b8" stroke-width="0.5"/><text class="th" x="324" y="140" text-anchor="middle" fill="#fff">Mail server</text><rect x="274" y="156" width="100" height="28" rx="4" fill="#475569" stroke="#94a3b8" stroke-width="0.5"/><text class="th" x="324" y="174" text-anchor="middle" fill="#fff">DNS server</text><rect x="274" y="190" width="100" height="28" rx="4" fill="#475569" stroke="#94a3b8" stroke-width="0.5"/><text class="th" x="324" y="208" text-anchor="middle" fill="#fff">VPN gateway</text><line x1="384" y1="162" x2="414" y2="162" stroke="#94a3b8" stroke-width="1.5"/><rect x="416" y="128" width="110" height="68" rx="6" fill="#1d9e75" stroke="#00c853" stroke-width="1"/><text class="th" x="471" y="148" text-anchor="middle" fill="#fff">NGFW / IPS</text><text class="ts" x="471" y="163" text-anchor="middle" fill="#e2e8f0">App-aware</text><text class="ts" x="471" y="176" text-anchor="middle" fill="#e2e8f0">Deep inspection</text><text class="ts" x="471" y="189" text-anchor="middle" fill="#00c853">Zone 2</text><line x1="526" y1="162" x2="556" y2="162" stroke="#94a3b8" stroke-width="1.5"/><rect x="558" y="100" width="102" height="124" rx="6" fill="#185fa5" stroke="#00b4d8" stroke-width="1"/><text class="th" x="609" y="120" text-anchor="middle" fill="#fff">Internal LAN</text><text class="ts" x="609" y="136" text-anchor="middle" fill="#e2e8f0">Workstations</text><text class="ts" x="609" y="150" text-anchor="middle" fill="#e2e8f0">File servers</text><text class="ts" x="609" y="164" text-anchor="middle" fill="#e2e8f0">Databases</text><text class="ts" x="609" y="178" text-anchor="middle" fill="#e2e8f0">AD / LDAP</text><text class="ts" x="609" y="194" text-anchor="middle" fill="#00b4d8">Zone 3 Trusted</text><line x1="20" y1="300" x2="660" y2="300" stroke="#475569" stroke-width="1"/><text class="ts" x="30" y="296" fill="#ef4444">No trust</text><text class="ts" x="570" y="296" fill="#00c853">Full trust</text><text class="ts" x="340" y="320" text-anchor="middle" fill="#64748b">Trust increases left to right - each firewall enforces stricter controls toward the internal network</text><text class="ts" x="340" y="336" text-anchor="middle" fill="#64748b">NGFW adds Layer 7 inspection: application ID, user identity, SSL decryption, IPS</text></svg>',
'notes': 'A firewall enforces a security policy by permitting or denying traffic based on '
                  'rules. Packet-filtering (stateless) firewalls inspect each packet against an '
                  'ACL of source/destination IP, port, and protocol with no memory of prior '
                  'packets - fast but blunt. Stateful firewalls track the state of connections so '
                  'return traffic for an established session is allowed automatically, which is '
                  'the modern baseline. Next-generation firewalls (NGFW) add deep packet '
                  'inspection, application awareness, and IPS features. Placement matters: a '
                  'perimeter firewall sits at the network edge between the inside and the '
                  'internet, often creating a DMZ (screened subnet) for public-facing servers like '
                  'web and mail so they are isolated from the internal LAN. Internal/segmentation '
                  'firewalls sit between internal zones to limit lateral movement. Host-based '
                  'firewalls run on individual endpoints. Rules are processed top-down, and most '
                  'firewalls end with an implicit deny-all.',
         'links': [('Cloudflare - What is a Firewall?',
                    'https://www.cloudflare.com/learning/security/what-is-a-firewall/'),
                   ('Cisco - Firewall Basics',
                    'https://www.cisco.com/c/en/us/products/security/firewalls/what-is-a-firewall.html'),
                   ('Professor Messer - Firewalls',
                    'https://www.professormesser.com/network-plus/n10-008/n10-008-training-course/')],
         'terms': [('Packet-filtering firewall',
                    'A stateless firewall that allows or blocks packets by IP, port, and '
                    'protocol.'),
                   ('Stateful firewall',
                    'A firewall that tracks connection state and allows return traffic for '
                    'established sessions.'),
                   ('NGFW',
                    'Next-generation firewall adding deep packet inspection, app awareness, and '
                    'IPS.'),
                   ('DMZ / screened subnet',
                    'An isolated zone for public-facing servers, separated from the internal LAN.'),
                   ('Implicit deny',
                    'The default final rule that blocks any traffic not explicitly permitted.'),
                   ('ACL',
                    'An access control list of ordered permit/deny rules a firewall evaluates '
                    'top-down.')],
         'questions': [('What is the difference between a stateless and a stateful firewall?',
                        'Stateless filters each packet independently; stateful tracks connections '
                        'and allows return traffic automatically.'),
                       ('Where would you place a public web server relative to the firewall?',
                        'In a DMZ (screened subnet), isolated from the internal LAN but reachable '
                        'from the internet.'),
                       ('What is an implicit deny?',
                        'A default final rule that blocks all traffic not explicitly allowed by '
                        'earlier rules.'),
                       ('What does a next-generation firewall add over a stateful firewall?',
                        'Deep packet inspection, application awareness, and integrated IPS '
                        'capabilities.')]},
 '6-1': {         'diagram': '<svg width="100%" viewBox="0 0 680 360" xmlns="http://www.w3.org/2000/svg"><defs><style>.th{font-family:Arial,sans-serif;font-size:12px;font-weight:700;}.ts{font-family:Arial,sans-serif;font-size:10px;}.tt{font-family:JetBrains Mono,monospace;font-size:11px;fill:#00d4ff;letter-spacing:2px;}</style></defs><text class="tt" x="340" y="22" text-anchor="middle">802.11 WIRELESS STANDARDS</text><rect x="30" y="35" width="90" height="28" rx="4" fill="#1e293b"/><text class="th" x="75" y="54" text-anchor="middle" fill="#94a3b8">Standard</text><rect x="125" y="35" width="70" height="28" rx="4" fill="#1e293b"/><text class="th" x="160" y="54" text-anchor="middle" fill="#94a3b8">Year</text><rect x="200" y="35" width="80" height="28" rx="4" fill="#1e293b"/><text class="th" x="240" y="54" text-anchor="middle" fill="#94a3b8">Band</text><rect x="285" y="35" width="100" height="28" rx="4" fill="#1e293b"/><text class="th" x="335" y="54" text-anchor="middle" fill="#94a3b8">Max speed</text><rect x="390" y="35" width="260" height="28" rx="4" fill="#1e293b"/><text class="th" x="520" y="54" text-anchor="middle" fill="#94a3b8">Key feature</text><rect x="30" y="67" width="90" height="30" rx="4" fill="#185fa5" stroke="#00b4d8" stroke-width="0.5"/><text class="th" x="75" y="86" text-anchor="middle" fill="#fff">802.11a</text><rect x="125" y="67" width="70" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="160" y="86" text-anchor="middle" fill="#94a3b8">1999</text><rect x="200" y="67" width="80" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="240" y="86" text-anchor="middle" fill="#fac775">5 GHz</text><rect x="285" y="67" width="100" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="335" y="86" text-anchor="middle" fill="#94a3b8">54 Mbps</text><rect x="390" y="67" width="260" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="520" y="86" text-anchor="middle" fill="#94a3b8">First 5 GHz standard, less interference</text><rect x="30" y="101" width="90" height="30" rx="4" fill="#185fa5" stroke="#00b4d8" stroke-width="0.5"/><text class="th" x="75" y="120" text-anchor="middle" fill="#fff">802.11b</text><rect x="125" y="101" width="70" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="160" y="120" text-anchor="middle" fill="#94a3b8">1999</text><rect x="200" y="101" width="80" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="240" y="120" text-anchor="middle" fill="#6ee7b7">2.4 GHz</text><rect x="285" y="101" width="100" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="335" y="120" text-anchor="middle" fill="#94a3b8">11 Mbps</text><rect x="390" y="101" width="260" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="520" y="120" text-anchor="middle" fill="#94a3b8">First mass-market Wi-Fi standard</text><rect x="30" y="135" width="90" height="30" rx="4" fill="#185fa5" stroke="#00b4d8" stroke-width="0.5"/><text class="th" x="75" y="154" text-anchor="middle" fill="#fff">802.11g</text><rect x="125" y="135" width="70" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="160" y="154" text-anchor="middle" fill="#94a3b8">2003</text><rect x="200" y="135" width="80" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="240" y="154" text-anchor="middle" fill="#6ee7b7">2.4 GHz</text><rect x="285" y="135" width="100" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="335" y="154" text-anchor="middle" fill="#94a3b8">54 Mbps</text><rect x="390" y="135" width="260" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="520" y="154" text-anchor="middle" fill="#94a3b8">Backward compat with 802.11b</text><rect x="30" y="169" width="90" height="30" rx="4" fill="#1d9e75" stroke="#00c853" stroke-width="0.5"/><text class="th" x="75" y="188" text-anchor="middle" fill="#fff">802.11n</text><rect x="125" y="169" width="70" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="160" y="188" text-anchor="middle" fill="#94a3b8">2009</text><rect x="200" y="169" width="80" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="240" y="188" text-anchor="middle" fill="#ffc700">Both bands</text><rect x="285" y="169" width="100" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="335" y="188" text-anchor="middle" fill="#94a3b8">600 Mbps</text><rect x="390" y="169" width="260" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="520" y="188" text-anchor="middle" fill="#94a3b8">MIMO introduced, dual-band</text><rect x="30" y="203" width="90" height="30" rx="4" fill="#1d9e75" stroke="#00c853" stroke-width="0.5"/><text class="th" x="75" y="222" text-anchor="middle" fill="#fff">802.11ac</text><rect x="125" y="203" width="70" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="160" y="222" text-anchor="middle" fill="#94a3b8">2013</text><rect x="200" y="203" width="80" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="240" y="222" text-anchor="middle" fill="#fac775">5 GHz</text><rect x="285" y="203" width="100" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="335" y="222" text-anchor="middle" fill="#94a3b8">3.5 Gbps</text><rect x="390" y="203" width="260" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="520" y="222" text-anchor="middle" fill="#94a3b8">Wi-Fi 5, MU-MIMO, beamforming</text><rect x="30" y="237" width="90" height="30" rx="4" fill="#534ab7" stroke="#7f77dd" stroke-width="0.5"/><text class="th" x="75" y="256" text-anchor="middle" fill="#fff">802.11ax</text><rect x="125" y="237" width="70" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="160" y="256" text-anchor="middle" fill="#94a3b8">2019</text><rect x="200" y="237" width="80" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="240" y="256" text-anchor="middle" fill="#ffc700">2.4+5+6 GHz</text><rect x="285" y="237" width="100" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="335" y="256" text-anchor="middle" fill="#94a3b8">9.6 Gbps</text><rect x="390" y="237" width="260" height="30" rx="4" fill="#111827" stroke="#1e293b" stroke-width="0.5"/><text class="ts" x="520" y="256" text-anchor="middle" fill="#94a3b8">Wi-Fi 6, OFDMA, dense environments</text><text class="ts" x="340" y="300" text-anchor="middle" fill="#64748b">Blue = older  |  Green = widely deployed  |  Purple = current generation</text><text class="ts" x="340" y="316" text-anchor="middle" fill="#64748b">2.4 GHz = longer range, more interference  |  5/6 GHz = faster, shorter range</text></svg>',
'notes': 'The IEEE 802.11 family defines Wi-Fi standards. 802.11a (1999) used the 5 GHz '
                  'band at up to 54 Mbps. 802.11b (1999) used 2.4 GHz at up to 11 Mbps with '
                  'greater range but more interference. 802.11g (2003) brought 54 Mbps to 2.4 GHz '
                  'and is backward compatible with b. 802.11n (Wi-Fi 4, 2009) introduced MIMO and '
                  'channel bonding across both 2.4 and 5 GHz for hundreds of Mbps. 802.11ac (Wi-Fi '
                  '5, 2013) is 5 GHz only, adding wider channels, more spatial streams, and '
                  'MU-MIMO for gigabit-class speeds. 802.11ax (Wi-Fi 6/6E, 2019+) operates on 2.4, '
                  '5, and (6E) 6 GHz, using OFDMA and improved MU-MIMO for higher efficiency in '
                  'dense environments. The 2.4 GHz band penetrates walls better but is crowded and '
                  'has only three non-overlapping channels (1, 6, 11); 5 GHz offers more channels '
                  'and speed with shorter range.',
         'links': [('Cisco - 802.11 Wi-Fi Standards',
                    'https://www.cisco.com/c/en/us/products/wireless/what-is-wi-fi.html'),
                   ('Wi-Fi Alliance - Wi-Fi Generations', 'https://www.wi-fi.org/discover-wi-fi'),
                   ('Professor Messer - Wireless Standards',
                    'https://www.professormesser.com/network-plus/n10-008/n10-008-training-course/')],
         'terms': [('802.11n (Wi-Fi 4)',
                    'Dual-band (2.4/5 GHz) standard introducing MIMO and channel bonding.'),
                   ('802.11ac (Wi-Fi 5)',
                    '5 GHz-only standard with wider channels and MU-MIMO for gigabit speeds.'),
                   ('802.11ax (Wi-Fi 6/6E)',
                    'Standard using OFDMA across 2.4/5/6 GHz for efficiency in dense areas.'),
                   ('MIMO',
                    'Multiple-Input Multiple-Output: multiple antennas/streams to boost '
                    'throughput.'),
                   ('Non-overlapping channels',
                    'In 2.4 GHz, channels 1, 6, and 11 that do not interfere with each other.'),
                   ('Channel bonding',
                    'Combining adjacent channels into a wider channel for more bandwidth.')],
         'questions': [('Which bands does 802.11ax operate on?',
                        '2.4 GHz, 5 GHz, and (with 6E) the 6 GHz band.'),
                       ('Why is 802.11ac 5 GHz only?',
                        'It targets higher throughput with wider channels available in the 5 GHz '
                        'band.'),
                       ('What are the three non-overlapping channels in 2.4 GHz?',
                        'Channels 1, 6, and 11.'),
                       ('What is the trade-off between 2.4 GHz and 5 GHz?',
                        '2.4 GHz has better range/wall penetration but more interference; 5 GHz is '
                        'faster with more channels but shorter range.')]},
 '6-3': {'notes': 'Authentication protocols verify identity before granting network access. WPA2 '
                  'and WPA3 are wireless security standards: WPA2 uses AES-CCMP encryption, while '
                  'WPA3 adds SAE (Simultaneous Authentication of Equals) to resist offline '
                  'password guessing. Wireless networks run in two modes: Personal (PSK), where '
                  'everyone shares one pre-shared key, and Enterprise (802.1X), where each user '
                  'authenticates individually against a RADIUS server. 802.1X is the port-based '
                  'access control framework with three roles: the supplicant (client), the '
                  'authenticator (switch or access point), and the authentication server (RADIUS). '
                  'EAP (Extensible Authentication Protocol) is the framework that carries the '
                  'actual credential exchange, with variants like EAP-TLS (certificate-based, '
                  'strongest), PEAP, and EAP-TTLS. AAA servers - RADIUS (UDP, encrypts only the '
                  'password) and TACACS+ (TCP, encrypts the whole payload and separates '
                  'authentication, authorization, and accounting) - centralize these decisions. '
                  'Kerberos uses time-sensitive tickets for single sign-on in Windows domains.',
         'links': [('Cloudflare - What is 802.1X / RADIUS?',
                    'https://www.cloudflare.com/learning/access-management/what-is-radius/'),
                   ('Cisco - RADIUS vs TACACS+',
                    'https://www.cisco.com/c/en/us/support/docs/security-vpn/remote-authentication-dial-user-service-radius/13838-10.html'),
                   ('Professor Messer - Authentication Protocols',
                    'https://www.professormesser.com/network-plus/n10-008/n10-008-training-course/')],
         'terms': [('802.1X',
                    'Port-based network access control using supplicant, authenticator, and auth '
                    'server.'),
                   ('EAP',
                    'Extensible Authentication Protocol - the framework carrying credential '
                    'exchanges.'),
                   ('RADIUS',
                    'AAA protocol over UDP that encrypts only the password; common for Wi-Fi.'),
                   ('TACACS+',
                    'Cisco AAA protocol over TCP that encrypts the full payload and separates AAA '
                    'functions.'),
                   ('WPA2 / WPA3',
                    'Wireless security standards; WPA3 adds SAE to resist offline password '
                    'attacks.'),
                   ('Kerberos',
                    'Ticket-based authentication providing single sign-on in Windows domains.')],
         'questions': [('What are the three roles in 802.1X?',
                        'Supplicant (client), authenticator (switch/AP), and authentication server '
                        '(RADIUS).'),
                       ('How does RADIUS differ from TACACS+?',
                        'RADIUS uses UDP and encrypts only the password; TACACS+ uses TCP, '
                        'encrypts the whole payload, and separates AAA.'),
                       ('What does WPA3 add over WPA2?',
                        'SAE (Simultaneous Authentication of Equals) to resist offline '
                        'dictionary/password attacks.'),
                       ('What is the difference between WPA2-Personal and WPA2-Enterprise?',
                        'Personal uses a shared pre-shared key; Enterprise authenticates each user '
                        'individually via 802.1X/RADIUS.')]},
 '6-4': {'notes': 'Wireless troubleshooting follows a structured approach to common RF and '
                  'configuration problems. Low signal strength (RSSI) usually points to distance, '
                  'obstructions, or AP placement - relocate or add access points. Interference '
                  'comes from other networks or non-Wi-Fi sources (microwaves, Bluetooth, cordless '
                  'phones); use a Wi-Fi analyzer to find clean channels and stick to '
                  'non-overlapping channels 1, 6, 11 in 2.4 GHz. Channel overlap and co-channel '
                  'contention slow throughput in dense deployments. Authentication failures often '
                  'mean a wrong passphrase, mismatched security mode (WPA2 vs WPA3), or a '
                  'misconfigured RADIUS server. Roaming issues occur when clients cling to a '
                  "distant AP ('sticky client') instead of switching to a closer one. Throughput "
                  'problems can stem from band steering, too many clients per AP, or falling back '
                  'to a slower standard. A site survey and heat map help validate coverage, '
                  'channel plan, and AP density. Always check the basics first: SSID broadcast, '
                  'correct band, client driver, and whether the issue is one device or all '
                  'devices.',
         'links': [('Cisco - Wireless Troubleshooting',
                    'https://www.cisco.com/c/en/us/support/wireless/index.html'),
                   ('Cloudflare - What is Wi-Fi Interference?',
                    'https://www.cloudflare.com/learning/network-layer/what-is-wi-fi/'),
                   ('Professor Messer - Wireless Troubleshooting',
                    'https://www.professormesser.com/network-plus/n10-008/n10-008-training-course/')],
         'terms': [('RSSI',
                    'Received Signal Strength Indicator - a measure of how strong the wireless '
                    'signal is.'),
                   ('Interference',
                    'Unwanted RF from other networks or devices that degrades the wireless '
                    'signal.'),
                   ('Channel overlap',
                    'When nearby APs use overlapping channels, causing contention and slowdowns.'),
                   ('Site survey / heat map',
                    'A coverage assessment used to plan AP placement, channels, and density.'),
                   ('Sticky client',
                    'A device that stays connected to a distant AP instead of roaming to a closer '
                    'one.'),
                   ('Band steering',
                    'A feature that pushes capable clients onto the less-congested 5 GHz band.')],
         'questions': [('A user reports a weak Wi-Fi signal far from the AP. What is the likely '
                        'cause?',
                        'Low RSSI due to distance/obstructions - relocate or add an access point '
                        'closer to the user.'),
                       ('How do you reduce interference in the 2.4 GHz band?',
                        'Use a Wi-Fi analyzer and select non-overlapping channels 1, 6, or 11.'),
                       ('A client cannot authenticate to a WPA2-Enterprise network. What should '
                        'you check?',
                        'The RADIUS server config, correct credentials, and matching security '
                        'mode/EAP method.'),
                       ('What tool validates wireless coverage and channel planning?',
                        'A site survey that produces a heat map of signal strength and '
                        'coverage.')]},
 '8-1': {'links': [['Professor Messer — Network+ Course (Free)',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'],
                   ['CompTIA Network+ Exam Objectives (Free PDF)',
                    'https://www.comptia.org/training/resources/exam-objectives'],
                   ['ExamCompass — Free Network+ Practice',
                    'https://www.comptia.org/training/certmaster-practice/network']],
         'notes': 'Troubleshooting methodology gives you a repeatable process so you fix the '
                  "actual root cause instead of guessing. CompTIA's seven-step model is: 1) "
                  'Identify the problem — gather information, question users, and identify '
                  'symptoms and recent changes. 2) Establish a theory of probable cause — question '
                  'the obvious and consider multiple approaches (top-to-bottom or bottom-to-top of '
                  'the OSI model, or divide and conquer). 3) Test the theory to determine the '
                  'cause — if confirmed, find the next steps; if not, establish a new theory or '
                  'escalate. 4) Establish a plan of action to resolve the problem and identify '
                  'potential effects. 5) Implement the solution or escalate as necessary. 6) '
                  'Verify full system functionality and, if applicable, implement preventive '
                  'measures. 7) Document findings, actions, and outcomes.\n'
                  '\n'
                  'Always change one thing at a time so you know what actually fixed the issue, '
                  'and keep a backout plan in case a change makes things worse. The OSI model is a '
                  'useful map: working bottom-up (Physical → Application) helps you rule out '
                  'cabling and link problems before chasing application bugs.',
         'questions': [["What is the first step in CompTIA's troubleshooting methodology?",
                        'Identify the problem — gather information, question users, and note '
                        'recent changes.'],
                       ['Why should you change only one thing at a time?',
                        'So you can tell which specific change resolved the issue and easily back '
                        'it out if needed.'],
                       ['What is the final step of the methodology?',
                        'Document findings, actions, and outcomes for future reference.'],
                       ['What should you do if testing shows your theory was wrong?',
                        'Establish a new theory of probable cause or escalate to someone with more '
                        'expertise.']],
         'terms': [['Root cause',
                    'The underlying reason a problem occurs, as opposed to its symptoms.'],
                   ['Top-to-bottom approach',
                    'Troubleshooting starting at the Application layer and moving down the OSI '
                    'stack.'],
                   ['Bottom-to-top approach',
                    'Troubleshooting starting at the Physical layer and moving up the OSI stack.'],
                   ['Divide and conquer',
                    'Starting in the middle of the OSI stack to narrow the problem domain '
                    'quickly.'],
                   ['Backout plan',
                    'A predefined way to reverse a change if it does not fix the issue or causes '
                    'new problems.']]},
 '8-2': {'links': [['Professor Messer — Network+ Course (Free)',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'],
                   ['CompTIA Network+ Exam Objectives (Free PDF)',
                    'https://www.comptia.org/training/resources/exam-objectives'],
                   ['ExamCompass — Free Network+ Practice',
                    'https://www.comptia.org/training/certmaster-practice/network']],
         'notes': 'These four command-line tools are the bread and butter of connectivity '
                  'troubleshooting. ping uses ICMP echo request/reply to test reachability and '
                  'measure round-trip latency; if ping to an IP works but the hostname fails, you '
                  'have a DNS problem, not a connectivity problem. traceroute (tracert on Windows) '
                  'shows each router hop along the path and where latency or packet loss begins, '
                  'which helps localize a failure between you and the destination. nslookup (or '
                  'dig) queries DNS directly so you can confirm name-to-IP resolution and test '
                  'specific record types or servers. netstat displays active connections, '
                  'listening ports, and routing/interface statistics, which is useful for '
                  'confirming a service is actually listening on the expected port.\n'
                  '\n'
                  'A reliable workflow is: ping the loopback (127.0.0.1) to verify the TCP/IP '
                  'stack, ping your default gateway to verify the local link, ping a public IP '
                  '(such as 8.8.8.8) to verify internet routing, then ping a hostname to verify '
                  'DNS. Wherever the chain breaks tells you which layer to investigate.',
         'questions': [['You can ping 8.8.8.8 but not google.com. What is the likely problem?',
                        'DNS resolution — connectivity works, but name-to-IP lookup is failing.'],
                       ['Which tool shows the router hops between you and a destination?',
                        'traceroute (tracert on Windows).'],
                       ['Which command shows active connections and listening ports on a host?',
                        'netstat.'],
                       ['What protocol does ping use?', 'ICMP (echo request and echo reply).'],
                       ['Why ping the loopback address first?',
                        'To confirm the local TCP/IP stack is installed and working before testing '
                        'the network.']],
         'terms': [['ping', 'Tests reachability and round-trip time to a host using ICMP.'],
                   ['traceroute / tracert',
                    'Reveals the path and per-hop latency to a destination.'],
                   ['nslookup / dig',
                    'Queries DNS to resolve names and inspect specific record types.'],
                   ['netstat',
                    'Displays active connections, listening ports, and interface statistics.'],
                   ['Default gateway',
                    'The router a host uses to reach networks outside its own subnet.']]},
 '8-3': {'links': [['Professor Messer — Network+ Course (Free)',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'],
                   ['CompTIA Network+ Exam Objectives (Free PDF)',
                    'https://www.comptia.org/training/resources/exam-objectives'],
                   ['ExamCompass — Free Network+ Practice',
                    'https://www.comptia.org/training/certmaster-practice/network']],
         'notes': 'Wireshark is a free, open-source packet analyzer that captures traffic off a '
                  'network interface and decodes it protocol by protocol. Reading captures is a '
                  'core troubleshooting skill because the packets show you exactly what happened '
                  'on the wire, rather than what a device claims happened. Capture filters (BPF '
                  'syntax) limit what is recorded, while display filters (such as ip.addr == '
                  '10.0.0.5, tcp.port == 443, or dns) narrow what you see after capture. Color '
                  'rules highlight resets, retransmissions, and errors at a glance.\n'
                  '\n'
                  'For TCP issues, watch the three-way handshake (SYN, SYN-ACK, ACK): a SYN with '
                  'no SYN-ACK points to a firewall drop or a service that is not listening, while '
                  'many retransmissions or duplicate ACKs suggest packet loss or congestion. '
                  'Follow TCP Stream reassembles a conversation so you can read it end to end. '
                  'Always capture as close to the problem as possible and remember that capturing '
                  'traffic can expose sensitive data, so handle saved captures responsibly.',
         'questions': [['What is the difference between a capture filter and a display filter?',
                        'A capture filter limits what packets are recorded; a display filter '
                        'limits what you see after capturing.'],
                       ['What three packets make up the TCP three-way handshake?',
                        'SYN, SYN-ACK, and ACK.'],
                       ['You see a SYN but no SYN-ACK. What does that suggest?',
                        'A firewall is dropping the traffic or no service is listening on that '
                        'port.'],
                       ['Which display filter shows only traffic to or from 10.0.0.5?',
                        'ip.addr == 10.0.0.5'],
                       ['What does a burst of TCP retransmissions usually indicate?',
                        'Packet loss or network congestion along the path.']],
         'terms': [['Packet capture (pcap)',
                    'A recorded set of network packets saved for analysis.'],
                   ['Display filter',
                    'A Wireshark expression that shows only matching packets after capture.'],
                   ['Three-way handshake',
                    'The SYN / SYN-ACK / ACK sequence that establishes a TCP connection.'],
                   ['Retransmission',
                    'A resent packet, indicating the original was lost or unacknowledged.'],
                   ['Follow TCP Stream',
                    'A Wireshark feature that reassembles a full TCP conversation.']]},
 '8-4': {'links': [['Professor Messer — Network+ Course (Free)',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'],
                   ['CompTIA Network+ Exam Objectives (Free PDF)',
                    'https://www.comptia.org/training/resources/exam-objectives'],
                   ['ExamCompass — Free Network+ Practice',
                    'https://www.comptia.org/training/certmaster-practice/network']],
         'notes': 'Most connectivity problems fall into a handful of recurring categories, and '
                  'knowing the common fixes saves time. Physical-layer issues include unplugged or '
                  'damaged cables, bad ports, and link/speed/duplex mismatches — check link lights '
                  'and interface counters first. Addressing issues include duplicate IP addresses, '
                  'wrong subnet mask, missing or wrong default gateway, and APIPA addresses '
                  "(169.254.x.x) that indicate a failed DHCP lease. DNS issues show up as 'works "
                  "by IP but not by name'; flush the resolver cache and verify the configured DNS "
                  'servers. Routing issues appear as reachable locally but not remotely — confirm '
                  'the gateway and the route table.\n'
                  '\n'
                  'Other frequent culprits are firewall or ACL rules blocking a specific port, '
                  'VLAN or trunking misconfiguration, exhausted DHCP scopes, MTU mismatches '
                  'causing fragmentation, and duplex mismatches causing slow throughput with '
                  'errors. Work the OSI model from the bottom up, verify one layer before moving '
                  'to the next, and confirm the fix end to end before closing the ticket.',
         'questions': [['A host has a 169.254.x.x address. What does that tell you?',
                        'It is an APIPA address — the host failed to obtain a DHCP lease.'],
                       ['A PC reaches local hosts but nothing on the internet. What should you '
                        'check first?',
                        'The default gateway setting and the route to remote networks.'],
                       ['Two devices intermittently lose connectivity and report an IP conflict. '
                        'What is the cause?',
                        'A duplicate IP address on the subnet.'],
                       ['Slow throughput with lots of interface errors often points to what?',
                        'A duplex mismatch between the two link partners.'],
                       ['Name resolves to the wrong or no IP. What is a quick first step?',
                        'Flush the DNS resolver cache and verify the configured DNS servers.']],
         'terms': [['APIPA',
                    'Automatic Private IP Addressing (169.254.x.x); assigned when DHCP fails.'],
                   ['Duplicate IP',
                    'Two hosts sharing the same address, causing intermittent connectivity.'],
                   ['Duplex mismatch',
                    'One side half-duplex and the other full-duplex, causing errors and slow '
                    'speeds.'],
                   ['MTU mismatch',
                    'Differing maximum frame sizes that lead to fragmentation or dropped packets.'],
                   ['ACL',
                    'Access Control List; rules that permit or deny traffic, often blocking '
                    'specific ports.']]},
 '8-6': {'links': [['Professor Messer — Network+ Course (Free)',
                    'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'],
                   ['CompTIA Network+ Exam Objectives (Free PDF)',
                    'https://www.comptia.org/training/resources/exam-objectives'],
                   ['ExamCompass — Free Network+ Practice',
                    'https://www.comptia.org/training/certmaster-practice/network']],
         'notes': 'Network diagrams document how a network is built and are essential for both '
                  'design and troubleshooting. Physical diagrams show the actual hardware and '
                  'cabling — which device connects to which port, cable types, and rack locations. '
                  'Logical diagrams show how data flows — IP subnets, VLANs, routing, and trust '
                  'boundaries — independent of physical layout. A rack diagram details the '
                  'U-position of each device in a cabinet, and a floor plan or wiring map records '
                  'cable runs and drop locations.\n'
                  '\n'
                  'Good diagrams use consistent, standard symbols (a router as a circle with '
                  'arrows, a switch as a rectangle, a firewall as a brick wall) and label '
                  'interfaces, IP ranges, and link speeds. Keep them current: an out-of-date '
                  'diagram is worse than none because it misleads responders during an outage. '
                  'Diagrams also support change management, capacity planning, and onboarding, and '
                  'they are often required for audits and compliance. Pair the diagram with an IP '
                  'address management (IPAM) record and a baseline of normal behavior so '
                  'deviations are easy to spot.',
         'questions': [['What is the difference between a physical and a logical network diagram?',
                        'Physical shows hardware and cabling; logical shows IP subnets, VLANs, and '
                        'data flow.'],
                       ['What does a rack diagram document?',
                        'The U-position and layout of each device within an equipment rack.'],
                       ['Why must network diagrams be kept current?',
                        'An outdated diagram misleads responders and can lengthen outages.'],
                       ['Which diagram would you use to plan IP subnets and VLAN boundaries?',
                        'A logical network diagram.'],
                       ['What record pairs well with diagrams for tracking address usage?',
                        'An IPAM (IP Address Management) record.']],
         'terms': [['Physical diagram', 'A drawing of actual devices, ports, and cabling.'],
                   ['Logical diagram', 'A drawing of subnets, VLANs, routing, and data flow.'],
                   ['Rack diagram',
                    'A layout of device positions (by U) within an equipment rack.'],
                   ['Baseline', 'A record of normal performance used to detect deviations.'],
                   ['IPAM',
                    'IP Address Management; tracking of allocated and available addresses.']]}}
