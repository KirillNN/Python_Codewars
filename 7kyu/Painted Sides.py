def painted_faces(length, n):
    result = dict()
    if length == 1:
        result = {6: 1}
    elif length == 2:
        result = {3: 8}
    elif length > 2:
        zero_side = (length - 2) ** 3
        one_side = (length - 2) ** 2 * 6
        two_side = (length - 2) * 12
        result = {0: zero_side, 1: one_side, 2: two_side, 3: 8}
    return result.get(n, 0)


print(painted_faces(4, 3))
print(painted_faces(5, 1))
print(painted_faces(10, 2))
print(painted_faces(9, 0))
