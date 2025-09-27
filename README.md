
# 🛰️ Network Packet Analyzer

A simple **Python-based packet sniffer tool** that captures and analyzes network packets.  
It displays useful information such as **source and destination IP addresses, ports, protocols, and payload data**.  

⚠️ This project is strictly for **educational purposes** and must be used ethically on networks you own or have permission to analyze.

---

## 🚀 Features
- Capture real-time network packets
- Display:
  - Source & Destination IP addresses
  - Protocol type (TCP, UDP, etc.)
  - Source & Destination Ports
  - Payload data (raw, preview)
- Cross-platform support (Linux, Windows, macOS)
- Lightweight and beginner-friendly

---

## 🛠️ Requirements
- Python **3.8+**
- Install dependencies:
  ```bash
  pip install scapy
````

* On **Windows**, install [Npcap](https://nmap.org/npcap/) (with *WinPcap compatibility mode* enabled).

---

## ▶️ Usage

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/network-packet-analyzer.git
cd network-packet-analyzer
```

### 2. Run the Program

#### 🔹 On Linux/macOS

```bash
sudo python app.py
```

#### 🔹 On Windows

1. Open **PowerShell as Administrator**
2. Run:

   ```powershell
   python app.py
   ```

---

## 📌 Example Output

```
[+] Packet Captured:
    Source IP: 192.168.1.10
    Destination IP: 142.250.182.78
    Protocol: TCP
    Source Port: 56723
    Destination Port: 443
    Payload (raw): b'GET / HTTP/1.1\r\nHost: www.google.com\r\n...'
```

---

## ⚖️ Ethical Disclaimer

This tool is made **only for educational purposes** to understand how packet sniffing works.
Do **not** use it on networks you don’t own or without proper authorization, as that may violate privacy laws.

---

## 📂 Project Structure

```
NPA/
│── app.py         # Main packet sniffer code
│── README.md      # Project documentation
│── venv/          # Virtual environment (optional)
```

---

## 📚 Learning Resources

* [Scapy Documentation](https://scapy.readthedocs.io/en/latest/)
* [Npcap (Windows Packet Capture Library)](https://nmap.org/npcap/)
* [Wireshark](https://www.wireshark.org/) (for advanced packet analysis)

---

## 👨‍💻 Author

Developed as part of a **Cybersecurity Educational Project (Task-05: Network Packet Analyzer)**.

```

---

Do you want me to also add a **"Demo GIF/Usage Screenshot" section** in the README so it looks even more professional on GitHub?
```
