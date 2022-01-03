#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or len(my_list) - 1 < idx:
        return my_list
    for i in range(len(my_list)):
        if i == idx:
            del my_list[i]
    return my_list
