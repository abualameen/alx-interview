#!/usr/bin/python3
"""
this is
"""


def sieve_of_eratosthenes(n):
    """ """
    primes = [True] * (n+1)
    p = 2
    while p*p <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n+1) if primes[p]]
    return prime_numbers


def isWinner(x, nums):
    """ """
    maria_wins, ben_wins = 0, 0
    player_turn = 'Maria'
    for i in range(x):
        original_set = set(range(1, nums[i]+1))
        while original_set:
            if player_turn == 'Maria':
                prime_nums = sieve_of_eratosthenes(max(original_set))
                player_input = min(prime_nums)
                # Remove the chosen prime number and its multiples from the set
                original_set -= {player_input}
                original_set -= {i for i in range(player_input*2,
                                                  max(original_set)+1, player_input)}           
                maria_wins += 1
                player_turn = 'Ben'   
            else:
                prime_nums = sieve_of_eratosthenes(max(original_set))
                player_input = min(prime_nums)  # Ben chooses the lowest prime number     
                # Remove the chosen prime number and its multiples from the set
                original_set -= {player_input}
                original_set -= {i for i in range(player_input*2,
                                      max(original_set)+1, player_input)}
                ben_wins += 1
                player_turn = 'Maria'
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
