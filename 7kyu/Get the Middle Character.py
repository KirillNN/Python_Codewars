def get_middle(s):
    print(s)
    len_s = len(s)
    if len_s % 2:
        return s[len_s // 2]
    return s[len_s // 2 - 1: len_s // 2 + 1]


print(get_middle('test'))
