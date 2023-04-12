#!/usr/bin/env python3
"""
a script that reads stdin line by line and computes metrics
"""
import sys

def print_metrics(total_file_size, status_codes):
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0
count = 0

try:
    for line in sys.stdin:
        count += 1
        split_line = line.split()
        status_code = int(split_line[-2])
        file_size = int(split_line[-1])
        total_file_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1
        if count % 10 == 0:
            print_metrics(total_file_size, status_codes)
except KeyboardInterrupt:
    print_metrics(total_file_size, status_codes)
    sys.exit(0)
