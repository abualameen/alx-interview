#!/usr/bin/python3
"""
Prime Game Module
"""

def isWinner(x, nums):
    """
    Determine the winner of the prime game after x rounds.
    """
    if not nums or x < 1:
        return None

    # Calculate the maximum number in nums to optimize the prime sieve
    max_num = max(nums)
    
    # Use Sieve of Eratosthenes to find all primes up to max_num
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    for start in range(2, int(max_num ** 0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, max_num + 1, start):
                sieve[multiple] = False

    # List of primes up to max_num
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    # Function to determine the winner for a given n
    def find_winner(n):
        current_set = list(range(1, n + 1))
        turn = 0  # Maria's turn is 0, Ben's turn is 1
        
        while True:
            # Find the next available prime
            available_prime = next((p for p in primes if p in current_set), None)
            if available_prime is None:
                break

            # Remove the prime and its multiples from the current set
            current_set = [num for num in current_set if num % available_prime != 0]

            # Switch turns
            turn = 1 - turn
        
        # If turn is 1, it means Maria couldn't play and lost, otherwise she won
        return 'Ben' if turn == 1 else 'Maria'

    # Count wins for Maria and Ben
    maria_wins = sum(1 for n in nums if find_winner(n) == 'Maria')
    ben_wins = x - maria_wins

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))