# coding: utf-8

def reconstruct_matrix(upper, lower, colsum):
    """
    1253. Reconstruct a 2-Row Binary Matrix
    
    Given the following details of a matrix with n columns and 2 rows :
        The matrix is a binary matrix, which means each element in the matrix can be 0 or 1.
        The sum of elements of the 0-th(upper) row is given as upper.
        The sum of elements of the 1-st(lower) row is given as lower.
        The sum of elements in the i-th column(0-indexed) is colsum[i], where colsum is given 
        as an integer array with length n.
    Your task is to reconstruct the matrix with upper, lower and colsum.
    Return it as a 2-D integer array.
    If there are more than one valid solution, any of them will be accepted.
    If no valid solution exists, return an empty 2-D array.

    Example:
        Input: upper = 2, lower = 1, colsum = [1,1,1]
        Output: [[1,1,0],[0,0,1]]
        Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.
    
    https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/
    """
    ans = [[],[]]
    
    for val in colsum:
        if val == 0: 
            ans[0].append(0)
            ans[1].append(0)
        elif val == 2:
            upper -= 1
            lower -= 1
            ans[0].append(1)
            ans[1].append(1)
        else:
            if upper > lower:
                upper -= 1
                ans[0].append(1)
                ans[1].append(0)
            else:
                lower -= 1
                ans[0].append(0)
                ans[1].append(1)
    
    return ans if upper == 0 and lower == 0 else []

print reconstruct_matrix(upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1])

def test_reconstruct_matrix_1():
    assert [[1,0,1],[0,1,0]] == reconstruct_matrix(upper = 2, lower = 1, colsum = [1,1,1])

def test_reconstruct_matrix_2():
    assert [] == reconstruct_matrix(upper = 2, lower = 3, colsum = [2,2,1,1])
    
def test_reconstruct_matrix_3():
    assert [[1, 0, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 1, 0, 0]] == reconstruct_matrix(upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1])
    