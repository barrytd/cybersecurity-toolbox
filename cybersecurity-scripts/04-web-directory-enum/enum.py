"""
Web Directory Enumerator
------------------------
Reads a wordlist of common path names (admin, backup, login, etc.) and sends
HTTP requests to <target>/<word> for each one. Reports any path that returns
a status code other than 404.

Planned libraries:
    requests          - send HTTP GET requests
    argparse          - parse command-line arguments
    concurrent.futures - run requests in parallel threads

Usage (planned):
    python enum.py --url http://example.com --wordlist common.txt --threads 20

Educational use only. Only enumerate sites you are authorized to test.
"""
