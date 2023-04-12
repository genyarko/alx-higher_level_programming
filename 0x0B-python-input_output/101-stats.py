#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""


import sys
from collections import defaultdict

file_size = 0
status_tally = defaultdict(int)

try:
    for i, line in enumerate(sys.stdin, 1):
        tokens = line.split()
        if len(tokens) >= 2 and tokens[-2] in status_tally:
            status_tally[tokens[-2]] += 1
            file_size += int(tokens[-1])
        if i % 10 == 0:
            print(f"File size: {file_size}")
            for key in sorted(status_tally.keys()):
                if status_tally[key]:
                    print(f"{key}: {status_tally[key]}")
    print(f"File size: {file_size}")
    for key in sorted(status_tally.keys()):
        if status_tally[key]:
            print(f"{key}: {status_tally[key]}")

except KeyboardInterrupt:
    print(f"File size: {file_size}")
    for key in sorted(status_tally.keys()):
        if status_tally[key]:
            print(f"{key}: {status_tally[key]}")
