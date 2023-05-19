from loguru import logger


@logger.catch()
def flatten_and_sort(array):
    result = []
    for ar in array:
        result.extend(ar)
    return sorted(result)


print(flatten_and_sort([[10, 2], [], [5, 3]]))
