# Mathematics Library

Home-made Mathematics library using the Python programming language. It will emulate the [math - Mathematical functions](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwj738W6iLv9AhX6kokEHejhDfcQFnoECAkQAQ&url=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fmath.html&usg=AOvVaw26GwSqIFLX1e1HscI8nzVo) library in Python, although it will be a much less complete version.

The math library will be rudimentary but fully functional, including all elementary arithmetic operations and some more advanced topics (exponents and logarithms).

## Library Functions

### Elementary Operations

1. Addition (`add`, `+`) 
2. Subtraction (`sub`, `-`)
3. Multiplication (`mult`) ** 2
4. Division (`div`)

#### `add`

This is a binary function that takes in two **numbers** (`augend` and `addend`) and returns the sum of two `numbers`.

```python
def add(augend: float, addend: float) -> float:
    """Addition function.

    Args:
        augend (float): The augend of the addition.
        addend (float): The addend of the addition.

    Returns:
        float: The sum of augend and addend.
    """
    return augend + addend
```

#### `sub`

This is a binary function that takes in two **numbers** (`minuend` and `subtrahend`) and returns the difference of two `numbers`.

```python
def sub(minuend: float, subtrahend: float) -> float:
    """Subtraction function.

    Args:
        minuend (float): The number being subtracted from.
        subtrahend (float): The number being subtracted from another.

    Returns:
        float: The difference of minuend and subtrahend.
    """
    return minuend - subtrahend
```

### Advanced Functions

1. Square Root (`sqrt`)
2. Exponentiation (`exp`) ** 4
3. Logarithm (`log`)

### Special Function

1. Absolute Value (`abs`) ** 1
2. Division and Modulus (`divmod`) ** 3

#### `abs`

This function returns the absolute value of a `number`.

```python
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
```
