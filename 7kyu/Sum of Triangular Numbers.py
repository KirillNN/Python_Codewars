def sum_triangular_numbers(n):
    if n <= 0:
        return 0
    sum_ = 0
    result = 0
    for i in range(1, n + 1):
        sum_ += i
        result += sum_
    return result


print(sum_triangular_numbers(6))
