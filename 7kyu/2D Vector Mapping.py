def map_vector(vector, circle1, circle2):
    dx, dy = vector[0] - circle1[0], vector[1] - circle1[1]
    multi = circle2[2] / circle1[2]
    dx *= multi
    dy *= multi
    return circle2[0] + dx, circle2[1] + dy


'''
basic_examples = [
    {
        "input": [(46, 58), (0, 0, 100), (0, 0, 100)],
        "output": (46, 58)
    },
    {
        "input": [(50, 88), (-25, 128, 100), (50, 50, 100)],
        "output": (125, 10)
    },
    {
        "input": [(120, 58), (100, 76, 36), (120, -62, 50)],
        "output": (147.78, -87.0)
    },
    {
        "input": [(5, 5), (10, 20, 42), (-100, -42, 60)],
        "output": (-107.14, -63.43)
    },
]
'''
