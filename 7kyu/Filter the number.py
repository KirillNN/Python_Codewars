def filter_string(string):
    result = list(filter(lambda x: x.isnumeric(), string))
    return int(''.join(result))


print(filter_string("aa 112 3dd"))
