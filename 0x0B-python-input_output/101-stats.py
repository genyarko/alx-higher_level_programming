#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""

import sys
from collections import defaultdict

file_size = 0
status_tally = defaultdict(int)
i = 0

try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 2:
            if tokens[-2] in status_tally:
                status_tally[tokens[-2]] += 1
                i += 1
            try:
                file_size += int(tokens[-1])
                i += 1
            except (ValueError, FileNotFoundError):
                pass
        if i % 10 == 0:
            print(f"File size: {file_size}")
            for key, value in sorted(status_tally.items()):
                if value:
                    print(f"{key}: {value}")
    print(f"File size: {file_size}")
    for key, value in sorted(status_tally.items()):
        if value:
            print(f"{key}: {value}")

except KeyboardInterrupt:
    print(f"File size: {file_size}")
    for key, value in sorted(status_tally.items()):
        if value:
            print(f"{key}: {value}")
