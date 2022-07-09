#!/bin/usr/python3

if __name__ == "__main__":
    import sys
    total = len(sys.argv)
    add = 0

    if total == 1:
        print(0)
        exit()
    for i in range(1, total):
        add += int(sys.argv[i])

    print('{}'.format(add, end=' '))
