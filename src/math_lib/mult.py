"""Multiplication module."""

from math_lib.add import add
from math_lib.sub import sub


def mult(multiplier: float, multiplicand: float) -> float:
    """Multiplication function.

    Args:
        multiplier (float): Multiplier.
        multiplicand (float): Multiplicand.

    Returns:
        float: Product of multiplier and multiplicand.
    """
    value = range(multiplicand)
    func = add
    if multiplicand < 0:
        value = range(0, multiplicand, -1)
        func = sub

    sum = 0

    for _ in value:
        sum = func(sum, multiplier)

    return sum
