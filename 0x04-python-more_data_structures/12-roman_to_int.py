#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    dic_x = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    total = 0
    for i in range(len(roman_string)):
        if i > 0 and dic_x[roman_string[i]] > dic_x[roman_string[i - 1]]:
            total += dic_x[roman_string[i]] - 2 * dic_x[roman_string[i - 1]]
        else:
            total += dic_x[roman_string[i]]
    return total
