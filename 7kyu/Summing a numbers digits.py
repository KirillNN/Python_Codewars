def sum_digits(number):
    number = abs(number)
    summ = 0
    while number:
        summ += number % 10
        number //= 10
    return summ
