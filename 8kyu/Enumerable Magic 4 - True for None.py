def none(lst, func):
    return not any(map(func, lst))


lst = [0, 1, 2, 3, 5, 8, 13]

print(none(lst, lambda x: x > 9))
