def factorial(n):
    if n < 0 or n > 12:
        raise ValueError()
    if not n:
        return 1
    return factorial(n - 1) * n


print(factorial(12))
