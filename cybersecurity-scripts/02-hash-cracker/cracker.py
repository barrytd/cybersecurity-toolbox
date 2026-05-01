"""
Hash Cracker
------------
Cracks an unsalted password hash by trying every word in a wordlist. Supports
MD5, SHA1, and SHA256.

Planned libraries:
    hashlib  - generate hashes for each candidate
    argparse - parse command-line arguments
    sys      - exit codes / stderr

Usage (planned):
    python cracker.py --hash <hash> --wordlist <path> --algo md5

Educational use only. Only crack hashes you are authorized to test.
"""
