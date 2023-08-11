def get_mean(arr, x, y):
    if x < 2 or y < 2 or x > len(arr) or y > len(arr):
        return -1
    a = sum(arr[:x]) / x
    b = sum(arr[-y:]) / y
    return (a + b) / 2


print(get_mean([1, 3, 2, 4], 2, 3))
print(get_mean([1, 3, 2], 2, 2))
