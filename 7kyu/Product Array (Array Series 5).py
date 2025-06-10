from functools import reduce

def product_array(numbers):
    result = []
    for i in range(len(numbers)):
        temp = numbers[:i] + numbers[i + 1:]
        result.append(reduce(lambda x,y: x*y, temp))
    return result


print(product_array([3,27,4,2]))