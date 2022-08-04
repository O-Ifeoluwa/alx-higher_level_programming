#!/usr/bin/python3

suzz = ""


def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            suzz = "FizzBuzz"
        elif num % 3 == 0:
            suzz = "Fizz"
        elif num % 5 == 0:
            suzz = "Buzz"
        else:
            suzz = str(num)
        print(suzz, end=" ")
