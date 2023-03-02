"""Multiplication module."""

from math_lib.add import add
from math_lib.sub import sub


def mult(a: float, b: float) -> float:
    """Multiplication function.

    Args:
        a (float): Multiplier.
        b (float): Multiplicand.

    Returns:
        float: Product of a and b.
    """
    value = range(b)
    func = add
    if b < 0:
        value = range(0, b, -1)
        func = sub

    sum = 0

    for _ in value:
        sum = func(sum, a)

    return sum
