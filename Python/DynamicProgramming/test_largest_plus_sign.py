# coding: utf-8

def order_of_largest_plus_sign(N, mines):
    """
    764. Largest Plus Sign(最大加号长度)

    In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the given list mines which are 0.
    What is the largest axis-aligned plus sign of 1s contained in the grid? Return the order of the plus sign. If there is none, return 0.
    An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up, 
    down, left, and right, and made of 1s. This is demonstrated in the diagrams below. Note that there could be 0s or 1s beyond the arms 
    of the plus sign, only the relevant area of the plus sign is checked for 1s.
    Examples of Axis-Aligned Plus Signs of Order k:
        00000
        00100
        01110
        00100
        00000

    Example:
        Input: N = 5, mines = [[4, 2]]
        Output: 2
        Explanation:
            11111
            11111
            11111
            11111
            11011    

    https://leetcode.com/problems/largest-plus-sign/
    """
    f = [[N] * N for i in range(N)]
    for mine in mines:
        f[mine[0]][mine[1]] = 0

    for i in range(N):
        l, r, u, d = 0, 0, 0, 0
        for j in range(N):
            l = l + 1 if f[i][j] > 0 else 0
            u = u + 1 if f[j][i] > 0 else 0
            r = r + 1 if f[N-i-1][N-j-1] > 0 else 0
            d = d + 1 if f[N-j-1][N-i-1] > 0 else 0

            f[i][j] = min(f[i][j], l)
            f[j][i] = min(f[j][i], u)
            f[N-i-1][N-j-1] = min(f[N-i-1][N-j-1], r)
            f[N-j-1][N-i-1] = min(f[N-j-1][N-i-1], d)
            
    res = 0
    for i in range(N):
        res = max(res, max(f[i]))

    return res

print order_of_largest_plus_sign(5, [[4,2]])

def test_order_of_largest_plus_sign_1():
    assert 2 == order_of_largest_plus_sign(5, [[4,2]])