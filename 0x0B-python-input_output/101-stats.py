#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""
import sys

# Initialize dictionary and variables
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
line_count = 0

try:
    while True:
        # Read input from stdin
        line = sys.stdin.readline().strip()

        # Extract status code and file size
        parts = line.split()
        status_code = parts[3]
        file_size = int(parts[4])

        # Update dictionary and variables
        status_codes[status_code] += 1
        total_size += file_size
        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")

except KeyboardInterrupt:
    # Terminate gracefully on keyboard interrupt
    print("\nFinal statistics:")
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
