"""
Packet Sniffer
--------------
Captures live network traffic on a chosen interface and prints a one-line
summary for each packet (timestamps, src/dst IP, protocol, ports). Optional
BPF filter to narrow the capture (e.g. "tcp port 80").

Planned libraries:
    scapy    - packet capture and dissection
    argparse - parse command-line arguments

Usage (planned):
    sudo python sniffer.py --iface eth0 --filter "tcp port 80"

Educational use only. Only sniff networks you own or have permission to monitor.
"""
