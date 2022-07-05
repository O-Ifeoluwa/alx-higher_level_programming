#!/usr/bin/python3
for letters in list(map(chr, range(97, 123))):
    if letters != 'e' and letters != 'q':
        print("{}".format(letters), end='')
