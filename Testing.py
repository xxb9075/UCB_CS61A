

def flatten(lst, lst_new = None):
    if lst_new is None:
        lst_new = []
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
