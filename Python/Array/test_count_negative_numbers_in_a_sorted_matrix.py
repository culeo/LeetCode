# coding: utf-8

def count_negatives(grid):
    """
    1351. Count Negative Numbers in a Sorted Matrix

    Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 
    Return the number of negative numbers in grid.

    Example:
        Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
        Output: 8
        Explanation: There are 8 negatives number in the matrix.

    https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
    """

    m, n = len(grid), len(grid[0])
    row, col =  0, n - 1
    ans = 0
    
    while row < m:
        if grid[row][col] < 0 and col >= 0:
            col -= 1
            ans += (m - row)
        else:
            row += 1
    
    return ans

print count_negatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])

def test_count_negatives_1():
    assert 8 == count_negatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])

def test_count_negatives_2():
    assert 0 == count_negatives([[3,2],[1,0]])

def test_count_negatives_3():
    assert 3 == count_negatives([[1,-1],[-1,-1]])

def test_count_negatives_4():
    assert 1 == count_negatives([[-1]])

    