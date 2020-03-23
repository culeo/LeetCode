# coding: utf-8

import collections

def min_set_size(arr):
    """
    1338. Reduce Array Size to The Half

    Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers 
    in the array.
    Return the minimum size of the set so that at least half of the integers of the array are removed.

    Example:
        Input: arr = [3,3,3,3,5,5,5,2,2,7]
        Output: 2
        Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 
            (i.e equal to half of the size of the old array).
            Possible sets of size 2 are {3,5},{3,2},{5,2}.
            Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] 
            which has size greater than half of the size of the old array.
            
    https://leetcode.com/problems/reduce-array-size-to-the-half/
    """
    counts = [count for num, count in collections.Counter(arr).items()]

    ans = 0
    rc = 0
  
    for c in counts:
        rc += c
        ans += 1
        if rc >= len(arr)/2.0: break
    
    return ans

print min_set_size([3,3,3,3,5,5,5,2,2,7])

def test_min_set_size_1():
    assert 2 == min_set_size([3,3,3,3,5,5,5,2,2,7])

def test_min_set_size_2():
    assert 1 == min_set_size([7,7,7,7,7,7])

def test_min_set_size_3():
    assert 1 == min_set_size([1,9])

def test_min_set_size_4():
    assert 1 == min_set_size([1000,1000,3,7])

def test_min_set_size_5():
    assert 5 == min_set_size([1,2,3,4,5,6,7,8,9,10])