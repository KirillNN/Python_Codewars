def sum_of_n(n):
    result = [0]
    for i in range(1, abs(n) + 1):
        if n > 0:
            result.append(i + result[i - 1])
        else:
            result.append((-i + result[i - 1]))
    return result


print(sum_of_n(3))
print(sum_of_n(-4))
