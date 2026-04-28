LESSON_CONTENT = {
    "1-1": {
        "notes": "A network is two or more devices connected together to share resources and communicate. The most common types are LANs (Local Area Networks), which cover a small geographic area like an office or home, WANs (Wide Area Networks), which span large distances and connect multiple LANs together, and MANs (Metropolitan Area Networks), which cover a city or campus. The internet itself is the largest WAN in existence.\n\nNetworks exist to share resources — files, printers, internet connections — and to enable communication between devices. Every device on a network needs a unique address so data can be delivered to the right place. Understanding these basic building blocks is the foundation for everything else in networking.",
        "terms": [
            ("LAN", "Local Area Network — a network confined to a small area like a home, office, or building"),
            ("WAN", "Wide Area Network — a network spanning large geographic distances, connecting multiple LANs"),
            ("MAN", "Metropolitan Area Network — covers a city or large campus, larger than LAN but smaller than WAN"),
            ("Node", "Any device connected to a network (computer, printer, switch, router)"),
            ("Bandwidth", "The maximum amount of data that can be transmitted over a network in a given time, measured in bits per second"),
        ],
        "questions": [
            ("What type of network would connect two offices in different countries?", "A WAN (Wide Area Network)"),
            ("What is the key difference between a LAN and a WAN?", "A LAN is limited to a small geographic area; a WAN spans large distances and connects multiple LANs"),
            ("What does every device on a network need to communicate?", "A unique address (IP address and/or MAC address)"),
        ],
        "links": [
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
            ("Cloudflare Learning — What is a Network?", "https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/"),
            ("CompTIA Network+ Exam Objectives (Free PDF)", "https://www.comptia.org/training/resources/exam-objectives"),
        ]
    },
    "1-2": {
        "notes": "Network topology describes the physical or logical arrangement of devices on a network. In a star topology, all devices connect to a central switch or hub — it's the most common in modern networks because a single cable failure only affects one device. In a bus topology, all devices share a single cable; if that cable breaks the whole network goes down. Ring topologies connect devices in a circular chain, where data travels in one direction around the ring.\n\nMesh topologies connect every device to every other device, providing maximum redundancy — if one path fails, data takes another route. Full mesh is expensive but used in critical infrastructure. Partial mesh is a compromise. Understanding topologies helps you design reliable networks and troubleshoot failures efficiently.",
        "terms": [
            ("Star Topology", "All devices connect to a central switch; most common modern topology"),
            ("Bus Topology", "All devices share a single cable backbone; a break affects the whole network"),
            ("Ring Topology", "Devices connected in a circle; data travels in one direction"),
            ("Mesh Topology", "Every device connects to every other; maximum redundancy"),
            ("Topology", "The arrangement or layout of devices and connections in a network"),
        ],
        "questions": [
            ("Which topology is most fault-tolerant?", "Mesh — multiple paths exist between devices so a single failure doesn't break the network"),
            ("In a star topology, what happens if the central switch fails?", "The entire network goes down as all devices depend on the central switch"),
            ("Which legacy topology used a single shared cable for all devices?", "Bus topology"),
        ],
        "links": [
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
            ("Cloudflare Learning Center", "https://www.cloudflare.com/learning/"),
            ("ExamCompass — Free Network+ Practice", "https://www.comptia.org/training/certmaster-practice/network"),
        ]
    },
    "1-3": {
        "notes": "The OSI (Open Systems Interconnection) model is a 7-layer framework that describes how data travels from one device to another across a network. Each layer has a specific job and communicates with the layers above and below it. From top to bottom: Application (layer 7) is where user-facing software lives; Presentation (6) handles data formatting and encryption; Session (5) manages connections; Transport (4) handles reliable delivery with TCP/UDP; Network (3) handles IP addressing and routing; Data Link (2) handles MAC addresses and switches; Physical (1) is the actual cables and signals.\n\nThe OSI model is critical for the Network+ exam and for troubleshooting. When something goes wrong, you work from layer 1 upward — is the cable plugged in? Is the IP address correct? Is the application configured properly? Every networking concept maps to a specific OSI layer.",
        "terms": [
            ("OSI Model", "A 7-layer conceptual framework describing how network communication works"),
            ("Layer 1 — Physical", "Cables, signals, network interface cards, hubs"),
            ("Layer 2 — Data Link", "MAC addresses, switches, frames, error detection"),
            ("Layer 3 — Network", "IP addresses, routers, packets, routing"),
            ("Layer 4 — Transport", "TCP/UDP, ports, segmentation, reliable delivery"),
            ("Layer 7 — Application", "HTTP, FTP, DNS, SMTP — user-facing protocols"),
        ],
        "questions": [
            ("At which OSI layer do routers operate?", "Layer 3 — Network layer (routers forward packets based on IP addresses)"),
            ("At which OSI layer do switches operate?", "Layer 2 — Data Link layer (switches forward frames based on MAC addresses)"),
            ("Which layer is responsible for encryption and data formatting?", "Layer 6 — Presentation layer"),
        ],
        "links": [
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
            ("Cloudflare — OSI Model Explained", "https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/"),
            ("TryHackMe — Free Networking Rooms", "https://tryhackme.com/hacktivities?tab=practice"),
        ]
    },
    "1-4": {
        "notes": "While the OSI model has 7 layers, the TCP/IP model is the practical framework that the internet actually uses, with 4 layers. The Application layer maps to OSI layers 5-7 and handles protocols like HTTP, DNS, and SMTP. The Transport layer (same as OSI layer 4) handles TCP and UDP. The Internet layer maps to OSI layer 3 and handles IP addressing. The Network Access layer maps to OSI layers 1-2 and handles physical transmission.\n\nThe TCP/IP model is what you'll use day-to-day in real networking. The OSI model is more of a teaching tool and troubleshooting reference. The Network+ exam tests both — you need to know which OSI layers map to which TCP/IP layers and what protocols live at each layer of both models.",
        "terms": [
            ("TCP/IP Model", "A 4-layer practical networking model used by the internet"),
            ("Application Layer", "Top layer handling HTTP, DNS, SMTP, FTP (maps to OSI 5-7)"),
            ("Transport Layer", "Handles TCP and UDP (maps to OSI layer 4)"),
            ("Internet Layer", "Handles IP addressing and routing (maps to OSI layer 3)"),
            ("Network Access Layer", "Handles physical transmission and MAC addressing (maps to OSI 1-2)"),
        ],
        "questions": [
            ("How many layers does the TCP/IP model have?", "4 layers: Application, Transport, Internet, Network Access"),
            ("Which TCP/IP layer corresponds to OSI layers 5, 6, and 7?", "The Application layer"),
            ("What is the main difference between OSI and TCP/IP models?", "OSI has 7 layers and is a conceptual reference model; TCP/IP has 4 layers and is the practical model the internet uses"),
        ],
        "links": [
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
            ("Cloudflare Learning Center", "https://www.cloudflare.com/learning/"),
            ("CompTIA Network+ Exam Objectives", "https://www.comptia.org/training/resources/exam-objectives"),
        ]
    },
    "1-5": {
        "notes": "This is a review quiz for Module 1. Test your understanding of network types, topologies, and the OSI and TCP/IP models before moving on. These concepts underpin everything in the rest of the course — if any answers are unclear, review the relevant lesson before continuing.\n\nTip for the exam: OSI layer numbers and what operates at each layer is one of the most frequently tested topics on Network+. Make sure you can name all 7 layers in order and give an example of a protocol or device at each one.",
        "terms": [
            ("Mnemonic for OSI layers (top to bottom)", "All People Seem To Need Data Processing — Application, Presentation, Session, Transport, Network, Data Link, Physical"),
            ("Mnemonic (bottom to top)", "Please Do Not Throw Sausage Pizza Away"),
        ],
        "questions": [
            ("Name the 7 OSI layers in order from layer 1 to layer 7.", "Physical, Data Link, Network, Transport, Session, Presentation, Application"),
            ("What type of network covers a single building?", "LAN — Local Area Network"),
            ("Which topology provides the most redundancy?", "Mesh topology"),
            ("At which OSI layer does IP addressing occur?", "Layer 3 — Network layer"),
            ("What are the 4 layers of the TCP/IP model?", "Network Access, Internet, Transport, Application"),
        ],
        "links": [
            ("Professor Messer — Free Practice Exams", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
            ("ExamCompass — Free Network+ Quizzes", "https://www.comptia.org/training/certmaster-practice/network"),
            ("CompTIA CertMaster Learn (Official)", "https://www.comptia.org/training/certmaster-learn/network"),
        ]
    },
    "2-1": {
        "notes": "An IPv4 address is a 32-bit number written as four octets in dotted decimal notation (e.g. 192.168.1.1). Each octet is 8 bits and can range from 0 to 255. IPv4 addresses were originally divided into classes: Class A (1-126 in first octet) for large networks with millions of hosts; Class B (128-191) for medium networks; Class C (192-223) for small networks up to 254 hosts. Class D (224-239) is used for multicast and Class E (240-255) is reserved.\n\nClassful addressing is largely obsolete — replaced by CIDR — but Network+ still tests it. The address 127.x.x.x is always the loopback range (127.0.0.1 = localhost). The address 0.0.0.0 means 'this network'. Understanding the structure of IP addresses is the foundation for subnetting.",
        "terms": [
            ("IPv4", "32-bit IP address written as four decimal octets, e.g. 192.168.1.1"),
            ("Octet", "8-bit section of an IP address; values range from 0-255"),
            ("Class A", "First octet 1-126; default mask /8; supports ~16 million hosts"),
            ("Class B", "First octet 128-191; default mask /16; supports ~65,000 hosts"),
            ("Class C", "First octet 192-223; default mask /24; supports 254 hosts"),
            ("Loopback", "127.0.0.1 — the address a device uses to refer to itself"),
        ],
        "questions": [
            ("What class is the IP address 172.16.5.10?", "Class B (first octet 128-191)"),
            ("How many bits are in an IPv4 address?", "32 bits"),
            ("What is the loopback address?", "127.0.0.1"),
            ("What is the maximum value of any single octet?", "255"),
        ],
        "links": [
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
            ("Subnet Calculator", "https://www.subnet-calculator.com"),
            ("CIDR.xyz — Visual Subnet Tool", "https://cidr.xyz"),
        ]
    },
    "2-2": {
        "notes": "A subnet mask defines which part of an IP address is the network portion and which part identifies the host. Written in dotted decimal (255.255.255.0) or CIDR notation (/24), it works by masking the network bits with 1s and host bits with 0s. A /24 mask means 24 bits are network, 8 bits are host — giving 256 addresses (254 usable, minus network and broadcast addresses).\n\nCIDR (Classless Inter-Domain Routing) replaced classful addressing and allows flexible subnet sizes. A /30 gives 4 addresses (2 usable) — perfect for point-to-point links. A /16 gives 65,536 addresses. The formula for usable hosts is 2^(host bits) - 2. You must be fast with these calculations for the Network+ exam.",
        "terms": [
            ("Subnet Mask", "32-bit number that separates network and host portions of an IP address"),
            ("CIDR Notation", "Slash notation indicating how many bits are the network portion, e.g. /24"),
            ("Network Address", "First address in a subnet — identifies the network itself, not usable for hosts"),
            ("Broadcast Address", "Last address in a subnet — sent to all hosts, not usable for individual hosts"),
            ("Usable Hosts", "Total addresses minus 2 (network + broadcast) = 2^host bits - 2"),
        ],
        "questions": [
            ("How many usable hosts does a /24 subnet provide?", "254 (2^8 = 256, minus 2 for network and broadcast)"),
            ("What is the subnet mask for a /24 in dotted decimal?", "255.255.255.0"),
            ("How many usable hosts does a /30 subnet provide?", "2 (2^2 = 4, minus 2)"),
            ("In CIDR notation, what does the number after the slash represent?", "The number of bits used for the network portion"),
        ],
        "links": [
            ("Subnet Calculator", "https://www.subnet-calculator.com"),
            ("CIDR.xyz — Visual Subnet Tool", "https://cidr.xyz"),
            ("Subnetting Practice", "https://subnettingpractice.com"),
        ]
    },
    "2-3": {
        "notes": "Subnetting divides a large network into smaller sub-networks. The process: 1) Convert the IP and mask to binary. 2) Determine how many subnets or hosts you need. 3) Borrow bits from the host portion to create subnets. Each bit borrowed doubles the number of subnets but halves the hosts per subnet.\n\nThe quick method: identify the 'interesting octet' (where the subnet mask isn't 255 or 0). The block size = 256 minus the mask value in that octet. Subnets increment by the block size. For example, /26 = 255.255.255.192 — block size is 256-192=64. Subnets are .0, .64, .128, .192. Practice this daily until it's automatic — it comes up on every Network+ exam.",
        "terms": [
            ("Subnetting", "Dividing a network into smaller logical sub-networks"),
            ("Block Size", "256 minus the subnet mask value in the interesting octet; the increment between subnets"),
            ("Interesting Octet", "The octet in the subnet mask that is neither 255 nor 0"),
            ("Borrowing Bits", "Taking bits from the host portion to create more subnets"),
            ("/26", "255.255.255.192 — 4 subnets of 62 hosts each within a /24"),
        ],
        "questions": [
            ("What is the block size for a /26 subnet?", "64 (256 - 192 = 64)"),
            ("For 192.168.1.0/26, what are the four subnet addresses?", ".0, .64, .128, .192"),
            ("How many hosts can a /26 subnet support?", "62 usable hosts (2^6 = 64, minus 2)"),
            ("You need 30 hosts per subnet. What prefix length should you use?", "/27 — provides 30 usable hosts (2^5=32, minus 2)"),
        ],
        "links": [
            ("Subnetting Practice — Free Drill Tool", "https://subnettingpractice.com"),
            ("Subnet Calculator", "https://www.subnet-calculator.com"),
            ("CIDR.xyz — Visual Subnet Tool", "https://cidr.xyz"),
        ]
    },
    "2-4": {
        "notes": "Private IP addresses are reserved ranges that are not routable on the public internet. They're defined in RFC 1918: 10.0.0.0/8 (Class A private), 172.16.0.0/12 (Class B private), and 192.168.0.0/16 (Class C private). Every home and office network uses these ranges internally. NAT (Network Address Translation) allows many private addresses to share a single public IP address.\n\nNAT works by maintaining a translation table — when a device at 192.168.1.5 sends traffic to the internet, the router replaces the private source IP with its public IP, records the mapping, and reverses the process for return traffic. PAT (Port Address Translation), also called NAT overload, allows thousands of private IPs to share one public IP by tracking port numbers. This is what your home router does.",
        "terms": [
            ("Private IP", "Non-routable IP ranges for internal use: 10.x, 172.16-31.x, 192.168.x"),
            ("Public IP", "Globally routable IP address assigned by ISPs"),
            ("NAT", "Network Address Translation — maps private IPs to public IPs for internet access"),
            ("PAT", "Port Address Translation — many private IPs share one public IP using port numbers"),
            ("RFC 1918", "The standard defining private IPv4 address ranges"),
        ],
        "questions": [
            ("Which three ranges are private IP addresses?", "10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16"),
            ("What does NAT allow?", "Multiple devices with private IPs to share a single public IP address"),
            ("Is 172.20.5.1 a private address?", "Yes — it falls within the 172.16.0.0/12 private range (172.16-172.31)"),
        ],
        "links": [
            ("Cloudflare — What is NAT?", "https://www.cloudflare.com/learning/network-layer/what-is-nat/"),
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
            ("RFC 1918 — Private Address Space", "https://datatracker.ietf.org/doc/html/rfc1918"),
        ]
    },
    "2-5": {
        "notes": "IPv6 was created to solve IPv4 address exhaustion. It uses 128-bit addresses written as eight groups of four hexadecimal digits separated by colons: 2001:0db8:85a3:0000:0000:8a2e:0370:7334. Leading zeros in a group can be omitted, and consecutive groups of zeros can be replaced with :: (but only once per address). IPv6 provides 340 undecillion addresses — essentially unlimited.\n\nKey IPv6 address types: unicast (one-to-one), multicast (one-to-many), anycast (one-to-nearest). There is no broadcast in IPv6. The loopback address is ::1. Link-local addresses start with fe80:: and are automatically assigned. Global unicast addresses (2000::/3) are the public internet addresses. IPv6 also has built-in IPsec support and simplified headers for faster routing.",
        "terms": [
            ("IPv6", "128-bit addressing scheme providing ~340 undecillion addresses"),
            ("Link-Local", "fe80::/10 — automatically assigned, only valid on local network segment"),
            ("Global Unicast", "2000::/3 — publicly routable IPv6 addresses"),
            (":: Notation", "Shorthand replacing one or more consecutive groups of all-zero hextets"),
            ("Loopback (IPv6)", "::1 — equivalent to 127.0.0.1 in IPv4"),
        ],
        "questions": [
            ("How many bits are in an IPv6 address?", "128 bits"),
            ("What does :: represent in an IPv6 address?", "One or more consecutive groups of zeros (can only be used once per address)"),
            ("What is the IPv6 loopback address?", "::1"),
            ("Does IPv6 use broadcast?", "No — IPv6 uses multicast and anycast instead of broadcast"),
        ],
        "links": [
            ("Cloudflare — What is IPv6?", "https://www.cloudflare.com/learning/network-layer/what-is-ipv6/"),
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
            ("Hurricane Electric IPv6 Certification (Free)", "https://ipv6.he.net/certification/"),
        ]
    },
    "2-6": {
        "notes": "This lab focuses on hands-on subnetting practice. Subnetting is the single most important skill for the Network+ exam — questions appear in multiple domains and performance-based questions will test it directly. Use the block size method: find the interesting octet, calculate block size (256 - mask value), and count up by that block size to find all subnets.\n\nFor speed: memorize the common prefix lengths and their properties. /24=254 hosts, /25=126, /26=62, /27=30, /28=14, /29=6, /30=2. Practice at subnettingpractice.com until you can answer in under 30 seconds. In the real exam you have 90 questions in 90 minutes — you cannot afford to spend 5 minutes on a subnetting question.",
        "terms": [
            ("/25", "255.255.255.128 — 2 subnets, 126 hosts each"),
            ("/26", "255.255.255.192 — 4 subnets, 62 hosts each"),
            ("/27", "255.255.255.224 — 8 subnets, 30 hosts each"),
            ("/28", "255.255.255.240 — 16 subnets, 14 hosts each"),
            ("/29", "255.255.255.248 — 32 subnets, 6 hosts each"),
            ("/30", "255.255.255.252 — 64 subnets, 2 hosts each (point-to-point links)"),
        ],
        "questions": [
            ("A host has IP 192.168.10.130/26. What subnet is it on?", "192.168.10.128/26 (block size 64: subnets at .0, .64, .128, .192)"),
            ("How many usable hosts does a /29 provide?", "6 hosts (2^3=8, minus 2)"),
            ("You need 50 hosts per subnet. What is the smallest prefix that works?", "/26 — provides 62 usable hosts"),
        ],
        "links": [
            ("Subnetting Practice — Free Drill Tool", "https://subnettingpractice.com"),
            ("Subnet Calculator", "https://www.subnet-calculator.com"),
            ("CIDR.xyz — Visual Subnet Tool", "https://cidr.xyz"),
        ]
    },
    "3-1": {
        "notes": "TCP (Transmission Control Protocol) is a connection-oriented protocol that guarantees reliable, ordered delivery of data. Before any data is sent, TCP performs a three-way handshake: SYN (client requests connection), SYN-ACK (server acknowledges and responds), ACK (client confirms). This establishes a session. TCP also handles flow control (preventing a fast sender from overwhelming a slow receiver) and congestion control (slowing down when the network is congested).\n\nTCP uses sequence numbers to reassemble out-of-order packets and acknowledgement numbers to confirm receipt. If a packet is lost, the sender retransmits it. This reliability comes at a cost — overhead and latency. TCP is used for HTTP, HTTPS, FTP, SMTP, and any application where data integrity matters more than speed.",
        "terms": [
            ("TCP", "Transmission Control Protocol — reliable, connection-oriented, ordered delivery"),
            ("Three-Way Handshake", "SYN → SYN-ACK → ACK — establishes a TCP connection"),
            ("Sequence Number", "Number identifying the order of bytes in a TCP stream"),
            ("Acknowledgement", "Confirmation that data was received; triggers retransmission if missing"),
            ("Flow Control", "Mechanism to prevent sender from overwhelming receiver (TCP window size)"),
        ],
        "questions": [
            ("What are the three steps of the TCP handshake?", "SYN, SYN-ACK, ACK"),
            ("Why does TCP use sequence numbers?", "To reassemble packets in the correct order and detect missing data"),
            ("Name three protocols that use TCP.", "HTTP (80), HTTPS (443), FTP (21), SMTP (25), SSH (22)"),
        ],
        "links": [
            ("Cloudflare — What is TCP?", "https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/"),
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
            ("Wireshark — Free Download", "https://www.wireshark.org/download.html"),
        ]
    },
    "3-2": {
        "notes": "UDP (User Datagram Protocol) is connectionless — it sends packets without establishing a session and without confirming delivery. There's no handshake, no acknowledgement, no retransmission. This makes UDP much faster and lower overhead than TCP, but data can be lost, duplicated, or arrive out of order.\n\nUDP is ideal for applications where speed matters more than perfect reliability: video streaming (a dropped frame is acceptable), online gaming, VoIP calls, DNS lookups, and DHCP. If an application needs reliability over UDP, it implements its own error checking at the application layer. The key exam distinction: TCP = reliable, connection-oriented; UDP = fast, connectionless, best-effort.",
        "terms": [
            ("UDP", "User Datagram Protocol — fast, connectionless, no guaranteed delivery"),
            ("Connectionless", "No session established before sending; no handshake"),
            ("Best-Effort Delivery", "Packets are sent but delivery is not guaranteed or confirmed"),
            ("Latency", "Delay in data transmission; UDP has lower latency than TCP"),
            ("Jitter", "Variation in packet arrival times; problematic for VoIP and video"),
        ],
        "questions": [
            ("Why would a video streaming application use UDP instead of TCP?", "Speed — a dropped frame is acceptable; retransmission would cause worse lag than the dropped frame"),
            ("Does UDP perform a three-way handshake?", "No — UDP is connectionless with no handshake"),
            ("Name three protocols that use UDP.", "DNS (53), DHCP (67/68), TFTP (69), SNMP (161), VoIP/RTP"),
        ],
        "links": [
            ("Cloudflare — TCP vs UDP", "https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/"),
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
            ("ExamCompass — Free Network+ Practice", "https://www.comptia.org/training/certmaster-practice/network"),
        ]
    },
    "3-3": {
        "notes": "A port number identifies a specific process or service on a device. IP addresses get data to the right machine; port numbers get data to the right application on that machine. Together they form a socket (e.g. 192.168.1.5:443). Port numbers range from 0-65535. Well-known ports (0-1023) are assigned to standard services. Registered ports (1024-49151) are used by applications. Dynamic/ephemeral ports (49152-65535) are assigned temporarily to clients.\n\nYou must memorise key port numbers for Network+: HTTP=80, HTTPS=443, FTP=20/21, SSH=22, Telnet=23, SMTP=25, DNS=53, DHCP=67/68, POP3=110, IMAP=143, RDP=3389, SNMP=161. A socket is the combination of IP address + port number and uniquely identifies a connection endpoint.",
        "terms": [
            ("Port", "A 16-bit number identifying a specific application or service (0-65535)"),
            ("Socket", "The combination of an IP address and port number, e.g. 10.0.0.1:80"),
            ("Well-Known Ports", "Ports 0-1023 assigned to standard services by IANA"),
            ("Ephemeral Port", "Temporary port (49152-65535) assigned to a client for a session"),
            ("Port 443", "HTTPS — encrypted web traffic"),
        ],
        "questions": [
            ("What port does HTTPS use?", "443"),
            ("What port does SSH use?", "22"),
            ("What port does DNS use?", "53"),
            ("What is a socket?", "The combination of an IP address and a port number"),
            ("What port does RDP use?", "3389"),
        ],
        "links": [
            ("IANA — Official Port Number Registry", "https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml"),
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
            ("ExamCompass — Free Network+ Practice", "https://www.comptia.org/training/certmaster-practice/network"),
        ]
    },
    "3-4": {
        "notes": "ICMP (Internet Control Message Protocol) is used for network diagnostics and error reporting — it operates at Layer 3 and is part of the IP suite. Ping uses ICMP Echo Request and Echo Reply messages to test whether a host is reachable and measure round-trip time. Traceroute (tracert on Windows) uses ICMP with incrementing TTL values to map the path packets take across a network.\n\nTTL (Time to Live) is a counter in each IP packet that decrements by 1 at each router hop. When TTL reaches 0, the router discards the packet and sends an ICMP 'Time Exceeded' message back. Traceroute exploits this — it sends packets with TTL=1, 2, 3... and collects the 'Time Exceeded' responses to identify each hop. ICMP is also used for 'Destination Unreachable' and 'Redirect' messages.",
        "terms": [
            ("ICMP", "Internet Control Message Protocol — used for diagnostics and error reporting, Layer 3"),
            ("Ping", "Uses ICMP Echo Request/Reply to test host reachability and measure latency"),
            ("Traceroute", "Maps the path to a destination by sending packets with incrementing TTL values"),
            ("TTL", "Time to Live — decrements at each router hop; packet discarded when it reaches 0"),
            ("Echo Request/Reply", "ICMP message types used by ping (type 8 = request, type 0 = reply)"),
        ],
        "questions": [
            ("What protocol does ping use?", "ICMP — specifically Echo Request and Echo Reply messages"),
            ("What happens when a packet's TTL reaches 0?", "The router discards it and sends an ICMP Time Exceeded message back to the source"),
            ("What is traceroute used for?", "Mapping the path packets take to a destination and identifying where delays or failures occur"),
        ],
        "links": [
            ("Cloudflare — What is ICMP?", "https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/"),
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
            ("Wireshark — Free Download", "https://www.wireshark.org/download.html"),
        ]
    },
    "3-5": {
        "notes": "Wireshark is the industry-standard free packet analyser. It captures all network traffic passing through a network interface and displays it in a human-readable format. You can filter by protocol (tcp, udp, icmp, dns, http), by IP address (ip.addr == 192.168.1.1), or by port (tcp.port == 443). Wireshark is essential for troubleshooting and understanding how protocols actually work in practice.\n\nFor this lab: install Wireshark from wireshark.org, start a capture on your network interface, then open a browser or run ping. Watch the packets appear. Try filtering for 'icmp' and run a ping — you'll see the Echo Request and Reply packets. Try 'dns' and browse to a website — you'll see the DNS query and response. This hands-on practice cements the theory in a way reading never can.",
        "terms": [
            ("Packet Capture", "Recording network traffic for analysis; also called a pcap"),
            ("Display Filter", "Wireshark filter to show only specific traffic, e.g. 'tcp.port == 80'"),
            ("Promiscuous Mode", "NIC mode that captures all packets, not just those addressed to it"),
            ("Follow TCP Stream", "Wireshark feature to reconstruct and read an entire TCP conversation"),
            (".pcap file", "Standard file format for saved packet captures"),
        ],
        "questions": [
            ("What Wireshark filter shows only ICMP traffic?", "icmp"),
            ("What Wireshark filter shows traffic to/from a specific IP?", "ip.addr == x.x.x.x"),
            ("What Wireshark filter shows only DNS traffic?", "dns or udp.port == 53"),
        ],
        "links": [
            ("Wireshark — Free Download", "https://www.wireshark.org/download.html"),
            ("Wireshark User Guide", "https://www.wireshark.org/docs/wsug_html_chunked/"),
            ("Wireshark Display Filter Reference", "https://www.wireshark.org/docs/dfref/"),
        ]
    },
    "4-1": {
        "notes": "A hub is a Layer 1 device that simply repeats incoming signals to all ports — every device receives every packet, causing collisions and wasted bandwidth. Hubs are obsolete. A switch is a Layer 2 device that learns MAC addresses and forwards frames only to the correct port. Switches build a MAC address table by recording the source MAC of every incoming frame. When a frame arrives, the switch looks up the destination MAC and forwards it only to that port — all other devices are unaware of the traffic.\n\nThis makes switches far more efficient than hubs. A collision domain is a network segment where packets can collide — each switch port is its own collision domain. A broadcast domain is the area where broadcasts are sent — an entire switch (without VLANs) is one broadcast domain. Understanding the difference between Layer 1, 2, and 3 devices is fundamental to Network+.",
        "terms": [
            ("Switch", "Layer 2 device that forwards frames based on MAC addresses"),
            ("Hub", "Layer 1 device that repeats signals to all ports; causes collisions; obsolete"),
            ("MAC Address Table", "Table a switch builds mapping MAC addresses to ports"),
            ("Collision Domain", "Network segment where simultaneous transmissions cause collisions; each switch port is its own"),
            ("Broadcast Domain", "Area where broadcast frames are forwarded; bounded by routers"),
        ],
        "questions": [
            ("At which OSI layer do switches operate?", "Layer 2 — Data Link"),
            ("How does a switch decide where to forward a frame?", "It looks up the destination MAC address in its MAC address table"),
            ("What is the difference between a collision domain and a broadcast domain?", "Collision domain: area where collisions can occur (per switch port). Broadcast domain: area where broadcasts reach (entire VLAN/switch)"),
        ],
        "links": [
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
            ("Cloudflare Learning Center", "https://www.cloudflare.com/learning/"),
            ("Packet Tracer — Free Cisco Network Simulator", "https://www.netacad.com/courses/packet-tracer"),
        ]
    },
    "4-2": {
        "notes": "A router is a Layer 3 device that forwards packets between different networks based on IP addresses. Where a switch connects devices within the same network, a router connects different networks together. Routers maintain a routing table — a list of known networks and the best path to reach them. When a packet arrives, the router looks up the destination IP in its routing table and forwards the packet out the appropriate interface.\n\nRouting can be static (manually configured routes) or dynamic (routes learned automatically via protocols like OSPF, EIGRP, or BGP). The default gateway on any device is the router's IP address — it's where traffic is sent when the destination is not on the local network. Every time traffic crosses from one network to another, it passes through at least one router.",
        "terms": [
            ("Router", "Layer 3 device that forwards packets between networks based on IP addresses"),
            ("Routing Table", "List of networks and next-hop addresses a router uses to forward traffic"),
            ("Default Gateway", "The router IP address that a host sends traffic to when the destination is off-network"),
            ("Static Route", "Manually configured route that doesn't change automatically"),
            ("Dynamic Routing", "Routes learned automatically via protocols like OSPF, EIGRP, BGP"),
        ],
        "questions": [
            ("At which OSI layer do routers operate?", "Layer 3 — Network layer"),
            ("What is a default gateway?", "The IP address of the router that a host sends traffic to for destinations outside its subnet"),
            ("What is the difference between a router and a switch?", "A switch forwards frames within a network using MAC addresses (L2); a router forwards packets between networks using IP addresses (L3)"),
        ],
        "links": [
            ("Cloudflare — What is a Router?", "https://www.cloudflare.com/learning/network-layer/what-is-a-router/"),
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
            ("Packet Tracer — Free Cisco Network Simulator", "https://www.netacad.com/courses/packet-tracer"),
        ]
    },
    "4-3": {
        "notes": "A firewall filters traffic based on rules, blocking unauthorised access while allowing legitimate traffic. Stateful firewalls track the state of connections — they know whether an incoming packet is part of an established connection or a new unsolicited one. Next-gen firewalls (NGFW) add deep packet inspection, application awareness, and intrusion prevention.\n\nAn IDS (Intrusion Detection System) monitors traffic and alerts on suspicious activity but doesn't block it. An IPS (Intrusion Prevention System) actively blocks threats in real time — it sits inline in the network path. A load balancer distributes incoming traffic across multiple servers to prevent overload and provide redundancy. These devices all appear in the Network+ exam's security and infrastructure domains.",
        "terms": [
            ("Firewall", "Filters network traffic based on rules; blocks unauthorised access"),
            ("Stateful Firewall", "Tracks connection state; knows if traffic is part of an established session"),
            ("IDS", "Intrusion Detection System — monitors and alerts on suspicious traffic; passive"),
            ("IPS", "Intrusion Prevention System — monitors and actively blocks threats; inline"),
            ("Load Balancer", "Distributes traffic across multiple servers for performance and redundancy"),
        ],
        "questions": [
            ("What is the difference between an IDS and an IPS?", "IDS detects and alerts (passive); IPS detects and blocks (active, inline)"),
            ("What makes a stateful firewall different from a simple packet filter?", "A stateful firewall tracks connection state so it can distinguish established traffic from new unsolicited connections"),
            ("What does a load balancer do?", "Distributes incoming connections across multiple servers to balance load and provide redundancy"),
        ],
        "links": [
            ("Cloudflare — What is a Firewall?", "https://www.cloudflare.com/learning/security/what-is-a-firewall/"),
            ("Cloudflare — IDS vs IPS", "https://www.cloudflare.com/learning/security/glossary/intrusion-detection-prevention/"),
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
        ]
    },
    "4-4": {
        "notes": "A VLAN (Virtual LAN) logically segments a physical network into separate broadcast domains without requiring separate physical switches. Ports on a switch are assigned to VLANs — devices in VLAN 10 cannot communicate directly with devices in VLAN 20 without going through a router (or Layer 3 switch). This improves security, reduces broadcast traffic, and enables logical grouping of users regardless of physical location.\n\nTrunk ports carry traffic for multiple VLANs between switches using 802.1Q tagging — a 4-byte tag is added to the frame header identifying which VLAN it belongs to. Access ports connect to end devices and carry only one VLAN. Inter-VLAN routing requires a router or Layer 3 switch. VLANs are essential for network segmentation — separating staff from guests, or finance from IT.",
        "terms": [
            ("VLAN", "Virtual LAN — logical network segment on a physical switch"),
            ("802.1Q", "The standard for VLAN tagging on trunk links"),
            ("Trunk Port", "Switch port carrying traffic for multiple VLANs, tagged with 802.1Q"),
            ("Access Port", "Switch port assigned to a single VLAN, connects to end devices"),
            ("Inter-VLAN Routing", "Routing traffic between VLANs using a router or Layer 3 switch"),
        ],
        "questions": [
            ("Can two devices on different VLANs communicate without a router?", "No — VLANs are separate broadcast domains; a router or L3 switch is required"),
            ("What standard is used for VLAN tagging on trunk links?", "IEEE 802.1Q"),
            ("What is the difference between a trunk port and an access port?", "Trunk port carries multiple VLANs (tagged); access port carries one VLAN (untagged) for end devices"),
        ],
        "links": [
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
            ("Packet Tracer — Free Cisco Network Simulator", "https://www.netacad.com/courses/packet-tracer"),
            ("Cloudflare Learning Center", "https://www.cloudflare.com/learning/"),
        ]
    },
    "5-1": {
        "notes": "DNS (Domain Name System) translates human-readable domain names into IP addresses. When you type google.com, your device sends a DNS query to a resolver (usually your ISP or a public resolver like 8.8.8.8). The resolver checks its cache, then queries root servers, then TLD servers (.com), then the authoritative name server for google.com, which returns the IP address.\n\nThis hierarchical process is called recursive resolution. The result is cached at multiple levels to speed up future queries — TTL (Time to Live) in the DNS record controls how long it's cached. DNS operates on port 53 and uses UDP for queries (fast) and TCP for zone transfers (reliable). Understanding DNS is critical for troubleshooting connectivity issues — 'it's always DNS' is a famous sysadmin joke because DNS failures cause so many apparent outages.",
        "terms": [
            ("DNS", "Domain Name System — translates domain names to IP addresses"),
            ("Resolver", "The DNS server your device queries; usually your ISP or 8.8.8.8"),
            ("Authoritative Name Server", "The server that holds the actual DNS records for a domain"),
            ("Root Server", "Top of the DNS hierarchy; 13 sets worldwide; knows where TLD servers are"),
            ("DNS Cache", "Temporary storage of DNS query results to speed up future lookups"),
            ("TTL", "Time to Live — how long a DNS record is cached before being refreshed"),
        ],
        "questions": [
            ("What port does DNS use?", "Port 53 (UDP for queries, TCP for zone transfers)"),
            ("What is the role of an authoritative name server?", "It holds the actual DNS records for a domain and answers queries about it definitively"),
            ("Why does DNS caching matter?", "It speeds up resolution by avoiding repeated queries and reduces load on DNS servers"),
        ],
        "links": [
            ("Cloudflare — How DNS Works", "https://www.cloudflare.com/learning/dns/what-is-dns/"),
            ("Cloudflare — DNS Record Types", "https://www.cloudflare.com/learning/dns/dns-records/"),
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
        ]
    },
    "5-2": {
        "notes": "DNS uses different record types for different purposes. An A record maps a hostname to an IPv4 address. An AAAA record maps a hostname to an IPv6 address. A CNAME (Canonical Name) record creates an alias pointing to another hostname — for example, www.example.com might CNAME to example.com. An MX (Mail Exchanger) record specifies the mail server for a domain. An NS record identifies the authoritative name servers for a domain.\n\nOther important records: TXT records store arbitrary text, used for domain verification and SPF/DKIM email security. PTR records are reverse DNS — mapping an IP address back to a hostname. SOA (Start of Authority) records contain administrative info about a zone. On the Network+ exam, you'll need to know the purpose of each record type and recognize them in troubleshooting scenarios.",
        "terms": [
            ("A Record", "Maps a hostname to an IPv4 address"),
            ("AAAA Record", "Maps a hostname to an IPv6 address"),
            ("CNAME", "Canonical Name — an alias pointing to another hostname"),
            ("MX Record", "Mail Exchanger — specifies mail servers for a domain"),
            ("PTR Record", "Reverse DNS — maps an IP address to a hostname"),
            ("TXT Record", "Stores text data; used for SPF, DKIM, domain verification"),
        ],
        "questions": [
            ("What DNS record type maps a hostname to an IPv4 address?", "A record"),
            ("What DNS record type is used for email routing?", "MX (Mail Exchanger) record"),
            ("What is a CNAME record used for?", "Creating an alias — pointing one hostname to another hostname"),
            ("What DNS record is used for reverse lookups (IP to hostname)?", "PTR record"),
        ],
        "links": [
            ("Cloudflare — DNS Record Types", "https://www.cloudflare.com/learning/dns/dns-records/"),
            ("Cloudflare — How DNS Works", "https://www.cloudflare.com/learning/dns/what-is-dns/"),
            ("MXToolbox — DNS Lookup Tool", "https://mxtoolbox.com/DNSLookup.aspx"),
        ]
    },
    "5-3": {
        "notes": "DHCP (Dynamic Host Configuration Protocol) automatically assigns IP addresses and network configuration to devices. Without DHCP, every device would need a manually configured IP, subnet mask, default gateway, and DNS server. DHCP uses a four-step process called DORA: Discover (client broadcasts looking for a DHCP server), Offer (server offers an IP address), Request (client requests the offered address), Acknowledge (server confirms the lease).\n\nDHCP leases are temporary — devices must renew them periodically. A DHCP scope defines the range of addresses the server can assign. DHCP can also assign options: default gateway, DNS servers, domain name, NTP server. DHCP Relay (ip helper-address on Cisco) forwards DHCP broadcasts across routers so one DHCP server can serve multiple subnets. DHCP uses UDP ports 67 (server) and 68 (client).",
        "terms": [
            ("DHCP", "Dynamic Host Configuration Protocol — automatically assigns IP configuration to hosts"),
            ("DORA", "Discover, Offer, Request, Acknowledge — the four steps of DHCP"),
            ("DHCP Lease", "Temporary assignment of an IP address; must be renewed"),
            ("DHCP Scope", "The pool of IP addresses a DHCP server can assign"),
            ("DHCP Relay", "Forwards DHCP broadcasts across routers (ip helper-address)"),
            ("Ports 67/68", "DHCP server listens on 67; client on 68; both use UDP"),
        ],
        "questions": [
            ("What does DORA stand for?", "Discover, Offer, Request, Acknowledge"),
            ("What ports does DHCP use?", "UDP 67 (server) and UDP 68 (client)"),
            ("What is a DHCP scope?", "The range of IP addresses a DHCP server is configured to assign"),
            ("Why is DHCP Relay needed?", "DHCP uses broadcasts which don't cross routers; relay forwards DHCP messages across subnets"),
        ],
        "links": [
            ("Cloudflare — What is DHCP?", "https://www.cloudflare.com/learning/network-layer/what-is-dhcp/"),
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
            ("Packet Tracer — Free Cisco Network Simulator", "https://www.netacad.com/courses/packet-tracer"),
        ]
    },
    "5-4": {
        "notes": "Command-line tools are essential for network troubleshooting. nslookup queries DNS — type nslookup google.com to see what IP it resolves to, or nslookup -type=MX google.com for mail records. dig (Linux/Mac) is a more powerful DNS tool. ipconfig (Windows) / ifconfig (Linux) shows your current IP configuration including IP address, subnet mask, and default gateway. ipconfig /all shows MAC addresses and DHCP info.\n\nOther key commands: ipconfig /flushdns clears the DNS cache. ipconfig /release and /renew release and renew a DHCP lease. route print (Windows) / ip route (Linux) shows the routing table. arp -a shows the ARP cache (IP-to-MAC mappings). These tools appear directly in Network+ performance-based questions — practice them in your terminal until they're second nature.",
        "terms": [
            ("nslookup", "Command-line DNS query tool; works on Windows, Linux, Mac"),
            ("dig", "Linux/Mac DNS query tool; more detailed output than nslookup"),
            ("ipconfig", "Windows command showing IP configuration; /all for full details"),
            ("ifconfig", "Linux/Mac equivalent of ipconfig (older; ip addr is the modern version)"),
            ("ipconfig /flushdns", "Clears the local DNS cache on Windows"),
            ("arp -a", "Shows the ARP cache — learned IP-to-MAC address mappings"),
        ],
        "questions": [
            ("What command shows your IP address on Windows?", "ipconfig (or ipconfig /all for full details)"),
            ("What command queries DNS from the command line?", "nslookup (Windows/Linux/Mac) or dig (Linux/Mac)"),
            ("What command clears the DNS cache on Windows?", "ipconfig /flushdns"),
            ("What command shows the ARP table?", "arp -a"),
        ],
        "links": [
            ("MXToolbox — DNS Lookup Tool", "https://mxtoolbox.com/DNSLookup.aspx"),
            ("SS64 — Windows Command Reference", "https://ss64.com/nt/"),
            ("SS64 — Linux Command Reference", "https://ss64.com/bash/"),
        ]
    },
    "6-1": {
        "notes": "Common network attacks you must know for Network+: A Man-in-the-Middle (MITM) attack intercepts communication between two parties — the attacker secretly relays and potentially alters messages. ARP Spoofing/Poisoning sends fake ARP replies to associate the attacker's MAC with a legitimate IP, enabling MITM on local networks. A DoS (Denial of Service) attack floods a target with traffic to overwhelm it; a DDoS uses many compromised systems simultaneously.\n\nOther attacks: VLAN Hopping allows an attacker to send traffic to a different VLAN by exploiting trunk ports. DNS Spoofing/Poisoning inserts false DNS records to redirect users to malicious sites. A Rogue DHCP server gives clients incorrect network configuration. Recognising these attacks and knowing their mitigations is a significant portion of the Network+ security domain.",
        "terms": [
            ("MITM", "Man-in-the-Middle — attacker intercepts communication between two parties"),
            ("ARP Spoofing", "Sending fake ARP replies to associate attacker's MAC with a legitimate IP"),
            ("DoS", "Denial of Service — flooding a target to make it unavailable"),
            ("DDoS", "Distributed DoS — DoS using many compromised systems simultaneously"),
            ("VLAN Hopping", "Exploiting trunk port configuration to send traffic to another VLAN"),
            ("Rogue DHCP", "Unauthorised DHCP server giving clients incorrect network configuration"),
        ],
        "questions": [
            ("How does ARP spoofing enable a MITM attack?", "The attacker sends fake ARP replies mapping their MAC to a legitimate IP, so traffic intended for that IP goes to the attacker instead"),
            ("What is the difference between DoS and DDoS?", "DoS is from one source; DDoS uses many compromised systems (botnet) to overwhelm the target"),
            ("What mitigation prevents rogue DHCP servers?", "DHCP snooping on switches — only trusted ports can send DHCP offers"),
        ],
        "links": [
            ("Cloudflare — DDoS Explained", "https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/"),
            ("Cloudflare — What is a MITM Attack?", "https://www.cloudflare.com/learning/security/threats/man-in-the-middle-attack/"),
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
        ]
    },
    "6-2": {
        "notes": "Encryption protects data in transit from eavesdropping. TLS (Transport Layer Security) is the current standard for encrypting web traffic — HTTPS is HTTP over TLS. TLS uses a handshake to negotiate encryption algorithms and exchange keys before data is transmitted. SSL is the predecessor to TLS and is now deprecated and insecure — but the term 'SSL' is still commonly (incorrectly) used to mean TLS.\n\nA VPN (Virtual Private Network) creates an encrypted tunnel across an untrusted network (like the internet). Site-to-site VPNs connect entire offices. Client VPNs let remote workers securely access company resources. IPsec is a suite of protocols for encrypting IP traffic — used heavily in VPNs. It operates in tunnel mode (encrypts the entire packet) or transport mode (encrypts just the payload). OpenVPN and WireGuard are popular open-source VPN protocols.",
        "terms": [
            ("TLS", "Transport Layer Security — encrypts data in transit; successor to SSL"),
            ("HTTPS", "HTTP over TLS — encrypted web browsing on port 443"),
            ("VPN", "Virtual Private Network — encrypted tunnel over an untrusted network"),
            ("IPsec", "IP Security — suite of protocols for encrypting IP traffic, used in VPNs"),
            ("Tunnel Mode", "IPsec mode that encrypts the entire IP packet including headers"),
            ("SSL", "Secure Sockets Layer — deprecated predecessor to TLS; no longer secure"),
        ],
        "questions": [
            ("What is the difference between SSL and TLS?", "SSL is deprecated and insecure; TLS is its secure successor. Most references to 'SSL' today actually mean TLS"),
            ("What port does HTTPS use?", "443"),
            ("What is the difference between site-to-site and client VPN?", "Site-to-site connects two networks permanently; client VPN connects an individual user's device to a network"),
        ],
        "links": [
            ("Cloudflare — TLS Explained", "https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/"),
            ("Cloudflare — What is a VPN?", "https://www.cloudflare.com/learning/access-management/what-is-a-vpn/"),
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
        ]
    },
    "6-3": {
        "notes": "Authentication protocols verify the identity of users and devices trying to access a network. RADIUS (Remote Authentication Dial-In User Service) is a centralised AAA (Authentication, Authorisation, Accounting) protocol. When a user tries to connect to a network, the authenticator (e.g. a switch or VPN server) forwards credentials to the RADIUS server, which approves or denies access. RADIUS uses UDP ports 1812/1813.\n\nTACACS+ (Terminal Access Controller Access-Control System Plus) is a Cisco proprietary AAA protocol that encrypts the entire payload (RADIUS only encrypts the password). TACACS+ uses TCP port 49 and separates authentication, authorisation, and accounting into separate functions. RADIUS is typically used for network access (Wi-Fi, VPN); TACACS+ is used for device administration (router/switch login). 802.1X is a port-based access control standard that uses RADIUS for authenticating devices before they're allowed network access.",
        "terms": [
            ("RADIUS", "Remote Authentication Dial-In User Service — centralised AAA; UDP 1812/1813"),
            ("TACACS+", "Cisco AAA protocol; encrypts full payload; TCP port 49"),
            ("AAA", "Authentication (who are you?), Authorisation (what can you do?), Accounting (what did you do?)"),
            ("802.1X", "Port-based network access control; uses RADIUS to authenticate devices before network access"),
            ("Authenticator", "The device (switch, AP) that forwards credentials to the RADIUS server"),
        ],
        "questions": [
            ("What ports does RADIUS use?", "UDP 1812 (authentication) and 1813 (accounting)"),
            ("What is the key security difference between RADIUS and TACACS+?", "TACACS+ encrypts the entire packet; RADIUS only encrypts the password"),
            ("What does AAA stand for?", "Authentication, Authorisation, Accounting"),
            ("What protocol is used with 802.1X?", "RADIUS"),
        ],
        "links": [
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
            ("Cloudflare — What is 802.1X?", "https://www.cloudflare.com/learning/access-management/what-is-802.1x/"),
            ("ExamCompass — Free Network+ Practice", "https://www.comptia.org/training/certmaster-practice/network"),
        ]
    },
    "6-4": {
        "notes": "Wireless security has evolved significantly. WEP (Wired Equivalent Privacy) was the original standard but is completely broken and should never be used. WPA (Wi-Fi Protected Access) improved on WEP but also has vulnerabilities. WPA2 uses AES encryption and is the current standard for home and business networks — WPA2-Personal uses a pre-shared key (PSK); WPA2-Enterprise uses 802.1X with RADIUS for per-user authentication.\n\nWPA3 is the latest standard with stronger encryption and protection against offline dictionary attacks. It uses SAE (Simultaneous Authentication of Equals) instead of PSK. For enterprise networks, WPA2/WPA3-Enterprise with 802.1X is the gold standard — each user authenticates individually and a compromised password only affects one account. Common wireless attacks include evil twin (rogue AP), deauth attacks, and WPS brute-forcing (disable WPS on all networks).",
        "terms": [
            ("WEP", "Wired Equivalent Privacy — original wireless security; completely broken; never use"),
            ("WPA2-Personal", "Uses a pre-shared key (PSK/passphrase); suitable for home networks"),
            ("WPA2-Enterprise", "Uses 802.1X and RADIUS for individual user authentication; business standard"),
            ("WPA3", "Latest Wi-Fi security standard; SAE handshake; resistant to offline attacks"),
            ("Evil Twin", "Rogue access point mimicking a legitimate one to capture traffic"),
            ("SAE", "Simultaneous Authentication of Equals — WPA3 handshake replacing PSK"),
        ],
        "questions": [
            ("Why should WEP never be used?", "WEP's encryption is completely broken and can be cracked in minutes with freely available tools"),
            ("What is the difference between WPA2-Personal and WPA2-Enterprise?", "Personal uses a shared passphrase; Enterprise uses 802.1X with individual user credentials via RADIUS"),
            ("What attack does WPA3 protect against that WPA2 doesn't?", "Offline dictionary attacks — WPA3's SAE handshake doesn't allow captured handshakes to be brute-forced offline"),
        ],
        "links": [
            ("Wi-Fi Alliance — Security Overview", "https://www.wi-fi.org/discover-wi-fi/security"),
            ("Cloudflare — WPA3 Explained", "https://www.cloudflare.com/learning/network-layer/what-is-wpa3/"),
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
        ]
    },
    "6-5": {
        "notes": "This is a review quiz for Module 6 — Network Security. Security is one of the most heavily weighted domains on the Network+ exam. Make sure you can identify attack types, explain mitigation strategies, distinguish encryption protocols, and understand authentication frameworks.\n\nKey areas to be solid on: port numbers for security protocols (SSH=22, HTTPS=443, RADIUS=1812), the difference between IDS and IPS, WPA2 vs WPA3, RADIUS vs TACACS+, and common network attacks with their mitigations.",
        "terms": [
            ("SSH", "Secure Shell — encrypted remote access; port 22; replacement for Telnet"),
            ("Telnet", "Unencrypted remote access; port 23; never use on production networks"),
            ("SNMP", "Simple Network Management Protocol — network monitoring; port 161 (UDP)"),
            ("Syslog", "Standard for sending log messages; UDP port 514"),
        ],
        "questions": [
            ("What port does SSH use?", "22"),
            ("Why is Telnet insecure?", "Telnet transmits data including passwords in plaintext — anyone on the network can intercept it"),
            ("What is the difference between IDS and IPS?", "IDS detects and alerts (passive); IPS detects and blocks (active/inline)"),
            ("Which wireless security protocol should be used on enterprise networks?", "WPA2-Enterprise or WPA3-Enterprise with 802.1X authentication"),
            ("What does DHCP snooping prevent?", "Rogue DHCP servers — only trusted ports can send DHCP offers"),
        ],
        "links": [
            ("Professor Messer — Free Practice Exams", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
            ("ExamCompass — Free Network+ Quizzes", "https://www.comptia.org/training/certmaster-practice/network"),
            ("CompTIA Network+ Exam Objectives (Free PDF)", "https://www.comptia.org/training/resources/exam-objectives"),
        ]
    },
    "7-1": {
        "notes": "CompTIA's official troubleshooting methodology has seven steps: 1) Identify the problem — gather information and symptoms. 2) Establish a theory of probable cause — what do you think is wrong? 3) Test the theory — confirm or deny your hypothesis. 4) Establish a plan of action — how will you fix it with minimal disruption? 5) Implement the solution — make the change. 6) Verify full functionality — confirm the fix worked and nothing else broke. 7) Document findings — record what happened and how you fixed it.\n\nIn practice, experienced engineers often jump to step 2 based on intuition — but the methodology exists to avoid missing obvious causes. Always start at Layer 1 (is the cable plugged in?) and work up. The OSI model is your troubleshooting map: Physical → Data Link → Network → Transport → Application.",
        "terms": [
            ("Troubleshooting Methodology", "CompTIA's 7-step process: Identify, Theory, Test, Plan, Implement, Verify, Document"),
            ("Bottom-Up Approach", "Start troubleshooting at Layer 1 (physical) and work up through OSI layers"),
            ("Top-Down Approach", "Start at Layer 7 (application) and work down — used when software issues are suspected"),
            ("Divide and Conquer", "Start at Layer 3 (network) and work up or down based on test results"),
            ("Documentation", "Recording the problem, cause, and solution — essential for future reference"),
        ],
        "questions": [
            ("What is the first step in CompTIA's troubleshooting methodology?", "Identify the problem — gather information, question users, observe symptoms"),
            ("Why is documentation the final step?", "To create a record for future reference, track recurring issues, and help other engineers"),
            ("If a user can ping by IP but not by name, which layer/service is the problem?", "DNS — name resolution failure (application layer service)"),
        ],
        "links": [
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
            ("CompTIA Network+ Exam Objectives (Free PDF)", "https://www.comptia.org/training/resources/exam-objectives"),
            ("ExamCompass — Free Network+ Practice", "https://www.comptia.org/training/certmaster-practice/network"),
        ]
    },
    "7-2": {
        "notes": "Essential CLI tools for every network engineer. ping tests basic connectivity — if it fails, work down the OSI model. tracert (Windows) / traceroute (Linux) shows the path to a destination and identifies where failures or latency occur. netstat shows active connections, listening ports, and network statistics — useful for finding what's using a port or how many connections exist. arp -a shows the ARP cache; arp -d clears it.\n\nroute print (Windows) / ip route (Linux) shows the routing table — essential for diagnosing routing issues. nslookup and dig diagnose DNS. netstat -an shows all connections and listening ports numerically. On Cisco devices: show ip interface brief, show ip route, show mac address-table, show vlan brief, and show running-config are the essential show commands. Practice all of these until they're instinctive.",
        "terms": [
            ("ping", "Tests ICMP reachability; measures round-trip time"),
            ("tracert/traceroute", "Maps the path to a destination hop by hop"),
            ("netstat", "Shows active connections and listening ports"),
            ("netstat -an", "Shows all connections and ports numerically (no DNS resolution)"),
            ("route print", "Shows the Windows routing table (ip route on Linux)"),
            ("arp -a", "Displays the ARP cache — IP to MAC address mappings"),
        ],
        "questions": [
            ("A user can ping 8.8.8.8 but not google.com. What is likely wrong?", "DNS resolution is failing — the IP stack works but name resolution doesn't"),
            ("What command shows which ports are listening on a Windows machine?", "netstat -an"),
            ("What does traceroute help you identify?", "The path packets take and where failures or high latency occur along the route"),
        ],
        "links": [
            ("SS64 — Windows Command Reference", "https://ss64.com/nt/"),
            ("SS64 — Linux Command Reference", "https://ss64.com/bash/"),
            ("MXToolbox — Network Tools", "https://mxtoolbox.com/NetworkTools.aspx"),
        ]
    },
    "7-3": {
        "notes": "Network diagrams visually represent the layout of a network. A physical diagram shows actual hardware locations, cable runs, and rack layouts. A logical diagram shows IP addressing, VLANs, routing, and how traffic flows — regardless of physical location. Both types appear in Network+ performance-based questions.\n\nStandard symbols: clouds represent the internet or an ISP, cylinders represent servers, rectangles are switches, the routing symbol is a circle with arrows, firewalls are represented by brick wall icons (varies by tool). Cisco uses specific icons for its devices. Being able to read and draw network diagrams is essential for planning, documentation, and troubleshooting. Tools like draw.io (free) or Lucidchart are commonly used.",
        "terms": [
            ("Physical Diagram", "Shows actual hardware, locations, and cable connections"),
            ("Logical Diagram", "Shows IP addressing, VLANs, and traffic flow regardless of physical layout"),
            ("Network Topology", "The arrangement of network components shown in a diagram"),
            ("Rack Diagram", "Shows equipment installed in server racks with U-space measurements"),
            ("draw.io", "Free online tool for creating network diagrams"),
        ],
        "questions": [
            ("What is the difference between a physical and logical network diagram?", "Physical shows actual hardware and cables; logical shows IP addressing and traffic flow"),
            ("Why are network diagrams important for troubleshooting?", "They provide a reference for understanding how the network is connected, making it faster to identify where a failure might be"),
        ],
        "links": [
            ("draw.io — Free Network Diagram Tool", "https://app.diagrams.net"),
            ("Lucidchart — Network Diagram Tool", "https://www.lucidchart.com/pages/network-diagram"),
            ("Packet Tracer — Free Cisco Network Simulator", "https://www.netacad.com/courses/packet-tracer"),
        ]
    },
    "7-4": {
        "notes": "Troubleshooting scenarios test your ability to apply methodology and tools to realistic problems. Common scenarios: 1) Duplicate IP address — two devices share an IP; symptoms are intermittent connectivity for both. Fix: use arp -a to find the conflict, assign a unique IP. 2) Wrong subnet mask — device can't reach some hosts but not others. Fix: ipconfig /all to verify mask. 3) Default gateway missing — device can reach local network but not the internet. Fix: verify gateway config. 4) DNS failure — can ping IPs but not names. Fix: nslookup to test, check DNS server assignment.\n\n5) Switching loop — broadcast storm, all ports at 100%, network unusable. Fix: STP should prevent this; check for disabled STP or non-managed switches. 6) VLAN mismatch — devices on the wrong VLAN can't communicate. Fix: verify switchport access vlan on Cisco. Practice recognising these patterns — they're exactly what appears in Network+ performance-based questions.",
        "terms": [
            ("Duplicate IP", "Two devices with the same IP; causes intermittent connectivity for both"),
            ("Broadcast Storm", "Network flooding caused by a switching loop; STP prevents this"),
            ("STP", "Spanning Tree Protocol — prevents switching loops by blocking redundant paths"),
            ("APIPA", "169.254.x.x — automatic address assigned when DHCP fails; indicates DHCP problem"),
            ("Default Gateway", "Missing or wrong gateway = can reach local network but not internet"),
        ],
        "questions": [
            ("A device gets a 169.254.x.x address. What does this indicate?", "APIPA — the device failed to get a DHCP lease; check DHCP server and connectivity"),
            ("A user can reach local servers but not the internet. What should you check first?", "The default gateway — it may be missing, wrong, or the router may be down"),
            ("What protocol prevents switching loops?", "STP — Spanning Tree Protocol (or RSTP, the faster version)"),
        ],
        "links": [
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
            ("ExamCompass — Free Network+ Practice", "https://www.comptia.org/training/certmaster-practice/network"),
            ("Packet Tracer — Free Cisco Network Simulator", "https://www.netacad.com/courses/packet-tracer"),
        ]
    },
    "8-1": {
        "notes": "The CompTIA Network+ N10-009 exam has up to 90 questions and a 90-minute time limit. The passing score is 720 out of 900. Question types include multiple choice (single and multiple answer), drag-and-drop, and performance-based questions (PBQs) — simulations where you configure devices or troubleshoot a network. PBQs appear at the start of the exam and are time-consuming — some candidates skip them and return at the end.\n\nThe five exam domains and their weights: Networking Fundamentals (23%), Network Implementation (19%), Network Operations (17%), Network Security (20%), Network Troubleshooting (21%). Security and Troubleshooting together make up 41% of the exam. The exam costs around $370 USD. CompTIA recommends 9-12 months of networking experience. Vouchers can often be found cheaper through academic or partner programs.",
        "terms": [
            ("N10-009", "Current CompTIA Network+ exam code"),
            ("PBQ", "Performance-Based Question — simulation requiring hands-on tasks"),
            ("Passing Score", "720 out of 900 (on a scaled score)"),
            ("Exam Domains", "Fundamentals 23%, Implementation 19%, Operations 17%, Security 20%, Troubleshooting 21%"),
            ("Exam Duration", "90 minutes, up to 90 questions"),
        ],
        "questions": [
            ("What is the passing score for Network+?", "720 out of 900"),
            ("How long is the Network+ exam?", "90 minutes"),
            ("What are PBQs and how should you approach them?", "Performance-Based Questions are simulations. Many candidates skip them initially and return at the end to avoid spending all their time on them"),
            ("Which two domains have the highest combined weight?", "Security (20%) and Troubleshooting (21%) — together 41% of the exam"),
        ],
        "links": [
            ("CompTIA Network+ Exam Objectives (Free PDF)", "https://www.comptia.org/training/resources/exam-objectives"),
            ("CompTIA Network+ Certification Page", "https://www.comptia.org/certifications/network"),
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
        ]
    },
    "8-2": {
        "notes": "This is your full timed practice exam. Set a timer for 90 minutes and attempt all questions without looking anything up. Treat it exactly like the real exam. When you finish, review every wrong answer — not just the right answer, but why the other options were wrong. This is how you learn the most.\n\nAfter the practice exam, identify your weak domains and return to those modules. Aim for 80%+ on practice exams before sitting the real thing. Professor Messer's practice exams and ExamCompass are excellent free resources. Jason Dion's Udemy course includes high-quality practice exams. Remember: the real exam has scenario-based questions that test application, not just memorisation.",
        "terms": [
            ("Process of Elimination", "On tricky questions, eliminate obviously wrong answers first to improve odds"),
            ("Keyword Analysis", "Read questions carefully for words like 'MOST', 'BEST', 'LEAST', 'NOT' — they change the answer"),
            ("Flag and Return", "Flag uncertain questions and return to them — don't spend too long on any single question"),
        ],
        "questions": [
            ("What score should you aim for on practice exams before sitting the real test?", "80% or higher consistently across multiple practice exams"),
            ("What should you do after reviewing wrong answers?", "Understand WHY each wrong answer was wrong, not just what the right answer is — this prevents the same mistake twice"),
        ],
        "links": [
            ("Professor Messer — Free Practice Exams", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
            ("ExamCompass — Free Network+ Quizzes", "https://www.comptia.org/training/certmaster-practice/network"),
            ("CompTIA CertMaster Practice (Official)", "https://www.comptia.org/training/certmaster-practice/network"),
        ]
    },
    "8-3": {
        "notes": "Final cram sheet — the highest-yield facts for the Network+ exam. Port numbers: FTP 20/21, SSH 22, Telnet 23, SMTP 25, DNS 53, DHCP 67/68, HTTP 80, POP3 110, IMAP 143, HTTPS 443, RDP 3389, RADIUS 1812/1813. OSI layers 1-7: Physical, Data Link, Network, Transport, Session, Presentation, Application. Private ranges: 10/8, 172.16/12, 192.168/16. Subnetting: /24=254 hosts, /25=126, /26=62, /27=30, /28=14, /29=6, /30=2.\n\nKey protocols: RADIUS UDP 1812, TACACS+ TCP 49, SNMP UDP 161, Syslog UDP 514, NTP UDP 123. Wireless: WEP=broken, WPA2-Personal=PSK, WPA2-Enterprise=802.1X, WPA3=SAE. IPv6 loopback=::1, link-local=fe80::/10. Troubleshooting: APIPA=169.254.x.x means DHCP failed. Always start at Layer 1 and work up.",
        "terms": [
            ("APIPA Range", "169.254.0.0/16 — assigned when DHCP fails"),
            ("NTP", "Network Time Protocol — synchronises clocks; UDP port 123"),
            ("SNMP", "Simple Network Management Protocol — monitoring; UDP 161/162"),
            ("Syslog", "Log collection protocol; UDP 514"),
            ("RDP", "Remote Desktop Protocol — Windows remote access; TCP 3389"),
        ],
        "questions": [
            ("What port does RDP use?", "TCP 3389"),
            ("What does an APIPA address indicate?", "DHCP failure — the device could not reach a DHCP server"),
            ("What is the IPv6 link-local prefix?", "fe80::/10"),
            ("What port does SNMP use?", "UDP 161 (queries) and 162 (traps)"),
            ("Name all 7 OSI layers in order.", "Physical, Data Link, Network, Transport, Session, Presentation, Application"),
        ],
        "links": [
            ("CompTIA Network+ Exam Objectives (Free PDF)", "https://www.comptia.org/training/resources/exam-objectives"),
            ("CompTIA Network+ Certification Page", "https://www.comptia.org/certifications/network"),
            ("Professor Messer — Network+ Course (Free)", "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"),
        ]
    },
}
