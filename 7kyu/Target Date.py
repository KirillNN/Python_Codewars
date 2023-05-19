from datetime import datetime, timedelta
from math import log, ceil


def date_nb_days(a0, a, p):
    # delta = 0
    # while a > a0:
    #     a0 += a0 * p / 36000
    #     delta += 1
    # x = datetime(2016, 1, 1) + timedelta(delta)
    # return x.strftime("%Y-%m-%d")

    # a = a0 * (1 + p / 36000) ** x
    delta = ceil(log(a / a0, (1 + p / 36000)))
    x = datetime(2016, 1, 1) + timedelta(delta)
    return x.strftime("%Y-%m-%d")


print(date_nb_days(100, 101, 0.98))

# testing(date_nb_days(4281, 5087, 2), "2024-07-03")
# testing(date_nb_days(4620, 5188, 2), "2021-09-19")
# testing(date_nb_days(9999, 11427, 6), "2018-03-13")
# testing(date_nb_days(3525, 4822, 3), "2026-04-18")
# testing(date_nb_days(5923, 6465, 6), "2017-06-10")
# testing(date_nb_days(4254, 4761, 8), "2017-05-22")
# testing(date_nb_days(1244, 2566, 4), "2033-11-04")
# testing(date_nb_days(6328, 7517, 5), "2019-05-25")
# testing(date_nb_days(2920, 3834, 2), "2029-06-03")
# testing(date_nb_days(7792, 8987, 4), "2019-07-09")
