def neutralise(s1, s2):
    res = [['0', x][x == y] for x, y in zip(s1, s2)]
    return ''.join(res)


print(neutralise("--++--", "++--++"))
