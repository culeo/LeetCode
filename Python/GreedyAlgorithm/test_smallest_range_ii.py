# coding: utf-8

def smallest_range_ii(A, K):
    """
    910. Smallest Range II

    Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, 
    and add x to A[i] (only once).
    After this process, we have some array B.
    Return the smallest possible difference between the maximum value of B and the minimum value of B.

    Example:
        Input: A = [1,3,6], K = 3
        Output: 3
        Explanation: B = [4,6,3]
    
    https://leetcode.com/problems/smallest-range-ii/
    """
    A.sort()
    ans = A[-1] - A[0]
    for i in range(len(A) - 1):
        ans = min(ans, max(A[-1] - K, A[i] + K) - min(A[0] + K, A[i+1] - K))

    return ans

print smallest_range_ii(A = [1,3,6], K = 3)

def test_smallest_range_ii_1():
    assert 0 == smallest_range_ii(A = [1], K = 0)

def test_smallest_range_ii_2():
    assert 6 == smallest_range_ii(A = [0,10], K = 2)

def test_smallest_range_ii_3():
    assert 3 == smallest_range_ii(A = [1,3,6], K = 3)
