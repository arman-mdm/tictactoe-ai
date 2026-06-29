"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0 
    count_o = 0
    for row in board:
        for cell in row:
            if cell == X:
                count_x +=1
            elif cell == O:
                count_o +=1
    
    if count_x == count_o:
        return X
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                moves.add ((i,j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action in actions(board):
        newboard = []

        for row in board:
            newboard.append (row.copy())
        i, j = action
        newplayer = player(board)
        newboard[i][j] = newplayer 
        return newboard

    else:
        raise Exception("Invalid action")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row [1] == row [2] != EMPTY:
            return row[0]
        
    for j in range (3):
        if board[0][j] == board[1][j] == board[2][j] != EMPTY:
            return board[0][j]
        
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]    
               
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        if terminal(board):
            return utility(board)
        v = -math.inf
        for action in actions(board):
            newboard = result(board,action)
            score = min_value(newboard)
            if score > v:
                v = score
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = math.inf 
        for action in actions(board):
            newboard = result(board,action)
            score = max_value(newboard)
            if score < v:
                v = score
        return v
    
    if terminal(board):
        return None
    

    if player(board) == X:
        best_score = -math.inf
        best_action = None
        for action in actions(board):
            newboard = result(board,action)
            score = min_value(newboard)
            if score > best_score:
                best_score = score
                best_action = action
        return best_action
    
    elif player(board) == O:
        best_score = math.inf
        best_action = None
        for action in actions(board):
            newboard = result(board,action)
            score = max_value(newboard)
            if score < best_score:
                best_score = score
                best_action = action
        return best_action