def min_sum(arr: list):
    arr.sort()
    length = len(arr) // 2
    return sum(i * j for i, j in zip(arr[:length], arr[:length - 1:-1]))


print(min_sum([12, 6, 10, 26, 3, 24]))
