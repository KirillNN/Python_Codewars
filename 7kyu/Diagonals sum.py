import numpy as np


def sum_diagonals(matrix):
    arr = np.array(matrix)
    primary_sum = np.trace(arr)
    secondary_sum = np.trace(np.fliplr(arr))
    return primary_sum + secondary_sum
