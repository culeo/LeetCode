# coding: utf-8

from bisect import bisect_left
from bisect import bisect_right

def find_the_distance_value(arr1, arr2, d):
    """
    1385. Find the Distance Value Between Two Arrays

    Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.
    The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] 
    where |arr1[i]-arr2[j]| <= d.

    Example:
        Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
        Output: 2
        Explanation: 
            For arr1[0]=4 we have: 
            |4-10|=6 > d=2 
            |4-9|=5 > d=2 
            |4-1|=3 > d=2 
            |4-8|=4 > d=2 
            For arr1[1]=5 we have: 
            |5-10|=5 > d=2 
            |5-9|=4 > d=2 
            |5-1|=4 > d=2 
            |5-8|=3 > d=2
            For arr1[2]=8 we have:
            |8-10|=2 <= d=2
            |8-9|=1 <= d=2
            |8-1|=7 > d=2
            |8-8|=0 <= d=2

    https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
    """
    
    arr2.sort()
    
    return sum([bisect_left(arr2, num - d) == bisect_right(arr2, num + d) for num in arr1])

print find_the_distance_value(arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3)

def test_find_the_distance_value_1():
    assert 2 == find_the_distance_value(arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3)

def test_find_the_distance_value_2():
    assert 1 == find_the_distance_value(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6)

