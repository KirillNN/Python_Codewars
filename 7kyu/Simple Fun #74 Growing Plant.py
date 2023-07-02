def growing_plant(up_speed, down_speed, desired_height):
    day = 1
    height = up_speed
    while desired_height > height:
        height -= down_speed
        day += 1
        height += up_speed
        if desired_height <= height:
            break

    return day


print(growing_plant(100, 10, 910))