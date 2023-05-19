def sum_no_duplicates(l):
    res = [x for x in l if l.count(x) == 1]
    return sum(res)


print(sum_no_duplicates([1, 1, 2, 3]))
