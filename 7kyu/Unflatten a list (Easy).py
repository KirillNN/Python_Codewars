def unflatten(flat_array):
    i = 0
    result = []
    while i < len(flat_array):
        if flat_array[i] < 3:
            result.append(flat_array[i])
            i += 1
        else:
            result.append(flat_array[i:i+flat_array[i]])
            i += flat_array[i]
    return result


x = [1, 4, 5, 2, 1, 2, 4, 5, 2, 6, 2, 3, 3]
print(unflatten(x))
# y = [1, [4, 5, 2, 1], 2, [4, 5, 2, 6], 2, [3, 3]]
# print(y)
