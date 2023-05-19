def even_numbers(arr, n):
    return [x for x in arr if x % 2 == 0][-n:]


print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
