def eliminate_unset_bits(string):
    return 2 ** (string.count('1')) - 1

# def eliminate_unset_bits(number):
#     res = ''
#     for i in number:
#         if i == '1':
#             res += i
#     return int(res, 2) if len(res) > 0 else 0


print(eliminate_unset_bits(
    "111101001100111000111000010110011010000011000000001000110100000001000111101011111010111110011000100"))


print(eliminate_unset_bits('0'))