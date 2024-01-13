def evaluate_board(board, player, opponent):
    # Check if the current player wins
    if is_winner(board, player):
        return 1
    # Check if the opponent wins
    elif is_winner(board, opponent):
        return -1
    # Check for a tie
    elif is_board_full(board):
        return 0
    else:
        # Calculate the heuristic score based on various factors
        score = 0

        # Heuristic 1: Center control
        score += center_control(board, player)

        # Heuristic 2: Blocking opponent's winning moves
        score += block_opponent_win(board, player, opponent)

        # Heuristic 3: Completing own winning moves
        score += complete_own_win(board, player)

        # Heuristic 4: Corner control
        score += corner_control(board, player)

        # Heuristic 5: Balanced control
        score += balanced_control(board, player)

        return score

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    # Check if the board is full (a tie)
    return all(cell != ' ' for row in board for cell in row)

def center_control(board, player):
    # Heuristic: Prioritize center control
    center_cell = board[1][1]
    return 1 if center_cell == player else 0

def block_opponent_win(board, player, opponent):
    # Heuristic: Block opponent's winning moves
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                # Simulate making a move and check if it blocks the opponent's win
                board[i][j] = opponent
                if is_winner(board, opponent):
                    board[i][j] = ' '  # Undo the move
                    return -1
                board[i][j] = ' '  # Undo the move
    return 0

def complete_own_win(board, player):
    # Heuristic: Complete own winning moves
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                # Simulate making a move and check if it completes the player's win
                board[i][j] = player
                if is_winner(board, player):
                    board[i][j] = ' '  # Undo the move
                    return 1
                board[i][j] = ' '  # Undo the move
    return 0

def corner_control(board, player):
    # Heuristic: Prioritize corner control
    corners = [board[0][0], board[0][2], board[2][0], board[2][2]]
    return sum(1 for corner in corners if corner == player)

def balanced_control(board, player):
    # Heuristic: Aim for balanced control
    row_counts = [sum(1 for cell in row if cell == player) for row in board]
    col_counts = [sum(1 for row in board if row[i] == player) for i in range(3)]
    return min(row_counts + col_counts)
