# coding: utf-8

def max_sum_sub_array(nums):
    """
    53. Maximum Subarray(连续子数组的最大和问题)
    
    Given an integer array nums, find the contiguous subarray (containing at least one number) 
    which has the largest sum and return its sum.

    Example:
        Input: [-2,1,-3,4,-1,2,1,-5,4],
        Output: 6
        Explanation: 
            [4,-1,2,1] has the largest sum = 6.
    """
    f = list()
    f.append(nums[0])

    for idx in range(1, len(nums)):
        f.append(max(f[idx-1] + nums[idx], nums[idx]))

    return max(f)

def test_max_sum_sub_array_1():
    assert 6 == max_sum_sub_array([-2,1,-3,4,-1,2,1,-5,4])