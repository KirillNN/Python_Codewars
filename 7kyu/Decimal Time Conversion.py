def to_industrial(time):
    if isinstance(time, int):
        return round(time / 60, 2)
    x = time.split(":")
    return round(int(x[0]) + int(x[1]) / 60, 2)


def to_normal(time):
    return f"{int(time // 1)}:{round(time % 1 * 60):02}"



print(to_normal(75.09))