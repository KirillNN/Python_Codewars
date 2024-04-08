def open_or_senior(data):
    return ['Senior' if x >= 55 and y > 7 else 'Open' for x, y in data]


print(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]))
