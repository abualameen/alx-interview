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
        
        # Count the number of leading '1's in the binary representation
        if byte >> 7 == 0:
            # Single-byte character: 0xxxxxxx
            index += 1
        elif byte >> 5 == 0b110:
            # Two-byte character: 110xxxxx 10xxxxxx
            if index + 1 >= len(data) or data[index + 1] >> 6 != 0b10:
                return False
            index += 2
        elif byte >> 4 == 0b1110:
            # Three-byte character: 1110xxxx 10xxxxxx 10xxxxxx
            if index + 2 >= len(data) or data[index + 1] >> 6 != 0b10 or data[index + 2] >> 6 != 0b10:
                return False
            index += 3
        elif byte >> 3 == 0b11110:
            # Four-byte character: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
            if index + 3 >= len(data) or data[index + 1] >> 6 != 0b10 or data[index + 2] >> 6 != 0b10 or data[index + 3] >> 6 != 0b10:
                return False
            index += 4
        else:
            # Invalid leading bits
            return False
    
    # All bytes conform to UTF-8 encoding rules
    return True
