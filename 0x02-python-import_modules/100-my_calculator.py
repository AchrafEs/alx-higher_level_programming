#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv, exit

if __name__ == "__main__":
    if len(argv) != 4 or len(argv[2]) != 1:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    result = 0

    if operator == '+':
        result = add(a, b)
        print("{} + {} = {}".format(a, b, result))
    elif operator == '-':
        result = sub(a, b)
        print("{} - {} = {}".format(a, b, result))
    elif operator == '*':
        result = mul(a, b)
        print("{} * {} = {}".format(a, b, result))
    elif operator == '/':
        result = div(a, b)
        print("{} / {} = {}".format(a, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
