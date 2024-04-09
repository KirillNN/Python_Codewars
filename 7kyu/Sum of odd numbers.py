# 2 6 12 20 30
def row_sum_odd_numbers(n):
    start = 1 + sum(range(2, n * 2, 2))
    return sum(range(start, start + 2 * n, 2))


print(row_sum_odd_numbers(5))
print(row_sum_odd_numbers(1))
