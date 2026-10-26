
ASSESSMENT_SECTIONS = [
    {
        "id": "s1",
        "title": "Networking Fundamentals",
        "type": "rated",
        "questions": [
            {"id": "s1q1", "text": "How proficient are you with the OSI model and its application to troubleshooting?"},
            {"id": "s1q2", "text": "How proficient are you with the TCP/IP protocol suite?"},
            {"id": "s1q3", "text": "How proficient are you with IPv4 addressing, subnetting, and CIDR notation?"},
            {"id": "s1q4", "text": "How proficient are you with IPv6 addressing and routing?"},
            {"id": "s1q5", "text": "How proficient are you with TCP and UDP communications, including session establishment and teardown?"},
            {"id": "s1q6", "text": "How proficient are you with ARP, ICMP, DNS, and DHCP?"},
            {"id": "s1q7", "text": "How proficient are you with MTU, MSS, and packet fragmentation?"},
            {"id": "s1q8", "text": "How proficient are you with interpreting packet headers and protocol behavior?"},
        ]
    },
    {
        "id": "s2",
        "title": "Layer 2 Switching",
        "type": "rated",
        "questions": [
            {"id": "s2q1", "text": "How proficient are you with VLAN configuration and 802.1Q trunking?"},
            {"id": "s2q2", "text": "How proficient are you with Spanning Tree Protocol (STP, RSTP, MSTP)?"},
            {"id": "s2q3", "text": "How proficient are you with link aggregation and LACP?"},
            {"id": "s2q4", "text": "How proficient are you with MAC address tables and Layer 2 forwarding?"},
            {"id": "s2q5", "text": "How proficient are you with switch port security and 802.1X authentication?"},
            {"id": "s2q6", "text": "How proficient are you with troubleshooting broadcast storms, loops, and MAC flapping?"},
            {"id": "s2q7", "text": "How proficient are you with MLAG, vPC, or equivalent multi-chassis switching technologies?"},
        ]
    },
    {
        "id": "s3",
        "title": "Routing",
        "type": "rated",
        "questions": [
            {"id": "s3q1", "text": "How proficient are you with static and default routing?"},
            {"id": "s3q2", "text": "How proficient are you with OSPF configuration and troubleshooting?"},
            {"id": "s3q3", "text": "How proficient are you with BGP configuration and troubleshooting?"},
            {"id": "s3q4", "text": "How proficient are you with route redistribution between routing protocols?"},
            {"id": "s3q5", "text": "How proficient are you with policy-based routing?"},
            {"id": "s3q6", "text": "How proficient are you with ECMP and asymmetric routing?"},
            {"id": "s3q7", "text": "How proficient are you with VRFs and route segmentation?"},
            {"id": "s3q8", "text": "How proficient are you with troubleshooting routing convergence and failover?"},
        ]
    },
    {
        "id": "s4",
        "title": "Network Security",
        "type": "rated",
        "questions": [
            {"id": "s4q1", "text": "How proficient are you with stateful firewall operation and rule configuration?"},
            {"id": "s4q2", "text": "How proficient are you with next-generation firewall capabilities and application identification?"},
            {"id": "s4q3", "text": "How proficient are you with IDS and IPS deployment and operation?"},
            {"id": "s4q4", "text": "How proficient are you with network segmentation and microsegmentation?"},
            {"id": "s4q5", "text": "How proficient are you with site-to-site and remote-access VPN technologies?"},
            {"id": "s4q6", "text": "How proficient are you with Zero Trust Network Access (ZTNA)?"},
            {"id": "s4q7", "text": "How proficient are you with TLS/SSL inspection and encrypted traffic visibility?"},
            {"id": "s4q8", "text": "How proficient are you with network security policy design and rule optimization?"},
            {"id": "s4q9", "text": "How proficient are you with network threat detection and response (NDR)?"},
            {"id": "s4q10", "text": "How proficient are you with troubleshooting security-related connectivity problems?"},
        ]
    },
    {
        "id": "s5",
        "title": "Network Troubleshooting and Analysis",
        "type": "rated",
        "questions": [
            {"id": "s5q1", "text": "How proficient are you with Wireshark or equivalent packet analysis tools?"},
            {"id": "s5q2", "text": "How proficient are you with TCP retransmissions, windowing, and connection analysis?"},
            {"id": "s5q3", "text": "How proficient are you with diagnosing latency, jitter, and packet loss?"},
            {"id": "s5q4", "text": "How proficient are you with identifying network congestion and oversubscription?"},
            {"id": "s5q5", "text": "How proficient are you with SNMP monitoring and interface statistics?"},
            {"id": "s5q6", "text": "How proficient are you with NetFlow, IPFIX, or sFlow traffic analysis?"},
            {"id": "s5q7", "text": "How proficient are you with SPAN, RSPAN, ERSPAN, and network TAPs?"},
            {"id": "s5q8", "text": "How proficient are you with correlating network events across multiple devices?"},
            {"id": "s5q9", "text": "How proficient are you with troubleshooting intermittent application connectivity problems?"},
        ]
    },
    {
        "id": "s6",
        "title": "Network Architecture and Design",
        "type": "rated",
        "questions": [
            {"id": "s6q1", "text": "How proficient are you with designing enterprise LAN/WAN architectures?"},
            {"id": "s6q2", "text": "How proficient are you with designing high-availability and redundant networks?"},
            {"id": "s6q3", "text": "How proficient are you with network capacity planning?"},
            {"id": "s6q4", "text": "How proficient are you with QoS design and implementation?"},
            {"id": "s6q5", "text": "How proficient are you with SD-WAN architecture and operation?"},
            {"id": "s6q6", "text": "How proficient are you with data center spine-leaf architectures?"},
            {"id": "s6q7", "text": "How proficient are you with network resiliency, disaster recovery, and failover design?"},
            {"id": "s6q8", "text": "How proficient are you with network design documentation and topology development?"},
        ]
    },
    {
        "id": "s7",
        "title": "Cloud and Virtual Networking",
        "type": "rated",
        "questions": [
            {"id": "s7q1", "text": "How proficient are you with AWS VPC networking?"},
            {"id": "s7q2", "text": "How proficient are you with Microsoft Azure virtual networking?"},
            {"id": "s7q3", "text": "How proficient are you with hybrid cloud networking and connectivity?"},
            {"id": "s7q4", "text": "How proficient are you with cloud routing, security groups, and network ACLs?"},
            {"id": "s7q5", "text": "How proficient are you with VMware virtual switching and distributed switches?"},
            {"id": "s7q6", "text": "How proficient are you with Linux networking, bridges, and virtual interfaces?"},
            {"id": "s7q7", "text": "How proficient are you with container and Kubernetes networking?"},
            {"id": "s7q8", "text": "How proficient are you with troubleshooting connectivity between cloud and on-premises environments?"},
        ]
    },
    {
        "id": "s8",
        "title": "Network Automation and Management",
        "type": "rated",
        "questions": [
            {"id": "s8q1", "text": "How proficient are you with Python scripting for network automation?"},
            {"id": "s8q2", "text": "How proficient are you with REST APIs for network device management?"},
            {"id": "s8q3", "text": "How proficient are you with Ansible or equivalent configuration automation tools?"},
            {"id": "s8q4", "text": "How proficient are you with network configuration backup and version control?"},
            {"id": "s8q5", "text": "How proficient are you with infrastructure-as-code concepts and tools?"},
            {"id": "s8q6", "text": "How proficient are you with network monitoring platforms and alert configuration?"},
            {"id": "s8q7", "text": "How proficient are you with automating repetitive troubleshooting or configuration tasks?"},
        ]
    },
    {
        "id": "s9",
        "title": "Advanced Networking and Security",
        "type": "rated",
        "questions": [
            {"id": "s9q1", "text": "How proficient are you with multicast networking and protocols such as IGMP and PIM?"},
            {"id": "s9q2", "text": "How proficient are you with MPLS and service-provider routing concepts?"},
            {"id": "s9q3", "text": "How proficient are you with VXLAN and EVPN overlays?"},
            {"id": "s9q4", "text": "How proficient are you with inline network security deployments and bypass technologies?"},
            {"id": "s9q5", "text": "How proficient are you with load balancing and application delivery controllers?"},
            {"id": "s9q6", "text": "How proficient are you with network packet brokers and traffic distribution architectures?"},
            {"id": "s9q7", "text": "How proficient are you with identifying and mitigating asymmetric network flows?"},
            {"id": "s9q8", "text": "How proficient are you with network performance benchmarking and throughput validation?"},
            {"id": "s9q9", "text": "How proficient are you with securing and monitoring east-west data center traffic?"},
            {"id": "s9q10", "text": "How proficient are you with integrating network telemetry into SIEM, XDR, or other security platforms?"},
        ]
    },
    {
        "id": "s10",
        "title": "Practical Engineering Experience",
        "type": "multiple_choice",
        "questions": [
            {"id": "s10q1", "text": "How many years of professional networking experience do you have?",
             "options": ["Less than 1 year", "1-3 years", "4-7 years", "8-15 years", "More than 15 years"]},
            {"id": "s10q2", "text": "What is the largest network environment you have supported?",
             "options": ["Fewer than 100 network devices", "100-500 devices", "501-2000 devices", "More than 2000 devices", "Unsure / Not applicable"]},
            {"id": "s10q3", "text": "Which network equipment vendors do you have hands-on experience with? (Select all that apply.)",
             "options": ["Cisco", "Juniper", "Arista", "HPE / Aruba", "Fortinet", "Palo Alto Networks", "Check Point", "Extreme Networks", "Other"],
             "multi": True},
            {"id": "s10q4", "text": "Which network security technologies have you personally deployed or managed? (Select all that apply.)",
             "options": ["Firewalls", "IDS/IPS", "NDR", "VPN", "ZTNA", "Network access control", "DDoS protection", "Secure web gateways", "Cloud network security", "Other"],
             "multi": True},
            {"id": "s10q5", "text": "Which certifications do you currently hold? (Select all that apply.)",
             "options": ["CompTIA Network+", "CompTIA Security+", "Cisco CCNA", "Cisco CCNP", "Cisco CCIE", "Juniper JNCIA/JNCIS/JNCIP/JNCIE", "CISSP", "AWS networking or cloud certification", "Azure networking or cloud certification", "Vendor-specific security certifications", "Other / None"],
             "multi": True},
        ]
    },
    {
        "id": "s11",
        "title": "Engineering Judgment and Problem Solving",
        "type": "open",
        "questions": [
            {"id": "s11q1", "text": "A customer reports intermittent application latency, but interface utilization remains below 30%. How would you investigate?"},
            {"id": "s11q2", "text": "A network experiences asymmetric routing through two stateful firewalls. What problems could occur, and how would you resolve them?"},
            {"id": "s11q3", "text": "An application works correctly within one VLAN but fails when communicating across VLANs. Describe your troubleshooting approach."},
            {"id": "s11q4", "text": "A packet capture shows TCP retransmissions but no obvious interface errors. What would you investigate next?"},
            {"id": "s11q5", "text": "You are designing a highly available data center network. What are the most important architectural considerations?"},
            {"id": "s11q6", "text": "A customer complains that an IPS deployment is affecting application performance. How would you validate or disprove that hypothesis?"},
            {"id": "s11q7", "text": "Describe the most complex networking problem you have personally resolved. What was the root cause?"},
            {"id": "s11q8", "text": "Describe a network architecture you designed or significantly improved. What trade-offs did you make?"},
        ]
    },
    {
        "id": "s12",
        "title": "Professional Development",
        "type": "open",
        "questions": [
            {"id": "s12q1", "text": "What are your three strongest technical networking skills?"},
            {"id": "s12q2", "text": "Which three networking technologies would you most like to improve?"},
            {"id": "s12q3", "text": "Which networking or security certifications are you currently pursuing or planning to pursue?"},
            {"id": "s12q4", "text": "Are you comfortable serving as a technical mentor for other engineers?",
             "options": ["Yes", "No", "With assistance"], "type": "single"},
            {"id": "s12q5", "text": "Which networking technologies would you consider yourself qualified to teach?"},
            {"id": "s12q6", "text": "What technical training, lab equipment, or resources would most improve your effectiveness?"},
            {"id": "s12q7", "text": "What type of engineering work interests you most?",
             "options": ["Network operations", "Troubleshooting", "Network design", "Security architecture", "Automation", "Cloud networking", "Technical leadership", "Other"],
             "type": "single"},
        ]
    },
]

RATING_LABELS = {
    1: "No Experience",
    2: "Basic",
    3: "Proficient",
    4: "Advanced",
    5: "Expert"
}

COMPETENCY_LEVELS = [
    (1.0, 1.99, "Foundational"),
    (2.0, 2.99, "Developing"),
    (3.0, 3.74, "Proficient"),
    (3.75, 4.49, "Advanced"),
    (4.5, 5.0, "Expert"),
]

def get_competency(score):
    for low, high, label in COMPETENCY_LEVELS:
        if low <= score <= high:
            return label
    return "N/A"
