#!/usr/bin/python3
""" """
def sieve_of_eratosthenes(n):
    """
    Find all prime numbers up to a given limit, n, using the Sieve of Eratosthenes algorithm.
    
    Args:
        n (int): The upper limit for finding prime numbers.
    
    Returns:
        list: A list of prime numbers up to n.
    """
    primes = [True] * (n+1)
    p = 2
    while p*p <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n+1) if primes[p]]
    return prime_numbers

def is_prime(num):
    """
    Check if a given number is prime.
    
    Args:
        num (int): The number to be checked for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def isWinner(x, nums):
    """
    Simulate a game played by Maria and Ben, where they choose prime numbers and remove their multiples.
    
    Args:
        x (int): The number of rounds played.
        nums (list): An array of n values for each round.
    
    Returns:
        str: The name of the player who won the most rounds, or 'None' if undetermined.
    """
    maria_wins, ben_wins = 0, 0
    player_turn = 'Maria'
    
    for _ in range(x):
        original_set = set(nums)
        
        while original_set:
            if player_turn == 'Maria':
                prime_numbs = [num for num in original_set if is_prime(num)]
                while True:
                    try:
                        player_input = int(input(f"{player_turn}'s turn. Choose a prime number: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid prime number:")
                # Remove the chosen prime number and its multiples from the set
                original_set -= {player_input}
                original_set -= {i for i in range(player_input*2, max(original_set)+1, player_input)}
                
                maria_wins += 1
                player_turn = 'Ben'
                
            else:
                prime_numbs = [num for num in original_set if is_prime(num)]
                while True:
                    try:
                        player_input = int(input(f"{player_turn}'s turn. Choose a prime number: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid prime number:")
                # Remove the chosen prime number and its multiples from the set
                original_set -= {player_input}
                original_set -= {i for i in range(player_input*2, max(original_set)+1, player_input)}
                
                ben_wins += 1
                player_turn = 'Maria'

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None

                

                
