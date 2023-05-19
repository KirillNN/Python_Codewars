# def get_the_vowels(word):
#     n = 0
#     vowels = 'aeiou'
#     for letter in word:
#         if letter == vowels[0]:
#             n += 1
#             vowels = vowels[1:]+vowels[0]
#     return n

def get_the_vowels(word, n=0):
    while word.find('aeiou'[n % 5]) != -1:
        word = word[word.find('aeiou'[n % 5]) + 1:]
        n += 1
    return n


#
#
# def get_the_vowels(word):
#     n = 0
#     for i in word:
#         if i == "aeiou"[n % 5]:
#             n += 1
#     return n


string = "agrtertyfikfmroyrntbvsukldkfa"
print(get_the_vowels(string))  # 6

string = 'erfaiekjudhyfimngukduo'
print(get_the_vowels(string))  # 4

string = 'akfheujfkgiaaaofmmfkdfuaiiie'
print(get_the_vowels(string))  # 7
