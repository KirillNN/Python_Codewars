# def is_divisible(*args):
#     first = args[0]
#     last = args[1:]
#     z = list(zip([first] * len(last), last))
#     print(z)
#     x = [a % b == 0 for a, b in z]
#     print(x)
#     result = all(x)
#     return result

# def is_divisible(*args):
#     first = args[0]
#     last = args[1:]
#     pairs = list(zip([first] * len(last), last))
#     result = all([a % b == 0 for a, b in pairs])
#     return result
#
# def is_divisible(n, *args):
#     return all(not n % i for i in args)
#
#
# def is_divisible(n, *args):
#   return all(n % a == 0 for a in args)
#
# is_divisible(12, 3, 4)
# is_divisible(100, 5, 4, 10, 25, 20)


current_list = [[10, 6, 9], [0, 14, 16, 80], [8, 12, 30, 44]]
sorted_list = lambda x: (sorted(i) for i in x)
second_largest = lambda x, func: [y[len(y) - 2] for y in func(x)]
result = second_largest(current_list, sorted_list)
print(result)
