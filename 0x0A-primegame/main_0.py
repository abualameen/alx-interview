#!/usr/bin/python3
# import random

# Set the seed for reproducibility
# random.seed(42)

# Generate 100 random integers between 1 and 10,000
# random_integers = [random.randint(1, 10000) for _ in range(10000)]

# print(random_integers)

isWinner = __import__('0-prime_game').isWinner



# print("Winner: {}".format(isWinner(10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2])))
print("Winner: {}".format(isWinner(6, [1, 1, 0, 0, 1, 8])))
# print("Winner: {}".format(isWinner(6, [1, 1, 0, 0, 1, 8])))

