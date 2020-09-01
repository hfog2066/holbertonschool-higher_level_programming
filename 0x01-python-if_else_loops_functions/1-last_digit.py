#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % (-10 if number < 0 else 10)

print("Last digit of {:d} is {:d} ".format(number, digit), end='')

if digit < 6 and digit:
    print("and is less than 6 and not 0")
elif digit > 5:
    print("and is greater than 5")
else:
    print("and is 0")
