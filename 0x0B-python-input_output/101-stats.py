#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""

import sys

# initialize variables to store metrics
total_file_size = 0
status_code_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
}

try:
    # loop through stdin line by line
    for i, line in enumerate(sys.stdin):
        # parse the line into its components
        parts = line.split()
        ip_address = parts[0]
        date = parts[2][1:]
        status_code = parts[5]
        file_size = int(parts[6])

        # update metrics
        total_file_size += file_size
        status_code_counts[status_code] += 1

        # print metrics every 10 lines
        if (i+1) % 10 == 0:
            print(f'Total file size: {total_file_size}')

            for code, count in sorted(status_code_counts.items()):
                if count > 0:
                    print(f'{code}: {count}')

            print()

except KeyboardInterrupt:
    # print final metrics on keyboard interrupt
    print(f'Total file size: {total_file_size}')

    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f'{code}: {count}')

