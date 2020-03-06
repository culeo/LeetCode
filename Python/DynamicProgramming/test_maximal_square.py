# coding: utf-8

def maximal_square(matrix):
    """
    221. Maximal Square(最大正方形)

    Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

    Example:    
        Input: 
            1 0 1 0 0
            1 0 1 1 1
            1 1 1 1 1
            1 0 0 1 0
        Output: 4

    https://leetcode.com/problems/maximal-square/
    """
    if len(matrix) == 0: return 0

    f = [[0] * len(matrix[0]) for i in range(len(matrix))]
    res = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 or j == 0 or int(matrix[i][j]) == 0:
                f[i][j] = int(matrix[i][j])
            else:
                f[i][j] = min(f[i-1][j-1], f[i][j-1], f[i-1][j]) + 1
            res = max(res, f[i][j])

    return res * res

print maximal_square([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])

def test_maximal_square_1():
    assert 4 == maximal_square([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
