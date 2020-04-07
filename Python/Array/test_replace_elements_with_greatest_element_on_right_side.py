# coding: utf-8

def replace_elements(arr):
    """
    1299. Replace Elements with Greatest Element on Right Side

    Given an array arr, replace every element in that array with the greatest element among 
    the elements to its right, and replace the last element with -1.
    After doing so, return the array.

    Example:
        Input: arr = [17,18,5,4,6,1]
        Output: [18,6,6,6,1,-1]
    
    https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
    """
    max_num = -1
    
    for i in range(len(arr) - 1, -1, -1):
        arr[i], max_num = max_num, max(arr[i], max_num)
        
    return arr

print replace_elements([17,18,5,4,6,1])

def test_replace_elements_1():
    assert [18,6,6,6,1,-1] == replace_elements([17,18,5,4,6,1])