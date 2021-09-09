#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    j = len(argv) - 1

    if j == 0:
        print("{:d} argument.".format(j))
    elif j == 1:
        print("{:d} argument:".format(j))
    else:
        print("{:d} arguments:".format(j))
    for i in range(1, j + 1):
        print("{:d}: {:s}".format(i, argv[i]))
