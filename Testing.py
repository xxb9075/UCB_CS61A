

def flatten(lst, lst_new = []):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    i = 0
    while i < len(lst):
        if type(lst[i]) != list:
            lst_new.append(lst[i])
            i += 1
        else:
            flatten(lst[i], lst_new)
            i += 1
    return lst_new

x = [[1, [1, 1]], 1, [1, 1]]
print(flatten(x))

x = [1, [2, 3], 4]
print(flatten(x))