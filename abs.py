"""Absolute value module."""

def abs(number: float) -> float:
    """Absolute function.

    Args:
        number (float): Real number.

    Returns:
        float: Absolute value of number.
    """
    if number < 0:
        number = -1 * number

    return number


if __name__ == "__main__":
    print(abs(0))
    print(abs(1))
    print(abs(30))
    print(abs(-1))
    print(abs(-30))
