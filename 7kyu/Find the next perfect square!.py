def find_next_square(sq):
    return -1 if int(sq ** 0.5) ** 2 != sq else (int(sq ** 0.5) + 1) ** 2


print(find_next_square(114))
