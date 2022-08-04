#!/usr/bin/python3

for number in range(10):
    for numb in range(number + 1, 10):
        print(
            "{}{}".format(number, num),
            end=", " if int(str(number) + str(num)) < 89 else "\n"
            )
