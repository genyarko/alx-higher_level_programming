#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""

#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""


import sys

file_size = 0
status_tally = [0] * 8
i = 0

try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 2:
            if tokens[-2].isdigit():
                status_code = int(tokens[-2])
                if status_code >= 200 and status_code <= 500:
                    status_tally[status_code // 100 - 2] += 1
                    i += 1
            if tokens[-1].isdigit():
                file_size += int(tokens[-1])
        if i % 10 == 0:
            print(f"File size: {file_size}")
            for code, count in enumerate(status_tally):
                if count:
                    print(f"{code+200}: {count}")
    print(f"File size: {file_size}")
    for code, count in enumerate(status_tally):
        if count:
            print(f"{code+200}: {count}")
except KeyboardInterrupt:
    print(f"File size: {file_size}")
    for code, count in enumerate(status_tally):
        if count:
            print(f"{code+200}: {count}")
