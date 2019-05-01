#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = (-1) * ((number * -1) % 10)
else:
    last = number % 10
if last > 5:
    s = " and is greater than 5"
elif last == 0:
    s = " and is 0"
elif last < 6 and last != 0:
    s = " and is less than 6 and not 0"
else:
    s = ""
print("Last digit of {:d} is {:d}{}".format(number, last, s))
