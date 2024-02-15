from typing import List


def get_column(arr, n) -> List[int]:
    """ Возвращает список элементов столбца n"""
    return [x[n] for x in arr]


def get_row(arr, n) -> List[int]:
    """ Возвращает список элементов строки n"""
    return arr[n]


def sudoku(puzzle) -> List:
    """return the solved puzzle as a 2d array of 9 x 9"""
    result = get_column(puzzle, 1)
    result = get_row(puzzle, 1)
    return result


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

print(*sudoku((puzzle)), sep='\n')
