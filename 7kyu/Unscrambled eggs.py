import re


def unscramble_eggs(word):
    return re.sub(r'(?<=[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])egg', '', word)
