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


def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    # result = get_column(puzzle, 1)
    pass
    for i in range(0, 9):
        find_element = find_in_row(i, puzzle)
        if find_element:
            puzzle[find_element['x']][find_element['y']] = find_element['element'][0]
            pass
        print()
    pass
    for i in range(0, 9):
        find_element = find_in_column(i, puzzle)
        if find_element:
            puzzle[find_element['x']][find_element['y']] = find_element['element'][0]
            pass
        print()
    pass
    # return row, missed_elements

def find_in_column(idx_column, puzzle):
    column = get_column(puzzle, idx_column)
    print(f'столбец {column}')
    missed_elements = find_missed_elements(column)
    print(f'пропущены {missed_elements}')
    for idx_row in range(0, 9):  # идем по элементам столбца
        if column[idx_row] == 0:
            row = get_row(puzzle, idx_row)
            print(f'ряд {row}')
            result = dict()
            result['element'] = []
            for element in missed_elements:
                if element not in row:
                    print(element, end=' ')
                    result['element'].append(element)
            if len(result['element']) == 1:
                result['x'] = idx_column
                result['y'] = idx_row
                return result
            print()
    return None

def find_in_row(idx_row, puzzle):
    row = get_row(puzzle, idx_row)
    print(f'ряд {row}')
    missed_elements = find_missed_elements(row)
    print(f'пропущены {missed_elements}')
    for idx_column in range(0, 9):  # идем по элементам ряда
        if row[idx_column] == 0: # если элемент ряда ноль
            column = get_column(puzzle, idx_column) # берем столбец
            print(f'столбец {column}')
            result = dict()
            result['element'] = []
            for element in missed_elements: # идем по элементам, которых нет в ряду.
                if element not in column: # если текущий пропущенный элемент отсутствует в столбце
                    print(element, end=' ')
                    result['element'].append(element)
            if len(result['element']) == 1:
                result['x'] = idx_column
                result['y'] = idx_row
                return result
            else:
                pass
            print()
    return None


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
