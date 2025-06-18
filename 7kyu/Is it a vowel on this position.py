# def check_vowel(strng: str, position: int) -> bool:
#     if position < 0:
#         return False
#     return strng[position].lower() in 'aeiou' if position < len(strng) else False

def check_vowel(strng: str, position: int) -> bool:
    return strng[position].lower() in 'aeiou' if 0 <= position < len(strng) else False


print(check_vowel('sdf', 2))
