def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def count_partitions(n, m):
        """Count the ways to partition n using parts up to m."""
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif m == 0:
            return 0
        else:
            return count_partitions(n - m, m) + count_partitions(n, m//2)

    def coin_max(n):
        t = 1
        while 2**t <= n:
            t += 1
        return t

    return count_partitions(amount, 2**coin_max(amount))


count_change(7)