#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""

import sys

STATUS_CODES = ("200", "301", "400", "401", "403", "404", "405", "500")

def print_stats(file_size, status_tally):
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

file_size = 0
status_tally = {code: 0 for code in STATUS_CODES}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        tokens = line.split()
        if len(tokens) >= 7:
            status_code = tokens[-2]
            if status_code in status_tally:
                status_tally[status_code] += 1
            try:
                file_size += int(tokens[-1])
            except ValueError:
                pass

        if line_count % 10 == 0:
            print_stats(file_size, status_tally)

    print_stats(file_size, status_tally)

except KeyboardInterrupt:
    print_stats(file_size, status_tally)
