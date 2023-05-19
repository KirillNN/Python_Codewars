def evaluate(equation):
    x = list(map(int, equation.split(' @ ')))
    if len(x) == 2:
        a, b = x
        res = (a + b) + (a - b) + (a * b) + (a // b)
        return res
    else:
        a, b = x[0], x[1]
        res = (a + b) + (a - b) + (a * b) + (a // b)
        return


print(evaluate('1 @ 1'))
