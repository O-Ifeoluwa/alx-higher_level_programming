#!/usr/bin/python3
"""prints numbers from 0-99"""

for number in range(0, 100):
    if number == 99:
        print("{}."format(number))
    else:
        print("{0:0=2d}, ".format(number), end="")
