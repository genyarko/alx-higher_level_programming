#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""
import sys

file_size = 0
status_count = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
line_count = 0

try:
    for line in sys.stdin:
        tokens = line.split()

        if len(tokens) < 5:
            continue

        status_code = tokens[3]
        file_size += int(tokens[4])
        status_count[status_code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print("Total file size: File size: {:d}".format(file_size))
            for code in sorted(status_count.keys()):
                if status_count[code] > 0:
                    print("{:s}: {:d}".format(code, status_count[code]))

    print("Total file size: File size: {:d}".format(file_size))
    for code in sorted(status_count.keys()):
        if status_count[code] > 0:
            print("{:s}: {:d}".format(code, status_count[code]))

except KeyboardInterrupt:
    print("Total file size: File size: {:d}".format(file_size))
    for code in sorted(status_count.keys()):
        if status_count[code] > 0:
            print("{:s}: {:d}".format(code, status_count[code]))
