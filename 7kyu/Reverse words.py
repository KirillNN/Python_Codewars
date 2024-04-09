def reverse_words(text):
    words = text.split(' ')
    return ' '.join([''.join(reversed(x)) for x in words])


print(reverse_words('double  spaced  words'))
