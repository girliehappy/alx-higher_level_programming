#!/usr/bin/python3
# 100-print_tebahpla.py

""""Print the ASCII alphabet, in reverse order, alternating upper and lowercase."""
h = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - h)), end="")
    h = 32 if h == 0 else 0
