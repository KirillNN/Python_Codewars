def number(bus_stops):
    return sum([x - y for x, y in bus_stops])


print(number([[10, 0], [3, 5], [5, 8]]))
