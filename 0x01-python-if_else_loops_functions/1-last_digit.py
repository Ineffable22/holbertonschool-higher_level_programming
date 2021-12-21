#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    digit = number % 10
else:
    digit = -number % 10
    digit = -digit

if digit == 0:
    print('Last digit of {:d} is 0 and is 0'.format(number))
elif digit < 6:
    print('Last digit of {:d} is {:d} and is less than 6 and not \
0'.format(number, digit))
else:
    print('Last digit of {:d} is {:d} and is greater than 5\
'.format(number, digit))
