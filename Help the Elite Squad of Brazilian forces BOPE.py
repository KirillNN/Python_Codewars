from typing import Tuple
from math import ceil

mag = {"PT92": 17, "M4A1": 30, "M16A2": 30, "PSG1": 5}


def mag_number(info: Tuple[str, int]) -> int:
    gun, street = info
    # gun_mag = mag.get(gun)
    # x = street * 3 / gun_mag
    # print(gun, street, gun_mag, ceil(x))
    return ceil(street * 3 / mag.get(gun))


print(mag_number(("PT92", 6)))
print(mag_number(("M4A1", 1000000000)))
