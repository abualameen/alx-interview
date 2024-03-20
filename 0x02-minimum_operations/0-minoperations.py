#!/usr/bin/python3
"""
Defines a function minOperations(n) that calculates the fewest number of
operations needed to result in exactly n H characters in a text file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to achieve exactly n H
    characters in a text file using only Copy All and Paste operations.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The fewest number of operations needed to achieve exactly n H
             characters. If it's impossible to achieve n
             H characters, returns 0.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            n //= divisor
            operations += divisor
        divisor += 1

    return operations
