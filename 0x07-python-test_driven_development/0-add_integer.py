#!/usr/bin/python3


def add_integer(a, b=98):

    

    if not isinstance(b, int) and not isinstance(b, float):
        raise ValueError("b must be an integer")
    elif not isinstance(a, int) and not isinstance(a, float):
        raise ValueError("a must be an integer")

    return int(a) + int(b)
