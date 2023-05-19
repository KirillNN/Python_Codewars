def remove(s):
    return ' '.join([x for x in s.split() if x.count('!') != 1])


print(remove('!!!Hi !!hi!!! !hi'))
