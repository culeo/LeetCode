# coding: utf-8

def find_length_of_LCIS(nums):
    """
    674. Longest Continuous Increasing Subsequence(最长连续递增序列)

    Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

    Example 1:
        Input: [1,3,5,4,7]
        Output: 3
        Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
                     Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 
                     are separated by 4. 

    https://leetcode.com/problems/longest-continuous-increasing-subsequence/
    """
    if len(nums) < 1: return 0

    f = list()
    f.append(1)

    for i in range(1, len(nums)):
        if (nums[i] > nums[i-1]):
            f.append(f[i-1] + 1)
        else:
            f.append(1)

    return max(f)

print find_length_of_LCIS([2,3,1])

def test_find_length_of_LCIS_1():
    assert 3 == find_length_of_LCIS([1,3,5,4,7])

def test_find_length_of_LCIS_2():
    assert 1 == find_length_of_LCIS([2,2,2,2,2])

def test_find_length_of_LCIS_3():
    assert 2 == find_length_of_LCIS([2,3,1])