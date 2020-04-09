# coding: utf-8

def num_rook_captures(board):
    """
    999. Available Captures for Rook
    
    On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, 
    and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. 
    Uppercase characters represent white pieces, and lowercase characters represent black pieces.
    The rook moves as in the rules of Chess: it chooses one of four cardinal directions 
    (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the 
    edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  
    Also, rooks cannot move into the same square as other friendly bishops.
    Return the number of pawns the rook can capture in one move.

    Example:
        Input: [[".",".",".",".",".",".",".","."],
                [".",".",".","p",".",".",".","."],
                [".",".",".","R",".",".",".","p"],
                [".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".","."],
                [".",".",".","p",".",".",".","."],
                [".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".","."]]
        Output: 3
        Explanation: 
            In this example the rook is able to capture all the pawns.
    """
    ans, r_i, r_j = 0, 0, 0
    size = len(board)
    
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'R':
                r_i, r_j = i, j
                break
        
    for ori_x, ori_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x, y = r_i + ori_x, r_j + ori_y
        while x >= 0 and y >= 0 and x < size and y < size:
            if board[x][y] == 'B': break
            if board[x][y] == 'p':
                ans += 1
                break
            x, y = x + ori_x, y + ori_y

    return ans

print num_rook_captures([[".",".",".",".",".",".",".","."],
                         [".",".",".","p",".",".",".","."],
                         [".",".",".","R",".",".",".","p"],
                         [".",".",".",".",".",".",".","."],
                         [".",".",".",".",".",".",".","."],
                         [".",".",".","p",".",".",".","."],
                         [".",".",".",".",".",".",".","."],
                         [".",".",".",".",".",".",".","."]])

def test_num_rook_captures_1():
    assert 3 == num_rook_captures([[".",".",".",".",".",".",".","."],
                                   [".",".",".","p",".",".",".","."],
                                   [".",".",".","R",".",".",".","p"],
                                   [".",".",".",".",".",".",".","."],
                                   [".",".",".",".",".",".",".","."],
                                   [".",".",".","p",".",".",".","."],
                                   [".",".",".",".",".",".",".","."],
                                   [".",".",".",".",".",".",".","."]])                    


def test_num_rook_captures_2():
    assert 0 == num_rook_captures([[".",".",".",".",".",".",".","."],
                                   [".","p","p","p","p","p",".","."],
                                   [".","p","p","B","p","p",".","."],
                                   [".","p","B","R","B","p",".","."],
                                   [".","p","p","B","p","p",".","."],
                                   [".","p","p","p","p","p",".","."],
                                   [".",".",".",".",".",".",".","."],
                                   [".",".",".",".",".",".",".","."]])

def test_num_rook_captures_3():
    assert 3 == num_rook_captures([[".",".",".",".",".",".",".","."],
                                   [".",".",".","p",".",".",".","."],
                                   [".",".",".","p",".",".",".","."],
                                   ["p","p",".","R",".","p","B","."],
                                   [".",".",".",".",".",".",".","."],
                                   [".",".",".","B",".",".",".","."],
                                   [".",".",".","p",".",".",".","."],
                                   [".",".",".",".",".",".",".","."]])
