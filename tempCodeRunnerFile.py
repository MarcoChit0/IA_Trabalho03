def vertical_expansion(board, queen_pos, queens):
    for ver in range(8):
        if board[ver][queen_pos[1]] != QUEEN_VALUE:
            print("ola")
            board[ver][queen_pos[1]] = board[ver][queen_pos[1]] + 1
        else:
            update_queen_list(queen_pos, queens)