import datetime
import re
import math
from math import ceil
from math import tan
from math import pi
from numpy import prod


def time_interval(time1, time2, res):  # time_interval('12 13 59', '10 23 54', 1575000)
    x1 = [int(x) for x in time1.split()]
    x2 = [int(x) for x in time2.split()]
    x3 = x1[0] * 3600 + x1[1] * 60 + x1[2] - (x2[0] * 3600 + x2[1] * 60 + x2[2])
    x4 = x3 // 3600  # Получение целой части от деления - часы
    x5 = x3 % 3600  # Получение остатка от деления
    x6 = x5 // 60  # Получение целой части от деления - минуты
    x7 = x5 % 60  # Получение остатка от деления - секунды
    result = 'Разница в секундах: ' + str(x3) + '. Разница в ЧМС: ' + str(x4) + ' ч. ' + str(x6) + ' мин. ' + str(x7) + \
             ' сек. Скорость сбора ' + str(res / x3 * 3600) + ' ед. в час'
    return result


# print(time_interval('12 13 59', '10 23 54', 1575000))
# print(time_interval('12 15 2', '10 24 56', 1575000))
# print(time_interval('12 15 18', '10 25 13', 1575000))
# print(time_interval('11 39 39', '10 26 52', 1041057))


# test.assert_equals(xMasTree(3), ['__#__', '_###_', '#####', '__#__', '__#__'])
# test.assert_equals(xMasTree(7), ['______#______', '_____###_____', '____#####____', '___#######___', '__#########__',
#                                  '_###########_', '#############', '______#______', '______#______'])
# test.assert_equals(xMasTree(2), ['_#_', '###', '_#_', '_#_'])
# test.assert_equals(xMasTree(4), ['___#___', '__###__', '_#####_', '#######', '___#___', '___#___'])
# test.assert_equals(xMasTree(6), ['_____#_____', '____###____', '___#####___', '__#######__', '_#########_',
# '###########', '_____#_____', '_____#_____'])


def xMasTree(n):
    out = []
    for x in range(1, n + 1):
        out.append('_' * (n - x) + '#' * ((x - 1) * 2 + 1) + '_' * (n - x))
    out.append(out[0])
    out.append(out[0])
    return out


# print(xMasTree(7))


# ---#---#---#---# (Kata) Your order, please #---#---#---#---#

# Test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
# Test.assert_equals(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
# Test.assert_equals(order(""), "")

def order(sentence):
    if sentence == "":
        return ""
    else:
        return ' '.join(sorted(sentence.split(), key=lambda x: re.findall('[1-9]', x)[0]))


# print(order("4of Fo1r pe6ople g3ood th5e the2"))

# ---#---#---#---# (Kata) Sum of positive #---#---#---#---#

# Test.describe("positive_sum")
#
# Test.it("works for some examples")
# Test.assert_equals(positive_sum([1,2,3,4,5]),15)
# Test.assert_equals(positive_sum([1,-2,3,4,5]),13)
# Test.assert_equals(positive_sum([-1,2,3,4,-5]),9)
#
# Test.it("returns 0 when array is empty")
# Test.assert_equals(positive_sum([]),0)
#
# Test.it("returns 0 when all elements are negative")
# Test.assert_equals(positive_sum([-1,-2,-3,-4,-5]),0)

def positive_sum(arr):
    return sum(x for x in arr if x > 0)


# print(positive_sum([1, -2, 3, 4, 5]))


# ---#---#---#---# (Kata) Sum of Digits / Digital Root #---#---#---#---#
# Test.assert_equals(digital_root(16), 7)
# Test.assert_equals(digital_root(942), 6)
# Test.assert_equals(digital_root(132189), 6)
# Test.assert_equals(digital_root(493193), 2)

def digital_root(n):
    while n > 9:
        n = sum(list(map(int, str(n))))
    return n


# print(digital_root(132189))

# ---#---#---#---# (Kata) Sequence convergence #---#---#---#---#
# Test.assert_equals(convergence(3),5)
# Test.assert_equals(convergence(5),6)
# Test.assert_equals(convergence(10),5)
# Test.assert_equals(convergence(15),2)
# Test.assert_equals(convergence(500),29)
# Test.assert_equals(convergence(5000),283)
def add_next_number(mod_list):
    if mod_list[-1] < 10:
        mod_list.append(mod_list[-1] * 2)
    else:
        x = [x for x in list(map(int, str(mod_list[-1]))) if x > 0]
        p = 1
        for i in range(len(x)):
            p *= x[i]
        mod_list.append(mod_list[-1] + p)
    return mod_list


def convergence(n):
    count = 0
    series_base = [1]
    series_test = [n]
    flag = 1
    while flag:
        add_next_number(series_base)
        add_next_number(series_test)
        x = list(set(series_base) & set(series_test))  # Находим пересечения (одинаковые элементы)
        if len(x) > 0:
            return series_test.index(x[0])
        count += 1


# ---#---#---#---# (Kata) Split Strings #---#---#---#---#
# tests = (
#     ("asdfadsf", ['as', 'df', 'ad', 'sf']),
#     ("asdfads", ['as', 'df', 'ad', 's_']),
#     ("", []),
#     ("x", ["x_"]),
# )
def solution(s):
    if s == '':
        return []
    if len(s) % 2 == 1:
        s += '_'
    _out = []
    for x in range(0, len(s), 2):
        _out.append(s[x:x + 2])
    return _out


# print(solution('asdfadsf'))
# print(solution('asdfads'))
# print(solution(''))
# print(solution('x'))

# ---#---#---#---# (Kata) Upside down numbers #---#---#---#---#
# test.assert_equals(solve(0,10),3)
# test.assert_equals(solve(10,100),4)
# test.assert_equals(solve(100,1000),12)
# test.assert_equals(solve(1000,10000),20)
# test.assert_equals(solve(10000,15000),6)
# test.assert_equals(solve(15000,20000),9)
# test.assert_equals(solve(60000,70000),15)
# test.assert_equals(solve(60000,130000),55)

def solve(a, b):
    result = 0
    for x in range(a, b):
        x_rev = str(x)[::-1]
        if re.findall('[23457]', x_rev):
            continue
        else:
            # print(x_rev)
            x_rev_rep = ''
            for i in range(len(x_rev)):
                if x_rev[i] == '6':
                    x_rev_rep += '9'
                    continue
                if x_rev[i] == '9':
                    x_rev_rep += '6'
                    continue
                x_rev_rep += x_rev[i]
            # print(x_rev_rep)
            if str(x) == x_rev_rep:
                print(x)
                result += 1
    return result


# solve(10, 100)

# ---#---#---#---# (Kata) Bit Counting #---#---#---#---#
# test.assert_equals(count_bits(0), 0)
# test.assert_equals(count_bits(4), 1)
# test.assert_equals(count_bits(7), 3)
# test.assert_equals(count_bits(9), 2)
# test.assert_equals(count_bits(10), 2)

def count_bits(n):
    return len(re.findall('[1]', bin(n)))
    # return bin(n).count("1") # можно так


# print(count_bits(7))

# ---#---#---#---# (Kata) Rot13 #---#---#---#---#
# test.assert_equals(rot13("test"),"grfg")
# test.assert_equals(rot13("Test"),"Grfg")
# ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
# NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm


def rot13(message):
    a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    b = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'

    result = ''
    for x in message:
        index = a.find(x)
        if index == -1:
            result += x
        else:
            result += b[index]
    return result


# print(rot13('test'))


# ---#---#---#---# (Kata) Square Every Digit #---#---#---#---#
# test.assert_equals(square_digits(9119), 811181)

def square_digits(num):
    # x=list(str(num))
    # x = [int(x) * int(x) for x in list(str(num))]
    # x = map(str, str(num))
    return int(''.join(map(str, [int(x) * int(x) for x in list(str(num))])))


# print(square_digits(9119))

# ---#---#---#---# (Kata) Find the unique number #---#---#---#---#
# test.assert_equals(find_uniq([1, 1, 1, 2, 1, 1]), 2)
# test.assert_equals(find_uniq([0, 0, 0.55, 0, 0]), 0.55)
# test.assert_equals(find_uniq([3, 10, 3, 3, 3]), 10)

def find_uniq(arr):
    a1 = arr[0]
    a2 = arr[1]
    a3 = arr[2]
    if a1 == a2 == a3:
        # print('Надо искать не этот элемент', a1)
        x = set(arr) - set([a1])
        # x = set(arr).difference(set([a1])) # можно так
        for result in x:
            return result
    else:
        if a1 == a2:
            # print('Элемент найден: это ', a3)
            return a3
        else:
            if a1 == a3:
                # print('Элемент найден: это ', a2)
                return a2
            else:
                # print('Элемент найден: это ', a1)
                return a1


# print(find_uniq([1, 1, 1, 2, 1, 1]))

# ---#---#---#---# (Kata) Grasshopper - Grade book #---#---#---#---#
# test.assert_equals(get_grade(95, 90, 93), "A", "get_grade(95, 90, 93)")
#         test.assert_equals(get_grade(100, 85, 96), "A", "get_grade(100, 85, 96)")
#         test.assert_equals(get_grade(92, 93, 94), "A", "get_grade(92, 93, 94)")
#         test.assert_equals(get_grade(100, 100, 100), "A", "get_grade(100, 100, 100)")
#
#     @test.it("should return a B")
#     def b_test_case():
#         test.assert_equals(get_grade(70, 70, 100), "B", "get_grade(70, 70, 100)")
#         test.assert_equals(get_grade(82, 85, 87), "B", "get_grade(82, 85, 87)")
#         test.assert_equals(get_grade(84, 79, 85), "B", "get_grade(84, 79, 85)")
#
#     @test.it("should return a C")
#     def c_test_case():
#         test.assert_equals(get_grade(70, 70, 70), "C", "get_grade(70, 70, 70)")
#         test.assert_equals(get_grade(75, 70, 79), "C", "get_grade(75, 70, 79)")
#         test.assert_equals(get_grade(60, 82, 76), "C", "get_grade(60, 82, 76)")
#
#     @test.it("should return a D")
#     def d_test_case():
#         test.assert_equals(get_grade(65, 70, 59), "D", "get_grade(65, 70, 59)")
#         test.assert_equals(get_grade(66, 62, 68), "D", "get_grade(66, 62, 68)")
#         test.assert_equals(get_grade(58, 62, 70), "D", "get_grade(58, 62, 70)")

def get_grade(s1, s2, s3):
    mean = (s1 + s2 + s3) / 3
    print(type(mean))
    if 90 <= mean <= 100:
        return "A"
    if 80 <= mean < 90:
        return "B"
    if 70 <= mean < 80:
        return "C"
    if 60 <= mean < 70:
        return "D"
    if 0 <= mean < 60:
        return "F"


# get_grade(65, 70, 59)

# ---#---#---#---# (Kata) Highest and Lowest #---#---#---#---#
# test.assert_equals(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214");
# test.assert_equals(high_and_low("1 -1"), "1 -1");
# test.assert_equals(high_and_low("1 1"), "1 1");
# test.assert_equals(high_and_low("-1 -1"), "-1 -1");
# test.assert_equals(high_and_low("1 -1 0"), "1 -1");
# test.assert_equals(high_and_low("1 1 0"), "1 0");
# test.assert_equals(high_and_low("-1 -1 0"), "0 -1");
# test.assert_equals(high_and_low("42"), "42 42");

def high_and_low(numbers):
    x = sorted(list(map(int, numbers.split())))
    return str(x[-1]) + ' ' + str(x[0])


# print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
# print(high_and_low("42"))

# ---#---#---#---# (Kata) Quarter of the year #---#---#---#---#
# test.assert_equals(quarter_of(3), 1)
# test.assert_equals(quarter_of(8), 3)
# test.assert_equals(quarter_of(11), 4)

def quarter_of(month):
    return ceil(month / 3)


# for i in range(1, 13):
#     print(quarter_of(i))

# ---#---#---#---# (Kata) Limit string length - 1 #---#---#---#---#
# test.assert_equals(solution('Testing String',3), 'Tes...')
# test.assert_equals(solution('Testing String',8), 'Testing ...')
# test.assert_equals(solution('Test', 10), 'Test')
# test.assert_equals(solution('Test', 4), 'Test')

def solution(st, limit):
    if len(st) <= limit:
        return st
    return st[:limit] + '...'


# print(solution('Testing String',8))

# ---#---#---#---# (Kata) Love vs friendship #---#---#---#---#
# test.assert_equals(words_to_marks('attitude'), 100)
# test.assert_equals(words_to_marks('friends'), 75)
# test.assert_equals(words_to_marks('family'), 66)
# test.assert_equals(words_to_marks('selfness'), 99)
# test.assert_equals(words_to_marks('knowledge'), 96)

def words_to_marks(s):
    return sum(list(map(lambda x: ord(x) - 96, s)))
    # return sum(ord(c)-96 for c in s) # можно так


# print(words_to_marks('attitude'))


# ---#---#---#---# (Kata) Construct a bit vector set #---#---#---#---#
# @test.it("should return 0 if empty array is provided")
#     def test_case():
#         test.assert_equals(sort_by_bit([]), 0)
#     @test.it("should return 1 if array with zero is provided")
#     def test_case():
#         test.assert_equals(sort_by_bit([0]), 1)
#     @test.it("should return 3 if array with zero and 1 is provided")
#     def test_case():
#         test.assert_equals(sort_by_bit([0, 1]), 3)
#     @test.it("should return 3 if array with zero and 1 is provided, order shouldn't matter")
#     def test_case():
#         test.assert_equals(sort_by_bit([1, 0]), 3)
#     @test.it("should return 1073741825 if array with 30 and 0 provided")
#     def test_case():
#         test.assert_equals(sort_by_bit([30, 0]), 1073741825)

def sort_by_bit(seq):
    return sum(2 ** x for x in seq)


# print(sort_by_bit([0, 30]))

# ---#---#---#---# (Kata) Summy #---#---#---#---#
# test.assert_equals(summy("1 2 3"), 6)
# test.assert_equals(summy("1 2 3 4"), 10)
# test.assert_equals(summy("1 2 3 4 5"), 15)
# test.assert_equals(summy("10 10"), 20)
# test.assert_equals(summy("0 0"), 0)

def summy(string_of_ints):
    return sum(int(x) for x in string_of_ints.split())
    # return sum(map(int,string_of_ints.split())) # можно так


# print(summy("1 2 3 4 5"))


# ---#---#---#---# (Kata) A Rule of Divisibility by 7 #---#---#---#---#
# test.assert_equals(seven(1603), (7, 2))
# test.assert_equals(seven(371), (35, 1))
# test.assert_equals(seven(483), (42, 1))
# test.assert_equals(seven(483595), (28, 4))

def seven(m):
    count = 0
    while m > 99:
        m = m // 10 - m % 10 * 2
        count += 1
    return m, count


# print(seven(1603))
# print(seven(371))
# print(seven(483))
# print(seven(483595))


# ---#---#---#---# (Kata) Find the first non-consecutive number #---#---#---#---#
# test.assert_equals(first_non_consecutive([1,2,3,4,6,7,8]), 6)
# test.assert_equals(first_non_consecutive([1,2,3,4,5,6,7,8]), None)
# test.assert_equals(first_non_consecutive([4,6,7,8,9,11]), 6)
# test.assert_equals(first_non_consecutive([4,5,6,7,8,9,11]), 11)
# test.assert_equals(first_non_consecutive([31,32]), None)
# test.assert_equals(first_non_consecutive([-3,-2,0,1]), 0)
# test.assert_equals(first_non_consecutive([-5,-4,-3,-1]), -1)

def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if (arr[i] - arr[i - 1]) != 1:
            return arr[i]
    return None


# print(first_non_consecutive([1, 2, 3, 4, 6, 7, 8]))
# print(first_non_consecutive([-5, -4, -3, -1]))
# print(first_non_consecutive([31, 32]))

# ---#---#---#---# (Kata) Growth of a Population #---#---#---#---#
# test.assert_equals(nb_year(1500, 5, 100, 5000), 15)
# test.assert_equals(nb_year(1500000, 2.5, 10000, 2000000), 10)
# test.assert_equals(nb_year(1500000, 0.25, 1000, 2000000), 94)

def nb_year(p0, percent, aug, p, year=0):
    if p0 < p:
        p0 = int(p0 * (1 + percent / 100)) + aug
        year += 1
        return nb_year(p0, percent, aug, p, year)
    return year


# nb_year(1500, 5, 100, 5000)

# ---#---#---#---# (Kata) Error correction #1 - Hamming Code #---#---#---#---#
#     @test.it("Should work with short word")
#     def test_short_word():
#         test.assert_equals(encode("hey"), "000111111000111000000000000111111000000111000111000111111111111000000111")
#     @test.it("Should work with long word")
#     def test_long_word():
#         test.assert_equals(encode("The Sensei told me that i can do this kata"), "000111000111000111000000000111111000111000000000000111111000000111000111000000111000000000000000000111000111000000111111000111111000000111000111000111111000111111111000000111111111000000111111000111111000000111000111000111111000111000000111000000111000000000000000000111111111000111000000000111111000111111111111000111111000111111000000000111111000000111000000000000111000000000000000000111111000111111000111000111111000000111000111000000111000000000000000000111111111000111000000000111111000111000000000000111111000000000000111000111111111000111000000000000111000000000000000000111111000111000000111000000111000000000000000000111111000000000111111000111111000000000000111000111111000111111111000000000111000000000000000000111111000000111000000000111111000111111111111000000111000000000000000000111111111000111000000000111111000111000000000000111111000111000000111000111111111000000111111000000111000000000000000000111111000111000111111000111111000000000000111000111111111000111000000000111111000000000000111")
#     @test.it("Should work with numbers")
#     def test_short_word():
#         test.assert_equals(encode("T3st"), "000111000111000111000000000000111111000000111111000111111111000000111111000111111111000111000000")
#     @test.it("Should work with special characters")
#     def test_short_word():
#         test.assert_equals(encode("T?st!%"), "000111000111000111000000000000111111111111111111000111111111000000111111000111111111000111000000000000111000000000000111000000111000000111000111")
#     @test.it("Should work with short word")
#     def test_short_word():
#         test.assert_equals(decode("100111111000111001000010000111111000000111001111000111110110111000010111"), "hey")
#     @test.it("Should work with long word")
#     def test_long_word():
#         test.assert_equals(decode("000111000111000111000100000111111000111000001000000111111000010111000111000100111000000000000100000111000111000000111111000111111000000111000111000111111000111111111000000111111111000000111111000110111000000111000111000111111000111000000111000000111000000000000000000111111111000111000000000111111000111111111111000111111000111111000000000111111000000111000001000000111000000000001000000111111000111111000111000111111000000111000111000000111000000000000000000111111111000111000000000111111000111000000000000111111000000010000111000111111111000111000000000100111000000000000000000111111000111000000111000000111000000000000000000111111000000000111111000111111000000000000111000111111000111111111000000000111000000000000010000111111000000111000000000111111000111111110111000000111000000000000000000111111111000111000000000111111000111000000000000111111000111000000111000111111111000000111111000000111000000000000000000111111000111000111111000111111000000000000111000111111111000111000000000111111000000000000111"), "The Sensei told me that i can do this kata")
#     @test.it("Should work with numbers")
#     def test_short_word():
#         test.assert_equals(decode("000111000111000111000010000000111111000000111111000111111111000000111111000111111111000111010000"), "T3st")
#     @test.it("Should work with special characters")
#     def test_short_word():
#         test.assert_equals(decode("000111000111000111000001000000111111110111111111000111111111000000111111000111111111000111000000000000111000000000000111000000111000000111000111"), "T?st!%")

def encode(string):
    x3 = [f'{s2:08b}' for s2 in [ord(s) for s in string]]
    x4 = ''.join([''.join([a3 * 3 for a3 in f'{a2:08b}']) for a2 in [ord(a1) for a1 in string]])
    print(len(x4))
    return x3, x4


def decode(bits):
    x1 = [bits[i:i + 3] for i in range(0, len(bits), 3)]  # Split the input into groups of three characters;
    x2 = []
    for item in x1:  # Check error: replace each group with the character that occurs most often, e.g. 010 --> 0, 110 --> 1
        if item.count('1') > 1:
            x2.append('1')
            continue
        x2.append('0')
    x3 = ''.join([chr(int(''.join(x2[i:i + 8]), 2)) for i in range(0, len(x2), 8)])
    # return x1, x2, x3
    return x3


# print(encode('hey'))
# print(encode('?>='))
# print(decode("100111111000111001000010000111111000000111001111000111110110111000010111"))

# ---#---#---#---# (Kata) Game Hit the target #---#---#---#---#
# test.assert_equals(solution([
#   ['>', ' '],
#   [' ', 'x']
# ]), False)
#
# test.assert_equals(solution([
#   [' ', ' ', ' ', ' ', ' '],
#   [' ', ' ', ' ', ' ', ' '],
#   [' ', ' ', ' ', ' ', ' '],
#   [' ', ' ', '>', ' ', 'x'],
#   [' ', ' ', '', ' ', ' ']
# ]), True)

def solution(mtrx):
    for row in mtrx:
        try:
            # x1 = row.index('>')
            # x2 = row.index('x')
            if row.index('>') < row.index('x'):
                return True
            return False
        except ValueError:
            pass
    return False
    # print('ValueError')
    # x1= mtrx.index.index('>')
    # return x1


# def solution(mtrx):
#     for row in mtrx:
#         if ">" in row and "x" in row:
#             return row.index(">") < row.index("x")
#     return False

# print(solution([['>', ' '], [' ', 'x']]))
# solution([['>', ' '], [' ', 'x']])

# ---#---#---#---# (Kata) Find the nth Reverse Number (Extreme) #---#---#---#---#
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101 => First 20 Reverse Numbers
# test.assert_equals(find_reverse_number(1), 0)
# test.assert_equals(find_reverse_number(2), 1)
# test.assert_equals(find_reverse_number(10), 9)
# test.assert_equals(find_reverse_number(100), 909)
# test.assert_equals(find_reverse_number(100 000 000 000), 900000000000000000009)

def find_reverse_number_file(n):
    count = 1
    value = 0
    f = open('text.txt', 'w')
    while True:
        if str(value) == str(value)[::-1]:
            # print(count, value)
            f.write(str(count) + '\t' + str(value) + '\n')
            if count == n:
                f.close()
                return value
            count += 1
        value += 1


def find_reverse_number(n):
    if n < 11:
        return n - 1
    if 10 < int(str(n)[0:2]) < 20:
        return int(str(n)[1:] + str(n)[:0:-1])
    if str(n)[0:2] == '10':
        s = str(n)[2:]
        # print(s)
        k = str(s)[-2::-1]
        # print(k)
        return int('9' + str(n)[2:] + str(n)[2:][-2::-1] + '9')
    s = str(int(str(n)[0]) - 1)
    print(s)
    k = str(n)[1:]
    print(k)
    v = str(n)[1:][-2::-1]
    print(v)
    return int(str(int(str(n)[0]) - 1) + str(n)[1:] + str(n)[1:][-2::-1] + str(int(str(n)[0]) - 1))


# print(find_reverse_number(23104))
# print(find_reverse_number(106))
# print(find_reverse_number(1062))

# ---#---#---#---# (Kata) Get the mean of an array #---#---#---#---#
def get_average(marks):
    # return int(sum(marks)/len(marks))
    return sum(marks) / len(marks)


# print(get_average([2,5,13,20,16,16,10]))

# ---#---#---#---# (Kata) My head is at the wrong end! #---#---#---#---#
def fix_the_meerkat(arr):
    return arr[::-1]


# print(fix_the_meerkat(["head", "body", "tail"]))


# ---#---#---#---# (Kata) Invert values #---#---#---#---#
def invert(lst):
    return [0 - x for x in lst]


# print(invert([1, -2, 3, -4, 5]))


# ---#---#---#---# (Kata) L1: Bartender, drinks! #---#---#---#---#
def get_drink_by_profession(param):
    d = {'Jabroni': 'Patron Tequila', 'School Counselor': 'Anything with Alcohol',
         'Programmer': 'Hipster Craft Beer', 'Bike Gang Member': 'Moonshine',
         'Politician': 'Your tax dollars', 'Rapper': 'Cristal'}
    return d.get(param.title(), 'Beer')


# print(get_drink_by_profession("scHOOl counselor"))


# ---#---#---#---# (Kata) Gravity Flip #---#---#---#---#
# test.assert_equals(flip('R', [3, 2, 1, 2]), [1, 2, 2, 3])
# test.assert_equals(flip('L', [1, 4, 5, 3, 5]), [5, 5, 4, 3, 1])
def flip(d, a):
    return sorted(a) if d == 'R' else sorted(a, reverse=True)
    # return sorted(a, reverse=d=='L') # можно так


# print(flip('R', [3, 2, 1, 2]))
# print(flip('L', [1, 4, 5, 3, 5]))

# ---#---#---#---# (Kata) Calculate BMI #---#---#---#---#
# test.assert_equals(bmi(50, 1.80), "Underweight")
# test.assert_equals(bmi(80, 1.80), "Normal")
# test.assert_equals(bmi(90, 1.80), "Overweight")
# test.assert_equals(bmi(110, 1.80), "Obese")
# test.assert_equals(bmi(50, 1.50), "Normal")

def bmi(weight, height):
    mass_index = weight / height / height
    if mass_index <= 18.5:
        return 'Underweight'
    if mass_index <= 25:
        return 'Normal'
    if mass_index <= 30:
        return 'Overweight'
    return 'Obese'


# print(bmi(76, 1.75))

# ---#---#---#---# (Kata) Smallest unused ID #---#---#---#---#
# test.assert_equals(next_id([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 11)
# test.assert_equals(next_id([5, 4, 3, 2, 1]), 0)
# test.assert_equals(next_id([0, 1, 2, 3, 5]), 4)
# test.assert_equals(next_id([0, 0, 0, 0, 0, 0]), 1)
# test.assert_equals(next_id([]), 0)
# test.assert_equals(next_id([0, 0, 1, 1, 2, 2]), 3)
# test.assert_equals(next_id([0, 1, 1, 1, 3, 2]), 4)
# test.assert_equals(next_id([0, 1, 0, 2, 0, 3]), 4)
# test.assert_equals(next_id([9, 8, 0, 1, 7, 6]), 2)
# test.assert_equals(next_id([9, 8, 7, 6, 5, 4]), 0)

def next_id(arr):
    for i in range(len(arr)):
        if i not in arr:
            return i
    return len(arr)


def next_id_(arr):  # лучшая версия
    t = 0
    while t in arr:
        t += 1
    return t


# print(next_id([]))
# print(next_id([5, 4, 3, 2, 1]))

# ---#---#---#---# (Kata) Super Duper Easy #---#---#---#---#
# test.assert_equals(problem("hello"), "Error")
# test.assert_equals(problem(1), 56)

def problem(a):
    return 'Error' if isinstance(a, str) else a * 50 + 6


# print(problem("hello"))
# print(problem(1))
# print(problem(1.2))


# ---#---#---#---# (Kata) Beginner Series #1 School Paperwork #---#---#---#---#
# def paperwork(n, m):
#     return n * m if n > 0 and m > 0 else 0
#
#
paperwork = lambda a, b: a * b if min(a, b) > 0 else 0

# print(paperwork(5, 5))

# ---#---#---#---# (Kata) Are arrow functions odd? #---#---#---#---#
odds = lambda arr: [x for x in arr if x % 2 == 1]


# print(odds([]))
# print(odds([2, 4, 6]))
# print(odds([1, 3, 5]))
# print(odds([1, 2, 3, 4, 5, 6]))

# def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
#     return ((given_mass1 / molar_mass1 + given_mass2 / molar_mass2) * 0.082 * (273.15 + temp)) / volume


# solution = lambda x: x[::-1]

# print(solution('world')) # print 'dlrow'

# def get_age(age):
#     return age.split()[0]

# get_age = lambda x: int(x.split()[0])

# print(get_age("2 years old"))

def to_csv_text(array):
    result = ''
    for x in array:
        for y in x:
            result += str(y) + ','
        result = result[:-1] + '\n'
    result = result[:-1]

    return result


# print(to_csv_text([
#     [0, 1, 2, 3, 45],
#     [10, 11, 12, 13, 14],
#     [20, 21, 22, 23, 24],
#     [30, 31, 32, 33, 34]
# ])
#
# )


def uefa_euro_2016(teams, scores):
    if scores[0] > scores[1]:
        return 'At match {0} - {1}, {0} won!'.format(teams[0], teams[1])
    if scores[1] > scores[0]:
        return 'At match {0} - {1}, {1} won!'.format(teams[0], teams[1])
    return 'At match {0} - {1}, teams played draw.'.format(teams[0], teams[1])


# print(uefa_euro_2016(['Germany', 'Ukraine'], [2, 0]))  # "At match Germany - Ukraine, Germany won!"
# print(uefa_euro_2016(['Belgium', 'Italy'], [0, 2]))  # "At match Belgium - Italy, Italy won!"
# print(uefa_euro_2016(['Portugal', 'Iceland'], [1, 1]))  # "At match Portugal - Iceland, teams played draw."

def ensure_question(x):
    if len(x) == 0:
        return '?'
    if (x[-1] == '?'):
        return x
    return x + '?'


# def ensure_question(s):
#     return s.rstrip('?') + '?'

# print(ensure_question(""))
# print(ensure_question("Yes"))
# print(ensure_question("No?"))


# def arr(*args):
#     if args == ():
#         return []
#     return [x for x in range(0, args[0])]
#
# def arr(n=0):
#     return list(range(n))
#
#
# print(arr(4))
# print(arr(0))
# print(arr())


def sum_str(a, b):
    if a == "" and b == "":
        return '0'
    if a == "":
        return b
    if b == "":
        return a
    return str(int(a) + int(b))


# def sum_str(a, b):
#     return str(int(a or 0) + int(b or 0))

#     test.assert_equals(sum_str("4", "5"), "9")
#     test.assert_equals(sum_str("34", "5"), "39")
#
#
# @test.it("Tests with empty strings")
# def empty_string():
#     test.assert_equals(sum_str("9", ""), "9", "x + empty = x")
#     test.assert_equals(sum_str("", "9"), "9", "empty + x = x")
#     test.assert_equals(sum_str("", ""), "0", "empty + empty = 0") 0")


# to_binary = lambda n: int(f'{n:b}')
#
# test.assert_equals(to_binary(1), 1)
# test.assert_equals(to_binary(2), 10)
# test.assert_equals(to_binary(3), 11)
# test.assert_equals(to_binary(5), 101)


# def format_money(amount):
#     return '${:.2f}'.format(amount)

# format_money = lambda amount: '${:.2f}'.format(amount)

# print(format_money(39.99))

def enough(cap, on, wait):
    res = cap - (on + wait)
    tmp1 = res < 0
    return [0, abs(res)][tmp1]


# print(enough(19, 15, 5))


# 'МУХ'
def ascii(astanaev):
    for item in astanaev:
        print(ord(item))


# ascii('МУХ')
# ascii('MYX')


area_or_perimeter = lambda l, w: [2 * (l + w), l * w][l == w]


# print(area_or_perimeter(4, 4))
# print(area_or_perimeter(6, 10))

def parse_float(string):
    try:
        return float(string)
    except:
        return None


# print(parse_float('1.0'))
# print(parse_float('a'))
# print(parse_float('234.0234'))
# print(parse_float(
#     ['r', '7', '1', '1', 'r', 'a', 'p', 'z', '1', '5', '7', '8', 'q', 'x', 'v', 'k', 't', 'x', '2', 'g', '5', 'y', 'w',
#      'h', '1', 'w', 'b', '.', 'q', 'y', '1', 'a', 'q', '1', '7', 'd', 'o', '1', '3', '4', 's', 'n']))


def repeat_str(repeat, string):
    return string * repeat


# print(repeat_str(4, 'a'))
# print(repeat_str(3, 'hello '))


# rooms = {'One': {'name': 'name', 'description': 'description', 'completed': 'completed'},
#          'Two': {'name': 'name', 'description': 'description', 'completed': 'completed'},
#          'Three': {'name': 'name', 'description': 'description', 'completed': 'completed'}}

# print(rooms)

base = {'english': 'Welcome',
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso',
        'IP_ADDRESS_INVALID': 'Welcome',
        'IP_ADDRESS_NOT_FOUND': 'Welcome',
        'IP_ADDRESS_REQUIRED': 'Welcome'
        }


def greet(language):
    return base.get(language, 'Welcome')


class Ball(object):
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type


# print(Ball().ball_type)
# print(Ball("super").ball_type)

# detect = lambda x: not x.find('Can someone explain', 0, 19)
detect = lambda x: x[:19] == 'Can someone explain'


# print(detect("Can someone explain to me what this kata is about?"))
# print(detect("Can someone solve this kata for me?"))
# print(detect("can someone explain how the ranking works?"))
# print(detect("I wonder when Can someone explain how the ranking works?"))

def get_planet_name(id):
    return {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune"
    }[id]


# print(get_planet_name(2))

# рекурсия ниже

def subtract_sum(number):
    fruit = {
        1: 'kiwi',
        2: 'pear',
        3: 'kiwi',
        4: 'banana',
        5: 'melon',
        6: 'banana',
        7: 'melon',
        8: 'pineapple',
        9: 'apple',
        10: 'pineapple',
        11: 'cucumber',
        12: 'pineapple',
        13: 'cucumber',
        14: 'orange',
        15: 'grape',
        16: 'orange',
        17: 'grape',
        18: 'apple',
        19: 'grape',
        20: 'cherry',
        21: 'pear',
        22: 'cherry',
        23: 'pear',
        24: 'kiwi',
        25: 'banana',
        26: 'kiwi',
        27: 'apple',
        28: 'melon',
        29: 'banana',
        30: 'melon',
        31: 'pineapple',
        32: 'melon',
        33: 'pineapple',
        34: 'cucumber',
        35: 'orange',
        36: 'apple',
        37: 'orange',
        38: 'grape',
        39: 'orange',
        40: 'grape',
        41: 'cherry',
        42: 'pear',
        43: 'cherry',
        44: 'pear',
        45: 'apple',
        46: 'pear',
        47: 'kiwi',
        48: 'banana',
        49: 'kiwi',
        50: 'banana',
        51: 'melon',
        52: 'pineapple',
        53: 'melon',
        54: 'apple',
        55: 'cucumber',
        56: 'pineapple',
        57: 'cucumber',
        58: 'orange',
        59: 'cucumber',
        60: 'orange',
        61: 'grape',
        62: 'cherry',
        63: 'apple',
        64: 'cherry',
        65: 'pear',
        66: 'cherry',
        67: 'pear',
        68: 'kiwi',
        69: 'pear',
        70: 'kiwi',
        71: 'banana',
        72: 'apple',
        73: 'banana',
        74: 'melon',
        75: 'pineapple',
        76: 'melon',
        77: 'pineapple',
        78: 'cucumber',
        79: 'pineapple',
        80: 'cucumber',
        81: 'apple',
        82: 'grape',
        83: 'orange',
        84: 'grape',
        85: 'cherry',
        86: 'grape',
        87: 'cherry',
        88: 'pear',
        89: 'cherry',
        90: 'apple',
        91: 'kiwi',
        92: 'banana',
        93: 'kiwi',
        94: 'banana',
        95: 'melon',
        96: 'banana',
        97: 'melon',
        98: 'pineapple',
        99: 'apple',
        100: 'pineapple'
    }
    number -= sum([int(x) for x in str(number)])
    return fruit[number] if number < 101 else subtract_sum(number)


# print(subtract_sum(10))


def expression_matter(a, b, c):
    return max([a + b + c, a * b + c, a * (b + c), a + b * c, (a + b) * c, a * b * c])


# print(expression_matter(2, 1, 2))
# print(expression_matter(3, 5, 7))
# print(expression_matter(2, 10, 3))


def points(games):
    score = 0
    for item in games:
        if item[0] == item[2]:
            score += 1
            continue
        if item[0] > item[2]:
            score += 3
    return score


def abbrev_name(name):
    return name.split()[0][0] + '.' + name.split()[1][0]


# print(abbrev_name("Patrick Feenan"))

# поиск элемента в списке
def check(seq, elem):
    return elem in seq


# def what_is(x):
#     if x is 42:
#         return 'everything'
#     elif x == 42 * 42:
#         return 'everything squared'
#     else:
#         return 'nothing'


# print(what_is(42 * 42))


def to_alternating_case(string):
    x = []
    for char in string:
        if char.isupper():
            x.append(char.lower())
        elif char.islower():
            x.append(char.upper())
        else:
            x.append(char)
    return ''.join(x)


# print(to_alternating_case('hello world'))
# print(to_alternating_case("HELLO WORLD"))
# print(to_alternating_case("1a2b3c4d5e"))


def array_madness(a, b):
    return sum([x ** 2 for x in a]) > sum([x ** 3 for x in b])


#
# def correct_polish_letters(st):
#     letters = {
#         'ą': 'a',
#         'ć': 'c',
#         'ę': 'e',
#         'ł': 'l',
#         'ń': 'n',
#         'ó': 'o',
#         'ś': 's',
#         'ź': 'z',
#         'ż': 'z'
#     }
#     # перебор словаря dict
#     for key in letters:
#         st = st.replace(key, letters[key])
#     return st
#

# групповая замена нескольких символов в строке
def correct_polish_letters(s):
    x = str.maketrans("ąćęłńóśźż", "acelnoszz")
    return s.translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))


def replace_exclamation(s):
    return s.translate(str.maketrans("aeiouAEIOU", "!" * 10))


def replace_exclamation(s):
    return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)


# удаление нескольких символов в строке
def shortcut(s):
    return ''.join('' if c in 'aeiou' else c for c in s)
    return ''.join(c for c in s if c not in 'aeiou')
    return s.translate(None, 'aeiou')


# correct_polish_letters('Jędrzej Błądziński')


def difference_in_ages(ages):
    return min(ages), max(ages), max(ages) - min(ages)


# print(difference_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88]))  # (3, 88, 85)


def find_longest(string):
    spl = string.split(' ')
    longest = 0
    for i in range(len(spl)):
        if len(spl[i]) > longest:
            longest = len(spl[i])
    return longest


# print(find_longest("The quick white fox jumped around the massive dog"))

# множества set
def merge_arrays(arr1, arr2):
    x = set(arr1) | set(arr2)  # объединенение множеств https://realpython.com/python-sets/
    return sorted(list(x))


# print(merge_arrays([1, 3, 5, 7, 9], [10, 8, 6, 4, 2]))
# print(merge_arrays([1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12]))

# вернуть инверсное число
def opposite(number):
    return -number


# Simple Fun #352: Reagent Formula
def isValid(formula):
    condition = [not (1 in formula and 2 in formula), not (3 in formula and 4 in formula),
                 not ((5 in formula) ^ (6 in formula)), 7 in formula or 8 in formula]
    return not False in condition


# print(isValid([1, 3, 7]))  # True
# print(isValid([1, 2, 7]))  # False
# print(isValid([6, 7, 8]))


def getVolumeOfCubiod(*a):
    return prod(a)


# print(getVolumeOfCubiod(1, 2, 2))

# Convert number to reversed array of digits
# Преобразовать число в массив цифр и перевернуть
def digitize(n):
    return [int(str(n)[x]) for x in range(len(str(n)))][::-1]
    return map(int, str(n)[::-1])
    return [int(x) for x in str(n)[::-1]]
    return [int(x) for x in reversed(str(n))]


# print(digitize(548702838394))

# noobCode 01: SUPERSIZE ME.... or rather, this integer!
def super_size(n):
    return int(''.join(sorted(str(n), reverse=True)))


# print(super_size(608719))  # 987610

# Remove First and Last Character - удалить первый и последний символ из строки
def remove_char(s):
    return s[1: -1]


# print(remove_char('eloquent'))  # 'loquen'


class Solution:
    def main(*args):
        print('Hello World!')


# Solution.main('23')

# Find numbers which are divisible by given number
def divisible_by(numbers, divisor):
    return [x for x in numbers if x % divisor == 0]


# test.assert_equals(divisible_by([1,2,3,4,5,6], 2), [2,4,6])
# test.assert_equals(divisible_by([1,2,3,4,5,6], 3), [3,6])
# test.assert_equals(divisible_by([0,1,2,3,4,5,6], 4), [0,4])
# test.assert_equals(divisible_by([0], 4), [0])
# test.assert_equals(divisible_by([1,3,5], 2), [])
# test.assert_equals(divisible_by([0,1,2,3,4,5,6,7,8,9,10], 1), [0,1,2,3,4,5,6,7,8,9,10])

# What is between?
def between(a, b):
    return list(range(a, b + 1))


# print(between(1, 4))


# Tip Calculator
def calculate_tip(amount, rating):
    if rating.title() == 'Terrible':
        return 0
    if rating.title() == 'Poor':
        return ceil(amount * 0.05)
    if rating.title() == 'Good':
        return ceil(amount * 0.1)
    if rating.title() == 'Great':
        return ceil(amount * 0.15)
    if rating.title() == 'Excellent':
        return ceil(amount * 0.2)
    return 'Rating not recognised'


# Еще вариант исполнения
def calculate_tip(amount, rating):
    tips = {
        'terrible': 0,
        'poor': .05,
        'good': .1,
        'great': .15,
        'excellent': .2
    }
    if rating.lower() in tips:
        return ceil(amount * tips[rating.lower()])
    else:
        return 'Rating not recognised'


# Draw stairs
def draw_stairs(n):
    x = ''
    for i in range(n):
        x += ' ' * i + 'I\n'
    return x[:-1]


def draw_stairs(n):
    return '\n'.join(' ' * i + 'I' for i in range(n))


# Well of Ideas - Easy Version
def well(x):
    if x.count('good') > 2:
        return 'I smell a series!'
    if x.count('good') > 0:
        return 'Publish!'
    return 'Fail!'


# The 'if' function
def _if(bool, func1, func2):
    return func1() if bool else func2()


def is_digit(n):
    return n.isdigit() and len(n) < 2


# print(is_digit("14"))

# Sort and Star
def two_sort(array):
    return '***'.join(sorted(array)[0])


# print(two_sort(
#     ["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))  # 'b***i***t***c***o***i***n'


def merge_arrays(first, second):
    return sorted(set(first) | set(second))


# print(merge_arrays([2, 4, 8], [2, 4, 6]))


def how_much_i_love_you(nb_petals):
    phrases = [
        'I love you',
        'a little',
        'a lot',
        'passionately',
        'madly',
        'not at all'
    ]
    return phrases[nb_petals % 6 - 1]


# print(how_much_i_love_you(6))

# Multiple of index
def multiple_of_index(arr):
    return [arr[i] for i in range(1, len(arr)) if arr[i] % i == 0]


# Simple validation of a username with regex
# Write a simple regex to validate a username. Allowed characters are:
# lowercase letters,
# numbers,
# underscore
# Length should be between 4 and 16 characters (both included).
# https://tproger.ru/translations/regular-expression-python/
# https://docs.python.org/3/library/re.html#regular-expression-syntax
def validate_usr(username):
    return re.match('^[a-z0-9_]{4,16}$', username) is not None
    # reg = re.match(r'[0-9a-z_]{4,16}', username)
    # return False if reg is None else username == reg.group()
    # if x is None:
    #     return False
    # return username == x.group()
    # return x.group(), username == x.group()
    # return username == re.match(r'[0-9a-z_]{4,16}', username).group()


# print(validate_usr('a'))
# print(validate_usr('asddsa'))

# Find the Integral
# Использую F-строки
def integrate(coefficient, exponent):
    return f'{int(coefficient / (exponent + 1))}x^{exponent + 1}'


# Swap Values
def swap_values(arr):
    arr[:] = arr[::-1]
    return arr


# arr = [1, 2]
# swap_values(arr)
# swap_values(arr)

def get_size(w, h, d):
    return [2 * (w * (h + d) + h * d), w * h * d]


# print(get_size(4, 2, 6))


# поиск любой подстроки в строке
def is_lock_ness_monster(s):
    return any(i in s for i in ('tree fiddy', 'three fifty', '3.50'))


def correct(s):
    return s.translate(str.maketrans("501", "SOI"))


def count_positives_sum_negatives(arr):
    if not arr:
        return []
    x = [0, 0]
    for i in arr:
        if i > 0:
            x[0] += 1
        if i < 0:
            x[1] += i
    return x


# print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))


# использование максимума max
def combat(health, damage):
    return max(0, health - damage)


# Closest elevator
def elevator(left, right, call):
    return ['left', 'right'][abs(right - call) <= abs(left - call)]


# выбор из словаря
def basic_op(operator, value1, value2):
    return {
        '+': value1 + value2,
        '-': value1 - value2,
        '*': value1 * value2,
        '/': value1 / value2
    }[operator]


# eval
def basic_op_v1(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))


def simple_multiplication(number):
    return [number * 8, number * 9][number % 2]


def count_by(x, n):
    return [i * x for i in range(1, n + 1)]


# print(count_by(1, 5))
# print(count_by(2, 5))

# последвательное применение функции к элементам массива
from functools import reduce

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])


# print(product)


def logical_calc(array, op):
    return {
        'AND': reduce((lambda x, y: x and y), array),
        'OR': reduce((lambda x, y: x or y), array),
        'XOR': reduce((lambda x, y: x ^ y), array)
    }[op]


def odd_count(n):
    return (n - 1) / 2 if n % 2 else n / 2


# метод групоовой замены элементов списка
def is_vow(inp):
    dic = {
        ord('a'): 'a',
        ord('e'): 'e',
        ord('i'): 'i',
        ord('o'): 'o',
        ord('u'): 'u'
    }
    return [dic[i] if i in dic else i for i in inp]


# print(is_vow(['a', 'e', 'i', 'o', 'u', 97]))  # [97, 101, 105, 111, 117]

# строку двочичную в число десятичное
def bin_to_decimal(inp):
    return int(inp, 2)


def stairs_in_20(stairs):
    x = [[6737, 7244, 5776, 9826, 7057, 9247, 5842, 5484, 6543, 5153, 6832, 8274, 7148, 6152, 5940, 8040, 9174, 7555,
          7682, 5252, 8793, 8837, 7320, 8478, 6063, 5751, 9716, 5085, 7315, 7859, 6628, 5425, 6331, 7097, 6249, 8381,
          5936, 8496, 6934, 8347, 7036, 6421, 6510, 5821, 8602, 5312, 7836, 8032, 9871, 5990, 6309, 7825],
         [9175, 7883, 7596, 8635, 9274, 9675, 5603, 6863, 6442, 9500, 7468, 9719, 6648, 8180, 7944, 5190, 6209, 7175,
          5984, 9737, 5548, 6803, 9254, 5932, 7360, 9221, 5702, 5252, 7041, 7287, 5185, 9139, 7187, 8855, 9310, 9105,
          9769, 9679, 7842, 7466, 7321, 6785, 8770, 8108, 7985, 5186, 9021, 9098, 6099, 5828, 7217, 9387],
         [8646, 6945, 6364, 9563, 5627, 5068, 9157, 9439, 5681, 8674, 6379, 8292, 7552, 5370, 7579, 9851, 8520, 5881,
          7138, 7890, 6016, 5630, 5985, 9758, 8415, 7313, 7761, 9853, 7937, 9268, 7888, 6589, 9366, 9867, 5093, 6684,
          8793, 8116, 8493, 5265, 5815, 7191, 9515, 7825, 9508, 6878, 7180, 8756, 5717, 7555, 9447, 7703],
         [6353, 9605, 5464, 9752, 9915, 7446, 9419, 6520, 7438, 6512, 7102, 5047, 6601, 8303, 9118, 5093, 8463, 7116,
          7378, 9738, 9998, 7125, 6445, 6031, 8710, 5182, 9142, 9415, 9710, 7342, 9425, 7927, 9030, 7742, 8394, 9652,
          5783, 7698, 9492, 6973, 6531, 7698, 8994, 8058, 6406, 5738, 7500, 8357, 7378, 9598, 5405, 9493],
         [6149, 6439, 9899, 5897, 8589, 7627, 6348, 9625, 9490, 5502, 5723, 8197, 9866, 6609, 6308, 7163, 9726, 7222,
          7549, 6203, 5876, 8836, 6442, 6752, 8695, 8402, 9638, 9925, 5508, 8636, 5226, 9941, 8936, 5047, 6445, 8063,
          6083, 7383, 7548, 5066, 7107, 6911, 9302, 5202, 7487, 5593, 8620, 8858, 5360, 6638, 8012, 8701],
         [5000, 5642, 9143, 7731, 8477, 8000, 7411, 8813, 8288, 5637, 6244, 6589, 6362, 6200, 6781, 8371, 7082, 5348,
          8842, 9513, 5896, 6628, 8164, 8473, 5663, 9501, 9177, 8384, 8229, 8781, 9160, 6955, 9407, 7443, 8934, 8072,
          8942, 6859, 5617, 5078, 8910, 6732, 9848, 8951, 9407, 6699, 9842, 7455, 8720, 5725, 6960, 5127],
         [5448, 8041, 6573, 8104, 6208, 5912, 7927, 8909, 7000, 5059, 6412, 6354, 8943, 5460, 9979, 5379, 8501, 6831,
          7022, 7575, 5828, 5354, 5115, 9625, 7795, 7003, 5524, 9870, 6591, 8616, 5163, 6656, 8150, 8826, 6875, 5242,
          9585, 9649, 9838, 7150, 6567, 8524, 7613, 7809, 5562, 7799, 7179, 5184, 7960, 9455, 5633, 9085]]
    summ = 0
    for i in x:
        for y in i:
            summ += y
    return summ * 20
    #     print(sum(sum(stairs)))
    # проход по вложенному массиву
    # return 20 * sum(map(sum, stairs))


# stairs_in_20('0')


def nearest_sq(n):
    # return int(math.sqrt(n) + 1) ** 2 if abs(math.sqrt(n) - int(math.sqrt(n))) > 0.5 else int(math.sqrt(n)) ** 2
    return round(n ** 0.5) ** 2


# for i in range(1, 150):
#     print(nearest_sq(i))


def cube_checker(volume, side):
    return (side ** 3 == volume) and (volume or side) > 0


# Count the number of cubes with paint on
def count_squares(x):
    res = 2 * (3 * x ** 2 + 1)
    return res  # an integer number


# удаление определенного числа символов слева направо
def remove(s, n):
    return s.replace("!", "", n)


# Find the force of gravity between two objects
def solution(arr_val, arr_unit):
    # массу в килограммы, расстояние в метры
    dic = {
        'kg': 1,
        'g': 1e-3,
        'mg': 1e-6,
        'μg': 1e-9,
        'lb': 0.453592,
        'm': 1,
        'cm': 1e-2,
        'mm': 1e-3,
        'μm': 1e-6,
        'ft': 0.3048
    }
    G = 6.67e-11  # gravitational constant  G = 6.67 x 10-11N.kg–2.m2
    m1 = arr_val[0] * dic[arr_unit[0]]
    m2 = arr_val[1] * dic[arr_unit[1]]
    r = arr_val[2] * dic[arr_unit[2]]
    F = G * m1 * m2 / r ** 2
    return F


# units = {"kg": 1, "g": 1e-3, "mg": 1e-6, "μg": 1e-9, "lb": 0.453592,
#          "m": 1, "cm": 1e-2, "mm": 1e-3, "μm": 1e-6, "ft": 0.3048,
#          "G": 6.67e-11}
#
# def solution(v, u):
#     m1, m2, r = (v[i] * units[u[i]] for i in range(3))
#     return units["G"] * m1 * m2 / r**2

def next_item(xs, item):
    it = iter(xs)
    for x in it:
        if x == item:
            break
    return next(it, None)


# print(next_item(iter(range(1, 30000)), 12))


def whatday(num):
    return {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
    }[num] if 0 < num < 8 else "Wrong, please enter a number between 1 and 7"


def whatday_1(n):
    WEEKDAY = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'}
    ERROR = 'Wrong, please enter a number between 1 and 7'
    return WEEKDAY.get(n, ERROR)


# SWAPCASE строки
def is_opposite(s1, s2):
    return s1 == s2.swapcase() and len(s1) > 0


# Remove duplicates from list
def distinct(seq):
    return list(dict.fromkeys(seq))


def sum_mul(n, m):
    return sum([x for x in range(1, m) if x % n == 0]) if m * n > 0 else 'INVALID'


# def human_years_cat_years_dog_years(h):
#     if h == 1:
#         return [h, 15, 15]
#     elif h == 2:
#         return [h, 24, 24]
#     else:
#         return [h, 24 + 4 * (h - 2), 24 + 5 * (h - 2)]

# логическое выражение используется как математическое
def human_years_cat_years_dog_years(n):
    tmp = n > 1
    tmp = 9 * (n > 1)
    cat_years = 15 + (9 * (n > 1)) + (4 * (n - 2) * (n > 2))
    dog_years = 15 + (9 * (n > 1)) + (5 * (n - 2) * (n > 2))
    return [n, cat_years, dog_years]


# human_years_cat_years_dog_years(1)
# human_years_cat_years_dog_years(2)
# human_years_cat_years_dog_years(3)
# human_years_cat_years_dog_years(4)


def string_clean(s):
    return ''.join([x for x in s if not x.isdigit()])


websites = ['codewars' for _ in range(1000)]

stock = {
    'football': 4,
    'boardgame': 10,
    'leggos': 1,
    'doll': 5,
}


def fillable(stock, merch, n):
    return stock.get(merch, 0) >= n


def cannons_ready(gunners):
    return 'Shiver me timbers!' if 'nay' in gunners.values() else 'Fire!'


def sale_hotdogs(n):
    return [n * 100, n * 95, n * 90][1 * (n < 5) - 1 or 2 * (5 <= n < 10) - 1 or 3 * (n >= 10) - 1]


def remove(s):
    return s[0:len(s) - 1] if s[-1] == '!' else s


# print(remove('Hi!'))

def list_animals(animals):
    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list


# print(list_animals([ 'dog', 'cat', 'elephant' ]))

def calculator(x, y, op):
    return {
        '+': x + y,
        '-': x - y,
        '*': x * y,
        '/': x / y
    }.get(op, 'unknown value')


# рекурсия ниже
# def hotpo(n, count=0):
#     if n == 1:
#         return count
#     count += 1
#     return hotpo(n / 2, count) if n % 2 == 0 else hotpo(3 * n + 1, count)

def hotpo(num, count=0):
    return count if num == 1 else hotpo(num / 2 if num % 2 == 0 else num * 3 + 1, count + 1)


# print(hotpo(23))


def symmetric_point(p, q):
    if q[0] > p[0]:
        x = 2 * q[0] - p[0]
    else:
        x = 2 * q[0] - p[0]
    if q[1] > p[1]:
        y = 2 * q[1] - p[1]
    else:
        y = 2 * q[1] - p[1]
    return [x, y]


# print(symmetric_point([2, 6], [-2, -6]))  # [-6, -18]

# def add_length(str_):
#     return list(map(lambda x: x + ' ' + str(len(x)), str_.split()))

def add_length(str_):
    return ["{} {}".format(i, len(i)) for i in str_.split(' ')]


def char_freq(message):
    dic = dict()
    for i in message:
        dic.update({i: message.count(i)})
    return dic


# test.assert_equals(char_freq("I like cats"), {'a': 1, ' ': 2, 'c': 1, 'e': 1, 'I': 1, 'k': 1, 'l': 1, 'i': 1, 's': 1, 't': 1})
# print(char_freq('I like cats'))


def rps(p1, p2):
    # scissors paper rock
    context = [0, p1, p2]
    if p1 == p2:
        return 'Draw!'
    if 'scissors' not in context:
        return f'Player {context.index("paper")} won!'
    if 'paper' not in context:
        return f'Player {context.index("rock")} won!'
    if 'rock' not in context:
        return f'Player {context.index("scissors")} won!'


# print(rps('scissors', 'paper'))


def multiply(n):
    return n * 5 ** len(str(abs(n)))


def evil(n):
    return "It's Evil!" if bin(n).count('1') % 2 == 0 else "It's Odious!"


def evil(n):
    return "It's %s!" % ["Evil", "Odious"][bin(n).count("1") % 2]


# for i in [3, 5, 6, 9, 10, 12, 15, 17, 18, 20]:
#     print(evil(i))
#
# for i in [1, 2, 4, 7, 8, 11, 13, 14, 16, 19]:
#     print(evil(i))

def add_extra(list_of_numbers):
    # list_of_numbers1 = list_of_numbers[:]
    # list_of_numbers1 = list_of_numbers + [4]
    return list_of_numbers + [4]


# x = len(add_extra([1,2]))
# print(x)


def remove_(s):
    # return ord(s[-1])
    return remove_(s[:-1]) if ord(s[-1]) == 33 else s


# print(remove_('cdcd!!!!'))


def whoseMove(lastPlayer, win):
    if lastPlayer == 'black' and win:
        return 'black'
    if lastPlayer == 'black' and not win:
        return 'white'
    if lastPlayer == 'white' and win:
        return 'white'
    if lastPlayer == 'white' and not win:
        return 'black'


# if else в генераторе списка
def square_or_square_root(arr):
    result = []
    for item in arr:
        if int(item ** 0.5) ** 2 == item:
            result.append(int(item ** 0.5))
        else:
            result.append(item ** 2)
    x = [int(x ** 0.5) if int(x ** 0.5) ** 2 == x else x ** 2 for x in arr]
    return result, x


def sum_array(arr):
    if arr is None or len(arr) < 3:
        return 0
    return sum(arr) - min(arr) - max(arr)


def my_first_kata(a, b):
    print(a, b)
    try:
        a = int(str(a))
        b = int(str(b))
        x = a % b
        y = b % a
        return a % b + b % a
    except:
        return False
    return False


# print(my_first_kata(838, 823))


def close_compare(a, b, margin=0):
    return 0 if abs(a - b) <= margin else -1 if b > a else 1


# print(close_compare(8.1, 5, 3))  # 1
# print(close_compare(1.99, 5, 3))  # -1
# print(close_compare(4853, 1326, 5374))  # -1


def validate_code(code):
    return re.match('^[123]', str(code)) is not None


def validate_hello(greetings):
    return any(i in greetings.lower() for i in ('hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc'))


def two_highest(arg1):
    arg1 = sorted(list(set(arg1)))
    if len(arg1) > 1:
        return [arg1[-1], arg1[-2]]
    else:
        return arg1


def mango(quantity, price):
    print(quantity, price)
    x = quantity // 3
    y = quantity % 3
    return price * ((quantity // 3) * 2 + (quantity % 3))


# print(mango(934, 353))  # 219919


def fuel_price(litres, ppl):
    if litres >= 10:
        return litres * (ppl - 0.25)
    if litres >= 8:
        return litres * (ppl - 0.2)
    if litres >= 6:
        return litres * (ppl - 0.15)
    if litres >= 4:
        return litres * (ppl - 0.1)
    if litres >= 2:
        return litres * (ppl - 0.05)
    return litres * ppl


def year_days(year):
    return f'{year} has 366 days' if (year % 4 == 0 and year % 100 != 0) or (
            year % 100 == 0 and year % 400 == 0) else f'{year} has 365 days'


def period_is_late(last, today, cycle_length):
    return datetime.timedelta(cycle_length) < today - last


# period_is_late(datetime.datetime(2016, 6, 13), datetime.datetime(2016, 7, 16), 35)

def bar_triang(pointA, pointB, pointC):
    return [round((pointA[0] + pointB[0] + pointC[0]) / 3, 4), round((pointA[1] + pointB[1] + pointC[1]) / 3, 4)]


def billboard(name, price=30, result=0):
    for i in range(len(name)):
        result += price
    return result


# print(billboard("Jeong-Ho Aristotelis"))

# import urllib
# from urllib.parse import urlparse
#
# def generate_link(user):
#     return f'http://www.codewars.com/users/{urllib.parse.quote(user)}'
#
#
# print(generate_link('matt c'))

def lowercase_count(strng):
    result = re.findall('[a-z]', strng)
    print(result)
    return len(re.findall('[a-z]', strng))


def eval_object(v):
    x = v['a']
    y = v['b']
    return {"+": v['a'] + v['b'],
            "-": v['a'] - v['b'],
            "/": v['a'] / v['b'],
            "*": v['a'] * v['b'],
            "%": v['a'] % v['b'],
            "**": v['a'] ** v['b']}.get(v['operation'], 1)


# print(eval_object({'a': 3, 'b': 1, 'operation': "+"}))


def each_cons(lst, n):
    result = []
    for i in range(len(lst) - n + 1):
        result.append(lst[i:i + n])
    return result
    # return [lst[i:i+n] for i in range(len(lst) - n + 1)]


def array_of_tiers(data):
    result = [data]
    while data > 9:
        data //= 10
        result.append(data)
    return result[::-1]


# Пример:
# array_of_tiers(420) ==> [4, 42, 420]
# array_of_tiers(2021) ==> [2, 20, 202, 2021]
# array_of_tiers(80200) == [8, 80, 802, 8020, 80200]

# print(array_of_tiers(420))
# print(array_of_tiers(2021))
# print(array_of_tiers(80200))


def min_max_rotate():
    result = input("Введите массив: ")
    return result.split()


# print(min_max_rotate())


def circle_diameter(sides, side_length):
    alpha = 360 / sides / 2
    a = side_length / 2
    x = tan(alpha * pi / 180)
    result = a / x * 2
    return round(result, 3)


# circle_diameter = lambda sides, side_length: round(side_length / tan((180 / sides) * pi / 180), 3)

# def circle_diameter(sides, side_length):
#     alpha = 360 / sides / 2
#     a = side_length / 2
#     n = 2  # Accuracy calculation tan(alpha) Must be no less 4 for tests passed
#     tan_x = circle_diameter_sin(alpha, n) / circle_diameter_cos(alpha, n)
#     result = a / tan_x * 2
#     return round(result, 3)
#
#
# def circle_diameter_sin(angle, n):  # 0.3826834324 for 22.5
#     x = angle * 3.14159265358979323846 / 180  # Angle in radians
#     result = 0
#     for n in range(0, n):
#         result += ((-1) ** n * x ** (2 * n + 1)) / circle_diameter_factorial(2 * n + 1)
#     return result
#
#
# def circle_diameter_cos(angle, n):  # 0.9238795325 for 22.5
#     x = angle * 3.14159265358979323846 / 180  # Angle in radians
#     result = 0
#     for n in range(0, n):
#         result += ((-1) ** n * x ** (2 * n)) / circle_diameter_factorial(2 * n)
#     return result
#
#
# def circle_diameter_factorial(n):
#     if n == 0:
#         return 1
#     return circle_diameter_factorial(n - 1) * n


print(circle_diameter(8, 9))


