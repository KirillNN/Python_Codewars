def pluralize(word: str):
    ends = ['s', 'x', 'z', 'ch', 'sh']
    if any(word.endswith(x) for x in ends):
        return word + 'es'

    consonants = "bcdfghjklmnpqrstvwxyz"
    if word[-1] == 'y' and word[-2] in consonants:
        return word[:-1] + 'ies'

    return word + 's'


print(pluralize('windoh'))
