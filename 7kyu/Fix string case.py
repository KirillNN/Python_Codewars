# def solve(s):
#     high = low = 0
#     for letter in s:
#         if letter.isupper():
#             high += 1
#         else:
#             low += 1
#     if high > low:
#         return s.upper()
#     return s.lower()

def solve(s):
    return s.upper() if len(list(filter(lambda x: x.isupper(), s))) > len(
        list(filter(lambda x: x.islower(), s))) else s.lower()


print(solve('aSDD'))
