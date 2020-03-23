# coding: utf-8

def matrix_score(A):
    """
    861. Score After Flipping Matrix

    We have a two dimensional matrix A where each value is 0 or 1.
    A move consists of choosing any row or column, and toggling each value in that row or column: 
    changing all 0s to 1s, and all 1s to 0s.
    After making any number of moves, every row of this matrix is interpreted as a binary number, 
    and the score of the matrix is the sum of these numbers.
    Return the highest possible score.

    Example:
        Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
        Output: 39
        Explanation:
            Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
            0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
    
    https://leetcode.com/problems/score-after-flipping-matrix/
    """
    
    m = len(A)
    if m == 0: return 0

    n = len(A[0])
    ans = m * (1 << (n - 1))

    for j in range(1, n):
        one = 0
        for i in range(m):
            if A[i][j] == A[i][0]: one += 1
        one = max(one, m - one)
        ans += one * (1 << (n - 1 - j))

    return ans

print matrix_score([[0,0,1,1],[1,0,1,0],[1,1,0,0]])

def test_matrix_score_1():
    assert 39 == matrix_score([[0,0,1,1],[1,0,1,0],[1,1,0,0]])