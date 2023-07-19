def tacofy(word):
    taco = ['shell']

    for letter in word:
        if letter.lower() == 'a' or letter.lower() == 'e' or letter.lower() == 'i' or letter.lower() == 'o' or letter.lower() == 'u':
            taco.append('beef')
        elif letter.lower() == 't':
            taco.append('tomato')
        elif letter.lower() == 'l':
            taco.append('lettuce')
        elif letter.lower() == 'c':
            taco.append('cheese')
        elif letter.lower() == 'g':
            taco.append('guacamole')
        elif letter.lower() == 's':
            taco.append('salsa')
    taco.append('shell')
    return taco


# Test cases
print(tacofy("Taco"))  # Output: ['shell', 'tomato', 'beef', 'cheese']
print(tacofy("Bell"))  # Output: ['shell', 'beef', 'lettuce', 'lettuce']
print(tacofy("Locos"))  # Output: ['shell', 'beef', 'beef', 'cheese', 'beef', 'salsa']
