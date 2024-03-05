#!/usr/bin/python3
"""
this module is a implementation of pascal triangle

"""


def generate_pascals_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.
    
    Parameters:
    - n: int, the number of rows to generate in Pascal's Triangle.
    
    Returns:
    - list of lists: Pascal's Triangle up to the nth row.
    """
    if n <= 0:
        return []  # Return an empty list for invalid input
    
    triangle = []  # Initialize an empty list to store Pascal's Triangle
    
    for i in range(n):
        row = [1]  # The first element of each row is always 1
        if i > 0:
            for j in range(1, i):
                # Calculate the value of the current element as the sum of the two elements directly above it
                value = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(value)
            row.append(1)  # The last element of each row is always 1
        triangle.append(row)  # Add the current row to the triangle list
        
    return triangle
