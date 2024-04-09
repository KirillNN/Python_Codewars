def is_triangle(a, b, c):
    if any([x <= 0 for x in (a, b, c)]):
        return False
    return a < b + c and b < a + c and c < a + b


print(is_triangle(1, -2, 2))
