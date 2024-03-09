# input is a string of three chars from the set 'D', 'F', 'I', 'K';
# output is a single char from this set
def trilingual_democracy(group):
    if len(set(group)) == 1:
        return group[0]
    lang = {'D', 'F', 'I', 'K'}
    if len(set(group)) == 3:
        return list(lang - set(group))[0]
    lang = [x for x in group if group.count(x) == 1]
    return lang[0]


print(trilingual_democracy('IIK'))
