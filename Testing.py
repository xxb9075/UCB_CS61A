from lab 03 import *

## Higher order functions


def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    def f(n)(x):
        if n%3 == 0:
            if n == 0:
                return x
            else:
                return f3(f2(f1(f(n-3))))
        if n%3 == 1:
            if n == 1:
                return f1(x)
            else:
                return f1(f(n-3)(x))
        if n%3 == 2:
            if n == 2:
                return f2(f1(x))
            else:
                return f2(f1(f(n-3)))

