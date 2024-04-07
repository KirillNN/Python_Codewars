def is_isogram(string):
    return len(set(string.lower())) == len(string)


print(is_isogram("Dermatoglyphics"))
