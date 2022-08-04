#!/usr/bin/python3

def remove_char_at(str, n):
    fp = str[:n]
    if n < 0:
        lp = str[n-0:]
    else:
        lp = str[n+1:]
    tp = fp + lp
    return tp
