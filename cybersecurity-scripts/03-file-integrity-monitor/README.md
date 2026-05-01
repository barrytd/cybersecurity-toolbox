# 03 - File Integrity Monitor

Detects unauthorized changes to files in a watched directory. On first run it builds a baseline of file hashes; on later runs it compares current hashes against the baseline and reports anything that has been added, modified, or deleted.

## How to Run

```bash
python monitor.py --path <dir> [--baseline baseline.json]
```

Example:

```bash
python monitor.py --path /etc --baseline baseline.json
```

## What I Learned

_(I'll fill this in as I build the tool.)_

## Example Output

```
(Coming soon — paste a real run here once the script works.)
```
