def get_issuer(number):
    number = str(number)
    length = len(number)
    amex = ['34', '37']
    mastercard = [str(x) for x in range(51, 56)]

    if any(number.startswith(x) for x in amex) and length == 15:
        return "AMEX"
    if number.startswith('6011') and length == 16:
        return 'Discover'
    if any(number.startswith(x) for x in mastercard) and length == 16:
        return "Mastercard"
    if number.startswith('4') and (length == 13 or length == 16):
        return "VISA"
    return 'Unknown'


print(get_issuer(2))
