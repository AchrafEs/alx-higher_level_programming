#!/usr/bin/python3
def uppercase(str):
    output = ""
    for char in str:
        up = chr(ord(char) - ord('a') + ord('A'))if 'a' <= char <= 'z'else char
        output += up
    print("{}".format(output))
