# coding: utf-8

import collections

def find_special_integer(arr):
    """
    1287. Element Appearing More Than 25% In Sorted Array
    
    Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that 
    occurs more than 25% of the time.
    Return that integer.

    Example:
        Input: arr = [1,2,2,6,6,6,6,7,10]
        Output: 6

    https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
    """
    
    total = len(arr)
    
    for k, v in collections.Counter(arr).items():
        if (v / (total * 1.0)) > 0.25: return k
    
    return arr[0]

print find_special_integer([1,2,2,6,6,6,6,7,10])

def test_find_special_integer_1():
    assert 6 == find_special_integer([1,2,2,6,6,6,6,7,10])