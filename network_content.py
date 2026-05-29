LESSON_CONTENT = {   '1-1': {   'links': [   (   'Professor Messer — Network+ Course (Free)',
                                'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                            (   'Cloudflare — OSI Model Explained',
                                'https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/'),
                            ('TryHackMe — Free Networking Rooms', 'https://tryhackme.com/hacktivities?tab=practice')],
               'notes': 'The OSI (Open Systems Interconnection) model is a 7-layer framework that describes how data '
                        'travels from one device to another across a network. Each layer has a specific job and '
                        'communicates with the layers above and below it. From top to bottom: Application (layer 7) is '
                        'where user-facing software lives; Presentation (6) handles data formatting and encryption; '
                        'Session (5) manages connections; Transport (4) handles reliable delivery with TCP/UDP; '
                        'Network (3) handles IP addressing and routing; Data Link (2) handles MAC addresses and '
                        'switches; Physical (1) is the actual cables and signals.\n'
                        '\n'
                        'The OSI model is critical for the Network+ exam and for troubleshooting. When something goes '
                        'wrong, you work from layer 1 upward — is the cable plugged in? Is the IP address correct? Is '
                        'the application configured properly? Every networking concept maps to a specific OSI layer.',
               'questions': [   (   'At which OSI layer do routers operate?',
                                    'Layer 3 — Network layer (routers forward packets based on IP addresses)'),
                                (   'At which OSI layer do switches operate?',
                                    'Layer 2 — Data Link layer (switches forward frames based on MAC addresses)'),
                                (   'Which layer is responsible for encryption and data formatting?',
                                    'Layer 6 — Presentation layer')],
               'terms': [   ('OSI Model', 'A 7-layer conceptual framework describing how network communication works'),
                            ('Layer 1 — Physical', 'Cables, signals, network interface cards, hubs'),
                            ('Layer 2 — Data Link', 'MAC addresses, switches, frames, error detection'),
                            ('Layer 3 — Network', 'IP addresses, routers, packets, routing'),
                            ('Layer 4 — Transport', 'TCP/UDP, ports, segmentation, reliable delivery'),
                            ('Layer 7 — Application', 'HTTP, FTP, DNS, SMTP — user-facing protocols')]},
    '1-2': {   'links': [   (   'Professor Messer — Network+ Course (Free)',
                                'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                            ('Cloudflare Learning Center', 'https://www.cloudflare.com/learning/'),
                            (   'CompTIA Network+ Exam Objectives',
                                'https://www.comptia.org/training/resources/exam-objectives')],
               'notes': 'While the OSI model has 7 layers, the TCP/IP model is the practical framework that the '
                        'internet actually uses, with 4 layers. The Application layer maps to OSI layers 5-7 and '
                        'handles protocols like HTTP, DNS, and SMTP. The Transport layer (same as OSI layer 4) handles '
                        'TCP and UDP. The Internet layer maps to OSI layer 3 and handles IP addressing. The Network '
                        'Access layer maps to OSI layers 1-2 and handles physical transmission.\n'
                        '\n'
                        "The TCP/IP model is what you'll use day-to-day in real networking. The OSI model is more of a "
                        'teaching tool and troubleshooting reference. The Network+ exam tests both — you need to know '
                        'which OSI layers map to which TCP/IP layers and what protocols live at each layer of both '
                        'models.',
               'questions': [   (   'How many layers does the TCP/IP model have?',
                                    '4 layers: Application, Transport, Internet, Network Access'),
                                ('Which TCP/IP layer corresponds to OSI layers 5, 6, and 7?', 'The Application layer'),
                                (   'What is the main difference between OSI and TCP/IP models?',
                                    'OSI has 7 layers and is a conceptual reference model; TCP/IP has 4 layers and is '
                                    'the practical model the internet uses')],
               'terms': [   ('TCP/IP Model', 'A 4-layer practical networking model used by the internet'),
                            ('Application Layer', 'Top layer handling HTTP, DNS, SMTP, FTP (maps to OSI 5-7)'),
                            ('Transport Layer', 'Handles TCP and UDP (maps to OSI layer 4)'),
                            ('Internet Layer', 'Handles IP addressing and routing (maps to OSI layer 3)'),
                            (   'Network Access Layer',
                                'Handles physical transmission and MAC addressing (maps to OSI 1-2)')]},
    '1-4': {   'links': [   (   'Professor Messer — Network+ Course (Free)',
                                'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                            ('Cloudflare Learning Center', 'https://www.cloudflare.com/learning/'),
                            (   'ExamCompass — Free Network+ Practice',
                                'https://www.comptia.org/training/certmaster-practice/network')],
               'notes': 'Network topology describes the physical or logical arrangement of devices on a network. In a '
                        "star topology, all devices connect to a central switch or hub — it's the most common in "
                        'modern networks because a single cable failure only affects one device. In a bus topology, '
                        'all devices share a single cable; if that cable breaks the whole network goes down. Ring '
                        'topologies connect devices in a circular chain, where data travels in one direction around '
                        'the ring.\n'
                        '\n'
                        'Mesh topologies connect every device to every other device, providing maximum redundancy — if '
                        'one path fails, data takes another route. Full mesh is expensive but used in critical '
                        'infrastructure. Partial mesh is a compromise. Understanding topologies helps you design '
                        'reliable networks and troubleshoot failures efficiently.',
               'questions': [   (   'Which topology is most fault-tolerant?',
                                    "Mesh — multiple paths exist between devices so a single failure doesn't break the "
                                    'network'),
                                (   'In a star topology, what happens if the central switch fails?',
                                    'The entire network goes down as all devices depend on the central switch'),
                                ('Which legacy topology used a single shared cable for all devices?', 'Bus topology')],
               'terms': [   ('Star Topology', 'All devices connect to a central switch; most common modern topology'),
                            (   'Bus Topology',
                                'All devices share a single cable backbone; a break affects the whole network'),
                            ('Ring Topology', 'Devices connected in a circle; data travels in one direction'),
                            ('Mesh Topology', 'Every device connects to every other; maximum redundancy'),
                            ('Topology', 'The arrangement or layout of devices and connections in a network')]},
    '1-5': {   'links': [   (   'Professor Messer — Free Practice Exams',
                                'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                            (   'ExamCompass — Free Network+ Quizzes',
                                'https://www.comptia.org/training/certmaster-practice/network'),
                            (   'CompTIA CertMaster Learn (Official)',
                                'https://www.comptia.org/training/certmaster-learn/network')],
               'notes': 'This is a review quiz for Module 1. Test your understanding of network types, topologies, and '
                        'the OSI and TCP/IP models before moving on. These concepts underpin everything in the rest of '
                        'the course — if any answers are unclear, review the relevant lesson before continuing.\n'
                        '\n'
                        'Tip for the exam: OSI layer numbers and what operates at each layer is one of the most '
                        'frequently tested topics on Network+. Make sure you can name all 7 layers in order and give '
                        'an example of a protocol or device at each one.',
               'questions': [   (   'Name the 7 OSI layers in order from layer 1 to layer 7.',
                                    'Physical, Data Link, Network, Transport, Session, Presentation, Application'),
                                ('What type of network covers a single building?', 'LAN — Local Area Network'),
                                ('Which topology provides the most redundancy?', 'Mesh topology'),
                                ('At which OSI layer does IP addressing occur?', 'Layer 3 — Network layer'),
                                (   'What are the 4 layers of the TCP/IP model?',
                                    'Network Access, Internet, Transport, Application')],
               'terms': [   (   'Mnemonic for OSI layers (top to bottom)',
                                'All People Seem To Need Data Processing — Application, Presentation, Session, '
                                'Transport, Network, Data Link, Physical'),
                            ('Mnemonic (bottom to top)', 'Please Do Not Throw Sausage Pizza Away')]},
    '2-1': {   'links': [   (   'Professor Messer — Network+ Course (Free)',
                                'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                            ('Subnet Calculator', 'https://www.subnet-calculator.com'),
                            ('CIDR.xyz — Visual Subnet Tool', 'https://cidr.xyz')],
               'notes': 'An IPv4 address is a 32-bit number written as four octets in dotted decimal notation (e.g. '
                        '192.168.1.1). Each octet is 8 bits and can range from 0 to 255. IPv4 addresses were '
                        'originally divided into classes: Class A (1-126 in first octet) for large networks with '
                        'millions of hosts; Class B (128-191) for medium networks; Class C (192-223) for small '
                        'networks up to 254 hosts. Class D (224-239) is used for multicast and Class E (240-255) is '
                        'reserved.\n'
                        '\n'
                        'Classful addressing is largely obsolete — replaced by CIDR — but Network+ still tests it. The '
                        'address 127.x.x.x is always the loopback range (127.0.0.1 = localhost). The address 0.0.0.0 '
                        "means 'this network'. Understanding the structure of IP addresses is the foundation for "
                        'subnetting.',
               'questions': [   ('What class is the IP address 172.16.5.10?', 'Class B (first octet 128-191)'),
                                ('How many bits are in an IPv4 address?', '32 bits'),
                                ('What is the loopback address?', '127.0.0.1'),
                                ('What is the maximum value of any single octet?', '255')],
               'terms': [   ('IPv4', '32-bit IP address written as four decimal octets, e.g. 192.168.1.1'),
                            ('Octet', '8-bit section of an IP address; values range from 0-255'),
                            ('Class A', 'First octet 1-126; default mask /8; supports ~16 million hosts'),
                            ('Class B', 'First octet 128-191; default mask /16; supports ~65,000 hosts'),
                            ('Class C', 'First octet 192-223; default mask /24; supports 254 hosts'),
                            ('Loopback', '127.0.0.1 — the address a device uses to refer to itself')]},
    '2-2': {   'links': [   ('Subnet Calculator', 'https://www.subnet-calculator.com'),
                            ('CIDR.xyz — Visual Subnet Tool', 'https://cidr.xyz'),
                            ('Subnetting Practice', 'https://subnettingpractice.com')],
               'notes': 'A subnet mask defines which part of an IP address is the network portion and which part '
                        'identifies the host. Written in dotted decimal (255.255.255.0) or CIDR notation (/24), it '
                        'works by masking the network bits with 1s and host bits with 0s. A /24 mask means 24 bits are '
                        'network, 8 bits are host — giving 256 addresses (254 usable, minus network and broadcast '
                        'addresses).\n'
                        '\n'
                        'CIDR (Classless Inter-Domain Routing) replaced classful addressing and allows flexible subnet '
                        'sizes. A /30 gives 4 addresses (2 usable) — perfect for point-to-point links. A /16 gives '
                        '65,536 addresses. The formula for usable hosts is 2^(host bits) - 2. You must be fast with '
                        'these calculations for the Network+ exam.',
               'questions': [   (   'How many usable hosts does a /24 subnet provide?',
                                    '254 (2^8 = 256, minus 2 for network and broadcast)'),
                                ('What is the subnet mask for a /24 in dotted decimal?', '255.255.255.0'),
                                ('How many usable hosts does a /30 subnet provide?', '2 (2^2 = 4, minus 2)'),
                                (   'In CIDR notation, what does the number after the slash represent?',
                                    'The number of bits used for the network portion')],
               'terms': [   ('Subnet Mask', '32-bit number that separates network and host portions of an IP address'),
                            (   'CIDR Notation',
                                'Slash notation indicating how many bits are the network portion, e.g. /24'),
                            (   'Network Address',
                                'First address in a subnet — identifies the network itself, not usable for hosts'),
                            (   'Broadcast Address',
                                'Last address in a subnet — sent to all hosts, not usable for individual hosts'),
                            ('Usable Hosts', 'Total addresses minus 2 (network + broadcast) = 2^host bits - 2')]},
    '2-3': {   'links': [   ('Subnetting Practice — Free Drill Tool', 'https://subnettingpractice.com'),
                            ('Subnet Calculator', 'https://www.subnet-calculator.com'),
                            ('CIDR.xyz — Visual Subnet Tool', 'https://cidr.xyz')],
               'notes': 'Subnetting divides a large network into smaller sub-networks. The process: 1) Convert the IP '
                        'and mask to binary. 2) Determine how many subnets or hosts you need. 3) Borrow bits from the '
                        'host portion to create subnets. Each bit borrowed doubles the number of subnets but halves '
                        'the hosts per subnet.\n'
                        '\n'
                        "The quick method: identify the 'interesting octet' (where the subnet mask isn't 255 or 0). "
                        'The block size = 256 minus the mask value in that octet. Subnets increment by the block size. '
                        'For example, /26 = 255.255.255.192 — block size is 256-192=64. Subnets are .0, .64, .128, '
                        ".192. Practice this daily until it's automatic — it comes up on every Network+ exam.",
               'questions': [   ('What is the block size for a /26 subnet?', '64 (256 - 192 = 64)'),
                                ('For 192.168.1.0/26, what are the four subnet addresses?', '.0, .64, .128, .192'),
                                ('How many hosts can a /26 subnet support?', '62 usable hosts (2^6 = 64, minus 2)'),
                                (   'You need 30 hosts per subnet. What prefix length should you use?',
                                    '/27 — provides 30 usable hosts (2^5=32, minus 2)')],
               'terms': [   ('Subnetting', 'Dividing a network into smaller logical sub-networks'),
                            (   'Block Size',
                                '256 minus the subnet mask value in the interesting octet; the increment between '
                                'subnets'),
                            ('Interesting Octet', 'The octet in the subnet mask that is neither 255 nor 0'),
                            ('Borrowing Bits', 'Taking bits from the host portion to create more subnets'),
                            ('/26', '255.255.255.192 — 4 subnets of 62 hosts each within a /24')]},
    '2-4': {   'links': [   (   'Cloudflare — What is NAT?',
                                'https://www.cloudflare.com/learning/network-layer/what-is-nat/'),
                            (   'Professor Messer — Network+ Course (Free)',
                                'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                            ('RFC 1918 — Private Address Space', 'https://datatracker.ietf.org/doc/html/rfc1918')],
               'notes': 'Private IP addresses are reserved ranges that are not routable on the public internet. '
                        "They're defined in RFC 1918: 10.0.0.0/8 (Class A private), 172.16.0.0/12 (Class B private), "
                        'and 192.168.0.0/16 (Class C private). Every home and office network uses these ranges '
                        'internally. NAT (Network Address Translation) allows many private addresses to share a single '
                        'public IP address.\n'
                        '\n'
                        'NAT works by maintaining a translation table — when a device at 192.168.1.5 sends traffic to '
                        'the internet, the router replaces the private source IP with its public IP, records the '
                        'mapping, and reverses the process for return traffic. PAT (Port Address Translation), also '
                        'called NAT overload, allows thousands of private IPs to share one public IP by tracking port '
                        'numbers. This is what your home router does.',
               'questions': [   (   'Which three ranges are private IP addresses?',
                                    '10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16'),
                                (   'What does NAT allow?',
                                    'Multiple devices with private IPs to share a single public IP address'),
                                (   'Is 172.20.5.1 a private address?',
                                    'Yes — it falls within the 172.16.0.0/12 private range (172.16-172.31)')],
               'terms': [   ('Private IP', 'Non-routable IP ranges for internal use: 10.x, 172.16-31.x, 192.168.x'),
                            ('Public IP', 'Globally routable IP address assigned by ISPs'),
                            ('NAT', 'Network Address Translation — maps private IPs to public IPs for internet access'),
                            (   'PAT',
                                'Port Address Translation — many private IPs share one public IP using port numbers'),
                            ('RFC 1918', 'The standard defining private IPv4 address ranges')]},
    '2-5': {   'links': [   (   'Cloudflare — What is IPv6?',
                                'https://www.cloudflare.com/learning/network-layer/what-is-ipv6/'),
                            (   'Professor Messer — Network+ Course (Free)',
                                'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                            ('Hurricane Electric IPv6 Certification (Free)', 'https://ipv6.he.net/certification/')],
               'notes': 'IPv6 was created to solve IPv4 address exhaustion. It uses 128-bit addresses written as eight '
                        'groups of four hexadecimal digits separated by colons: '
                        '2001:0db8:85a3:0000:0000:8a2e:0370:7334. Leading zeros in a group can be omitted, and '
                        'consecutive groups of zeros can be replaced with :: (but only once per address). IPv6 '
                        'provides 340 undecillion addresses — essentially unlimited.\n'
                        '\n'
                        'Key IPv6 address types: unicast (one-to-one), multicast (one-to-many), anycast '
                        '(one-to-nearest). There is no broadcast in IPv6. The loopback address is ::1. Link-local '
                        'addresses start with fe80:: and are automatically assigned. Global unicast addresses '
                        '(2000::/3) are the public internet addresses. IPv6 also has built-in IPsec support and '
                        'simplified headers for faster routing.',
               'questions': [   ('How many bits are in an IPv6 address?', '128 bits'),
                                (   'What does :: represent in an IPv6 address?',
                                    'One or more consecutive groups of zeros (can only be used once per address)'),
                                ('What is the IPv6 loopback address?', '::1'),
                                (   'Does IPv6 use broadcast?',
                                    'No — IPv6 uses multicast and anycast instead of broadcast')],
               'terms': [   ('IPv6', '128-bit addressing scheme providing ~340 undecillion addresses'),
                            ('Link-Local', 'fe80::/10 — automatically assigned, only valid on local network segment'),
                            ('Global Unicast', '2000::/3 — publicly routable IPv6 addresses'),
                            (':: Notation', 'Shorthand replacing one or more consecutive groups of all-zero hextets'),
                            ('Loopback (IPv6)', '::1 — equivalent to 127.0.0.1 in IPv4')]},
    '2-6': {   'links': [   ('Subnetting Practice — Free Drill Tool', 'https://subnettingpractice.com'),
                            ('Subnet Calculator', 'https://www.subnet-calculator.com'),
                            ('CIDR.xyz — Visual Subnet Tool', 'https://cidr.xyz')],
               'notes': 'This lab focuses on hands-on subnetting practice. Subnetting is the single most important '
                        'skill for the Network+ exam — questions appear in multiple domains and performance-based '
                        'questions will test it directly. Use the block size method: find the interesting octet, '
                        'calculate block size (256 - mask value), and count up by that block size to find all '
                        'subnets.\n'
                        '\n'
                        'For speed: memorize the common prefix lengths and their properties. /24=254 hosts, /25=126, '
                        '/26=62, /27=30, /28=14, /29=6, /30=2. Practice at subnettingpractice.com until you can answer '
                        'in under 30 seconds. In the real exam you have 90 questions in 90 minutes — you cannot afford '
                        'to spend 5 minutes on a subnetting question.',
               'questions': [   (   'A host has IP 192.168.10.130/26. What subnet is it on?',
                                    '192.168.10.128/26 (block size 64: subnets at .0, .64, .128, .192)'),
                                ('How many usable hosts does a /29 provide?', '6 hosts (2^3=8, minus 2)'),
                                (   'You need 50 hosts per subnet. What is the smallest prefix that works?',
                                    '/26 — provides 62 usable hosts')],
               'terms': [   ('/25', '255.255.255.128 — 2 subnets, 126 hosts each'),
                            ('/26', '255.255.255.192 — 4 subnets, 62 hosts each'),
                            ('/27', '255.255.255.224 — 8 subnets, 30 hosts each'),
                            ('/28', '255.255.255.240 — 16 subnets, 14 hosts each'),
                            ('/29', '255.255.255.248 — 32 subnets, 6 hosts each'),
                            ('/30', '255.255.255.252 — 64 subnets, 2 hosts each (point-to-point links)')]},
    '3-1': {   'links': [   (   'Cloudflare — What is a Router?',
                                'https://www.cloudflare.com/learning/network-layer/what-is-a-router/'),
                            (   'Professor Messer — Network+ Course (Free)',
                                'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                            (   'Packet Tracer — Free Cisco Network Simulator',
                                'https://www.netacad.com/courses/packet-tracer')],
               'notes': 'A router is a Layer 3 device that forwards packets between different networks based on IP '
                        'addresses. Where a switch connects devices within the same network, a router connects '
                        'different networks together. Routers maintain a routing table — a list of known networks and '
                        'the best path to reach them. When a packet arrives, the router looks up the destination IP in '
                        'its routing table and forwards the packet out the appropriate interface.\n'
                        '\n'
                        'Routing can be static (manually configured routes) or dynamic (routes learned automatically '
                        "via protocols like OSPF, EIGRP, or BGP). The default gateway on any device is the router's IP "
                        "address — it's where traffic is sent when the destination is not on the local network. Every "
                        'time traffic crosses from one network to another, it passes through at least one router.',
               'questions': [   ('At which OSI layer do routers operate?', 'Layer 3 — Network layer'),
                                (   'What is a default gateway?',
                                    'The IP address of the router that a host sends traffic to for destinations '
                                    'outside its subnet'),
                                (   'What is the difference between a router and a switch?',
                                    'A switch forwards frames within a network using MAC addresses (L2); a router '
                                    'forwards packets between networks using IP addresses (L3)')],
               'terms': [   ('Router', 'Layer 3 device that forwards packets between networks based on IP addresses'),
                            (   'Routing Table',
                                'List of networks and next-hop addresses a router uses to forward traffic'),
                            (   'Default Gateway',
                                'The router IP address that a host sends traffic to when the destination is '
                                'off-network'),
                            ('Static Route', "Manually configured route that doesn't change automatically"),
                            ('Dynamic Routing', 'Routes learned automatically via protocols like OSPF, EIGRP, BGP')]},
    '3-3': {   'links': [   (   'Professor Messer — Network+ Course (Free)',
                                'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                            (   'Packet Tracer — Free Cisco Network Simulator',
                                'https://www.netacad.com/courses/packet-tracer'),
                            ('Cloudflare Learning Center', 'https://www.cloudflare.com/learning/')],
               'notes': 'A VLAN (Virtual LAN) logically segments a physical network into separate broadcast domains '
                        'without requiring separate physical switches. Ports on a switch are assigned to VLANs — '
                        'devices in VLAN 10 cannot communicate directly with devices in VLAN 20 without going through '
                        'a router (or Layer 3 switch). This improves security, reduces broadcast traffic, and enables '
                        'logical grouping of users regardless of physical location.\n'
                        '\n'
                        'Trunk ports carry traffic for multiple VLANs between switches using 802.1Q tagging — a 4-byte '
                        'tag is added to the frame header identifying which VLAN it belongs to. Access ports connect '
                        'to end devices and carry only one VLAN. Inter-VLAN routing requires a router or Layer 3 '
                        'switch. VLANs are essential for network segmentation — separating staff from guests, or '
                        'finance from IT.',
               'questions': [   (   'Can two devices on different VLANs communicate without a router?',
                                    'No — VLANs are separate broadcast domains; a router or L3 switch is required'),
                                ('What standard is used for VLAN tagging on trunk links?', 'IEEE 802.1Q'),
                                (   'What is the difference between a trunk port and an access port?',
                                    'Trunk port carries multiple VLANs (tagged); access port carries one VLAN '
                                    '(untagged) for end devices')],
               'terms': [   ('VLAN', 'Virtual LAN — logical network segment on a physical switch'),
                            ('802.1Q', 'The standard for VLAN tagging on trunk links'),
                            ('Trunk Port', 'Switch port carrying traffic for multiple VLANs, tagged with 802.1Q'),
                            ('Access Port', 'Switch port assigned to a single VLAN, connects to end devices'),
                            ('Inter-VLAN Routing', 'Routing traffic between VLANs using a router or Layer 3 switch')]},
    '3-4': {   'links': [   (   'Cloudflare — What is ICMP?',
                                'https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/'),
                            (   'Professor Messer — Network+ Course (Free)',
                                'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                            ('Wireshark — Free Download', 'https://www.wireshark.org/download.html')],
               'notes': 'ICMP (Internet Control Message Protocol) is used for network diagnostics and error reporting '
                        '— it operates at Layer 3 and is part of the IP suite. Ping uses ICMP Echo Request and Echo '
                        'Reply messages to test whether a host is reachable and measure round-trip time. Traceroute '
                        '(tracert on Windows) uses ICMP with incrementing TTL values to map the path packets take '
                        'across a network.\n'
                        '\n'
                        'TTL (Time to Live) is a counter in each IP packet that decrements by 1 at each router hop. '
                        "When TTL reaches 0, the router discards the packet and sends an ICMP 'Time Exceeded' message "
                        "back. Traceroute exploits this — it sends packets with TTL=1, 2, 3... and collects the 'Time "
                        "Exceeded' responses to identify each hop. ICMP is also used for 'Destination Unreachable' and "
                        "'Redirect' messages.",
               'questions': [   (   'What protocol does ping use?',
                                    'ICMP — specifically Echo Request and Echo Reply messages'),
                                (   "What happens when a packet's TTL reaches 0?",
                                    'The router discards it and sends an ICMP Time Exceeded message back to the '
                                    'source'),
                                (   'What is traceroute used for?',
                                    'Mapping the path packets take to a destination and identifying where delays or '
                                    'failures occur')],
               'terms': [   (   'ICMP',
                                'Internet Control Message Protocol — used for diagnostics and error reporting, Layer '
                                '3'),
                            ('Ping', 'Uses ICMP Echo Request/Reply to test host reachability and measure latency'),
                            (   'Traceroute',
                                'Maps the path to a destination by sending packets with incrementing TTL values'),
                            ('TTL', 'Time to Live — decrements at each router hop; packet discarded when it reaches 0'),
                            (   'Echo Request/Reply',
                                'ICMP message types used by ping (type 8 = request, type 0 = reply)')]},
    '3-5': {   'links': [   ('Wireshark — Free Download', 'https://www.wireshark.org/download.html'),
                            ('Wireshark User Guide', 'https://www.wireshark.org/docs/wsug_html_chunked/'),
                            ('Wireshark Display Filter Reference', 'https://www.wireshark.org/docs/dfref/')],
               'notes': 'Wireshark is the industry-standard free packet analyser. It captures all network traffic '
                        'passing through a network interface and displays it in a human-readable format. You can '
                        'filter by protocol (tcp, udp, icmp, dns, http), by IP address (ip.addr == 192.168.1.1), or by '
                        'port (tcp.port == 443). Wireshark is essential for troubleshooting and understanding how '
                        'protocols actually work in practice.\n'
                        '\n'
                        'For this lab: install Wireshark from wireshark.org, start a capture on your network '
                        'interface, then open a browser or run ping. Watch the packets appear. Try filtering for '
                        "'icmp' and run a ping — you'll see the Echo Request and Reply packets. Try 'dns' and browse "
                        "to a website — you'll see the DNS query and response. This hands-on practice cements the "
                        'theory in a way reading never can.',
               'questions': [   ('What Wireshark filter shows only ICMP traffic?', 'icmp'),
                                ('What Wireshark filter shows traffic to/from a specific IP?', 'ip.addr == x.x.x.x'),
                                ('What Wireshark filter shows only DNS traffic?', 'dns or udp.port == 53')],
               'terms': [   ('Packet Capture', 'Recording network traffic for analysis; also called a pcap'),
                            ('Display Filter', "Wireshark filter to show only specific traffic, e.g. 'tcp.port == 80'"),
                            ('Promiscuous Mode', 'NIC mode that captures all packets, not just those addressed to it'),
                            (   'Follow TCP Stream',
                                'Wireshark feature to reconstruct and read an entire TCP conversation'),
                            ('.pcap file', 'Standard file format for saved packet captures')]},
    '4-1': {   'links': [   ('Cloudflare — How DNS Works', 'https://www.cloudflare.com/learning/dns/what-is-dns/'),
                            ('Cloudflare — DNS Record Types', 'https://www.cloudflare.com/learning/dns/dns-records/'),
                            (   'Professor Messer — Network+ Course (Free)',
                                'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/')],
               'notes': 'DNS (Domain Name System) translates human-readable domain names into IP addresses. When you '
                        'type google.com, your device sends a DNS query to a resolver (usually your ISP or a public '
                        'resolver like 8.8.8.8). The resolver checks its cache, then queries root servers, then TLD '
                        'servers (.com), then the authoritative name server for google.com, which returns the IP '
                        'address.\n'
                        '\n'
                        'This hierarchical process is called recursive resolution. The result is cached at multiple '
                        'levels to speed up future queries — TTL (Time to Live) in the DNS record controls how long '
                        "it's cached. DNS operates on port 53 and uses UDP for queries (fast) and TCP for zone "
                        'transfers (reliable). Understanding DNS is critical for troubleshooting connectivity issues — '
                        "'it's always DNS' is a famous sysadmin joke because DNS failures cause so many apparent "
                        'outages.',
               'questions': [   ('What port does DNS use?', 'Port 53 (UDP for queries, TCP for zone transfers)'),
                                (   'What is the role of an authoritative name server?',
                                    'It holds the actual DNS records for a domain and answers queries about it '
                                    'definitively'),
                                (   'Why does DNS caching matter?',
                                    'It speeds up resolution by avoiding repeated queries and reduces load on DNS '
                                    'servers')],
               'terms': [   ('DNS', 'Domain Name System — translates domain names to IP addresses'),
                            ('Resolver', 'The DNS server your device queries; usually your ISP or 8.8.8.8'),
                            ('Authoritative Name Server', 'The server that holds the actual DNS records for a domain'),
                            ('Root Server', 'Top of the DNS hierarchy; 13 sets worldwide; knows where TLD servers are'),
                            ('DNS Cache', 'Temporary storage of DNS query results to speed up future lookups'),
                            ('TTL', 'Time to Live — how long a DNS record is cached before being refreshed')]},
    '4-2': {   'links': [   (   'Cloudflare — What is DHCP?',
                                'https://www.cloudflare.com/learning/network-layer/what-is-dhcp/'),
                            (   'Professor Messer — Network+ Course (Free)',
                                'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                            (   'Packet Tracer — Free Cisco Network Simulator',
                                'https://www.netacad.com/courses/packet-tracer')],
               'notes': 'DHCP (Dynamic Host Configuration Protocol) automatically assigns IP addresses and network '
                        'configuration to devices. Without DHCP, every device would need a manually configured IP, '
                        'subnet mask, default gateway, and DNS server. DHCP uses a four-step process called DORA: '
                        'Discover (client broadcasts looking for a DHCP server), Offer (server offers an IP address), '
                        'Request (client requests the offered address), Acknowledge (server confirms the lease).\n'
                        '\n'
                        'DHCP leases are temporary — devices must renew them periodically. A DHCP scope defines the '
                        'range of addresses the server can assign. DHCP can also assign options: default gateway, DNS '
                        'servers, domain name, NTP server. DHCP Relay (ip helper-address on Cisco) forwards DHCP '
                        'broadcasts across routers so one DHCP server can serve multiple subnets. DHCP uses UDP ports '
                        '67 (server) and 68 (client).',
               'questions': [   ('What does DORA stand for?', 'Discover, Offer, Request, Acknowledge'),
                                ('What ports does DHCP use?', 'UDP 67 (server) and UDP 68 (client)'),
                                (   'What is a DHCP scope?',
                                    'The range of IP addresses a DHCP server is configured to assign'),
                                (   'Why is DHCP Relay needed?',
                                    "DHCP uses broadcasts which don't cross routers; relay forwards DHCP messages "
                                    'across subnets')],
               'terms': [   (   'DHCP',
                                'Dynamic Host Configuration Protocol — automatically assigns IP configuration to '
                                'hosts'),
                            ('DORA', 'Discover, Offer, Request, Acknowledge — the four steps of DHCP'),
                            ('DHCP Lease', 'Temporary assignment of an IP address; must be renewed'),
                            ('DHCP Scope', 'The pool of IP addresses a DHCP server can assign'),
                            ('DHCP Relay', 'Forwards DHCP broadcasts across routers (ip helper-address)'),
                            ('Ports 67/68', 'DHCP server listens on 67; client on 68; both use UDP')]},
    '4-3': {   'links': [   (   'Cloudflare — What is a Firewall?',
                                'https://www.cloudflare.com/learning/security/what-is-a-firewall/'),
                            (   'Cloudflare — IDS vs IPS',
                                'https://www.cloudflare.com/learning/security/glossary/intrusion-detection-prevention/'),
                            (   'Professor Messer — Network+ Course (Free)',
                                'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/')],
               'notes': 'A firewall filters traffic based on rules, blocking unauthorised access while allowing '
                        'legitimate traffic. Stateful firewalls track the state of connections — they know whether an '
                        'incoming packet is part of an established connection or a new unsolicited one. Next-gen '
                        'firewalls (NGFW) add deep packet inspection, application awareness, and intrusion '
                        'prevention.\n'
                        '\n'
                        'An IDS (Intrusion Detection System) monitors traffic and alerts on suspicious activity but '
                        "doesn't block it. An IPS (Intrusion Prevention System) actively blocks threats in real time — "
                        'it sits inline in the network path. A load balancer distributes incoming traffic across '
                        'multiple servers to prevent overload and provide redundancy. These devices all appear in the '
                        "Network+ exam's security and infrastructure domains.",
               'questions': [   (   'What is the difference between an IDS and an IPS?',
                                    'IDS detects and alerts (passive); IPS detects and blocks (active, inline)'),
                                (   'What makes a stateful firewall different from a simple packet filter?',
                                    'A stateful firewall tracks connection state so it can distinguish established '
                                    'traffic from new unsolicited connections'),
                                (   'What does a load balancer do?',
                                    'Distributes incoming connections across multiple servers to balance load and '
                                    'provide redundancy')],
               'terms': [   ('Firewall', 'Filters network traffic based on rules; blocks unauthorised access'),
                            (   'Stateful Firewall',
                                'Tracks connection state; knows if traffic is part of an established session'),
                            ('IDS', 'Intrusion Detection System — monitors and alerts on suspicious traffic; passive'),
                            ('IPS', 'Intrusion Prevention System — monitors and actively blocks threats; inline'),
                            (   'Load Balancer',
                                'Distributes traffic across multiple servers for performance and redundancy')]},
    '5-2': {   'links': [   (   'Cloudflare — TLS Explained',
                                'https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/'),
                            (   'Cloudflare — What is a VPN?',
                                'https://www.cloudflare.com/learning/access-management/what-is-a-vpn/'),
                            (   'Professor Messer — Network+ Course (Free)',
                                'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/')],
               'notes': 'Encryption protects data in transit from eavesdropping. TLS (Transport Layer Security) is the '
                        'current standard for encrypting web traffic — HTTPS is HTTP over TLS. TLS uses a handshake to '
                        'negotiate encryption algorithms and exchange keys before data is transmitted. SSL is the '
                        "predecessor to TLS and is now deprecated and insecure — but the term 'SSL' is still commonly "
                        '(incorrectly) used to mean TLS.\n'
                        '\n'
                        'A VPN (Virtual Private Network) creates an encrypted tunnel across an untrusted network (like '
                        'the internet). Site-to-site VPNs connect entire offices. Client VPNs let remote workers '
                        'securely access company resources. IPsec is a suite of protocols for encrypting IP traffic — '
                        'used heavily in VPNs. It operates in tunnel mode (encrypts the entire packet) or transport '
                        'mode (encrypts just the payload). OpenVPN and WireGuard are popular open-source VPN '
                        'protocols.',
               'questions': [   (   'What is the difference between SSL and TLS?',
                                    'SSL is deprecated and insecure; TLS is its secure successor. Most references to '
                                    "'SSL' today actually mean TLS"),
                                ('What port does HTTPS use?', '443'),
                                (   'What is the difference between site-to-site and client VPN?',
                                    'Site-to-site connects two networks permanently; client VPN connects an individual '
                                    "user's device to a network")],
               'terms': [   ('TLS', 'Transport Layer Security — encrypts data in transit; successor to SSL'),
                            ('HTTPS', 'HTTP over TLS — encrypted web browsing on port 443'),
                            ('VPN', 'Virtual Private Network — encrypted tunnel over an untrusted network'),
                            ('IPsec', 'IP Security — suite of protocols for encrypting IP traffic, used in VPNs'),
                            ('Tunnel Mode', 'IPsec mode that encrypts the entire IP packet including headers'),
                            ('SSL', 'Secure Sockets Layer — deprecated predecessor to TLS; no longer secure')]},
    '5-3': {   'links': [   (   'Cloudflare — DDoS Explained',
                                'https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/'),
                            (   'Cloudflare — What is a MITM Attack?',
                                'https://www.cloudflare.com/learning/security/threats/man-in-the-middle-attack/'),
                            (   'Professor Messer — Network+ Course (Free)',
                                'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/')],
               'notes': 'Common network attacks you must know for Network+: A Man-in-the-Middle (MITM) attack '
                        'intercepts communication between two parties — the attacker secretly relays and potentially '
                        "alters messages. ARP Spoofing/Poisoning sends fake ARP replies to associate the attacker's "
                        'MAC with a legitimate IP, enabling MITM on local networks. A DoS (Denial of Service) attack '
                        'floods a target with traffic to overwhelm it; a DDoS uses many compromised systems '
                        'simultaneously.\n'
                        '\n'
                        'Other attacks: VLAN Hopping allows an attacker to send traffic to a different VLAN by '
                        'exploiting trunk ports. DNS Spoofing/Poisoning inserts false DNS records to redirect users to '
                        'malicious sites. A Rogue DHCP server gives clients incorrect network configuration. '
                        'Recognising these attacks and knowing their mitigations is a significant portion of the '
                        'Network+ security domain.',
               'questions': [   (   'How does ARP spoofing enable a MITM attack?',
                                    'The attacker sends fake ARP replies mapping their MAC to a legitimate IP, so '
                                    'traffic intended for that IP goes to the attacker instead'),
                                (   'What is the difference between DoS and DDoS?',
                                    'DoS is from one source; DDoS uses many compromised systems (botnet) to overwhelm '
                                    'the target'),
                                (   'What mitigation prevents rogue DHCP servers?',
                                    'DHCP snooping on switches — only trusted ports can send DHCP offers')],
               'terms': [   ('MITM', 'Man-in-the-Middle — attacker intercepts communication between two parties'),
                            (   'ARP Spoofing',
                                "Sending fake ARP replies to associate attacker's MAC with a legitimate IP"),
                            ('DoS', 'Denial of Service — flooding a target to make it unavailable'),
                            ('DDoS', 'Distributed DoS — DoS using many compromised systems simultaneously'),
                            ('VLAN Hopping', 'Exploiting trunk port configuration to send traffic to another VLAN'),
                            ('Rogue DHCP', 'Unauthorised DHCP server giving clients incorrect network configuration')]},
    '5-4': {   'links': [   (   'Professor Messer — Network+ Course (Free)',
                                'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                            (   'Cloudflare — What is 802.1X?',
                                'https://www.cloudflare.com/learning/access-management/what-is-802.1x/'),
                            (   'ExamCompass — Free Network+ Practice',
                                'https://www.comptia.org/training/certmaster-practice/network')],
               'notes': 'Authentication protocols verify the identity of users and devices trying to access a network. '
                        'RADIUS (Remote Authentication Dial-In User Service) is a centralised AAA (Authentication, '
                        'Authorisation, Accounting) protocol. When a user tries to connect to a network, the '
                        'authenticator (e.g. a switch or VPN server) forwards credentials to the RADIUS server, which '
                        'approves or denies access. RADIUS uses UDP ports 1812/1813.\n'
                        '\n'
                        'TACACS+ (Terminal Access Controller Access-Control System Plus) is a Cisco proprietary AAA '
                        'protocol that encrypts the entire payload (RADIUS only encrypts the password). TACACS+ uses '
                        'TCP port 49 and separates authentication, authorisation, and accounting into separate '
                        'functions. RADIUS is typically used for network access (Wi-Fi, VPN); TACACS+ is used for '
                        'device administration (router/switch login). 802.1X is a port-based access control standard '
                        "that uses RADIUS for authenticating devices before they're allowed network access.",
               'questions': [   ('What ports does RADIUS use?', 'UDP 1812 (authentication) and 1813 (accounting)'),
                                (   'What is the key security difference between RADIUS and TACACS+?',
                                    'TACACS+ encrypts the entire packet; RADIUS only encrypts the password'),
                                ('What does AAA stand for?', 'Authentication, Authorisation, Accounting'),
                                ('What protocol is used with 802.1X?', 'RADIUS')],
               'terms': [   ('RADIUS', 'Remote Authentication Dial-In User Service — centralised AAA; UDP 1812/1813'),
                            ('TACACS+', 'Cisco AAA protocol; encrypts full payload; TCP port 49'),
                            (   'AAA',
                                'Authentication (who are you?), Authorisation (what can you do?), Accounting (what did '
                                'you do?)'),
                            (   '802.1X',
                                'Port-based network access control; uses RADIUS to authenticate devices before network '
                                'access'),
                            (   'Authenticator',
                                'The device (switch, AP) that forwards credentials to the RADIUS server')]},
    '5-5': {   'links': [   (   'Professor Messer — Free Practice Exams',
                                'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                            (   'ExamCompass — Free Network+ Quizzes',
                                'https://www.comptia.org/training/certmaster-practice/network'),
                            (   'CompTIA Network+ Exam Objectives (Free PDF)',
                                'https://www.comptia.org/training/resources/exam-objectives')],
               'notes': 'This is a review quiz for Module 6 — Network Security. Security is one of the most heavily '
                        'weighted domains on the Network+ exam. Make sure you can identify attack types, explain '
                        'mitigation strategies, distinguish encryption protocols, and understand authentication '
                        'frameworks.\n'
                        '\n'
                        'Key areas to be solid on: port numbers for security protocols (SSH=22, HTTPS=443, '
                        'RADIUS=1812), the difference between IDS and IPS, WPA2 vs WPA3, RADIUS vs TACACS+, and common '
                        'network attacks with their mitigations.',
               'questions': [   ('What port does SSH use?', '22'),
                                (   'Why is Telnet insecure?',
                                    'Telnet transmits data including passwords in plaintext — anyone on the network '
                                    'can intercept it'),
                                (   'What is the difference between IDS and IPS?',
                                    'IDS detects and alerts (passive); IPS detects and blocks (active/inline)'),
                                (   'Which wireless security protocol should be used on enterprise networks?',
                                    'WPA2-Enterprise or WPA3-Enterprise with 802.1X authentication'),
                                (   'What does DHCP snooping prevent?',
                                    'Rogue DHCP servers — only trusted ports can send DHCP offers')],
               'terms': [   ('SSH', 'Secure Shell — encrypted remote access; port 22; replacement for Telnet'),
                            ('Telnet', 'Unencrypted remote access; port 23; never use on production networks'),
                            ('SNMP', 'Simple Network Management Protocol — network monitoring; port 161 (UDP)'),
                            ('Syslog', 'Standard for sending log messages; UDP port 514')]},
    '6-2': {   'links': [   ('Wi-Fi Alliance — Security Overview', 'https://www.wi-fi.org/discover-wi-fi/security'),
                            (   'Cloudflare — WPA3 Explained',
                                'https://www.cloudflare.com/learning/network-layer/what-is-wpa3/'),
                            (   'Professor Messer — Network+ Course (Free)',
                                'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/')],
               'notes': 'Wireless security has evolved significantly. WEP (Wired Equivalent Privacy) was the original '
                        'standard but is completely broken and should never be used. WPA (Wi-Fi Protected Access) '
                        'improved on WEP but also has vulnerabilities. WPA2 uses AES encryption and is the current '
                        'standard for home and business networks — WPA2-Personal uses a pre-shared key (PSK); '
                        'WPA2-Enterprise uses 802.1X with RADIUS for per-user authentication.\n'
                        '\n'
                        'WPA3 is the latest standard with stronger encryption and protection against offline '
                        'dictionary attacks. It uses SAE (Simultaneous Authentication of Equals) instead of PSK. For '
                        'enterprise networks, WPA2/WPA3-Enterprise with 802.1X is the gold standard — each user '
                        'authenticates individually and a compromised password only affects one account. Common '
                        'wireless attacks include evil twin (rogue AP), deauth attacks, and WPS brute-forcing (disable '
                        'WPS on all networks).',
               'questions': [   (   'Why should WEP never be used?',
                                    "WEP's encryption is completely broken and can be cracked in minutes with freely "
                                    'available tools'),
                                (   'What is the difference between WPA2-Personal and WPA2-Enterprise?',
                                    'Personal uses a shared passphrase; Enterprise uses 802.1X with individual user '
                                    'credentials via RADIUS'),
                                (   "What attack does WPA3 protect against that WPA2 doesn't?",
                                    "Offline dictionary attacks — WPA3's SAE handshake doesn't allow captured "
                                    'handshakes to be brute-forced offline')],
               'terms': [   (   'WEP',
                                'Wired Equivalent Privacy — original wireless security; completely broken; never use'),
                            ('WPA2-Personal', 'Uses a pre-shared key (PSK/passphrase); suitable for home networks'),
                            (   'WPA2-Enterprise',
                                'Uses 802.1X and RADIUS for individual user authentication; business standard'),
                            ('WPA3', 'Latest Wi-Fi security standard; SAE handshake; resistant to offline attacks'),
                            ('Evil Twin', 'Rogue access point mimicking a legitimate one to capture traffic'),
                            ('SAE', 'Simultaneous Authentication of Equals — WPA3 handshake replacing PSK')]},
    '6-5': {   'links': [   (   'Professor Messer — Free Practice Exams',
                                'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                            (   'ExamCompass — Free Network+ Quizzes',
                                'https://www.comptia.org/training/certmaster-practice/network'),
                            (   'CompTIA Network+ Exam Objectives (Free PDF)',
                                'https://www.comptia.org/training/resources/exam-objectives')],
               'notes': 'This is a review quiz for Module 6 — Network Security. Security is one of the most heavily '
                        'weighted domains on the Network+ exam. Make sure you can identify attack types, explain '
                        'mitigation strategies, distinguish encryption protocols, and understand authentication '
                        'frameworks.\n'
                        '\n'
                        'Key areas to be solid on: port numbers for security protocols (SSH=22, HTTPS=443, '
                        'RADIUS=1812), the difference between IDS and IPS, WPA2 vs WPA3, RADIUS vs TACACS+, and common '
                        'network attacks with their mitigations.',
               'questions': [   ('What port does SSH use?', '22'),
                                (   'Why is Telnet insecure?',
                                    'Telnet transmits data including passwords in plaintext — anyone on the network '
                                    'can intercept it'),
                                (   'What is the difference between IDS and IPS?',
                                    'IDS detects and alerts (passive); IPS detects and blocks (active/inline)'),
                                (   'Which wireless security protocol should be used on enterprise networks?',
                                    'WPA2-Enterprise or WPA3-Enterprise with 802.1X authentication'),
                                (   'What does DHCP snooping prevent?',
                                    'Rogue DHCP servers — only trusted ports can send DHCP offers')],
               'terms': [   ('SSH', 'Secure Shell — encrypted remote access; port 22; replacement for Telnet'),
                            ('Telnet', 'Unencrypted remote access; port 23; never use on production networks'),
                            ('SNMP', 'Simple Network Management Protocol — network monitoring; port 161 (UDP)'),
                            ('Syslog', 'Standard for sending log messages; UDP port 514')]},
    '7-1': {   'links': [   (   'Professor Messer — Network+ Course (Free)',
                                'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                            (   'CompTIA Network+ Exam Objectives (Free PDF)',
                                'https://www.comptia.org/training/resources/exam-objectives'),
                            (   'ExamCompass — Free Network+ Practice',
                                'https://www.comptia.org/training/certmaster-practice/network')],
               'notes': "CompTIA's official troubleshooting methodology has seven steps: 1) Identify the problem — "
                        'gather information and symptoms. 2) Establish a theory of probable cause — what do you think '
                        'is wrong? 3) Test the theory — confirm or deny your hypothesis. 4) Establish a plan of action '
                        '— how will you fix it with minimal disruption? 5) Implement the solution — make the change. '
                        '6) Verify full functionality — confirm the fix worked and nothing else broke. 7) Document '
                        'findings — record what happened and how you fixed it.\n'
                        '\n'
                        'In practice, experienced engineers often jump to step 2 based on intuition — but the '
                        'methodology exists to avoid missing obvious causes. Always start at Layer 1 (is the cable '
                        'plugged in?) and work up. The OSI model is your troubleshooting map: Physical → Data Link → '
                        'Network → Transport → Application.',
               'questions': [   (   "What is the first step in CompTIA's troubleshooting methodology?",
                                    'Identify the problem — gather information, question users, observe symptoms'),
                                (   'Why is documentation the final step?',
                                    'To create a record for future reference, track recurring issues, and help other '
                                    'engineers'),
                                (   'If a user can ping by IP but not by name, which layer/service is the problem?',
                                    'DNS — name resolution failure (application layer service)')],
               'terms': [   (   'Troubleshooting Methodology',
                                "CompTIA's 7-step process: Identify, Theory, Test, Plan, Implement, Verify, Document"),
                            (   'Bottom-Up Approach',
                                'Start troubleshooting at Layer 1 (physical) and work up through OSI layers'),
                            (   'Top-Down Approach',
                                'Start at Layer 7 (application) and work down — used when software issues are '
                                'suspected'),
                            (   'Divide and Conquer',
                                'Start at Layer 3 (network) and work up or down based on test results'),
                            (   'Documentation',
                                'Recording the problem, cause, and solution — essential for future reference')]},
    '7-2': {   'links': [   ('SS64 — Windows Command Reference', 'https://ss64.com/nt/'),
                            ('SS64 — Linux Command Reference', 'https://ss64.com/bash/'),
                            ('MXToolbox — Network Tools', 'https://mxtoolbox.com/NetworkTools.aspx')],
               'notes': 'Essential CLI tools for every network engineer. ping tests basic connectivity — if it fails, '
                        'work down the OSI model. tracert (Windows) / traceroute (Linux) shows the path to a '
                        'destination and identifies where failures or latency occur. netstat shows active connections, '
                        "listening ports, and network statistics — useful for finding what's using a port or how many "
                        'connections exist. arp -a shows the ARP cache; arp -d clears it.\n'
                        '\n'
                        'route print (Windows) / ip route (Linux) shows the routing table — essential for diagnosing '
                        'routing issues. nslookup and dig diagnose DNS. netstat -an shows all connections and '
                        'listening ports numerically. On Cisco devices: show ip interface brief, show ip route, show '
                        'mac address-table, show vlan brief, and show running-config are the essential show commands. '
                        "Practice all of these until they're instinctive.",
               'questions': [   (   'A user can ping 8.8.8.8 but not google.com. What is likely wrong?',
                                    "DNS resolution is failing — the IP stack works but name resolution doesn't"),
                                ('What command shows which ports are listening on a Windows machine?', 'netstat -an'),
                                (   'What does traceroute help you identify?',
                                    'The path packets take and where failures or high latency occur along the route')],
               'terms': [   ('ping', 'Tests ICMP reachability; measures round-trip time'),
                            ('tracert/traceroute', 'Maps the path to a destination hop by hop'),
                            ('netstat', 'Shows active connections and listening ports'),
                            ('netstat -an', 'Shows all connections and ports numerically (no DNS resolution)'),
                            ('route print', 'Shows the Windows routing table (ip route on Linux)'),
                            ('arp -a', 'Displays the ARP cache — IP to MAC address mappings')]},
    '7-3': {   'links': [   ('draw.io — Free Network Diagram Tool', 'https://app.diagrams.net'),
                            ('Lucidchart — Network Diagram Tool', 'https://www.lucidchart.com/pages/network-diagram'),
                            (   'Packet Tracer — Free Cisco Network Simulator',
                                'https://www.netacad.com/courses/packet-tracer')],
               'notes': 'Network diagrams visually represent the layout of a network. A physical diagram shows actual '
                        'hardware locations, cable runs, and rack layouts. A logical diagram shows IP addressing, '
                        'VLANs, routing, and how traffic flows — regardless of physical location. Both types appear in '
                        'Network+ performance-based questions.\n'
                        '\n'
                        'Standard symbols: clouds represent the internet or an ISP, cylinders represent servers, '
                        'rectangles are switches, the routing symbol is a circle with arrows, firewalls are '
                        'represented by brick wall icons (varies by tool). Cisco uses specific icons for its devices. '
                        'Being able to read and draw network diagrams is essential for planning, documentation, and '
                        'troubleshooting. Tools like draw.io (free) or Lucidchart are commonly used.',
               'questions': [   (   'What is the difference between a physical and logical network diagram?',
                                    'Physical shows actual hardware and cables; logical shows IP addressing and '
                                    'traffic flow'),
                                (   'Why are network diagrams important for troubleshooting?',
                                    'They provide a reference for understanding how the network is connected, making '
                                    'it faster to identify where a failure might be')],
               'terms': [   ('Physical Diagram', 'Shows actual hardware, locations, and cable connections'),
                            (   'Logical Diagram',
                                'Shows IP addressing, VLANs, and traffic flow regardless of physical layout'),
                            ('Network Topology', 'The arrangement of network components shown in a diagram'),
                            ('Rack Diagram', 'Shows equipment installed in server racks with U-space measurements'),
                            ('draw.io', 'Free online tool for creating network diagrams')]},
    '7-4': {   'links': [   (   'Professor Messer — Network+ Course (Free)',
                                'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                            (   'ExamCompass — Free Network+ Practice',
                                'https://www.comptia.org/training/certmaster-practice/network'),
                            (   'Packet Tracer — Free Cisco Network Simulator',
                                'https://www.netacad.com/courses/packet-tracer')],
               'notes': 'Troubleshooting scenarios test your ability to apply methodology and tools to realistic '
                        'problems. Common scenarios: 1) Duplicate IP address — two devices share an IP; symptoms are '
                        'intermittent connectivity for both. Fix: use arp -a to find the conflict, assign a unique IP. '
                        "2) Wrong subnet mask — device can't reach some hosts but not others. Fix: ipconfig /all to "
                        'verify mask. 3) Default gateway missing — device can reach local network but not the '
                        'internet. Fix: verify gateway config. 4) DNS failure — can ping IPs but not names. Fix: '
                        'nslookup to test, check DNS server assignment.\n'
                        '\n'
                        '5) Switching loop — broadcast storm, all ports at 100%, network unusable. Fix: STP should '
                        'prevent this; check for disabled STP or non-managed switches. 6) VLAN mismatch — devices on '
                        "the wrong VLAN can't communicate. Fix: verify switchport access vlan on Cisco. Practice "
                        "recognising these patterns — they're exactly what appears in Network+ performance-based "
                        'questions.',
               'questions': [   (   'A device gets a 169.254.x.x address. What does this indicate?',
                                    'APIPA — the device failed to get a DHCP lease; check DHCP server and '
                                    'connectivity'),
                                (   'A user can reach local servers but not the internet. What should you check first?',
                                    'The default gateway — it may be missing, wrong, or the router may be down'),
                                (   'What protocol prevents switching loops?',
                                    'STP — Spanning Tree Protocol (or RSTP, the faster version)')],
               'terms': [   ('Duplicate IP', 'Two devices with the same IP; causes intermittent connectivity for both'),
                            ('Broadcast Storm', 'Network flooding caused by a switching loop; STP prevents this'),
                            ('STP', 'Spanning Tree Protocol — prevents switching loops by blocking redundant paths'),
                            (   'APIPA',
                                '169.254.x.x — automatic address assigned when DHCP fails; indicates DHCP problem'),
                            (   'Default Gateway',
                                'Missing or wrong gateway = can reach local network but not internet')]},
    '8-5': {   'links': [   (   'Professor Messer — Free Practice Exams',
                                'https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/'),
                            (   'ExamCompass — Free Network+ Quizzes',
                                'https://www.comptia.org/training/certmaster-practice/network'),
                            (   'CompTIA CertMaster Practice (Official)',
                                'https://www.comptia.org/training/certmaster-practice/network')],
               'notes': 'This is your full timed practice exam. Set a timer for 90 minutes and attempt all questions '
                        'without looking anything up. Treat it exactly like the real exam. When you finish, review '
                        'every wrong answer — not just the right answer, but why the other options were wrong. This is '
                        'how you learn the most.\n'
                        '\n'
                        'After the practice exam, identify your weak domains and return to those modules. Aim for 80%+ '
                        "on practice exams before sitting the real thing. Professor Messer's practice exams and "
                        "ExamCompass are excellent free resources. Jason Dion's Udemy course includes high-quality "
                        'practice exams. Remember: the real exam has scenario-based questions that test application, '
                        'not just memorisation.',
               'questions': [   (   'What score should you aim for on practice exams before sitting the real test?',
                                    '80% or higher consistently across multiple practice exams'),
                                (   'What should you do after reviewing wrong answers?',
                                    'Understand WHY each wrong answer was wrong, not just what the right answer is — '
                                    'this prevents the same mistake twice')],
               'terms': [   (   'Process of Elimination',
                                'On tricky questions, eliminate obviously wrong answers first to improve odds'),
                            (   'Keyword Analysis',
                                "Read questions carefully for words like 'MOST', 'BEST', 'LEAST', 'NOT' — they change "
                                'the answer'),
                            (   'Flag and Return',
                                "Flag uncertain questions and return to them — don't spend too long on any single "
                                'question')]},}
