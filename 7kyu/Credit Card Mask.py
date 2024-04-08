def maskify(cc):
    if len(cc) < 5:
        return cc
    return "#" * (len(cc) - 4) + cc[-4:]
