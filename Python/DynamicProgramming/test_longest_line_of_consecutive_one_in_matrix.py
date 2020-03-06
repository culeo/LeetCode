# coding: utf-8

def longest_line(M):
    """
    562	Longest Line of Consecutive One in Matrix(矩阵中连续的最长的直线)

    Given a 01 matrix, find the longest line of consecutive 1 in the matrix. 
    The line could be horizontal, vertical, diagonal or anti-diagonal.

    Example:
        Input: 
            [[0,1,1,0],
             [0,1,1,0],
             [0,0,0,1]]
        Output: 3
        Explanation: (0,1) (1,2) (2,3)
    
    https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix
    https://www.lintcode.com/problem/longest-line-of-consecutive-one-in-matrix/description
    """

    if len(M) < 1: return 0

    n = len(M)
    m = len(M[0])

    f = [[[0] * 4 for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            if M[i][j] != 1: continue

            f[i][j] = [1] * 4
     
            if j > 0:
                f[i][j][0] += f[i][j-1][0]

            if i > 0:
                f[i][j][2] += f[i-1][j][2]
                if j > 0:
                    f[i][j][1] += f[i-1][j-1][1]
                elif j < m - 1:
                    f[i][j][3] += f[i-1][j+1][3]    
          
    return max(max(f[i][j]) for j in range(m) for i in range(n))

print longest_line([[0,1,1,0], [0,1,1,0], [0,0,0,1]])

def test_longest_line_1():
    assert 3 == longest_line([[0,1,1,0],
                              [0,1,1,0],
                              [0,0,0,1]])
def test_longest_line_2():
    assert 7 == longest_line([[1,0,1,1,0,0,1,0,0,1],
                              [0,1,1,0,1,0,1,0,1,1],
                              [0,0,1,0,1,0,0,1,0,0],
                              [1,0,1,0,1,1,1,1,1,1],
                              [0,1,0,1,1,0,0,0,0,1],
                              [0,0,1,0,1,1,1,0,1,0],
                              [0,1,0,1,0,1,0,0,1,1],
                              [1,0,0,0,1,1,1,1,0,1],
                              [1,1,1,1,1,1,1,0,1,0],
                              [1,1,1,1,0,1,0,0,1,1]])