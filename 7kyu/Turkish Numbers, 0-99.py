def convert_to_turkish_word(number):
    units = ["sıfır", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
    tens = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]

    if number < 10:
        return units[number]
    elif number < 100:
        unit_digit = number % 10
        ten_digit = number // 10
        if unit_digit == 0:
            return tens[ten_digit]
        else:
            return tens[ten_digit] + " " + units[unit_digit]
    else:
        return "Sayı 0 ile 99 arasında olmalıdır."


# Пример использования
for number in range(100):
    word = convert_to_turkish_word(number)
    print(number, ":", word)
