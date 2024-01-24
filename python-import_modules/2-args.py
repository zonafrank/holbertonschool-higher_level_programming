#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv
    print(args)
    num_args = len(args) - 1
    pluralize = "s" if num_args != 0 else ""
    period = ":" if num_args > 0 else "."
    print("{} argument{}{}".format(num_args, pluralize , period))
    for i in range(1, len(args)):
        print("{}: {}".format(i, args[i]))
