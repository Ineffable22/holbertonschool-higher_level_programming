#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{} Arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print("{} Argument:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{} Arguments:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
