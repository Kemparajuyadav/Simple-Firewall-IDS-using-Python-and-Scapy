from scapy.all import sniff, IP, TCP, Raw

# Suspicious keywords to check in payload
SUSPICIOUS_KEYWORDS = ["attack", "malware", "hack", "exploit"]

def alert(message, src, dst, dport):
    print(f"[!] ALERT: {message} from {src} → {dst}:{dport}")

def analyze_packet(packet):
    if packet.haslayer(IP):
        src = packet[IP].src
        dst = packet[IP].dst

        if packet.haslayer(TCP):
            sport = packet[TCP].sport
            dport = packet[TCP].dport

            # Simple port scan detection
            if sport > 1024 and dport < 1024:
                alert("Possible Port Scan Detected", src, dst, dport)

        if packet.haslayer(Raw):
            payload = packet[Raw].load.decode(errors="ignore")
            if any(word in payload.lower() for word in SUSPICIOUS_KEYWORDS):
                alert("Suspicious Payload Found", src, dst, 'N/A')

print("[*] Starting Simple IDS... Press CTRL+C to stop.")
sniff(prn=analyze_packet, store=False)
