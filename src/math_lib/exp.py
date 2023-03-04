from math_lib.mult import mult


def exp(base: float, exponent: float) -> float:
    """Exponential function.

    Returns the result of raising the given base to the power of the given exponent.

    Args:
        base (float): The base number.
        exponent (float): The exponent to raise the base to.

    Returns:
        float: The result of raising the base to the power of the exponent.
    """

    results = 1

    for _ in range(int(exponent)):
        results = mult(results, base)

    if exponent == 0:
        return results

    return results
