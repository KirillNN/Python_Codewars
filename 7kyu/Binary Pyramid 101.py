def binary_pyramid(m, n):
    return f'{sum(map(int, map(lambda x: f"{x:b}", range(m, n + 1)))):b}'


print(binary_pyramid(1, 4))
