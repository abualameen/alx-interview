#!/usr/bin/python3
"""
Prime Game Module
"""


def sieve_of_eratosthenes(max_num):
    """ Return a list of prime numbers up to max_num. """
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for start in range(2, int(max_num ** 0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, max_num + 1, start):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]


def play_round(primes, n):
    """ Simulate a single round of the game with set size n. """
    current_set = set(range(1, n + 1))
    turn = 0  # Maria's turn is 0, Ben's turn is 1
    while True:
        available_prime = next((p for p in primes if p in current_set), None)
        if available_prime is None:
            break
        # Remove the prime and its multiples from the current set
        current_set -= set(range(available_prime, n + 1, available_prime))
        turn = 1 - turn
    return 'Ben' if turn == 1 else 'Maria'


def isWinner(x, nums):
    """ Determine the overall winner after x rounds. """
    if not nums or x < 1:
        return None
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = play_round(primes, n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
