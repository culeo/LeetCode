# coding: utf-8

def length_of_LIS(nums):
    """
    300. Longest Increasing Subsequence(最长上升子序列)

    Given an unsorted array of integers, find the length of longest increasing subsequence.

    Example:
        Input: [10,9,2,5,3,7,101,18]
        Output: 4 
        Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

    https://leetcode.com/problems/longest-increasing-subsequence/
    """
    if len(nums) == 0: return 0

    f = list()
    f.append(1)
    for i in range(1, len(nums)):
        f.append(1)
        for k in range(i):
            if nums[i] > nums[k]:
                f[i] = max(f[i], f[k] + 1)
    return max(f)

def test_length_of_LIS_1():
    assert 4 == length_of_LIS([10,9,2,5,3,7,101,18])

def test_length_of_LIS_2():
    assert 6 == length_of_LIS([1,3,6,7,9,4,10,5,6])