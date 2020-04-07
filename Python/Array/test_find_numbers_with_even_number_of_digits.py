# coding: utf-8

def find_numbers(nums):
    """
    1295. Find Numbers with Even Number of Digits

    Given an array nums of integers, return how many of them contain an even number of digits.
    
    Example:
        Input: nums = [12,345,2,6,7896]
        Output: 2
        Explanation: 
            12 contains 2 digits (even number of digits). 
            345 contains 3 digits (odd number of digits). 
            2 contains 1 digit (odd number of digits). 
            6 contains 1 digit (odd number of digits). 
            7896 contains 4 digits (even number of digits). 
            Therefore only 12 and 7896 contain an even number of digits.
    
    https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
    """
    ans = 0
    for num in nums:
        if len(str(num)) & 1 == 0:
            ans += 1 
    return ans

print find_numbers([12,345,2,6,7896])

def test_find_numbers_1():
    assert 2 == find_numbers([12,345,2,6,7896])

def test_find_numbers_2():
    assert 1 == find_numbers([555,901,482,1771])
