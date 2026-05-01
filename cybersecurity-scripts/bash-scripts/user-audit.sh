#!/usr/bin/env bash
# user-audit.sh
# -------------
# Audits local user accounts: lists users with login shells, members of the
# sudo/wheel group, and recent successful/failed logins. Useful for spotting
# unexpected accounts or privilege escalation footholds.
#
# Planned commands: getent, awk, lastlog, last, grep
#
# Usage (planned):
#     sudo ./user-audit.sh
