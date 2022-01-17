#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as value:
        print("Exception: {}".format(value), file=sys.stderr)
        return None
