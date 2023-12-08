def camel_case(s):
    words = s.split()
    return ''.join(x.title() for x in words)


print(camel_case('hello case'))