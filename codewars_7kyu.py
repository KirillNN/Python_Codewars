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

import re


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
list1 = [
    {'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19,
     'language': 'JavaScript'},
    {'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28,
     'language': 'JavaScript'},
    {'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML'},
    {'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30,
     'language': 'CSS'}
]


def count_developers(lst):
    x=lst.count({})


print(count_developers(list1))
