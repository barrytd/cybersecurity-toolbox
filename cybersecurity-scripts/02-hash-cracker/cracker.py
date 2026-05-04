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

import hashlib
import argparse

parser = argparse.ArgumentParser(description="Simple hash cracker")
parser.add_argument("--hash", required=True)
parser.add_argument("--wordlist", default="wordlist.txt")
parser.add_argument("--algo", default="sha256", choices=["md5", "sha1", "sha256"])
args = parser.parse_args()

with open(args.wordlist) as f:
    wordlist = f.read().splitlines()
for word in wordlist:
    guess_hash = hashlib.new(args.algo, word.encode()).hexdigest()
    if guess_hash == args.hash:
        print(f"Password found: {word}")
        break
else:
    print("Password not found in wordlist.")