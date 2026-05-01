"""
Subnet Calculator
-----------------
Given an IPv4 address in CIDR form (e.g. 192.168.1.0/24), prints:
    - network address
    - broadcast address
    - subnet mask (dotted and prefix length)
    - first/last usable host
    - total usable hosts

Planned libraries:
    ipaddress - built-in IP/CIDR math (handles all the bitwise work for us)
    argparse  - parse command-line arguments

Usage (planned):
    python subnetcalc.py 192.168.1.0/24
"""
