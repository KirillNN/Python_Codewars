def number_of_hooks(length, max_hook_dist):
    result = 2
    mult = 0
    while length > max_hook_dist:
        result += 2 ** mult
        mult += 1
        length /= 2
    return result


print(number_of_hooks(200, 70))

# Давайте рассмотрим данную последовательность:
#
# 3, 5, 9, 17, 33, 65, 129, 257, 513, 1025
# Если мы внимательно посмотрим на разницу между последовательными элементами, то можем заметить следующее:
#
# 5 - 3 = 2
# 9 - 5 = 4
# 17 - 9 = 8
# 33 - 17 = 16
# 65 - 33 = 32
# 129 - 65 = 64
# 257 - 129 = 128
# 513 - 257 = 256
# 1025 - 513 = 512