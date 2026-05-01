# 05 - Log Parser

Parses common log formats (Apache/Nginx access logs, Linux auth.log) and extracts useful info: top IPs, failed logins, error counts, suspicious user agents.

## How to Run

```bash
python parser.py --file <logfile> [--type access|auth]
```

Example:

```bash
python parser.py --file /var/log/auth.log --type auth
```

## What I Learned

_(I'll fill this in as I build the tool.)_

## Example Output

```
(Coming soon — paste a real run here once the script works.)
```
