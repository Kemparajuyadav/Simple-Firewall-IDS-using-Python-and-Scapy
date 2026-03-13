import socket
from threading import Thread
from scapy.all import sniff, IP, TCP, Raw

# --- 1. THE SCANNER (Multi-threaded) ---
def scan_port(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.5)
    result = scanner.connect_ex((ip, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN on {ip}")
    scanner.close()

def run_scanner(ip, port_range):
    print(f"[*] Scanning {ip}...")
    for port in port_range:
        # Using threads makes the scan 100x faster
        t = Thread(target=scan_port, args=(ip, port))
        t.start()

# --- 2. THE IDS (Packet Sniffer) ---
SUSPICIOUS_KEYWORDS = ["attack", "malware", "exploit"]

def analyze_packet(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        src = packet[IP].src
        dport = packet[TCP].dport
        
        # Detection logic
        if packet.haslayer(Raw):
            payload = packet[Raw].load.decode(errors="ignore").lower()
            if any(word in payload for word in SUSPICIOUS_KEYWORDS):
                print(f"[!] ALERT: Suspicious keyword from {src} to port {dport}")

# --- EXECUTION ---
if __name__ == "__main__":
    # Start IDS in background
    print("[*] IDS Active... Listening for threats.")
    sniff(prn=analyze_packet, store=False, count=10) # Simplified for example
