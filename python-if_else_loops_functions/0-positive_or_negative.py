#!/usr/bin/python3
import random
number = random.randint(-10, 10)
sign = ""

if number < 0:
    sign = "negative"
elif number > 0:
    sign = "positive"
else:
    sign = "zero"

print(f"{number} is {sign}")
