def to_jaden_case(string: str):
    if string == '':
        return ''
    return ' '.join([x[0].upper() + x[1:].lower() for x in string.split(' ')])


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
