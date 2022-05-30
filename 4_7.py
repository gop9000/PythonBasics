from math import factorial
from itertools import count
from random import randint


def fnc():
    for i in count(1):
        yield factorial(i)


num = randint(1, 20)

for f in fnc():
    if num == 20:
        break
    else:
        num += 1
        print(f"The factorial of {num} is {f}!")
