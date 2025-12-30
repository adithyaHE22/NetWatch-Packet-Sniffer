# 🛡️ NetWatch – Real-Time Packet Sniffer

**NetWatch** is a lightweight, real-time network packet sniffing tool written in Python.
It captures raw network packets directly from a network interface and decodes them to provide a clear, readable summary of live network traffic.

Designed for **cybersecurity students**, **networking beginners**, and **blue team learners**, NetWatch helps users understand how data flows through a network at the packet level.

---

## 📌 Introduction

Modern networks constantly exchange thousands of packets every second. Understanding these packets is essential for learning **networking**, **cybersecurity**, and **defensive monitoring**.

**NetWatch** provides a simple yet powerful way to observe network traffic in real time. By using raw sockets and the Scapy library, NetWatch captures Ethernet frames directly from the network interface and displays protocol-level summaries of each packet.

This project focuses on:

* Learning how packet sniffers work internally
* Understanding Ethernet and higher-layer protocols
* Gaining hands-on experience with raw sockets
* Building a foundation for network monitoring and intrusion detection

NetWatch is intentionally kept **minimal and readable**, making it ideal for educational purposes and further extension.

---

## ✨ Features

* 📡 Real-time packet capture
* 🔍 Ethernet frame decoding
* 🧠 Human-readable packet summaries
* ⚡ Lightweight and fast
* 🧪 Ideal for labs and learning
* 🛑 Clean shutdown using CTRL+C
* 🎨 Professional ASCII banner

---

## 🧰 Technologies Used

* **Python 3**
* **Socket Programming**
* **Scapy (Packet Parsing Library)**
* **Linux Raw Sockets**

---

## ⚙️ Requirements

* Linux-based operating system
  (Raw sockets require Linux)
* Python 3.x
* Scapy library
* Root / Administrator privileges

Install Scapy:

```bash
pip install scapy
```

---

## 🚀 How to Run

> ⚠️ **Important:** Raw socket access requires root privileges.

1. Clone the repository:

```bash
git clone https://github.com/your-username/NetWatch.git
```

2. Navigate to the project directory:

```bash
cd NetWatch
```

3. Run the tool:

```bash
sudo python3 netwatch.py
```

---

## 🖥️ Example Output

```
Ether / IP / TCP 192.168.1.10:443 > 192.168.1.5:52344
Ether / ARP who has 192.168.1.1 says 192.168.1.5
Ether / IP / UDP 8.8.8.8:53 > 192.168.1.5:59321
```

Each line represents a captured packet with a concise protocol summary.

---

## 🧠 How It Works

1. A raw socket listens to all packets on the selected network interface.
2. Packets are captured at the Ethernet layer.
3. Scapy’s `Ether()` function parses raw bytes into readable packet structures.
4. A summary of each packet is printed in real time.
5. The tool runs continuously until interrupted by the user.

---

## 🎓 Educational Use Cases

* Learning packet sniffing fundamentals
* Understanding network protocols
* Cybersecurity labs and assignments
* Blue team defensive monitoring basics
* Networking and security demonstrations

---

## ⚠️ Legal & Ethical Notice

This tool is intended **strictly for educational and authorized use**.

> ❗ Capturing network traffic without permission may be illegal and unethical.

Only use NetWatch:

* On networks you own
* On systems you are authorized to test
* In controlled lab environments

The author is **not responsible for misuse** of this tool.

---

## 🔮 Future Improvements

* Protocol filtering (TCP, UDP, ICMP, DNS, HTTP)
* Save captured packets to file (PCAP)
* Packet statistics and summaries
* Alert system for suspicious traffic
* GUI version
* Multi-interface support

---

## 👨‍💻 Author

**NetWatch Security Lab**
Cybersecurity Learning Project

---

## ⭐ License

This project is open-source and intended for learning and research purposes.
