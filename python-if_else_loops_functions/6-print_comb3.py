#!/usr/bin/python3

first_print = 0

for i in range(0, 10):
    for j in range(1, 10):
        if j > i:
            print("{}{}{}".format(", " if first_print else "", i, j), end="")
            first_print = 1

print()
