def transpose_two_strings(arr):
    left, right = arr
    if len(left) > len(right):
        right = right.ljust(len(left))
    else:
        left = left.ljust(len(right))
    return '\n'.join([f'{x} {y}' for x, y in zip(left, right)])


print(transpose_two_strings(["joey", "louise"]))
