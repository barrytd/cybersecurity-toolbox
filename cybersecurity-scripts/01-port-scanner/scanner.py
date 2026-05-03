"""
Port Scanner - v1 (basic)
Try to connect to a single port on a target host and report open/closed.
"""

import socket
import argparse

parser = argparse.ArgumentParser(description="Simple TCP port scanner")
parser.add_argument("--target", default="scanme.nmap.org")
parser.add_argument("--start", type=int, default=20)
parser.add_argument("--end", type=int, default=25)
args = parser.parse_args()

for port in range(args.start, args.end + 1):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)  # Set a timeout for the connection attempt

    result = s.connect_ex((args.target, port))
    if result == 0:
        print (f"Port {port} is OPEN")
        try:
            banner = s.recv(1024).decode().strip()
            if banner:
                print(f" Banner: {banner}")
        except:
            pass
    else:
        print (f"Port {port} is CLOSED")

    s.close()
