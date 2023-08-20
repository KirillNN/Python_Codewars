def to24hourtime(hour, minute, period):
    result = ''
    if period == 'am':
        if hour == 12:
            result += '00'
        else:
            result += f'{hour:02}'
    else:
        if hour == 12:
            result += '12'
        else:
            result += f'{hour + 12:02}'
    result += f'{minute:02}'
    return result


def _to24hourtime(hour, minute, period): # форматированный вывод
    return '%02d%02d' % (hour % 12 + 12 * (period == 'pm'), minute)
