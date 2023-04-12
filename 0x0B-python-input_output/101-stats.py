#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""

import sys
from collections import defaultdict

def print_stats(file_size, status_tally):
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

file_size = 0
status_tally = defaultdict(int)
try:
    for i, line in enumerate(sys.stdin, start=1):
        tokens = line.split()
        if len(tokens) >= 2 and tokens[-2] in status_tally:
            status_tally[tokens[-2]] += 1
        try:
            file_size += int(tokens[-1])
        except (IndexError, ValueError):
            pass
        if i % 10 == 0:
            print_stats(file_size, status_tally)
    print_stats(file_size, status_tally)
except KeyboardInterrupt:
    print_stats(file_size, status_tally)
