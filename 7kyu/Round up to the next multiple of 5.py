def round_to_next5(n):
    if n % 5 == 0:
        return n
    if n > 0:
        return n + 5 - n % 5
    return n + abs(n) % 5


print(round_to_next5(-1))
