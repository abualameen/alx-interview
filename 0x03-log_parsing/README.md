# Log Parsing

This repository contains a Python script (`0-stats.py`) that parses log data read from `stdin`, computes metrics based on the parsed data, and handles keyboard interruptions (CTRL + C) gracefully. Here's a detailed guide on the concepts used in the script:

## File I/O in Python
File input/output (I/O) in Python involves reading from and writing to files. In this script, we utilize `sys.stdin` to read input from the standard input stream (`stdin`) line by line. This allows us to process log data as it is streamed in real-time.

**Resources:**
- [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)

## Signal Handling in Python
Signal handling in Python involves capturing and handling signals, such as keyboard interruptions (e.g., CTRL + C). We use signal handling to gracefully exit the script when a keyboard interruption occurs, ensuring that final statistics are printed before exiting.

**Resources:**
- [Python Signal Handling](https://docs.python.org/3/library/signal.html)

## Data Processing
Data processing involves extracting and manipulating data to derive insights or compute summaries. In this script, we parse log entries to extract specific data points such as IP addresses, dates, status codes, and file sizes. We then aggregate this data to compute statistics such as total file size and counts of different status codes.

## Regular Expressions
Regular expressions (regex) are patterns used to match and manipulate strings. We use regex to validate the format of each log line, ensuring that it matches the specified format before processing. This helps filter out irrelevant or malformed data.

**Resources:**
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)

## Dictionaries in Python
Dictionaries are data structures that store key-value pairs. In this script, we use dictionaries to count occurrences of different status codes and accumulate file sizes corresponding to each log entry. This allows us to efficiently track and update metrics as we process each log line.

**Resources:**
- [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

## Exception Handling
Exception handling in Python involves catching and handling errors that may occur during program execution. In this script, we handle possible exceptions that may arise during file reading, data processing, or signal handling. This ensures that the script can gracefully recover from errors and continue execution or exit cleanly.

**Resources:**
- [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)
