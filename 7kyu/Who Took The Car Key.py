def who_took_the_car_key(message):
    return ''.join(list(map(lambda x: chr(int(x, 2)), message)))


print(who_took_the_car_key(
    ['01000001', '01101100', '01100101', '01111000', '01100001', '01101110',
     '01100100', '01100101', '01110010']
))


