# coding: utf-8

def largest_sum_after_k_negations(A, K):
    """
    1005. Maximize Sum Of Array After K Negations

    Given an array A of integers, we must modify the array in the following way: 
    we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  
    (We may choose the same index i multiple times.)
    Return the largest possible sum of the array after modifying it in this way.

    Example 1:
        Input: A = [4,2,3], K = 1
        Output: 5
        Explanation: Choose indices (1,) and A becomes [4,-2,3].

    https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
    """
    if len(A) == 0: return 0
    
    A.sort()
    
    i = 0        
    while K - i != 0 and i < len(A):
        if A[i] >= 0:
            break
        A[i] = -A[i]
        i += 1

    if (K - i) % 2 == 0:
        return sum(A)
    else:
        return sum(A) - 2 * min(A)      

print largest_sum_after_k_negations([2,-3,-1,5,-4], 2)

def test_largest_sum_after_k_negations_1():
    assert 5 == largest_sum_after_k_negations(A = [4,2,3], K = 1)

def test_largest_sum_after_k_negations_2():
    assert 6 == largest_sum_after_k_negations(A = [3,-1,0,2], K = 3)

def test_largest_sum_after_k_negations_3():
    assert 13 == largest_sum_after_k_negations(A = [2,-3,-1,5,-4], K = 2)