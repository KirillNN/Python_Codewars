def remove_smallest(numbers):
    if not numbers:
        return []
    result = numbers[:]
    result.remove(min(result))
    return result


print(remove_smallest([1, 2, 3, 4, 5]))
