#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""


import sys

status_tally = [0] * 8
file_size = 0
i = 0

try:
    for line in sys.stdin:
        try:
            _, _, _, status, size = line.rsplit(maxsplit=4)
        except ValueError:
            continue

        try:
            size = int(size)
        except ValueError:
            continue

        file_size += size

        status_code = int(status[0] + '00')
        if status_code in [200, 300, 400, 500]:
            status_tally[(status_code // 100) - 2] += 1

        i += 1
        if i % 10 == 0:
            print(f"File size: {file_size}")
            for j in range(len(status_tally)):
                if status_tally[j] > 0:
                    print(f"{(j+2)*100}: {status_tally[j]}")

    print(f"File size: {file_size}")
    for j in range(len(status_tally)):
        if status_tally[j] > 0:
            print(f"{(j+2)*100}: {status_tally[j]}")

except KeyboardInterrupt:
    print(f"\nFile size: {file_size}")
    for j in range(len(status_tally)):
        if status_tally[j] > 0:
            print(f"{(j+2)*100}: {status_tally[j]}")
