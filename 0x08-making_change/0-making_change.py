#!/usr/bin/python3
"""Making Change."""


def makeChange(coins, total):
    """Calculate the fewest number of coins
       needed to meet the total.
    """
    if total <= 0:
        return 0
    m = len(coins)
    table = [0] + [float('inf')] * total
    for j in range(1, total + 1):
        for k in range(m):
            if coins[k] <= j:
                sub_res = table[j -coins[k]]
                if sub_res != float('inf') and sub_res + 1 < table[j]:
                    table[j] = sub_res + 1
    if table[total] != float('inf'):
        return table[total]
    else:
        return -1
    return table[total] 
