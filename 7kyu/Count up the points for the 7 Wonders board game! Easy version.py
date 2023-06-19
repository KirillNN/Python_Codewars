from functools import reduce


def seven_wonders_science(*args):
    step1 = min(args) * 7
    step2 = reduce(lambda x, y: x + y ** 2, args, 0)
    return step1 + step2


# test.assert_equals(seven_wonders_science(0, 0, 0), 0)
# test.assert_equals(seven_wonders_science(1, 1, 1), 10)
# test.assert_equals(seven_wonders_science(2, 1, 1), 13)
# test.assert_equals(seven_wonders_science(4, 2, 2), 38)
# test.assert_equals(seven_wonders_science(7, 2, 2), 71)

print(seven_wonders_science(4, 2, 2))
