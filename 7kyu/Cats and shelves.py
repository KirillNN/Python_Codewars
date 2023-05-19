def solution(start, finish):
    res = (finish - start) // 3
    tmp = finish - start - res * 3
    if tmp == 1:
        res += 1
    elif tmp == 2:
        res += 2
    return res
