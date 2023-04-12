#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""


import sys
from collections import defaultdict

def print_stats(total_size, status_codes):
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

def parse_line(line):
    parts = line.split()
    ip_address = parts[0]
    status_code = int(parts[3])
    file_size = int(parts[4])
    return ip_address, status_code, file_size

total_size = 0
status_codes = defaultdict(int)
count = 0

try:
    for line in sys.stdin:
        ip_address, status_code, file_size = parse_line(line)
        total_size += file_size
        status_codes[status_code] += 1
        count += 1
        if count % 10 == 0:
            print_stats(total_size, status_codes)
except KeyboardInterrupt:
    print_stats(total_size, status_codes)


