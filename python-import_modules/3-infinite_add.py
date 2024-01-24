#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv
    arg_count = len(args)
    sum = 0
    for i in range(1, arg_count):
        sum += int(args[i])
    print("{}".format(sum))
