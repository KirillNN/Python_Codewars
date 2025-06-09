def div_con(x):
    r = sum(map(int, filter(lambda _: isinstance(_, str), x)))
    rr = sum(filter(lambda _: isinstance(_, int), x))
    return rr - r


print(div_con([9, 3, '7', '3']))

# def basic_test_cases():
#     test.assert_equals(div_con([9, 3, '7', '3']), 2)
#     test.assert_equals(div_con(['5', '0', 9, 3, 2, 1, '9', 6, 7]), 14)
#     test.assert_equals(div_con(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']), 13)
#     test.assert_equals(div_con(['1', '5', '8', 8, 9, 9, 2, '3']), 11)
#     test.assert_equals(div_con([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61)
