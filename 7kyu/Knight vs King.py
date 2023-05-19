chess_ranks = '12345678'
chess_files = 'ABCDEFGH'
chess_board = dict(zip(chess_files, chess_ranks))


def knight_vs_king(knight_position, king_position):
    x = abs(knight_position[0] - king_position[0])
    y = abs(int(chess_board.get(knight_position[1])) - int(chess_board.get(king_position[1])))
    if x == 2 and y == 1 or x == 1 and y == 2:
        return 'Knight'
    if x < 2 and y < 2:
        return 'King'
    return 'None'


print(knight_vs_king([4, "C"], [6, "D"]))  # Knight
print(knight_vs_king([7, "B"], [6, "C"]))  # King
print(knight_vs_king([2, "F"], [6, "B"]))  # None
