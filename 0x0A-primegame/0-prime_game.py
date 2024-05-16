#!/usr/bin/python3
"""
Prime Game Module
"""

def sieve_of_eratosthenes(max_num):
    """ """
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False

    for start in range(2, int(max_num ** 0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, max_num + 1, start):
                sieve[multiple] = False

    return [num for num, is_prime in enumerate(sieve) if is_prime]

def find_winner(primes, n):
    """ """
    current_set = list(range(1, n + 1))
    turn = 0

    while True:
        available_prime = next((p for p in primes if p in current_set), None)
        if available_prime is None:
            break

        current_set = [num for num in current_set if num % available_prime != 0]
        turn = 1 - turn

    return 'Ben' if turn == 1 else 'Maria'

def isWinner(x, nums):
    """ """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = sum(1 for n in nums if find_winner(primes, n) == 'Maria')
    ben_wins = x - maria_wins

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
