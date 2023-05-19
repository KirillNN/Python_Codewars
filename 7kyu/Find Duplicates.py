def duplicates(arr):
    dubl = list()
    res = list()
    for i in arr:
        if i in dubl:
            res.append(i) if i not in res else 0
        else:
            dubl.append(i)
    return res

print(duplicates([1, 2, 4, 4, 3, 3, 1, 5, 3, '5']))


