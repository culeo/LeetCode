# coding: utf-8

def lucky_numbers (matrix):
    """
    1380. Lucky Numbers in a Matrix
    
    Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
    A lucky number is an element of the matrix such that it is the minimum element in its row and 
    maximum in its column.

    Example:
        Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
        Output: [15]
        Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column

    https://leetcode.com/problems/lucky-numbers-in-a-matrix/submissions/
    """
    m, n = len(matrix), len(matrix[0])
    
    row_min = set([min(x) for x in matrix])
    col_max = set([max(x) for x in zip(*matrix)])
    
    ans = list(row_min & col_max)
    
    return ans

print lucky_numbers([[3,7,8],[9,11,13],[15,16,17]])

def test_lucky_numbers_1():
    assert [15] == lucky_numbers([[3,7,8],[9,11,13],[15,16,17]])

def test_lucky_numbers_2():
    assert [12] == lucky_numbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]])

def test_lucky_numbers_3():
    assert [7] == lucky_numbers([[7,8],[1,2]])