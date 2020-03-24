# coding: utf-8

import math

def combination_sum(nums, target):
    """
    377. Combination Sum IV(组合数Ⅳ)
    
    Given an integer array with all positive numbers and no duplicates, 
    find the number of possible combinations that add up to a positive integer target.

    Example:
        nums = [1, 2, 3]
        target = 4
        The possible combination ways are:
        (1, 1, 1, 1)
        (1, 1, 2)
        (1, 2, 1)
        (1, 3)
        (2, 1, 1)
        (2, 2)
        (3, 1)
        Note that different sequences are counted as different combinations.
        Therefore the output is 7.
    
    https://leetcode.com/problems/combination-sum-iv/
    """
    if len(nums) < 1: return 0

    f = list()
    f.append(1)
 
    for k in range(1, target + 1):
        f.append(0)
        for num in nums:
            if num <= k:
                f[k] += f[k-num]

    return f[target]

print combination_sum([1,2,3], 4)

def test_combination_sum_1():
    assert 7 == combination_sum([1,2,3], 4)