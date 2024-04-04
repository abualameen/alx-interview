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
    # if not data:
    # return False
    bytes_to_follow = 0
    for byte in data:
        # Check if the byte is a continuation byte
        if bytes_to_follow > 0:
            # If the byte doesn't start with '10',
            # it's not a valid continuation byte
            if byte >> 6 != 0b10:
                return False
            bytes_to_follow -= 1
            if bytes_to_follow < 0 or bytes_to_follow > len(data) - 1:
                return False
        else:
            # Determine the number of bytes to follow
            # based on the leading bits
            if byte >> 7 == 0:
                continue  # Single byte character
            elif byte >> 5 == 0b110:
                bytes_to_follow = 1
            elif byte >> 4 == 0b1110:
                bytes_to_follow = 2
            elif byte >> 3 == 0b11110:
                bytes_to_follow = 3
            else:
                return False  # Invalid leading bits
        # Check for incomplete sequences
        # if bytes_to_follow < 0:
        # return False
    # Check for incomplete sequences
    return bytes_to_follow == 0
