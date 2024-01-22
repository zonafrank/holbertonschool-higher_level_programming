#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
below_six = ""

if (last_digit > 5):
    below_six = " and is greater than 5"
elif (last_digit == 0):
    below_six = " and is 0"
else:
    below_six = " and is less than 6 and not 0"

print(f"Last digit of {number} is {abs(number) % 10}{below_six}")
