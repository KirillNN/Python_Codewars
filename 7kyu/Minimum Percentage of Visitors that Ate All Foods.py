def minimum_percentage(foods):
    return max(0, sum(foods) - (len(foods) - 1) * 100)


print(minimum_percentage((37, 52)))
