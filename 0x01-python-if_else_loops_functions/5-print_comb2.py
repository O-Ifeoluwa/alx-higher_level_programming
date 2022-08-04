#!/usr/bin/python3
"""prints numbers from 0-99"""

for numbers in range(0, 100):
    if numbers == 99:
        print(99)
    else:
        print("{0:0=2d}, ".format(numbers), end="")
