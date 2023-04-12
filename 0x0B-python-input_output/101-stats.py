#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""

import sys

# Initialize variables for metrics
total_file_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}
line_count = 0

try:
    # Read from standard input line by line
    for line in sys.stdin:
        # Split the line into its components
        ip_address, _, date, request, status_code_str, file_size_str = line.split()

        # Convert the status code and file size to integers
        status_code = int(status_code_str)
        file_size = int(file_size_str)

        # Add the file size to the total
        total_file_size += file_size

        # Increment the count for the status code
        if status_code in status_codes:
            status_codes[status_code] += 1

        # Increment the line count
        line_count += 1

        # Every 10 lines, print the metrics so far
        if line_count % 10 == 0:
            print(f"Total file size: {total_file_size}")
            for code in sorted(status_codes.keys()):
                count = status_codes[code]
                if count > 0:
                    print(f"{code}: {count}")

except KeyboardInterrupt:
    # If there's a keyboard interruption, print the metrics and exit
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        count = status_codes[code]
        if count > 0:
            print(f"{code}: {count}")
    sys.exit(0)

