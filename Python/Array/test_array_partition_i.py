# coding: utf-8

def array_pair_sum(nums):
    """
    561. Array Partition I
    
    Given an array of 2n integers, your task is to group these integers into n pairs of integer, 
    say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to 
    n as large as possible.

    Example:
        Input: [1,4,3,2]
        Output: 4
        Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

    https://leetcode.com/problems/array-partition-i/
    """
    return sum(sorted(nums)[::2])

print array_pair_sum([1,4,3,2])

def test_array_pair_sum_1():
    assert 4 == array_pair_sum([1,4,3,2])