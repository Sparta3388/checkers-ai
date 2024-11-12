from main import Bot, GREY, PURPLE

def group1(bot, board):
    """
    Group 1 Algorithm: Simple Move Selection
    """
    best_move = None
    best_score = -float('inf') if bot.color == GREY else float('inf')

    for current_pos, legal_moves in bot.getPossibleMoves(board):
        for move in legal_moves:
            # Simulate the move
            simulated_board = board
            simulated_board.move_piece(current_pos[0], current_pos[1], move[0], move[1])

            # Evaluate the simulated board
            score = bot.evaluate(simulated_board)

            # Update the best move and score
            if bot.color == GREY:
                if score > best_score:
                    best_score = score
                    best_move = (current_pos, move)
            else:
                if score < best_score:
                    best_score = score
                    best_move = (current_pos, move)

    return best_move, best_score
