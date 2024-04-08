import re


def validate_pin(pin):
    if len(pin) != len(pin.strip()):
        return False
    tpl = r'^\d{4}$|^\d{6}$'
    if re.match(tpl, pin) is not None:
        return True
    return False
