#!/usr/bin/python3
"""Making Change."""

def makeChange(coins, total):
    """Calculate the fewest number of coins needed to meet the total."""
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

if __name__ == "__main__":
    coins = [1, 2, 25]
    total = 37
    print(makeChange(coins, total))

    coins = [1256, 54, 48, 16, 102]
    total = 1453
    print(makeChange(coins, total))
