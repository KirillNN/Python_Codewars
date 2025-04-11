def max_multiple(divisor, bound):
    return bound // divisor * divisor


print(max_multiple(2, 7))

# test.assert_equals(max_multiple(2, 7), 6)
# test.assert_equals(max_multiple(3, 10), 9)
# test.assert_equals(max_multiple(7, 17), 14)
# test.assert_equals(max_multiple(10, 50), 50)
# test.assert_equals(max_multiple(37, 200), 185)
# test.assert_equals(max_multiple(7, 100), 98)
