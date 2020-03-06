# coding: utf-8

def largest_divisible_subset(nums):
    """
    368. Largest Divisible Subset(最大可整除的子集合)

    Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) 
    of elements in this subset satisfies:
        Si % Sj = 0 or Sj % Si = 0.
    If there are multiple solutions, return any subset is fine.

    Example :
        Input: [1,2,3]
        Output: [1,2] (of course, [1,3] will also be ok)
    
    https://leetcode.com/problems/largest-divisible-subset/
    """

    if len(nums) < 2: return nums
    
    nums = sorted(nums)
    N = len(nums)

    f = [1] * N
    pi = [0] * N
    mx = 1
    mx_idx = 0

    for i in range(N):
        for j in range(i-1, -1, -1):
            if nums[i] % nums[j] == 0 and f[i] < f[j] + 1:
                f[i] = f[j] + 1
                pi[i] = j
                if mx < f[i]:
                    mx = f[i]
                    mx_idx = i

    res = list()
    for k in range(mx):
        res.append(nums[mx_idx])
        mx_idx = pi[mx_idx]

    return res[::-1]

print largest_divisible_subset([546,669])

def test_largest_divisible_subset_1():
    assert [1,2] == largest_divisible_subset([1,2,3])

def test_largest_divisible_subset_2():
    assert [1,2,4,8] == largest_divisible_subset([1,2,4,8])

def test_largest_divisible_subset_3():
    assert [546] == largest_divisible_subset([546,669])