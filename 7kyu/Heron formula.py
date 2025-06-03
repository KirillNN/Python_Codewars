def heron(a, b, c):
    s = (a + b + c) / 2
    result = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return result
