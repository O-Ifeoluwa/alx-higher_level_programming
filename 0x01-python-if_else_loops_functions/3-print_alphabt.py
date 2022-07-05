#!/usr/bin/python3
for letters in list(map(chr, range(97, 123))):
    if letters != 101 and letters != 113:
        print("{}".format(letters), end='')
