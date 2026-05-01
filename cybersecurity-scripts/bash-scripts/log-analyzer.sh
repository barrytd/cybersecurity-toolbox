#!/usr/bin/env bash
# log-analyzer.sh
# ---------------
# Pulls quick stats out of a log file: top source IPs, count of errors/warnings,
# most-requested URLs. A bash counterpart to the Python log parser project.
#
# Planned commands: awk, grep, sort, uniq -c, head
#
# Usage (planned):
#     ./log-analyzer.sh /var/log/nginx/access.log
