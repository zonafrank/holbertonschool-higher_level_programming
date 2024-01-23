#!/usr/bin/python3

for num in range(100):
    print("{}{:02}".format(", " if num else "", num), end="")
print()
