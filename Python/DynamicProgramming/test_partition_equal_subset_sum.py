# coding: utf-8

def can_partition(nums):
    """
    416. Partition Equal Subset Sum(相同子集和分割)
    Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets 
    such that the sum of elements in both subsets is equal.
    Note:
        Each of the array element will not exceed 100.
        The array size will not exceed 200.

    Example 1:
        Input: [1, 5, 11, 5]
        Output: true
        Explanation: The array can be partitioned as [1, 5, 5] and [11].

    https://leetcode.com/problems/partition-equal-subset-sum/
    """
    s = sum(n for n in nums)
    
    if s % 2 != 0: return False
    t = s / 2
    f = [False] * (t + 1)
    f[0] = True

    for num in nums:
       for k in range(t, num-1, -1):
           f[k] = f[k] or f[k-num]

    return f[t]

print can_partition([23,13,11,7,6,5,5])

def test_can_partition_1():
    assert True == can_partition([1,5,11,5])

def test_can_partition_2():
    assert True == can_partition([3,3,3,4,5])

def test_can_partition_3():
    assert False == can_partition([1, 5, 11, 3])

def test_can_partition_4():
    assert True == can_partition([23,13,11,7,6,5,5])