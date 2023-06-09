#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num_args = len(argv) - 1
    print("{}: arguments".format(num_args), end="")
    if num_args == 0:
        print(".")
    else:
        print(":")
        for i in range(1, len(argv)):
            print(i, end=": ")
            print(argv[i])
