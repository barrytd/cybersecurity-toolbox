"""
Log Parser
----------
Reads a log file line-by-line, applies regex patterns to extract fields, and
summarises interesting activity (top source IPs, failed logins, 4xx/5xx
counts, etc.).

Planned libraries:
    re          - regex pattern matching
    collections - Counter for top-N tallies
    argparse    - parse command-line arguments

Usage (planned):
    python parser.py --file /var/log/auth.log --type auth
"""
