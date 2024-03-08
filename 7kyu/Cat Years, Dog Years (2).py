def calc_years(years, after_second):
    if years >= 24:
        return 2 + (years - 24) // after_second
    if years >= 15:
        return 1 + (years - 15) // 9
    return 0


def owned_cat_and_dog(cat_years, dog_years):
    return [calc_years(cat_years, 4), calc_years(dog_years, 5)]

print(owned_cat_and_dog(9,7))