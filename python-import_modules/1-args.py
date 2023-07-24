#!/usr/bin/python3

import sys
if __name__ == "__main__":
    n_args = len(sys.argv) - 1

    if n_args == 0:
        print(f"{n_args} arguments.")
    elif n_args == 1:
        print(f"{n_args} argument:")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")
    else:
        print(f"{n_args} arguments:")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")