#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""

import sys

# use a list with fixed size instead of a dictionary
status_tally = [0] * 8
# index in list corresponds to status code, so we can increment directly

file_size = 0

try:
    for i, line in enumerate(sys.stdin, start=1):
        tokens = line.split()
        if len(tokens) >= 2:
            if tokens[-2].isdigit():
                # use index in list to increment status code tally
                status_tally[int(tokens[-2]) // 100 - 2] += 1
            try:
                file_size += int(tokens[-1])
            except ValueError:
                pass
        if i % 10 == 0:
            # move print statements outside of the loop
            print("File size: {:d}".format(file_size))
            for code, count in enumerate(status_tally, start=2):
                if count:
                    print(f"{code}00: {count}")
    # move print statements outside of the loop
    print("File size: {:d}".format(file_size))
    for code, count in enumerate(status_tally, start=2):
        if count:
            print(f"{code}00: {count}")

except KeyboardInterrupt:
    # move print statements outside of the loop
    print("File size: {:d}".format(file_size))
    for code, count in enumerate(status_tally, start=2):
        if count:
            print(f"{code}00: {count}")
