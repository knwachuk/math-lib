# Mathematics Library

Home-made Mathematics library using the Python programming language. It will emulate the [math - Mathematical functions](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwj738W6iLv9AhX6kokEHejhDfcQFnoECAkQAQ&url=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fmath.html&usg=AOvVaw26GwSqIFLX1e1HscI8nzVo) library in Python, although it will be a much less complete version.

The math library will be rudimentary but fully functional, including all elementary arithmetic operations (i.e., addition, subtraction, multiplication, and division) and some more advanced topics (i.e., exponents and logarithms) and two special functions (absolute value and division and modulus operation). 

**LIMITATION**

The only limitation is that only the Python `+` and `-` operators are allowed to be utilized. *Every other function MUST use these*. That is, no operational code is allowed to use 3rd party libraries or the operators exceptions `+` and `-`.

*For example*

The `mult` function uses the fact that *multiplication is a series of additions or subtractions* in compute the multiplication of two numbers.

## Library Functions

1. [Elementary Operations](#elementary-operations)
    1. Addition (`add`, `+`)
    2. Subtraction (`sub`, `-`)
    3. Multiplication (`mult`)
    4. Division (`div`)
2. [Advanced Functions](#advanced-functions)
    1. Square Root (`sqrt`)
    2. Exponentiation (`exp`)
    3. Logarithm (`log`)
3. [Special Functions](#special-function)
    1. Absolute Value (`abs`)
    2. Division and Modulus (`divmod`)



### Elementary Operations <a name="elementary-operations"></a>

1. Addition (`add`, `+`) 
2. Subtraction (`sub`, `-`)
3. Multiplication (`mult`) ** 2
4. Division (`div`)

> **Note**
>
> Only the Python `+` and `-` operators are allowed to be utilized in this library.

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

#### `mult`

This is a binary function that takes in two **numbers** (`multiplier` and `multiplicand`) and returns the product of the two `numbers`.

```python
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
```

### Advanced Functions <a name="advanced-functions"></a>

1. Square Root (`sqrt`)
2. Exponentiation (`exp`) ** 4
3. Logarithm (`log`)

### Special Function <a name="special-functions"></a>

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
