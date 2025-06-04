def find_longest(arr):
    return int(next(filter(lambda x: len(x) == max(map(len, map(str, arr))), map(str, arr))))


print(find_longest([8, 900, 500]))
