def keep_order(ary, val):
    for index, value in enumerate(ary):
        if val <= value:
            return index
    return len(ary)
