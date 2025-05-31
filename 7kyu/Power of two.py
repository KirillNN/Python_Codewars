def power_of_two(x):
    return format(x, 'b').count('1') == 1


print(power_of_two(0))