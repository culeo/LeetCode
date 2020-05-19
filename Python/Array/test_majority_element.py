# coding: utf-8

def majority_element(nums):
    """
    169. Majority Element
    
    Given an array of size n, find the majority element. The majority element is the element that appears more 
    than ⌊ n/2 ⌋ times.
    You may assume that the array is non-empty and the majority element always exist in the array.

    Example:
        Input: [3,2,3]
        Output: 3
    
    https://leetcode.com/problems/majority-element/submissions/
    """

    return sorted(nums)[len(nums)//2]

print majority_element([3,2,3])

def test_majority_element_1():
    assert 3 == majority_element([3,2,3])

def test_majority_element_2():
    assert 2 == majority_element([2,2,1,1,1,2,2])