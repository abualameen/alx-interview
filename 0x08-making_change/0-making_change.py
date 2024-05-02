#!/usr/bin/python3
"""Making Change."""


def makeChange(coins, total):
    """Calculate the fewest number of coins needed to meet the total."""
    if total <= 0:
        return 0

    # Initialize a memoization table to store previously computed results
    memo = {}

    def dp(amount):
        if amount in memo:
            return memo[amount]

        # Base case: If the total amount is 0, return 0 coins
        if amount == 0:
            return 0

        # Initialize the fewest number of coins needed to infinity
        min_coins = float('inf')

        # Iterate through each coin value
        for coin in coins:
            # Check if the coin value is less than or equal to the total amount
            if coin <= amount:
                # Recursively calculate the fewest number of
                # coins for the remaining amount
                num_coins = dp(amount - coin) + 1

                # Update the minimum number of coins if necessary
                min_coins = min(min_coins, num_coins)

        # Memoize the result for future use
        memo[amount] = min_coins
        return min_coins

    # Call the dynamic programming function
    result = dp(total)

    # If the result is infinity, return -1 (total cannot be met)
    return result if result != float('inf') else -1
