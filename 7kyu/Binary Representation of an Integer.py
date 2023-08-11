# представление отрицательных чисел в двоичном коде python bin dec
def show_bits(n):
    if n >= 0:
        x = bin(n)[2:].rjust(32, '0')
    else:
        x = int(bin(n)[3:])
        return x, type(x)
    return list(map(int, x))


# print(show_bits(4))
# print(show_bits(~4))
# x = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
# print(len((x)))
# вывод bin без 0b спереди
# y = bin(25)[2:]
# print(y, type(y))

# x = 200
# print(int('0b110', 2))


print(bin(3))
print(bin(~3))