def accum(st):
    result = []
    for i, v in enumerate(st):
        result.append(v.upper() + v.lower() * i)
    return '-'.join(result)


print(accum("abcd"))
