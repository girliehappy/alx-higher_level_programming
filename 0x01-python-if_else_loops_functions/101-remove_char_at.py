#!/usr/bin/python3
# 101-remove_char_at.py


def remove_char_at(str, n):
    """Creates a copy of the string, removing the character at position n."""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
