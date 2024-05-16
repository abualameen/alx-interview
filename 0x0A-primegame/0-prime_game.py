#!/usr/bin/python3
""" """
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
    mariaWins, benWins = 0, 0
    player_turn = 'Maria'
    original_set = set(nums)
    for i in range(x+1):
      
        while original_set:
            if player_turn == 'Maria':
                prime_numbs = sieve_of_eratosthenes(max(original_set))
                player_input = int(input(f"{player_turn}'s turn. Enter a number amongs {prime_numbs} : "))

                original_set.remove(player_input)
                original_set -= {i for i in range(player_input*2, max(original_set)+1, player_input)}
                mariaWins += 1
                player_turn = 'Ben'
            else:
                prime_numbs = sieve_of_eratosthenes(max(original_set))
                player_input = int(input(f"{player_turn}'s turn. Enter a number amongs {prime_numbs} : "))
                original_set.remove(player_input)
                original_set -= {i for i in range(player_input*2, max(original_set)+1, player_input)}
                benWins += 1
                player_turn = 'Maria'

    if mariaWins > benWins:
        return 'maria'
    elif benWins > mariaWins:
        return 'Ben'
    else:
        return None


                

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))                  
