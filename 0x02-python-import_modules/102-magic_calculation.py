#!/usr/bin/python3

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for h in range(4, 6):
            c = add(c, h)
        return (c)

    else:
        return(sub(a, b))
