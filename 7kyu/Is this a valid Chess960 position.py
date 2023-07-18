def is_valid(positions):
    pos_bishop_left, pos_bishop_right = positions.find('B'), positions.rfind('B')
    if not (pos_bishop_left + pos_bishop_right) % 2:
        return False
    pos_king = positions.find('K')
    pos_rook_left, pos_rook_right = positions.find('R'), positions.rfind('R')
    if pos_rook_left > pos_king or pos_rook_right < pos_king:
        return False
    return True


print(is_valid("RNBQKBNR"))

# For the purpose of this kata:
#
# Rooks are abbreviated as R the king must be placed on a square between the two rooks.
# Knights are abbreviated as N
# Bishops are abbreviated as B must start on differently colored squares.
# Queen is abbreviated as Q
# King is abbreviated as K
