# coding: utf-8

def sort_array_by_parity(A):
    """
    905. Sort Array By Parity
    
    Given an array A of non-negative integers, return an array consisting of all the even elements of A, 
    followed by all the odd elements of A.
    You may return any answer array that satisfies this condition.

    Example:
        Input: [3,1,2,4]
        Output: [2,4,3,1]
        The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

    https://leetcode.com/problems/sort-array-by-parity/
    """
    j = 0

    for i in range(0, len(A)):
        if A[i] & 1 == 0:
            A[j], A[i] = A[i], A[j]
            j += 1

    return A
            
print sort_array_by_parity([3,1,2,4])

def test_sort_array_by_parity_1():
    assert [2,4,3,1] == sort_array_by_parity([3,1,2,4])