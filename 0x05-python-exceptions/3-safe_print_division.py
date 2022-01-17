#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        data = a / b
    except (ZeroDivisionError, FloatingPointError):
        data = None
    finally:
        print("Inside result: {}".format(data))
    return data
