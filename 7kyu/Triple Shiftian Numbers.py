def triple_shiftian(base, n):
    if n < 3:
        return base[n]
    index = len(base)
    base.append(4 * base[index - 1] - 5 * base[index - 2] + 3 * base[index - 3])
    if len(base) == n + 1:
        return base[-1]
    else:
        return triple_shiftian(base, n)


print(triple_shiftian([1, 1, 1], 25))
