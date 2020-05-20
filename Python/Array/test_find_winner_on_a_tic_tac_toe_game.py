# coding: utf-8

def tictactoe(moves):
    """
    1275. Find Winner on a Tic Tac Toe Game
    
    Tic-tac-toe is played by two players A and B on a 3 x 3 grid.
    Here are the rules of Tic-Tac-Toe:
        1. Players take turns placing characters into empty squares (" ").
        2. The first player A always places "X" characters, while the second player B always places "O" characters.
        3. "X" and "O" characters are always placed into empty squares, never on filled ones.
        4. The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
        5. The game also ends if all squares are non-empty.
        6. No more moves can be played if the game is over.
        7. Given an array moves where each element is another array of size 2 corresponding to the row and column 
           of the grid where they mark their respective character in the order in which A and B play.
    Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", 
    if there are still movements to play return "Pending".
    You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), 
    the grid is initially empty and A will play first.

    Example:
        Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
        Output: "A"
        Explanation: "A" wins, he always plays first.
                     "X  "    "X  "    "X  "    "X  "    "X  "
                     "   " -> "   " -> " X " -> " X " -> " X "
                     "   "    "O  "    "O  "    "OO "    "OOX"

    https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
    """

    count = [0] * 8
    ret = 'B' if len(moves) % 2 == 0 else 'A'

    for i in range(len(moves) - 1, -1, -2):
        count[moves[i][0]] += 1
        if count[moves[i][0]] == 3: return ret

        count[moves[i][1] + 3] += 1
        if count[moves[i][1] + 3] == 3: return ret

        if moves[i][0] == moves[i][1]: count[6] += 1
        if count[6] == 3: return ret

        if moves[i][0] + moves[i][1] == 2: count[7] += 1
        if count[7] == 3: return ret

    return 'Pending' if len(moves) < 9 else 'Draw'


print tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]])

def test_tictactoe_1():
    assert 'A' == tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]])

def test_tictactoe_2():
    assert 'B' == tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]])

def test_tictactoe_3():
    assert 'Draw' == tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]])

def test_tictactoe_4():
    assert 'Pending' == tictactoe([[0,0],[1,1]])