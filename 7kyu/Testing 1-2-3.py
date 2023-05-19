def number(lines):
    if not lines:
        return []
    return [f'{i + 1}: {v}' for i, v in enumerate(lines)]

print(number(["a", "b", "c"]))