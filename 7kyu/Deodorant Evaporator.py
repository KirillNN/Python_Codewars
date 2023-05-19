def evaporator(content, evap_per_day, threshold):
    proc = 1
    count = 0
    while proc > threshold * 0.01:
        count += 1
        proc -= proc * evap_per_day * 0.01
    return count


print(evaporator(10, 10, 10))  # 22
