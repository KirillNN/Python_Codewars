def flick_switch(lst):
    flag = True
    result = []
    for i in lst:
        if i == 'flick':
            flag ^= True
        result.append(flag)
    return result
