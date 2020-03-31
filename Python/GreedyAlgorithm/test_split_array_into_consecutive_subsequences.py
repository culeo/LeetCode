# coding: utf-8

import collections

def is_possible(nums):
    """
    659. Split Array into Consecutive Subsequences 

    Given an array nums sorted in ascending order, return true if and only if you can split 
    it into 1 or more subsequences such that each subsequence consists of consecutive integers 
    and has length at least 3.

    Example:
        Input: [1,2,3,3,4,5]
        Output: True
        Explanation:
            You can split them into two consecutive subsequences : 
            1, 2, 3
            3, 4, 5

    https://leetcode.com/problems/split-array-into-consecutive-subsequences/
    """
    cnts  = collections.Counter(nums)
    tails = collections.Counter()

    for num in nums:
        if cnts[num] == 0: continue
        if tails[num] > 0:
            cnts[num] -= 1
            tails[num] -= 1
            tails[num + 1] += 1
        elif cnts[num + 1] > 0 and cnts[num + 2] > 0:
            cnts[num] -= 1
            cnts[num + 1] -= 1
            cnts[num + 2] -= 1
            tails[num + 3] += 1
        else: return False

    return True
   

print is_possible([1,2,3,7,8,9])

def test_is_possible_1():
    assert True == is_possible([1,2,3,3,4,5])

def test_is_possible_2():
    assert True == is_possible([1,2,3,3,4,4,5,5])

def test_is_possible_3():
    assert False == is_possible([1,2,3,4,4,5])