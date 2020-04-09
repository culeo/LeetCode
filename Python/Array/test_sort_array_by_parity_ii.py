# coding: utf-8

def sort_array_by_parity_ii(A):
    """
    922. Sort Array By Parity II

    Given an array A of non-negative integers, half of the integers in A are odd, 
    and half of the integers are even.
    Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
    You may return any answer array that satisfies this condition.

    Example:
        Input: [4,2,5,7]
        Output: [4,5,2,7]
        Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
    
    https://leetcode.com/problems/sort-array-by-parity-ii/
    """
    i, j = 0, 1
    size = len(A)
    
    while True:
        while i < size and A[i] & 1 == 0:
            i += 2
        while j < size and A[j] & 1 == 1:
            j += 2

        if i < size and j < size:
            A[i], A[j] = A[j], A[i]
        else:
            break
            
    return A
            
print sort_array_by_parity_ii([4,2,5,7])

def test_sort_array_by_parity_ii_1():
    assert [4,5,2,7] == sort_array_by_parity_ii([4,2,5,7])