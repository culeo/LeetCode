# coding: utf-8

def minimum_abs_difference(arr):
    """
    1200. Minimum Absolute Difference

    Given an array of distinct integers arr, find all pairs of elements with the minimum absolute 
    difference of any two elements. 
    Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
        a, b are from arr
        a < b
        b - a equals to the minimum absolute difference of any two elements in arr

    Example:
        Input: arr = [4,2,1,3]
        Output: [[1,2],[2,3],[3,4]]
        Explanation: The minimum absolute difference is 1. 
            List all pairs with difference equal to 1 in ascending order.
    
    https://leetcode.com/problems/minimum-absolute-difference/
    """
    arr.sort()
    min_dis = arr[1] - arr[0]
    ans = [[arr[0], arr[1]]]
    
    for i in range(2, len(arr)):
        if arr[i] - arr[i-1] < min_dis:
            min_dis = arr[i] - arr[i-1]
            ans = [[arr[i-1], arr[i]]]
        elif arr[i] - arr[i-1] == min_dis:
            ans.append([arr[i-1], arr[i]])

    return ans

print minimum_abs_difference([4,2,1,3])

def test_minimum_abs_difference_1():
    assert [[1,2],[2,3],[3,4]] == minimum_abs_difference([4,2,1,3])

def test_minimum_abs_difference_2():
    assert [[1,3]] == minimum_abs_difference([1,3,6,10,15])

def test_minimum_abs_difference_3():
    assert [[-14,-10],[19,23],[23,27]] == minimum_abs_difference([3,8,-10,23,19,-4,-14,27])

