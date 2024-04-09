def divisors(integer):
    result = []
    for i in range(2, integer // 2 + 1):
        if not integer % i:
            result.append(i)
    return result if result != [] else f'{integer} is prime'
