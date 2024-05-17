#!/usr/bin/python3
""" this is the module for the game """


def sieve_of_eratosthenes(n):
    """
    this sieve of eratosthenes
    """
    primess = [True] * (n+1)
    p = 2
    while p*p <= n:
        if primess[p]:
            for i in range(p*p, n+1, p):
                primess[i] = False
        p += 1
    prime_numbers = set([p for p in range(2, n+1) if primess[p]])
    return prime_numbers


def isWinner(x, nums):
    """
    this function computes the winner
    """
    if not nums or x < 1:
        return None
    maria_wins, ben_wins = 0, 0
    for i in range(x):
        maria_turn = True
        if nums[i] < 1:
            ben_wins += 1
            continue
        consecutive_nums = set(range(1, nums[i]+1))
        if len(consecutive_nums) == 1:
            ben_wins += 1
            continue
        primes = sieve_of_eratosthenes(max(consecutive_nums))
        # if len(primes) == 0 and maria_turn:
        #     maria_wins += 1
        while primes:
            if maria_turn:
                # primes = sieve_of_eratosthenes(max(consecutive_nums))
                maria_prime = min(primes)
                maria_picks = maria_prime
                consecutive_nums -= {maria_picks}
                primes -= {maria_prime}
                consecutive_nums -= {i for i in range(
                    maria_picks*2, max(consecutive_nums)+1, maria_picks)}
                # maria_wins += 1
                if len(primes) == 0 and maria_turn:
                    maria_wins += 1
                    maria_turn = False
                    ben_turn = True
                else:
                    maria_turn = False
                    ben_turn = True
            else:
                # primes = sieve_of_eratosthenes(max(consecutive_nums))
                ben_prime = min(primes)
                ben_picks = ben_prime
                primes -= {ben_prime}
                consecutive_nums -= {ben_picks}
                consecutive_nums -= {i for i in range(
                    ben_picks*2, max(consecutive_nums)+1, ben_picks)}
                if len(primes) == 0 and ben_turn:
                    ben_wins += 1
                    ben_turn = False
                    maria_turn = True
                else:
                    ben_turn = False
                    maria_turn = True
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
