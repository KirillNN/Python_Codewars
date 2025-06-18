def calculate(expr: str, values: dict[str, int]) -> int:
    for key, value in values.items():
        globals()[key] = value
    return eval(expr)


def calculate(expr, values):
    return eval(expr, values)


print(calculate("A & B & C", {"A": 0, "B": 1, "C": 0}))
