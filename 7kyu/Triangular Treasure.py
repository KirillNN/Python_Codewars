def triangular(n):
    if n <= 0:
        return 0
    if n % 2:
        res = n * (n // 2 + 1)
    else:
        res = (n + 1) * n // 2
    return res


print(triangular(4))  # 10
print(triangular(5))  # 15
print(triangular(6))  # 21
print(triangular(7))  # 28
print(triangular(8))  # 36
print(triangular(9))  # 45

# def triangular(n):
#     if n <= 0: return 0
#     res = 0
#     for i in range(n + 1):
#         res += i
#     return res
#
#
# print(triangular(4))  # 10
# print(triangular(5))  # 15
# print(triangular(6))  # 21
# print(triangular(7))  # 28
# print(triangular(8))  # 36
# print(triangular(9))  # 45
