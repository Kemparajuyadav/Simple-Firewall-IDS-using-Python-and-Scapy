# Simple-Firewall-IDS-using-Python-and-Scapy

📌 Project Overview
InsightScan is a Python-based security tool designed for network discovery and threat detection. It combines a high-speed, multi-threaded port scanner with a signature-based Intrusion Detection System (IDS) to monitor and secure local network traffic.

🚀 Key Features
Multi-threaded Scanning: Uses Python's threading and socket libraries to identify open ports 10x faster than sequential scanning.

Live Packet Sniffing: Leverages Scapy to intercept and dissect real-time TCP/IP traffic.

Signature-based Detection: Analyzes raw packet payloads for suspicious keywords (e.g., "attack", "exploit") using Deep Packet Inspection (DPI).

Heuristic Analysis: Detects potential port-scanning behavior by monitoring source-destination port patterns.

🛠️ Tech Stack
Language: Python 3.x
Libraries: Scapy, Socket, Threading
Environment: Windows (Compatible with Npcap)

📖 How It Works
Scanning Phase: The tool iterates through a range of ports, attempting to establish a 3-way handshake. Multi-threading allows multiple "probes" to happen simultaneously.

Monitoring Phase: The IDS engine enters a sniffing loop, capturing every packet on the network interface.

Analysis Phase: Each packet is "peeled" through its layers (IP -> TCP -> Raw). If the payload matches a known threat signature or if a host is probing sensitive ports, a real-time alert is triggered.

💻 Installation & Usage
Clone the repository:
Bash
git clone https://github.com/yourusername/insightscan.git
Install dependencies:
Bash
pip install scapy
Note: Ensure Npcap is installed for Windows packet capturing.
Run the tool:
Bash
python insightscan.py
Pro-Tips for your GitHub:
Screenshots: Take a screenshot of your code running and showing a "Port Open" or "Alert" message. Add that image to the README.

Pin it: On your main GitHub profile, use the "Pin" feature to make sure this project stays at the very top.

License: Add a simple "MIT License" file so it looks like a real open-source project.

1. Successful Network Browsing (Normal Traffic)
When the system detects standard web traffic or a safe connection, it logs the activity without triggering alerts.
[*] Monitoring Network...
[+] Connection established: 192.168.1.15 -> 93.184.216.34:443 (HTTPS)
[+] Packet captured: [TCP] Source: 192.168.1.15 | Destination: 8.8.8.8 | Size: 64 bytes
[+] Status: Successfully Browsing - No threats detected.


2. ⚠️ WARNING: Malicious Activity Detected
If a keyword like "exploit" or "attack" is found in the packet payload, or if a port scan is detected, the system triggers a high-priority warning.

Bash
[!] ALERT: SUSPICIOUS ACTIVITY DETECTED
------------------------------------------------------------
TYPE: Signature-based Detection (IDS)
SOURCE: 10.0.0.52
THREAT: Suspicious Payload Found
KEYWORD: "exploit"
ACTION: Packet flagged and logged to alerts.log
------------------------------------------------------------
[!] WARNING: Possible Port Scan from 10.0.0.52 to Port 22
