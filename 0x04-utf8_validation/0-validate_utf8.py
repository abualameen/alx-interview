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
    if not data:  # Edge case: Empty data
        return False

    bytes_to_follow = 0
    for byte in data:
        if bytes_to_follow > 0:
            if byte >> 6 != 0b10:  # Edge case: Invalid continuation byte
                return False
            bytes_to_follow -= 1
        else:
            if byte >> 7 == 0:
                continue  # Single byte character
            elif byte >> 5 == 0b110:
                bytes_to_follow = 1
            elif byte >> 4 == 0b1110:
                bytes_to_follow = 2
            elif byte >> 3 == 0b11110:
                bytes_to_follow = 3
            else:
                return False  # Edge case: Invalid leading bits
        
        if bytes_to_follow < 0:  # Edge case: Incomplete sequence
            return False

    return bytes_to_follow == 0
