# https://www.codewars.com/kata/5296bc77afba8baa690002d7/train/python
from typing import List


def find_missed_elements(list: List[int]) -> List[int]:
    """ Возвращает список отсутствующих элементов"""
    result = []
    for i in range(1, 10):
        if i not in list:
            result.append(i)
    return result


def get_column(arr, n) -> List[int]:
    """ Возвращает список элементов столбца n"""
    return [x[n] for x in arr]


def get_row(arr, n) -> List[int]:
    """ Возвращает список элементов строки n"""
    return arr[n]


def get_quad(puzzle, id_row, id_column):
    pos = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    for i, v in enumerate(pos):
        if id_row in v:
            index_row = v
        if id_column in v:
            index_column = v
    quad = []
    for x in index_row:
        for y in index_column:
            quad.append(puzzle[x][y])
    return quad


def check_positon(puzzle, id_column, id_row):
    row = get_row(puzzle, id_row)
    column = get_column(puzzle, id_column)
    quad = get_quad(puzzle, id_row, id_column)
    x = set(range(1, 10)).difference(set(row).union(set(column))).difference(set(quad))
    if len(x) == 1:
        return x.pop()
    return None


def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    while True:
        for id_row, row in enumerate(puzzle):
            for id_column, element in enumerate(row):
                if element == 0:
                    el = check_positon(puzzle, id_column, id_row)
                    if el:
                        puzzle[id_row][id_column] = el
                        break
            else:
                continue
            break
        else:
            break
    return puzzle


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

sudoku(puzzle)
# print(*sudoku((puzzle)), sep=' ')
