#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""

import sys

# Initialize variables
file_size = 0
status_tally = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
count = 0

# Process input line by line
try:
    for line in sys.stdin:
        tokens = line.split()

        # Only process valid input lines
        if len(tokens) >= 7:
            # Update file size
            file_size += int(tokens[-1])

            # Update status code count
            status_code = tokens[-2]
            if status_code in status_tally:
                status_tally[status_code] += 1

        # Print metrics every 10 lines
        count += 1
        if count % 10 == 0:
            print("File size: {:d}".format(file_size))
            for code in sorted(status_tally.keys()):
                if status_tally[code] > 0:
                    print("{}: {}".format(code, status_tally[code]))

# Handle keyboard interrupt gracefully
except KeyboardInterrupt:
    print("File size: {:d}".format(file_size))
    for code in sorted(status_tally.keys()):
        if status_tally[code] > 0:
            print("{}: {}".format(code, status_tally[code]))
