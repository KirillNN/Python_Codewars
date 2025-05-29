def adjacent_element_product(array):
    return max(i * j for i, j in zip(array, array[1:]))


print(adjacent_element_product([5, 8]), 40)
print(adjacent_element_product([1, 2, 3]), 6)
print(adjacent_element_product([1, 5, 10, 9]), 90)
print(adjacent_element_product([4, 12, 3, 1, 5]), 48)
print(adjacent_element_product([5, 1, 2, 3, 1, 4]), 6)
