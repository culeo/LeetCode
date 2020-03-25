# coding: utf-8

import collections

def is_possible_divide(nums, k):
    """
    1296. Divide Array in Sets of K Consecutive Numbers

    Given an array of integers nums and a positive integer k, find whether it's possible to divide this array 
    into sets of k consecutive numbers
    Return True if its possible otherwise return False.

    Example:
        Input: nums = [1,2,3,3,4,4,5,6], k = 4
        Output: true
        Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].

    https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
    """
    cnts = collections.Counter(nums)
 
    for num in sorted(cnts):
        cnt = cnts[num]
        if cnt > 0:
            for i in range(num + 1, num + k):
                cnts[i] -= cnt
                if cnts[i] < 0: return False
    
    return True

print is_possible_divide(nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3)

def test_is_possible_divide_1():
    assert True == is_possible_divide(nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3)

def test_is_possible_divide_2():
    assert True == is_possible_divide(nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3)

def test_is_possible_divide_3():
    assert True == is_possible_divide(nums = [3,3,2,2,1,1], k = 3)

def test_is_possible_divide_4():
    assert False == is_possible_divide(nums = [1,2,3,4], k = 3)

