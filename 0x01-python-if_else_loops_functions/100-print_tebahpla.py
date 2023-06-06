#!/usr/bin/python3
def print_alphabet():
    index = 0
    for i in range(ord('z'), ord('a') - 1, -1):
        print("{}".format(chr(i - i)), end="")
        index = 32 if index == 0 else 0
