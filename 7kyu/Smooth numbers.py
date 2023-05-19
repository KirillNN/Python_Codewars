def is_smooth(n, smooths=0):
    smooth = [2, 3, 5, 7]
    for i in smooth:
        if n % i == 0:
            smooths = max(smooths, i)
            return is_smooth(n // i, smooths)
    result = {2: 'power of 2', 3: '3-smooth', 5: 'Hamming number', 7: 'humble number'}

    return result[smooths] if n == 1 else 'non-smooth'


print(is_smooth(3125))
# test.assert_equals(is_smooth(16), "power of 2")
# test.assert_equals(is_smooth(36), "3-smooth")
# test.assert_equals(is_smooth(60), "Hamming number")
# test.assert_equals(is_smooth(98), "humble number")
# test.assert_equals(is_smooth(111), "non-smooth")
# test.assert_equals(is_smooth(4096), "power of 2")
# test.assert_equals(is_smooth(729), "3-smooth")
# test.assert_equals(is_smooth(3125), "Hamming number")
# test.assert_equals(is_smooth(7), "humble number")
# test.assert_equals(is_smooth(17), "non-smooth")
