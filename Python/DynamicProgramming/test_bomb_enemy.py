# coding: utf-8

def max_killed_enemies(grid):
    """
    361	Bomb Enemy(炸弹袭击)

    Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), 
    return the maximum enemies you can kill using one bomb.
    The bomb kills all the enemies in the same row and column from the planted point until it hits the 
    wall since the wall is too strong to be destroyed.

    Example:
        Input:
            grid =[
                "0E00",
                "E0WE",
                "0E00"
            ]
        Output: 3
        Explanation:
            Placing a bomb at (1,1) kills 3 enemies

    https://leetcode.com/problems/bomb-enemy
    https://www.lintcode.com/problem/bomb-enemy/description
    """
    if len(grid) == 0 or len(grid[0]) == 0: return 0

    n = len(grid)
    m = len(grid[0])


    f = [[[0] * m for j in range(n)] for i in range(4)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] != 'W':
                if grid[i][j] == 'E':
                    f[0][i][j] = 1
                    f[1][i][j] = 1
                if i > 0:
                    f[1][i][j] += f[1][i-1][j]
                if j > 0:
                    f[0][i][j] += f[0][i][j-1]
    
            k, z = n-i-1, m-j-1
            
            if grid[k][z] != 'W':
                if grid[k][z] == 'E':
                    f[2][k][z] = 1
                    f[3] [k][z]= 1
                if k < n-1:
                    f[3][k][z] += f[3][k+1][z]
                if z < m-1:
                    f[2] [k][z]+= f[2][k][z+1]

    res = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '0':
                t = f[0][i][j] + f[1][i][j] + f[2][i][j] + f[3][i][j]
                res = max(res, t)

    return res

print max_killed_enemies(["0E00","E0WE","0E00"])

def test_max_killed_enemies_1():
    assert 3 == max_killed_enemies(["0E00","E0WE","0E00"])

def test_max_killed_enemies_2():
    assert 2 == max_killed_enemies(["0E00", "EEWE", "0E00"])