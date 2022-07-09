#!/bin/usr/python3

if __name__ == "__main__":
    import sys
    total = len(sys.argv)
    sum = 0

    for i in range(1, total):
        sum += int(sys.argv[i])

    print('{}'.format(sys.argv[i], end=' ')
