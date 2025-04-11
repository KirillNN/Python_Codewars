def min_value(digits):
    return int(''.join(map(str, sorted(set(digits)))))


print(min_value([1, 3, 1]))
print(min_value([4, 8, 1, 4]))
# test.assert_equals(min_value([1, 3, 1]), 13)
# test.assert_equals(min_value([4, 7, 5, 7]), 457)
# test.assert_equals(min_value([4, 8, 1, 4]), 148)
