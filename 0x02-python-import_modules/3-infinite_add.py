#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the result of the addition of all arguments, followed by a new line."""
    import sys

    total = 0
    for h in range(len(sys.argv) - 1):
        total += int(sys.argv[h + 1])
    print("{}".format(total))
