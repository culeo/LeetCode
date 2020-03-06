# coding: utf-8

def max_coins(nums):
    """
    312. Burst Balloons(爆破气球)

    Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. 
    You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. 
    Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.
    Find the maximum coins you can collect by bursting the balloons wisely.
   
    Note:
        You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
        0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

    Example:
        Input: [3,1,5,8]
        Output: 167 
        Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
                     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

    https://leetcode.com/problems/burst-balloons/
    """
    N = len(nums)
    nums = [1] + nums + [1]

    f = [[0] * (N + 2) for i in range(N + 2)]

    for l in range(1, N + 1):
        for i in range(1, N-l+2):
            j = i + l - 1
            for k in range(i, j+1):
                f[i][j] = max(f[i][j], f[i][k - 1] + nums[i - 1] * nums[k] * nums[j + 1] + f[k + 1][j])  

    return f[1][N]
    
print max_coins([3,1,5,8])

def test_max_coins_1():
    assert 167 ==  max_coins([3,1,5,8])