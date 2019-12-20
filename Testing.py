def ten_pairs(n, count = 0):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    if n//10 == 0:
        return count
    else:
        r = n % 10

        def helper(n, count):
            if n//10 == 0:
                return count
            else:
                if n//10 % 10+r == 10:
                    count += 1
                return helper(n//10, count)

        return helper(n, count)+ten_pairs(n//10, count)