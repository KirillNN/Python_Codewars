def vampire_test(x, y):
    return sorted(str(x * y)) == sorted(str(x) + str(y))


print(vampire_test(-5, 2))
