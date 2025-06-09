def vert_mirror(strng):
    s = strng.split()
    return list(map(lambda x: x[::-1], s))


def hor_mirror(strng):
    s = strng.split()
    return s[::-1]


def oper(fct, s):
    return '\n'.join(fct(s))


s = "abcd\nefgh\nijkl\nmnop"
print(vert_mirror(s))
print(hor_mirror(s))
print(oper(vert_mirror, s))
