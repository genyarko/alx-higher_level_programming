#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""

import sys
import signal

total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_metrics():
    print(f"Total file size: {total_file_size}")
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")

def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    ip, _, _, status_code, file_size = line.split()
    total_file_size += int(file_size)
    status_codes[int(status_code)] += 1
    line_count += 1
    if line_count % 10 == 0:
        print_metrics()

