# Cybersecurity Scripting Portfolio

A collection of Python and Bash security tools I'm building while learning offensive and defensive security scripting. Each project starts simple and grows in features as I add new concepts.

This repo is a **learning portfolio** — the code is meant to demonstrate fundamentals (sockets, hashing, file I/O, parsing, networking) rather than replace production tools like Nmap, Hashcat, or AIDE.

**Author:** Robert

> **Status:** Active work-in-progress. Only **Project 01 (Port Scanner)** is currently in progress — the rest are placeholders for upcoming projects and will be filled in as I work through them. The structure is laid out in advance so the roadmap is visible.

---

## Projects

| # | Project | Description | Skills Learned |
|---|---------|-------------|----------------|
| 01 | [Port Scanner](./cybersecurity-scripts/01-port-scanner) | TCP port scanner that checks which ports are open on a target host | Sockets, TCP handshake, error handling, CLI args |
| 02 | [Hash Cracker](./cybersecurity-scripts/02-hash-cracker) | Dictionary-based hash cracker for MD5/SHA1/SHA256 | Hashing, file I/O, brute force concepts |
| 03 | [File Integrity Monitor](./cybersecurity-scripts/03-file-integrity-monitor) | Detects when files have been modified by comparing hashes | Hashing, JSON, filesystem walking |
| 04 | [Web Directory Enumerator](./cybersecurity-scripts/04-web-directory-enum) | Discovers hidden directories on a web server using a wordlist | HTTP requests, status codes, threading |
| 05 | [Log Parser](./cybersecurity-scripts/05-log-parser) | Parses auth/web logs to find suspicious activity | Regex, file parsing, dict counting |
| 06 | [Packet Sniffer](./cybersecurity-scripts/06-packet-sniffer) | Captures and inspects network packets on the wire | Scapy, network layers, protocols |
| 07 | [Subnet Calculator](./cybersecurity-scripts/07-subnet-calculator) | Calculates network/broadcast/host ranges from CIDR input | IP math, bitwise ops, ipaddress module |
| 08 | [SSH Monitor](./cybersecurity-scripts/08-ssh-monitor) | Watches auth logs for failed SSH login attempts | Log monitoring, regex, alerting |
| -- | [Bash Scripts](./cybersecurity-scripts/bash-scripts) | System info, log analysis, backups, user audit, ping sweep | Shell scripting, pipes, cron-friendly tools |

---

## Technologies Used

- **Python 3** — primary language for tooling
- **Bash** — system-level scripts and quick recon helpers
- **Key Python libraries:**
  - `socket` — low-level network connections (port scanner, sniffer)
  - `hashlib` — cryptographic hashing (cracker, integrity monitor)
  - `requests` — HTTP client (web enum)
  - `scapy` — packet crafting and sniffing
  - `ipaddress` — IP/CIDR math (subnet calc)
  - `argparse` — CLI argument parsing across all tools
  - `re` — regex pattern matching (log parser, ssh monitor)

---

## Other Portfolio

For my hands-on security work (CTF write-ups, lab walkthroughs, vulnerability research):
[security-lab-portfolio](https://github.com/barrytd/security-lab-portfolio)

---

## Disclaimer

These tools are for **educational use and authorized testing only**. Do not run them against systems you do not own or have explicit written permission to test.
