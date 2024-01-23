#!/usr/bin/python3

def fizzbuzz():
    for num in range(1, 101):
        div_by_3 = num % 3 == 0
        div_by_5 = num % 5 == 0
        out = num
        if div_by_3 and div_by_5:
            out = "FizzBuzz"
        elif div_by_3:
            out = "Fizz"
        elif div_by_5:
            out = "Buzz"

        print("{}".format(out), end="")

        if num < 100:
            print(" ", end="")

fizzbuzz()