def am_I_afraid(day, num):
    return {'Monday': num == 12,
            'Tuesday': num > 95,
            'Wednesday': num == 34,
            'Thursday': num == 0,
            'Friday': not num % 2,
            'Saturday': num == 56,
            'Sunday': abs(num) == 666}[day]


print(am_I_afraid('Monday', 12))
print(am_I_afraid('Monday', 13))
