#!/usr/bin/python3
def uppercase(str):
    for case in str:
        case = ord(case)
        if case >= 97 and case <= 122:
            case -= 32
        case = chr(case)
        print("{}".format(case), end='')
    print("")
