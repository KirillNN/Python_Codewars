walk, bus = 5, 8


def calculator(distance, bus_drive, bus_walk):
    time_walk = distance * 60 / walk
    if time_walk > 120:
        return "Bus"
    elif time_walk < 10:
        return "Walk"
    time_bus = bus_drive * 60 / bus + bus_walk * 60 / walk
    if time_bus < time_walk:
        return "Bus"
    else:
        return "Walk"


print(calculator(5, 6, 1))
