def drop_cap(words:str):
    for letter in words:
        if letter.isalpha():
            start = True

print(drop_cap('   space WALK   '))