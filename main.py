#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "???"


def add(x, y):
    """Add two integers. Handles negative values."""
    return (x) + (y)


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    mult = 0
    if x < 0 and y > 0:
        for i in range(y):
            mult = add(mult, x)
    elif x > 0 and y < 0:
        for i in range(x):
            mult = add(mult, y)
    elif x < 0 and y < 0:
        for i in range(-y):
            mult = add(mult, -x)
    else:
        for i in range(x):
            mult = add(mult, y)

    return mult


def power(x, n):
    """Raise x to power n, where n >= 0"""
    power = 1
    for i in range(n):
        power = multiply(power, x)
    return power


def factorial(x):
    """Compute factorial of x, where x > 0"""
    factorial = 1
    if x == 0:
        return 1
    else:
        for i in range(1, x + 1):
            factorial = multiply(factorial, i)
    return factorial


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    fibonacci = 1
    for i in range(n + 1):
        fibonacci = add(fibonacci, i)
    return fibonacci


if __name__ == '__main__':
    # your code to call functions above
    pass
