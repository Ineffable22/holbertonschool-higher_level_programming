#!/usr/bin/python3
def remove_char_at(str, n):
    count = 0
    new = ''
    for c in str:
        if count != n:
            new += str[count]
        count += 1
    return new
