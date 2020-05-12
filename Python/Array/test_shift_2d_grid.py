# coding: utf-8

def shift_grid(grid, k):
    """
    1260. Shift 2D Grid 

    Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
    In one shift operation:
        Element at grid[i][j] moves to grid[i][j + 1].
        Element at grid[i][n - 1] moves to grid[i + 1][0].
        Element at grid[m - 1][n - 1] moves to grid[0][0].
        Return the 2D grid after applying shift operation k times.

    Example:
        Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
        Output: [[9,1,2],[3,4,5],[6,7,8]]
    
    https://leetcode.com/problems/shift-2d-grid/
    """
    m = len(grid)
    n = len(grid[0])
    
    k = k % (m * n)
    
    lt = [grid[i][j] for i in range(m)  for j in range(n)]
    lt = lt[-k:] + lt[:-k]
    
    return [[lt[i * n + j] for j in range(n)] for i in range(m)]

print shift_grid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1)

def test_shift_grid_1():
    assert [[9,1,2],[3,4,5],[6,7,8]] == shift_grid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1)

def test_shift_grid_2():
    assert [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]] == shift_grid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4)

def test_shift_grid_3():
    assert [[1,2,3],[4,5,6],[7,8,9]] == shift_grid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9)
