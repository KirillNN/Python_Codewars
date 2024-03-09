def gaslighting(shirt_word: str, your_word: str, friends_letters: str) -> bool:
    return any([x != y and any(letter in x + y for letter in friends_letters) for x, y in zip(shirt_word, your_word)])


print(gaslighting("snack", "snake", "c"))
