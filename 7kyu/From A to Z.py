from string import ascii_letters


def gimme_the_letters(sp):
    start, stop = ascii_letters.index(sp[0]), ascii_letters.index(sp[-1])
    return ascii_letters[start:stop + 1]


print(gimme_the_letters('h-o'))
print(gimme_the_letters('Q-Z'))
print(gimme_the_letters('J-J'))
