#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
"""

import sys

total_file_size = 0
status_counts = [0] * 8
line_count = 0

try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 2:
            if tokens[-2].isdigit():
                status_code = int(tokens[-2])
                if status_code >= 200 and status_code <= 500:
                    status_counts[status_code // 100 - 2] += 1
                    line_count += 1
            if tokens[-1].isdigit():
                file_size = int(tokens[-1])
                total_file_size += file_size
        if line_count % 10 == 0:
            print(f"Total file size: {total_file_size}")
            for code, count in enumerate(status_counts):
                if count:
                    print(f"{code+200}: {count}")
    print(f"Total file size: {total_file_size}")
    for code, count in enumerate(status_counts):
        if count:
            print(f"{code+200}: {count}")
except KeyboardInterrupt:
    print(f"Total file size: {total_file_size}")
    for code, count in enumerate(status_counts):
        if count:
            print(f"{code+200}: {count}")
