# coding: utf-8

import collections

def relative_sort_array(arr1, arr2):
    """
    1122. Relative Sort Array
    
    Given two arrays arr1 and arr2, the elements of arr2 are distinct, 
    and all elements in arr2 are also in arr1.
    Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  
    Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

    Example:
        Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
        Output: [2,2,2,1,4,3,3,9,6,7,19]

    https://leetcode.com/problems/relative-sort-array/
    """
    cnts = collections.Counter(arr1)
    ans = []
    
    for num in arr2:
        ans += [num] * cnts.pop(num)
    
    ans += sorted(cnts.elements())
    
    return ans

print relative_sort_array(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6])

def test_relative_sort_array_1():
    assert [2,2,2,1,4,3,3,9,6,7,19] == relative_sort_array(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6])