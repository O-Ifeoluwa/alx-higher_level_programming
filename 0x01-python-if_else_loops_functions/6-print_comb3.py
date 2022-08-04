#!/usr/bin/python3

for number in range(10):
    for numb in range(number + 1, 10):
        print(
            "{}{}".format(number, numb),
            end=", " if int(str(number) + str(numb)) < 89 else "\n"
            )
