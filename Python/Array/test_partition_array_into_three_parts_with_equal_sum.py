# coding: utf-8

import collections

def can_three_parts_equal_sum(A):
    """
    1013. Partition Array Into Three Parts With Equal Sum
    
    Given an array A of integers, return true if and only if we can partition the array into 
    three non-empty parts with equal sums.
    Formally, we can partition the array if we can find indexes i+1 < j with 
    (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

    Example:
        Input: A = [0,2,1,-6,6,-7,9,1,2,0,1]
        Output: true
        Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

    https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
    """

    total = sum(A)
    if total % 3 != 0: return False

    target = total // 3
    time = 0

    for a in A:
        if time == 2: return True

        target -= a
        if target == 0:
            time += 1
            target = total // 3

    return False

 
print can_three_parts_equal_sum([1,-1,1,-1])

def test_can_three_parts_equal_sum_1():
    assert True == can_three_parts_equal_sum([0,2,1,-6,6,-7,9,1,2,0,1])

def test_can_three_parts_equal_sum_2():
    assert False == can_three_parts_equal_sum([0,2,1,-6,6,7,9,-1,2,0,1])

def test_can_three_parts_equal_sum_3():
    assert True == can_three_parts_equal_sum([3,3,6,5,-2,2,5,1,-9,4])

def test_can_three_parts_equal_sum_4():
    assert False == can_three_parts_equal_sum([1,-1,1,-1])