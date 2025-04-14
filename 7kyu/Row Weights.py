def row_weights(array):
    num_1 = sum(array[::2])
    num_2 = sum(array[1::2])
    return num_1, num_2


print(row_weights([100,50]))

# test.assert_equals(row_weights([80]), (80,0))
# test.assert_equals(row_weights([100,50]), (100,50))
# test.assert_equals(row_weights([50,60,70,80]), (120,140))
# test.assert_equals(row_weights([13,27,49]), (62,27))
# test.assert_equals(row_weights([70,58,75,34,91]), (236,92))
# test.assert_equals(row_weights([29,83,67,53,19,28,96]), (211,164))
# test.assert_equals(row_weights([100,51,50,100]), (150,151))
# test.assert_equals(row_weights([39,84,74,18,59,72,35,61]), (207,235))
