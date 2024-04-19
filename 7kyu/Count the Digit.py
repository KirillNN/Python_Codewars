def count_digit(number, digit):
    count = 1 if number == 0 and digit == 0 else 0
    while number:
        if number % 10 == digit:
            count += 1
        number //= 10
    return count


def nb_dig(n, d):
    count = 0
    for i in range(n + 1):
        count += count_digit(i ** 2, d)
    return count


print(nb_dig(10891, 0))
