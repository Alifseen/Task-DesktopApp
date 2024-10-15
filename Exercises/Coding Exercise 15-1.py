"""Your task is to create a program that generates a random whole number."""

import random

lower = int(input("Lower Bound: "))
upper = int(input("Upper Bound: "))

print(random.randrange(lower,upper))