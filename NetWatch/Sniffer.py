import socket
from scapy.all import Ether


print("=" * 70)
print(r"""
███╗   ██╗███████╗████████╗██╗    ██╗ █████╗ ████████╗ ██████╗██╗  ██╗
████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔══██╗╚══██╔══╝██╔════╝██║  ██║
██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║███████║   ██║   ██║     ███████║
██║╚██╗██║██╔══╝     ██║   ██║███╗██║██╔══██║   ██║   ██║     ██╔══██║
██║ ╚████║███████╗   ██║   ╚███╔███╔╝██║  ██║   ██║   ╚██████╗██║  ██║
╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝

        ▓▒░ Real-Time Network Monitoring ░▒▓
""")
print("=" * 70)


# Create raw socket
sniffer_socket = socket.socket(
    socket.AF_PACKET,
    socket.SOCK_RAW,
    socket.ntohs(3)
)

# Network interface
interface = "eth0"
sniffer_socket.bind((interface, 0))

print(f"[+] Listening on interface: {interface}")
print("[+] Press CTRL+C to stop\n")

try:
    while True:
        raw_data, addr = sniffer_socket.recvfrom(65535)
        packet = Ether(raw_data)
        print(packet.summary())

except KeyboardInterrupt:
    print("\n[!] Stopping NetWatch...")
    sniffer_socket.close()