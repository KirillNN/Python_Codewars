def collinearity(x1, y1, x2, y2):
    if x1 == y1 == 0 or x2 == y2 == 0 or x1 == x2 == 0 or y1 == y2 == 0:
        return True
    if x1 == y2 == 0 or x2 == y1 == 0:
        return False
    try:
        return y1 / x1 == y2 / x2
    except:
        return False


def collinearity_v1(x1, y1, x2, y2):
    return x1 * y2 == x2 * y1