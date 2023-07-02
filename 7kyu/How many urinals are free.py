def get_free_urinals(urinals, counter=0, start=True):
    if urinals == '1':
        return 0
    if urinals == '0':
        return 1
    if '11' in urinals:
        return -1
    if start:
        urinals = list('0' + urinals + '0')
    for i, v in enumerate(urinals[1:-1]):
        if urinals[i - 1] == urinals[i] == urinals[i + 1] == '0':
            urinals[i+1] = '1'
            return get_free_urinals(urinals, counter+1, False)
    return counter


print(get_free_urinals('00000'))
# print(get_free_urinals('110'))
