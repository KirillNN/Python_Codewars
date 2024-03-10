def decode_resistor_colors(bands: str):
    codes = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5,
             'blue': 6, 'violet': 7, 'gray': 8, 'white': 9}
    first, second, third, *other = bands.split()
    percent = '20%' if not other else '10%' if other == ['silver'] else '5%'
    value = (codes.get(first) * 10 + codes.get(second)) * 10 ** codes.get(third)
    if value > 999_999:
        return f'{value / 1e6}M ohms, {percent}'.replace('.0', '')
    if value > 999:
        return f'{value / 1e3}k ohms, {percent}'.replace('.0', '')
    return f'{value} ohms, {percent}'.replace('.0', '')


print(decode_resistor_colors('brown black black'))
print(decode_resistor_colors('brown black brown gold'))
print(decode_resistor_colors('yellow violet brown silver'))
