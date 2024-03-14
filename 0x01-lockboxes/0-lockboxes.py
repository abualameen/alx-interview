#!/usr/bin/python3
"""
this module implements the lockbok problem

"""


def canUnlockAll(boxes):
    """
    this function is the canunlockall function

    """
    num_boxes = len(boxes)  # Total number of boxes
    visited = set()  # Set to keep track of visited boxes
    keys = set([0])
    stack = [0]

    while stack:
        current_box = stack.pop()
        visited.add(current_box)
        # Collect keys from the current box
        for key in boxes[current_box]:
            if key not in keys:
                keys.add(key)
                stack.append(key)
        # Check if all boxes can be opened
        if len(visited) == num_boxes:
            return True
    return False  # If not all boxes can be visited
