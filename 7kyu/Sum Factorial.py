def sum_factorial(lst, result=0):
    for i in lst:
        fact = 1
        for j in range(1, i + 1):
            fact *= j
        result += fact
    return result
