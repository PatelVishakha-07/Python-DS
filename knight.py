def knight_moves(row, col, steps, board_size):
    if steps == 0:
        print(f"({row} {col})")
        return
    
    for r, c in moves:
        new_row = row + r
        new_col = col + c

        if 1 <= new_row <= board_size and 1 <= new_col <= board_size:
            knight_moves(new_row, new_col, steps-1, board_size)


moves = [
    (-2, -1), (-2, 1), 
    (-1, -2), (-1, 2),
    (2, -1), (2, 1),
    (1, -2), (1,2)
]

knight_moves(3,3, 2, 4)