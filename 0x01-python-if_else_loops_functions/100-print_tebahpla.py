#!/usr/bin/python3
value = 122
flag = 0
while value >= 97:
    if value % 2:
        value -= 32
        flag = 1
    print("{}".format(chr(value)), end='')
    if flag == 1:
        value += 32
        flag = 0
    value -= 1
