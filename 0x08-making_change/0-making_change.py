#!/usr/bin/python3
"""Making Change."""


def makeChange(coins, total):
    """Calculate the fewest number of coins
       needed to meet the total.
    """
    def helper(remaining):
        if remaining == 0:
            return 0
        if remaining < 0:
            return float('inf')

        if dp[remaining] != -1:
            return dp[remaining]

        min_coins = float('inf')
        for coin in coins:
            min_coins = min(min_coins, helper(remaining - coin) + 1)

        dp[remaining] = min_coins
        return min_coins

    if total <= 0:
        return 0

    dp = [-1] * (total + 1)
    return helper(total) if helper(total) != float('inf') else -1
