#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        var = "s."
    elif len(sys.argv) == 2:
        var = ":"
    else:
        var = "s:"
    print("{} argument{}".format(sys.argv[i], var))
    for i in range(1, len(sys.argv)):
        print("{} argument{}".format(sys.argv[i], var))
