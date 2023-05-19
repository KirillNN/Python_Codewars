mat = [[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24]]


def get_neighbourhood(n_type, mat, coordinates):
    row, col = coordinates
    if row >= len(mat) or col >= len(mat[0]):
        return []
    von_neumann = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    result = []

    def add_values(row, col, neighbourhood):
        for x, y in neighbourhood:
            if (row + x) >= 0 and (col + y) >= 0:
                try:
                    result.append(mat[row + x][col + y])
                except IndexError:
                    pass
        return result

    add_values(row, col, von_neumann)
    if n_type == 'von_neumann':
        return result
    moore_add = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    add_values(row, col, moore_add)
    return result

    # return mat[row][col]
    # return mat[-1][-1]


print(get_neighbourhood('moore', mat, (1, 1)))  # [0, 1, 2, 5, 7, 10, 11, 12]
print(get_neighbourhood('von_neumann', mat, (1, 1)))  # [1,5,7,11]
print(get_neighbourhood('moore', mat, (0, 0)))  # [1, 5, 6]
print(get_neighbourhood('von_neumann', mat, (0, 0)))
print(get_neighbourhood("moore", mat, (4, 2)))  # [21, 16, 17, 18, 23]

'''
\ n   0    1    2    3    4
m  --------------------------
0  |  0 |  1 |  2 |  3 |  4 |
1  |  5 |  6 |  7 |  8 |  9 |
2  | 10 | 11 | 12 | 13 | 14 |
3  | 15 | 16 | 17 | 18 | 19 |
4  | 20 | 21 | 22 | 23 | 24 |
   --------------------------
'''
