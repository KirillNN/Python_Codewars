def capitals(word):
    result = []
    for i, v in enumerate(word):
        if v.isupper():
            result.append(i)
    return result


capitals('a')
