def printer_error(s):
    len_s = len(s)
    count_s = sum([x > 'm' for x in s])
    return f'{count_s}/{len_s}'


s = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
print(printer_error(s))
