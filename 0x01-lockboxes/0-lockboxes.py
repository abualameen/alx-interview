#!/usr/bin/python3
"""
This module implements the lockbox problem.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.
    """
    # Check if input is valid
    if not isinstance(boxes, list) or len(boxes) < 1:
        return False
    num_boxes = len(boxes)
    visited = set()
    keys = set([0])
    stack = [0]
    while stack:
        current_box = stack.pop()
        visited.add(current_box)
        # Collect valid keys from the current box
        for key in boxes[current_box]:
            if isinstance(key, int) and 0 <= key < num_boxes \
                    and key not in keys:
                keys.add(key)
                stack.append(key)
        # Check if all boxes can be opened
        if len(visited) == num_boxes:
            return True
    return False  # If not all boxes can be visited
