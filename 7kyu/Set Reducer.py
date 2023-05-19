def set_reducer(inp):
    if len(inp) == 1:
        return inp[0]
    else:
        res = [1] * len(inp)
        index_res = 0
        for i in range(len(inp[:-1])):
            if inp[i] == inp[i + 1]:
                res[index_res] += 1
                res.pop()
            else:
                index_res += 1

        return set_reducer(res)


print(set_reducer([0, 4, 6, 8, 8, 8, 5, 5, 7]))
print(set_reducer([8, 1, 6, 1, 2, 7, 7, 7, 7, 6, 5, 3, 2, 1, 8]))


from itertools import groupby

def set_reducer(inp):
    while len(inp) > 1:
        inp = [len(list(b)) for a, b in groupby(inp)]
    return inp[0]