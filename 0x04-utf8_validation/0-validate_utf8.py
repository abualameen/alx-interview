#!/usr/bin/python3
"""
Module to validate UTF-8 encoding
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing bytes of data.

    Returns:
        True if data is a valid UTF-8 encoding, else False.
     """
    # Iterate through each byte in the data set
    index = 0
    while index < len(data):
        byte = data[index]
        # Check the UTF-8 encoding pattern of the byte
        # Count the number of leading '1's in the binary representation
        if byte >> 7 == 0:
            # Single-byte character: 0xxxxxxx
            index += 1
            continue
        elif byte >> 5 == 0b110:
            # Two-byte character: 110xxxxx 10xxxxxx
            bytes_to_follow = 1
        elif byte >> 4 == 0b1110:
            # Three-byte character: 1110xxxx 10xxxxxx 10xxxxxx
            bytes_to_follow = 2
        elif byte >> 3 == 0b11110:
            # Four-byte character: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
            bytes_to_follow = 3
        else:
            # Invalid leading bits
            return False
        # Check continuation bytes
        index += 1
        for _ in range(bytes_to_follow):
            # Move to the next byte
            index += 1
            # If there are no more bytes, or if the
            # byte does not start with '10',
            # it's not a valid continuation byte
            if index >= len(data) or (data[index] >> 6) != 0b10:
                return False
    # All bytes conform to UTF-8 encoding rules
    return True
