#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        ldig = ((-1 * number) % 10)
    else:
        ldig = number % 10
    print("{}".format(ldig), end="")
    return (ldig)
