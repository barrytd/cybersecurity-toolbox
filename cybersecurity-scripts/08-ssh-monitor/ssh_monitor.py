"""
SSH Monitor
-----------
Tails an SSH auth log, parses each line for "Failed password" events, and
prints an alert when a single source IP exceeds a configurable failure
threshold inside a time window.

Planned libraries:
    re          - regex to pull IPs/usernames out of log lines
    collections - Counter / defaultdict to track per-IP attempts
    time        - sleep loop for tailing
    argparse    - parse command-line arguments

Usage (planned):
    sudo python ssh_monitor.py --log /var/log/auth.log --threshold 5
"""
