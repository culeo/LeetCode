# coding: utf-8

def max_product(nums):
    """
    152. Maximum Product Subarray(求最大子数组乘积)

    Given an integer array nums, find the contiguous subarray within an array (containing at least one number) 
    which has the largest product.

    Example:
        Input: [2,3,-2,4]
        Output: 6
        Explanation: [2,3] has the largest product 6.

    https://leetcode.com/problems/maximum-product-subarray/
    """
    if len(nums) < 2: return nums[0]

    l = len(nums)
    fa = list()
    fb = list()
    fa.append(nums[0])
    fb.append(nums[0])
    m = nums[0]

    for i in range(1, l):
        fa.append(max(nums[i], fa[i-1] * nums[i], fb[i-1] * nums[i]))
        fb.append(min(nums[i], fb[i-1] * nums[i], fa[i-1] * nums[i]))
    
        m = max(m, fa[i], fb[i], fb[i-1] * nums[i])

    return m

print max_product([2,-5,-2,-4,3])

def test_max_product_1():
    assert 6 == max_product([2,3,-2,4])

def test_max_product_2():
    assert 0 == max_product([-2,0,-1])

def test_max_product_3():
    assert 2 == max_product([0, 2])

def test_max_product_4():
    assert 24 == max_product([-2,3,-4])

def test_max_product_5():
    assert 108 == max_product([-1,-2,-9,-6])

def test_max_product_6():
    assert 24 == max_product([2,-5,-2,-4,3])