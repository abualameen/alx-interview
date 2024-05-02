#!/usr/bin/python3
"""Making Change."""


def makeChange(coins, total):
    """Calculate the fewest number of coins needed to meet the total."""
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins needed for each total amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update dp array for each possible total amount
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means total cannot be reached with the given coins
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]


if __name__ == "__main__":
    coins = [1, 2, 25]
    total = 37
    print(makeChange(coins, total))

    coins = [1256, 54, 48, 16, 102]
    total = 1453
    print(makeChange(coins, total))
