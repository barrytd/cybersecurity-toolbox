# 08 - SSH Monitor

Watches `/var/log/auth.log` (or equivalent) for failed SSH login attempts and prints alerts when an IP exceeds a configurable threshold.

## How to Run

```bash
python ssh_monitor.py [--log /var/log/auth.log] [--threshold 5]
```

Example:

```bash
sudo python ssh_monitor.py --log /var/log/auth.log --threshold 5
```

## What I Learned

_(I'll fill this in as I build the tool.)_

## Example Output

```
(Coming soon — paste a real run here once the script works.)
```
