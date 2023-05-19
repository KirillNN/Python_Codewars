def solution(string, ending):
    if ending == '':
        return True
    len_ending = len(ending)
    if string[-len_ending:] == ending:
        return True
    return False


print(solution('abcde', 'cde'))  # True
print(solution('abcde', 'abc'))  # False
print(solution('abcde', ''))  # True
