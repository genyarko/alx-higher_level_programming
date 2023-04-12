#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""

import sys
from collections import defaultdict

# initialize the required variables
total_size = 0
status_counts = defaultdict(int)
line_count = 0

# process the input lines
for line in sys.stdin:
    try:
        # parse the line using the provided format
        ip, _, date, request, status, size = line.split(' ')
        if request != 'GET /projects/260 HTTP/1.1':
            continue
        status = int(status)
        size = int(size)
        
        # update the variables
        total_size += size
        status_counts[status] += 1
        line_count += 1
        
        # print the statistics after every 10 lines
        if line_count % 10 == 0:
            print('Total file size:', total_size)
            for status_code in sorted(status_counts.keys()):
                print(status_code, ':', status_counts[status_code])
                
    except KeyboardInterrupt:
        # handle keyboard interruption (CTRL + C)
        print('Total file size:', total_size)
        for status_code in sorted(status_counts.keys()):
            print(status_code, ':', status_counts[status_code])
        break



