# представление отрицательных чисел в двоичном коде python bin dec
def show_bits(n):
    if n >= 0:
        x = bin(n)[2:].rjust(32, '0')
    else:
        n = abs(n) - 1
        n = bin(n)[2:]
        x = ''.join(['1' if x == '0' else '0' for x in n]).rjust(32, '1')
    return list(map(int, x))


print(show_bits(-245))
# print(show_bits(~4))
# x = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
# print(len((x)))
# вывод bin без 0b спереди
# y = bin(25)[2:]
# print(y, type(y))

# x = 200
# print(int('0b110', 2))


print(bin(3))
print(bin(244))
