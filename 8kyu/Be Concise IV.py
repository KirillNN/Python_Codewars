def find(a, e):
    return a.index(e) if e in a else 'Not found'


array = [2, 3, 5, 7, 11]
print(find(array, 5))