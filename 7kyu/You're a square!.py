def is_square(n):
    return int(n ** 0.5) ** 2 == n if n >= 0 else False


print(is_square(10343707743355944185080337))
