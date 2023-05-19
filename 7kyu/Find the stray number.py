def stray(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i


def stray1(arr):
    return min(arr, key=arr.count)
