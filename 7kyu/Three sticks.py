def maxlen(L1, L2):
    min_number, max_number = (L1, L2) if L1 < L2 else (L2, L1)
    if max_number >= min_number * 3:
        return max_number / 3
    elif max_number >= min_number * 2:
        return min_number
    return max_number / 2


print(maxlen(5, 12))
print(maxlen(15, 12))
