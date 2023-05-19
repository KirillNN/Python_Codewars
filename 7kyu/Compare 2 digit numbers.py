def compare(a, b):
    a, b = sorted(str(a)), sorted(str(b))
    if a == b:
        return '100%'
    if a[0] == b[0] or a[1] == b[1] or a[0] == b[1] or a[1] == b[0]:
        return '50%'
    return '0%'


compare(29, 92)
