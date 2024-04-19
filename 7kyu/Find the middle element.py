def gimme(input_array):
    copy_array = input_array[:]
    input_array.remove(max(input_array))
    input_array.remove(min(input_array))
    return copy_array.index(input_array.pop())


print(gimme([2, 3, 1]))
