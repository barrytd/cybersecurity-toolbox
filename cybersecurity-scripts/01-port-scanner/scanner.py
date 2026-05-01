"""
Port Scanner - v1 (basic)
Try to connect to a single port on a target host and report open/closed.
"""

import socket
target = "scanme.nmap.org"
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(3)

result = s.connect_ex((target, port))
if result == 0:
    print (f"Port {port} is OPEN")
else:
    print (f"Port {port} is CLOSED")

s.close()