def decode(s):
    print(encode("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(encode("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(encode("!@#$%^&*()_+-"))
    a, b, c, d,e,f = "", "", "", "", "",""
    for w in "abcdefghijklmnopqrstuvwxyz":
        a += encode("" + w)[0]
        b += encode("_" + w)[1]
        c += encode("__" + w)[2]
        d += encode("___" + w)[3]
        e += encode("____" + w)[4]
        f += encode("_____" + w)[5]
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    return s


x = 'flxVC5WE94UA1OoD70MkvRuPqHabdhpF,82QsLirJejtNmzZKgnB3SwTyXG ?.6YIc'
print(len(x))