def tail_swap(strings):
    a, b = strings
    c, d = a.split(':')
    e, f = b.split(':')
    return [c + ":" + f, e + ":" + d]
