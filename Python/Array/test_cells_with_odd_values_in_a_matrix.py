# coding: utf-8

def odd_cells(n, m, indices):
    """
    1252. Cells with Odd Values in a Matrix

    Given n and m which are the dimensions of a matrix initialized by zeros and given an array 
    indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all 
    cells in row ri and column ci by 1.
    Return the number of cells with odd values in the matrix after applying the increment to all indices.

    Example:
        Input: n = 2, m = 3, indices = [[0,1],[1,1]]
        Output: 6
        Explanation: Initial matrix = [[0,0,0],[0,0,0]].
            After applying first increment it becomes [[1,2,1],[0,1,0]].
            The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.
        
    https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
    """
    rows = [0] * n
    cols = [0] * m
    
    for r, c in indices:
        rows[r] ^= 1
        cols[c] ^= 1
    
    odd_rows = sum(rows)
    odd_cols = sum(cols)
    
    return odd_rows * (m - odd_cols) + odd_cols * (n - odd_rows)

print odd_cells(n = 2, m = 3, indices = [[0,1],[1,1]])

def test_odd_cells_1():
    assert 6 == odd_cells(n = 2, m = 3, indices = [[0,1],[1,1]])

def test_odd_cells_2():
    assert 0 == odd_cells(n = 2, m = 2, indices = [[1,1],[0,0]])
