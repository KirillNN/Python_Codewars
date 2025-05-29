def predict_age(*args):
    return int(sum(map(lambda x: x * x, args)) ** 0.5 / 2)


# def predict_age(*args):
#     return int(sum(x * x for x in args) ** 0.5 / 2)


print(predict_age(65, 60, 75, 55, 60, 63, 64, 45))
