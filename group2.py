import random
import time

def group2(self, board):
    """
    Enhanced function to choose the best move based on the evaluation of captures and choices
    """
    possible_moves = self.getPossibleMoves(board)

    if not possible_moves:
        self.game.end_turn()
        return None, None  # Return None if no moves are available

    # Define the number of simulations for the Monte Carlo algorithm
    num_simulations = 10000

    # Initialize the best move and its corresponding captures and choices
    best_move = None
    max_captures = -1
    max_choices = -1

    # Perform the Monte Carlo simulations
    for _ in range(num_simulations):
        # Select a random move from the possible moves
        move = random.choice(possible_moves)

        # Simulate the move to evaluate potential captures
        captures = sum(1 for choice in move[2] if choice[0] != choice[1])  # Count captures using a generator expression
        move_choices = len(move[2])  # Assuming move[2] contains possible choices for this move

        # Update if this move has more captures or more choices than previously found
        if captures > max_captures or (captures == max_captures and move_choices > max_choices):
            max_captures = captures
            max_choices = move_choices
            best_move = move

    # If a best move is found, select a choice for it
    if best_move:
        # Select a random choice from the best move
        selected_choice = random.choice(best_move[2])

        # Add a delay before returning the move
        time.sleep(1)  # Delay for 1 second (adjust as needed)

        return best_move, selected_choice

    return None, None  # Return None if no best move is found

def group1(self, board):
    # Retrieve all possible moves
    possible_moves = self.getPossibleMoves(board)
    
    # If no possible moves are available, end the turn
    if not possible_moves:
        self.game.end_turn()
        return
    
    # Initialize variables to track the best move
    best_move = None
    max_choices = -1
    
    # Evaluate each move to find the one with the most choices
    for move in possible_moves:
        move_choices = len(move[2])  # Assuming move[2] contains possible choices for this move
        
        # Update if this move has more choices than previously found
        if move_choices > max_choices:
            max_choices = move_choices
            best_move = move
    
    # Select a choice for the best move 
    selected_choice = random.choice(best_move[2])
    
    return best_move, selected_choice

def group(self, board):
    # First, try to find the best move using the group2 function
    best_move = group2(self, board)
    
    # If no best move is found, use the group1 function as a fallback
    if best_move is None:
        best_move = group1(self, board)
    
    return best_move
