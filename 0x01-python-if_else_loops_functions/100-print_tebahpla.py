#!/usr/bin/python3
def print_alphabet():
    for i in range(90, 64, -1):
        print("{}{}".format(chr(i + 32), chr(i)), end="")
