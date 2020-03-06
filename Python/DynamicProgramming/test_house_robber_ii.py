# coding: utf-8

def rob(nums):
    """
    213. House Robber II(打家劫舍II)

    You are a professional robber planning to rob houses along a street. 
    Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
    That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security 
    system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
    Given a list of non-negative integers representing the amount of money of each house, 
    determine the maximum amount of money you can rob tonight without alerting the police.

    Example 1:
        Input: [2,3,2]
        Output: 3   
        Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
                     because they are adjacent houses.

    https://leetcode.com/problems/house-robber-ii/
    """ 
    
    n = len(nums)
    if n == 0: return 0
    if n == 1: return nums[0]

    fa = list()
    fb = list()
    if len(nums) > 0:
        fa.append(nums[0])
        fb.append(0)
    if len(nums) > 1:
        fa.append(max(nums[0], nums[1]))
        fb.append(nums[1])

    m = max(fa[1], fb[1])

    for i in range(2, n):
        if (i == n - 1):
            fa.append(max(nums[i] + fb[i - 2], fa[i - 1]))
            fb.append(max(nums[i] + fb[i - 2], fa[i - 1]))
        else:
            print i, nums[i], fa, fb
            fa.append(max(nums[i] + fa[i - 2], fa[i - 1]))
            fb.append(max(nums[i] + fb[i - 2], fb[i - 1]))
        
        m = max(fa[i], fb[i], m)

    return m

print rob([4,1,2,7,5,3,1])

def test_rob_1():
    assert 3 == rob([2,3,2])

def test_rob_2():
    assert 4 == rob([1,2,3,1])

def test_rob_3():
    assert 0 == rob([])

def test_rob_4():
    assert 2 == rob([2,1])

def test_rob_5():
    assert 14 == rob([4,1,2,7,5,3,1])