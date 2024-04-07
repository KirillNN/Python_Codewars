def filter_list(l):
    return list(filter(lambda x: isinstance(x, int), l))


print(filter_list([1, 2, 'a', 'b']))
