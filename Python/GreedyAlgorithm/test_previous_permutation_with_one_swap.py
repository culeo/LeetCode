# coding: utf-8

def prev_perm_opt1(A):
    """
    1053. Previous Permutation With One Swap

    Given an array A of positive integers (not necessarily distinct), return the lexicographically 
    largest permutation that is smaller than A, that can be made with one swap (A swap exchanges 
    the positions of two numbers A[i] and A[j]).  If it cannot be done, then return the same array.

    Example 1:
        Input: [3,2,1]
        Output: [3,1,2]
        Explanation: Swapping 2 and 1.

    https://leetcode.com/problems/previous-permutation-with-one-swap/
    """
    target_idx = -1
    
    for i in range(len(A) - 1, 0, -1):
        if A[i] < A[i-1]:
            target_idx = i - 1
            break
    
    if target_idx == -1: return A

    source_idx = target_idx + 1
    for i in range(source_idx + 1, len(A)):
        if  A[i-1] < A[i] < A[target_idx]:
            source_idx = i
            
    A[source_idx], A[target_idx] = A[target_idx], A[source_idx]
    
    return A

print prev_perm_opt1([3,1,1,3])

def test_prev_perm_opt1_1():
    assert [3,1,2] == prev_perm_opt1([3,2,1])

def test_prev_perm_opt1_2():
    assert [1,1,5] == prev_perm_opt1([1,1,5])

def test_prev_perm_opt1_3():
    assert [1,7,4,6,9] == prev_perm_opt1([1,9,4,6,7])

def test_prev_perm_opt1_4():
    assert [1,3,1,3] == prev_perm_opt1([3,1,1,3])