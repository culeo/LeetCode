# coding: utf-8

def find_number_of_LIS(nums):
    """
    673. Number of Longest Increasing Subsequence(最长上升子序列个数)

    Given an unsorted array of integers, find the number of longest increasing subsequence.

    Example:
        Input: [1,3,5,4,7]
        Output: 2
        Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].

    https://leetcode.com/problems/number-of-longest-increasing-subsequence/
    """
    
    if len(nums) < 2: return len(nums)

    fl = list()
    fl.append(1)

    fc = list()
    fc.append(1)
    
    for j in range(1, len(nums)):
        count = 1
        max_l = 1

        for i in range(j):
            if nums[i] < nums[j]:
                if max_l < fl[i] + 1:
                    max_l = max(max_l, fl[i] + 1)
                    count = fc[i]
                elif max_l == fl[i] + 1:
                    count += fc[i]

        fl.append(max_l)
        fc.append(count)
    print fc
    longest = max(fl)
    return sum(fc[i] for i in range(len(fl)) if fl[i] == longest)

print find_number_of_LIS([1,1,1,2,2,2,3,3,3])

def test_find_number_of_LIS_1():
    assert 2 == find_number_of_LIS([1,3,5,4,7])

def test_find_number_of_LIS_2():
    assert 5 == find_number_of_LIS([2,2,2,2,2])

def test_find_number_of_LIS_2():
    assert 3 == find_number_of_LIS([1,2,4,3,5,4,7,2])

def test_find_number_of_LIS_2():
    assert 27 == find_number_of_LIS([1,1,1,2,2,2,3,3,3])
    