def chain(init_val, functions):
    if functions == []:
        return init_val
    for function in functions:
        init_val = function(init_val)
    return init_val

# print(chain(50, [mul30, add10]))