# 06 - Packet Sniffer

Captures network packets on a chosen interface and prints summaries of each one (source/destination IP, protocol, port).

> Requires admin/root privileges to access raw sockets.

## How to Run

```bash
sudo python sniffer.py --iface <interface> [--filter "tcp port 80"]
```

Example:

```bash
sudo python sniffer.py --iface eth0 --filter "tcp port 80"
```

## What I Learned

_(I'll fill this in as I build the tool.)_

## Example Output

```
(Coming soon — paste a real run here once the script works.)
```
