from datetime import datetime


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code != correct_code or not entered_code:
        return False
    current = datetime.strptime(current_date, "%B %d, %Y")
    expiration = datetime.strptime(expiration_date, "%B %d, %Y")
    return current <= expiration


print(check_coupon(0, False, 'September 5, 2014', 'September 25, 2014'))
