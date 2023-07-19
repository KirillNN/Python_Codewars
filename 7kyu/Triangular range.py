def triangular_range(start, stop):
    pairs = dict()
    summ = 0
    for i in range(1, 1_000_000):
        summ += i
        if start <= summ <= stop:
            pairs[i] = summ
        elif summ > stop:
            break

    return pairs


print(triangular_range(13, 5490))

# {5: 15, 6: 21, 7: 28, 8: 36, 9: 45, 10: 55, 11: 66, 12: 78, 13: 91, 14: 105, 15: 120, 16: 136, 17: 153, 18: 171,
#  19: 190, 20: 210, 21: 231, 22: 253, 23: 276, 24: 300, 25: 325, 26: 351, 27: 378, 28:
