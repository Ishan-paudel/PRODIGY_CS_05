from scapy.all import sniff, IP, TCP, UDP, Raw

# Function to process each captured packet
def analyze_packet(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        print(f"\n[+] Packet Captured:")
        print(f"    Source IP: {ip_src}")
        print(f"    Destination IP: {ip_dst}")

        if protocol == 6:  # TCP
            print("    Protocol: TCP")
            if TCP in packet:
                print(f"    Source Port: {packet[TCP].sport}")
                print(f"    Destination Port: {packet[TCP].dport}")

        elif protocol == 17:  # UDP
            print("    Protocol: UDP")
            if UDP in packet:
                print(f"    Source Port: {packet[UDP].sport}")
                print(f"    Destination Port: {packet[UDP].dport}")
        else:
            print(f"    Protocol: {protocol}")

        # Payload data
        if Raw in packet:
            payload_data = packet[Raw].load
            print(f"    Payload (raw): {payload_data[:50]}")  # limit preview

# Sniff packets (use Ctrl+C to stop)
print("Starting Network Packet Analyzer...\nPress Ctrl+C to stop.\n")
sniff(prn=analyze_packet, store=False)
