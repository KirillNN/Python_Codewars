def best_friend(txt, a, b):
    if a == b:
        return False
    for i, v in enumerate(txt[:-1]):
        if v == a and txt[i + 1] != b:
            return False
    for i, v in enumerate(txt[1:]):
        if v == b and txt[i - 1] != a:
            return False

    return True


print(best_friend('he headed to the store', 'h', 'e'))
