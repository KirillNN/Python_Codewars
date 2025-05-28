def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1
    a1, a2 = sorted(map(len, a1)), sorted(map(len, a2))
    return max((abs(a1[0] - a2[-1]), abs(a1[-1] - a2[0])))


s1 = ["zxx", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(s1, s2))
