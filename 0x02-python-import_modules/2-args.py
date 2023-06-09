#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num = len(argv) - 1
    if num == 0:
        print("0 arguments.")
    else:
        print("{} {}".format(num, "argument" if num == 1 else "arguments"))
        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))
