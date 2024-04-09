def binary_array_to_number(arr):
    return sum([v * 2 ** i for i, v in enumerate(reversed(arr))])


print(binary_array_to_number([0, 1, 1, 1]))
