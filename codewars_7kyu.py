import re


def tap_code_translation(text):
    dots = []
    for c in text:
        if c in "abcdefghij":
            x = ord(c) - 97
        elif c == 'k':
            x = ord(c) - 105
        else:
            x = ord(c) - 98
        y = x // 5
        z = x % 5
        # print(c + ': ', x, y+1, z+1)
        dots.append('.' * (x // 5 + 1) + ' ' + '.' * (x % 5 + 1))
    return ' '.join(dots)


# tap_code_translation("abcdefghijklmnopqrstuvwxyz")
# print(tap_code_translation("breaks"))  # . .. .... .. . ..... . . . ... .... ...


def count_salutes(hallway):
    count = 0
    data = hallway[:]
    while data.find('>') != -1:
        right = data.find('>')
        count += data.count('<', right)
        data = data[right + 1:]
    print(count * 2)


# count_salutes('>>>>>>>>>>>>>>>>>>>>>----<->')


def filter_long_words(sentence, long):
    return [word for word in sentence.split() if len(word) > long]


# def calc(x):
#     total1 = ''.join(list(map(str, map(ord, x))))
#     total2 = total1.replace('7', '1')
#     result = sum([int(x) for x in total1]) - sum([int(x) for x in total2])
#     return total1, total2, result


def calc(x):
    return ''.join(list(map(str, map(ord, x)))).count('7') * 6


# print(calc('abcdef'))


def divisions(n, divisor, count=0):
    n = n // divisor
    return divisions(n, divisor, count=count + 1) if n else count


# print(divisions(6, 2))


def buy(x, arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == x and i != j:
                return [i, j]
    return None


# print(buy(5, [1, 2, 3, 4, 5]))  # [0, 3]


def reverse_number(n):
    return int(str(n)[::-1]) if n >= 0 else int('-' + str(n)[:0:-1])


# print(reverse_number(-12423))


def reverse_letter(string):
    result = re.sub('[^a-zA-Z]', '', string)[::-1]
    return result


# print(reverse_letter("ultr53o?n"))  # "nortlu"

from math import ceil


def new_avg(arr, newavg):
    if ceil(newavg * (len(arr) + 1) - sum(arr)) > 0:
        return ceil(newavg * (len(arr) + 1) - sum(arr))
    else:
        raise Exception('Error expected')


# The vowels "eiou" are disallowed as are the slash "/", asterisk "*", and period "." characters.
def davasaan(x, c=0):
    return davasaan(x=x - 10, c=c + 1) if x > 9 else c


# print(davasaan(11))

def is_narcissistic(i):
    res = sum(map(lambda x: int(x) ** len(str(i)), str(i)))
    return sum(map(lambda x: int(x) ** len(str(i)), str(i))) == i


# is_narcissistic(153)

def pyramid(balls, lvl=0):
    balls -= lvl + 1
    if balls >= 0:
        lvl += 1
        return pyramid(balls, lvl)
    else:
        return lvl


# print(pyramid(6))


def word_to_bin(word):
    return [f'{ord(x):08b}' for x in word]


# print(word_to_bin('man'))
list1 = [{'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19,
          'language': 'JavaScript'},
         {'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28,
          'language': 'JavaScript'},
         {'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35,
          'language': 'HTML'},
         {'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30,
          'language': 'CSS'}]


def count_developers(lst):
    count = 0
    for item in lst:
        if item['language'] == 'JavaScript' and item['continent'] == 'Europe':
            count += 1
    return count
    # return sum(x["language"] == "JavaScript" and x["continent"] == "Europe" for x in lst)


# print(count_developers(list1))


# Evens times last
def even_last(numbers):
    return sum(numbers[::2]) * numbers[-1] if numbers != [] else 0


# print(even_last([-38, 64, -17, 11, 83, 84, 69, 64, -47, -35]))  # -1750

num_grid = [[1, 2, 3, 4], [5, 6, 7, 8, 9], [0, 2, 4]]
char_grid = [['h', 'E', 'l', 'l', 'O'], ['w', 'O', 'r', 'L', 'd']]


def grid_map(inp, op):
    return exec(op(inp))


# print(grid_map(char_grid, lambda x: x.upper()))

# Назовем строку классной, если она образована только латинскими буквами и нет двух строчных
# и двух прописных букв на соседних позициях. Учитывая строку, проверьте, классная ли она.
# match - Этот метод ищет по заданному шаблону в начале строки!!!!!!!!!!!!!!!!!!
# по этому используем search
def cool_string(s):
    # x = re.match('[^a-zA-Z]|[a-z]{2}|[A-Z]{2}', s)
    # x = re.match('[a-z]{2}', s)
    return re.search('[^a-zA-Z]|[a-z]{2}|[A-Z]{2}', s) is None


# print(cool_string("lBC"))


# Given 2 strings, a and b, return a string of the form: shorter+reverse(longer)+shorter.
# In other words, the shortest string has to be put as prefix and as suffix of the reverse of the longest.
# Strings a and b may be empty, but not null (In C# strings may also be null. Treat them as if they are empty.).
# If a and b have the same length treat a as the longer producing b+reverse(a)+b

def shorter_reverse_longer(a, b):
    return b + a[::-1] + b if len(a) >= len(b) else a + b[::-1] + a


# print(shorter_reverse_longer("first", "abcde"))
# print(shorter_reverse_longer("hello", "bau"))
# print(shorter_reverse_longer("abcde", "fghi"))

def not_visible_cubes(n):
    return max(0, (n - 2) ** 3)


def chess_knight(cell):
    result = 0
    moves = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
    for move in moves:
        new_x = chr(ord(cell[0]) + move[0])
        new_y = int(cell[1]) + move[1]
        if new_x in 'abcdefgh' and 1 <= new_y <= 8:
            result += 1
    return result


# print(chess_knight('h3'))


# рекурсия ниже
# def last_survivor(letters, coords):
#     if not coords:
#         return letters
#     letters = letters[:coords[0]]+letters[coords[0]+1:]
#     return last_survivor(letters, coords[1:])
#
# print(last_survivor('abc', [1, 1]), 'a')
# print(last_survivor('kbc', [0, 1]), 'b')
# print(last_survivor('zbk', [2, 1]), 'z')


def last_survivor(letters, coords):
    return letters if not coords else last_survivor(letters[:coords[0]] + letters[coords[0] + 1:], coords[1:])


def is_sator_square(tablet):
    dict_word_ltr = []
    dict_word_rtl = []
    dict_word_ttb = []
    dict_word_btt = []
    len_ = len(tablet)

    for item in tablet:
        word = ''.join(item)
        dict_word_ltr.append(word)
    for x in range(len_ - 1, -1, -1):
        word = ''.join(tablet[x][::-1])
        dict_word_rtl.append(word)
    for x in range(len_):
        word = ''
        for y in range(len_):
            word += tablet[y][x]
        dict_word_ttb.append(word)
    for x in range(len_ - 1, -1, -1):
        word = ''
        for y in range(len_ - 1, -1, -1):
            word += tablet[y][x]
        dict_word_btt.append(word)

    return dict_word_rtl == dict_word_ltr == dict_word_ttb == dict_word_btt


# print(is_sator_square([
#     ['S', 'A', 'T', 'O', 'R'],
#     ['A', 'R', 'E', 'P', 'O'],
#     ['T', 'E', 'N', 'E', 'T'],
#     ['O', 'P', 'E', 'R', 'A'],
#     ['R', 'O', 'T', 'A', 'S']
# ]))
#
# print(is_sator_square([
#     ['B', 'A', 'T', 'S'],
#     ['#', 'B', 'U', 'T'],
#     ['T', 'U', 'B', '#'],
#     ['S', 'T', 'A', 'B']
# ]))


# print(sorted([66, 55, 100, 68, 46, -82, 12, 72, 12, 38]))
# make_valley(a) --> [100, 68, 55, 38, 12, *-82*, 12, 46, 66, 72]
# https://www.codewars.com/kata/56e3cd1d93c3d940e50006a4/train/python

def find_squares(num):
    return '-'.join([str((num // 2 + 1) ** 2), str((num // 2) ** 2)])


# print(find_squares(7))

def t_area(t_str):
    # print(t_str.split('\n'))
    # print(t_str.split('\n')[-2])
    # print(t_str.split('\n')[-2].split())
    # print(len(t_str.split('\n')[-2].split()))
    # print(len(t_str.split('\n')[-2].split())-1)
    # print((len(t_str.split('\n')[-2].split())-1)**2/2)
    return (len(t_str.split('\n')[-2].split()) - 1) ** 2 / 2


assert t_area(
    '\n.\n. .\n. . .\n. . . .\n. . . . .\n. . . . . .\n. . . . . . .\n. . . . . . . .\n. . . . . . . . .\n') == 32.0


# https://www.codewars.com/kata/5f0ed36164f2bc00283aed07/train/python
def over_the_road(address, n):
    max_addr = n * 2
    in_ser = address // 2
    if address % 2 != 0:
        result = max_addr - in_ser * 2
    else:
        result = max_addr - 1 - (in_ser - 1) * 2
    return result


assert over_the_road(1, 3) == 6
assert over_the_road(3, 3) == 4
assert over_the_road(2, 3) == 5
assert over_the_road(4, 3) == 3
assert over_the_road(3, 5) == 8
assert over_the_road(7, 11) == 16
assert over_the_road(23633656673, 310027696726) == 596421736780


# https://www.codewars.com/kata/51fd6bc82bc150b28e0000ce/train/python
def no_odds(values):
    return [x for x in values if x % 2 == 0]


assert no_odds([0, 1, 2, 3]) == [0, 2]


# групповая замена нескольких символов в строке
def DNA_strand(dna):
    return dna.translate(str.maketrans("ATCG", "TAGC"))


assert DNA_strand("ATTGC") == "TAACG"


# https://www.codewars.com/kata/60dda5a66c4cf90026256b75/train/python
# функция в функции
def some_but_not_all(seq, pred):
    return any(map(pred, seq)) and not all(map(pred, seq))


# print(some_but_not_all('abcdefg&%$', str.isalpha))
assert some_but_not_all('abcdefg&%$', str.isalpha) == True


# https://www.codewars.com/kata/5981a139f5471fd1b2000071/train/python
def task(w, n, c):
    names = ['James', 'John', 'Robert', 'Michael', 'William']
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return f'It is {w} today, {names[days.index(w)]}, you have to work, you must spray {n} trees and you need {n * c} dollars to buy liquid'


assert task('Wednesday', 10,
            2) == 'It is Wednesday today, Robert, you have to work, you must spray 10 trees and you need 20 dollars to buy liquid'
assert task('Monday', 4,
            3) == 'It is Monday today, James, you have to work, you must spray 4 trees and you need 12 dollars to buy liquid'
assert task('Friday', 5,
            4) == 'It is Friday today, William, you have to work, you must spray 5 trees and you need 20 dollars to buy liquid'
assert task('Tuesday', 6,
            1) == 'It is Tuesday today, John, you have to work, you must spray 6 trees and you need 6 dollars to buy liquid'
assert task('Thursday', 5,
            3) == 'It is Thursday today, Michael, you have to work, you must spray 5 trees and you need 15 dollars to buy liquid'


# https://www.codewars.com/kata/562f91ff6a8b77dfe900006e/train/python
def movie(card, ticket, perc):
    count = 1
    sys_a = ticket
    sys_b = card + ticket * perc
    while True:
        if int(sys_b) + 1 < sys_a:
            return count
        else:
            count += 1
            sys_a = ticket * count
            sys_b += ticket * perc ** count


print(movie(983964, 3, 0.25))
