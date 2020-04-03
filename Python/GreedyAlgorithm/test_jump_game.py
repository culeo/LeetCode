# coding: utf-8

# coding: utf-8

def can_jump(nums):
    """
    55. Jump Game

    Given an array of non-negative integers, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Determine if you are able to reach the last index.

    Example:
        Input: [2,3,1,1,4]
        Output: true
        Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
    
    https://leetcode.com/problems/jump-game/
    """
    end_idx = len(nums)
    max_idx = 1
    cur_idx = 0
    while cur_idx < max_idx and cur_idx < end_idx:
        max_idx = max(max_idx, cur_idx + nums[cur_idx] + 1)
        cur_idx += 1

    return max_idx >= end_idx

print can_jump([0,1])

def test_can_jump_1():
    assert True == can_jump([2,3,1,1,4])

def test_can_jump_2():
    assert False == can_jump([3,2,1,0,4])

def test_can_jump_3():
    assert False == can_jump([0,1])

    