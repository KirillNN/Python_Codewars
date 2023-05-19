def are_coprime(n, m):
    while n != 0 and m != 0:
        if n > m:
            n = n % m
        else:
            m = m % n
    return True if n + m == 1 else False
