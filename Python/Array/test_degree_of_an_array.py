# coding:  utf-8

import collections

def find_shortest_sub_array(nums):
    """
    697. Degree of an Array
    
    Given a non-empty array of non-negative integers nums, the degree of this array is defined as the 
    maximum frequency of any one of its elements.
    Your task is to find the smallest possible length of a (contiguous) subarray of nums, 
    that has the same degree as nums.

    Example:
        Input: [1, 2, 2, 3, 1]
        Output: 2
        Explanation: 
            The input array has a degree of 2 because both elements 1 and 2 appear twice.
            Of the subarrays that have the same degree:
            [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
            The shortest length is 2. So return 2.

    https://leetcode.com/problems/degree-of-an-array/
    """

    left, right, count = {}, {}, {}
    for i, num in enumerate(nums):
        if num not in left: left[num] = i
        right[num] = i
        count[num] = count.get(num, 0) + 1
    
    degree = max(count.values())
    ans = len(nums)

    for num in count:
        if count[num] == degree:
            ans = min(ans, right[num] - left[num] + 1)

    return ans

print find_shortest_sub_array([1,2,2,3,1,4,2])

def test_find_shortest_sub_array_1():
    assert 2 == find_shortest_sub_array([1,2,2,3,1])

def test_find_shortest_sub_array_2():
    assert 6 == find_shortest_sub_array([1,2,2,3,1,4,2])

def test_find_shortest_sub_array_3():
    assert 7 == find_shortest_sub_array([2,1,1,2,1,3,3,3,1,3,1,3,2])