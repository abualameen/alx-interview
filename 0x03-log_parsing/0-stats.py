#!/usr/bin/python3


"""
Log Parsing Script

This script reads log entries from standard input (stdin) line by line,
parses them based on a specific format, and computes metrics.

"""


import sys


def print_metrics(total_size, status_codes):
    """
    Prints the computed metrics.
    """
    print("File size: {}".format(total_size))
    sorted_status_codes = sorted(status_codes.items())
    for code, count in sorted_status_codes:
        print("{}: {}".format(code, count))


def parse_line(line):
    """
    Parses a log line and returns the file size and status code.
    """
    parts = line.strip().split()
    if len(parts) < 9:
        return None, None
    status_code = parts[-2]
    try:
        size = int(parts[-1])
    except ValueError:
        return None, None
    return status_code, size


def main():
    """
    Main function to read logs from stdin and compute metrics.
    """
    total_size = 0
    status_codes = {str(code): 0 for code in [
        200, 301, 400, 401, 403, 404, 405, 500]}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            status_code, size = parse_line(line)
            if status_code is not None and size is not None:
                total_size += size
                if status_code in status_codes:
                    status_codes[status_code] += 1

            if count == 10:
                print_metrics(total_size, status_codes)
                count = 0

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
