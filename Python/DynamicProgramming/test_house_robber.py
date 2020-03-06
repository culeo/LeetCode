# coding: utf-8

def rob(nums):
    """
    198. House Robber(打家劫舍问题)
        
    You are a professional robber planning to rob houses along a street. 
    Each house has a certain amount of money stashed, the only constraint stopping 
    you from robbing each of them is that adjacent houses have security system connected 
    and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given a list of non-negative integers representing the amount of money of each house, 
    determine the maximum amount of money you can rob tonight without alerting the police.
    
    Example:
        Input: [1,2,3,1]
        Output: 4
        Explanation:
            Rob house 1 (money = 1) and then rob house 3 (money = 3).
            Total amount you can rob = 1 + 3 = 4.

    https://leetcode.com/problems/house-robber/
    """ 
    if len(nums) == 0: return 0
        
    f = list()
    if len(nums) > 0: f.append(nums[0])
    if len(nums) > 1: f.append(max(nums[0], nums[1]))

    for idx in range(2, len(nums)):
        f.append(max(nums[idx] + f[idx - 2], f[idx - 1]))
    return f[len(nums) - 1]

def test_rob_1():
    assert 4 == rob([1,2,3,1])

def test_rob_2():
    assert 12 == rob([2,7,9,3,1])

def test_rob_3():
    assert 2 == rob([2,1])