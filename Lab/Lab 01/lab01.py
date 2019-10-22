"""Lab 1: Expressions and Control Structures"""

# Coding Practice

def repeated(f, n, x):
    """Returns the result of composing f n times on x.

    >>> def square(x):
    ...     return x * x
    ...
    >>> repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
    81
    >>> repeated(square, 1, 4)  # square(4)
    16
    >>> repeated(square, 6, 2)  # big number
    18446744073709551616
    >>> def opposite(b):
    ...     return not b
    ...
    >>> repeated(opposite, 4, True)
    True
    >>> repeated(opposite, 5, True)
    False
    >>> repeated(opposite, 631, 1)
    False
    >>> repeated(opposite, 3, 0)
    True
    """
    temp = x
    while n>0:
        temp = f(temp)
        n -= 1
    return temp

def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    s = 0
    i = 0
    d = 1
    while n // d != 0:
        d = 10 ** i
        s = n // d % 10 + s #The way you retrieve a digit from a number
        i += 1
    return s

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    i = 0
    d = 1
    while n // d != 0:
        d = 10 ** i
        digit = n // d % 10  # The way you retrieve a digit from a number
        if digit == 8:
            i += 1
            d = 10 ** i
            digit = n // d % 10  # The way you retrieve a digit from a number
            if digit == 8:
                return True
        else:
            i += 1
    return False
