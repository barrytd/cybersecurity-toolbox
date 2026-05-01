"""
File Integrity Monitor
----------------------
Walks a directory, computes a SHA256 hash of every file, and saves the result
as a JSON baseline. Subsequent runs compare current hashes against the baseline
and report added, modified, or deleted files.

Planned libraries:
    hashlib  - SHA256 hash of file contents
    os       - walk the filesystem
    json     - persist the baseline
    argparse - parse command-line arguments

Usage (planned):
    python monitor.py --path <dir> --baseline baseline.json
"""
