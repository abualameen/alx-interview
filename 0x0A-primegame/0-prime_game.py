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


def find_winner(primes, n):
    """ Determine the winner for a single round with set size n. """
    current_set = list(range(1, n + 1))
    turn = 0  # Maria's turn is 0, Ben's turn is 1
    while True:
        available_prime = next((p for p in primes if p <= n), None)
        if available_prime is None:
            break
        # Remove the prime and its multiples from the current set
        current_set = [num for num in current_set if num %
                       available_prime != 0]
        turn = 1 - turn
    return 'Ben' if turn == 1 else 'Maria'


def isWinner(x, nums):
    """ Determine the overall winner after x rounds. """
    if not nums or x < 1:
        return None
    for n in nums:
        max_num = max(n, n)  # Use the upper limit for each round
        primes = sieve_of_eratosthenes(max_num)
        winner = find_winner(primes, n)
        if winner == 'Maria':
            return 'Maria'
        elif winner == 'Ben':
            return 'Ben'
    return None  # If no winner is determined after all rounds
