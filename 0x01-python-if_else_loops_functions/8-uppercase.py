#!/usr/bin/python3
def uppercase(str):
    output = ""
    for char in str:
        uppercase_char = chr(ord(char) - ord('a') + ord('A')) if 'a' <= char <= 'z' else char
        output += uppercase_char
    print(output)
