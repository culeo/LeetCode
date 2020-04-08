# coding: utf-8

import collections

def find_lucky(arr):
    """
   1394. Find Lucky Integer in an Array

    Given an array of integers arr, a lucky integer is an integer which has a frequency 
    in the array equal to its value.
    Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. 
    If there is no lucky integer return -1.

    Example:
        Input: arr = [2,2,3,4]
        Output: 2
        Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

    https://leetcode.com/problems/find-lucky-integer-in-an-array/
    """
    return max([num for num, cnt in collections.Counter(arr).items() if num == cnt] or [-1])

print find_lucky([2,2,3,4])

def test_find_lucky_1():
    assert 2 == find_lucky([2,2,3,4])

def test_find_lucky_2():
    assert 3 == find_lucky([1,2,2,3,3,3])

def test_find_lucky_3():
    assert -1 == find_lucky([2,2,2,3,3])