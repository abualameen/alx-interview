#!/usr/bin/python3
"""Making Change."""


def makeChange(coins, total):
    """Calculate the fewest number of coins needed to meet the total."""
    if total <= 0:
        return 0

    # Sort coins array in descending order
    coins.sort(reverse=True)

    # Initialize count to store the number of coins used
    count = 0

    # Iterate through each coin value
    for coin in coins:
        # Determine the number of coins of current denomination that can be used
        num_coins = total // coin
        # Update the total amount remaining after using the current coin denomination
        total -= num_coins * coin
        # Update the count with the number of coins used
        count += num_coins
        # If the total amount remaining becomes 0, break the loop
        if total == 0:
            break

    # If the total amount remaining is not 0 after using all coins, return -1
    if total != 0:
        return -1

    return count
