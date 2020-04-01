# coding: utf-8

def wiggle_max_length(nums):
    """
    376. Wiggle Subsequence
    
    A sequence of numbers is called a wiggle sequence if the differences between successive numbers 
    strictly alternate between positive and negative. The first difference (if one exists) 
    may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.
    For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive 
    and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its 
    first two differences are positive and the second because its last difference is zero.
    Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. 
    A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original 
    sequence, leaving the remaining elements in their original order.

    Example:
        Input: [1,7,4,9,2,5]
        Output: 6
        Explanation: The entire sequence is a wiggle sequence.
    
    https://leetcode.com/problems/wiggle-subsequence/
    """
    if len(nums) < 2: return len(nums)
    
    pre_diff = nums[1] - nums[0]
    ans = 1 if pre_diff == 0 else 2
    for i in range(2, len(nums)):
        diff = nums[i] - nums[i-1]
        if ((diff > 0 and pre_diff <= 0) or (diff < 0 and pre_diff >= 0)):
            ans += 1
            pre_diff = diff
    
    return ans

print wiggle_max_length([1,7,4,9,2,5])

def test_wiggle_max_length_1():
    assert 6 == wiggle_max_length([1,7,4,9,2,5])

def test_wiggle_max_length_2():
    assert 7 == wiggle_max_length([1,17,5,10,13,15,10,5,16,8])

def test_wiggle_max_length_3():
    assert 2 == wiggle_max_length([1,2,3,4,5,6,7,8,9])

def test_wiggle_max_length_4():
    assert 1 == wiggle_max_length([0,0])

def test_wiggle_max_length_5():
    assert 1 == wiggle_max_length([0,0,0])
