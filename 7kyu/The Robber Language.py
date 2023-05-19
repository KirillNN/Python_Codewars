letters = 'bcdfghjklmnpqrstvwxyz'


def robber_encode(sentence):
    result = ''
    for letter in sentence:
        if letter.lower() in letters:
            if letter.islower():
                result += letter + 'o' + letter
            else:
                result += letter + 'O' + letter
        else:
            result += letter
    return result


print(robber_encode("hello world"))  # "hohelollolo wowororloldod"
print(robber_encode("S.O.S"))  # "SOS.O.SOS"
