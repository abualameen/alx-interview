#!/usr/bin/python3

import sys
import re

# Regular expression pattern for parsing log entries

LOG_PATTERN = (
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET '
    r'\/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
)


# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {
    200: 0, 301: 0, 400: 0, 401: 0,
    403: 0, 404: 0, 405: 0, 500: 0
}


# Function to print statistics
def print_statistics():
    print(f'Total file size: {total_file_size}')
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print(f'{code}: {status_code_counts[code]}')


# Function to process log lines
def process_log_line(line):
    global total_file_size
    global status_code_counts

    match = re.match(LOG_PATTERN, line)
    if match:
        # Extract data from log entry
        ip_address = match.group(1)
        date = match.group(2)
        status_code = int(match.group(3))
        file_size = int(match.group(4))

        # Update metrics
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        # Check if 10 lines have been processed
        if sum(status_code_counts.values()) % 10 == 0:
            print_statistics()


try:
    # Process input lines from stdin
    for line in sys.stdin:
        process_log_line(line.strip())

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_statistics()
