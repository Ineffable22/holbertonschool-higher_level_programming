#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = dict(a_dictionary)
    for i in set(new):
        new[i] *= 2
    return new
