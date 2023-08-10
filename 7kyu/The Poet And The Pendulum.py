def pendulum(values):
    values.sort()
    result = [values.pop(0)]
    for i, v in enumerate(values):
        if i % 2 == 0:
            result.extend([v])
        else:
            result = [v] + result
    return result


print(pendulum([4, 6, 8, 7, 5]))
print(pendulum([19, 30, 16, 19, 28, 26, 28, 17, 21, 17]))
