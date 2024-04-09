def series_sum(n):
    result = 0
    for i in range(1, n * 3 + 1, 3):
        result += 1 / i
    return f"{result:.2f}"


print(series_sum(5))
