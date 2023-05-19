def least_larger(a, i):
    goal = result_index = float('inf')
    for index, value in enumerate(a):
        if a[i] < value < goal:
            result_index = index
            goal = value
    return result_index if result_index != float('inf') else -1


print(least_larger([4, 1, 3, 5, 6], 4))

# test.assert_equals(least_larger([4, 1, 3, 5, 6], 0), 3)
# test.assert_equals(least_larger([4, 1, 3, 5, 6], 4), -1)
# test.assert_equals(least_larger([1, 3, 5, 2, 4], 0), 3)
