# coding: utf-8

def array_rank_transform(arr):
    """
    1331. Rank Transform of an Array

    Given an array of integers arr, replace each element with its rank.
    The rank represents how large the element is. The rank has the following rules:
        1. Rank is an integer starting from 1.
        2. The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
        3. Rank should be as small as possible.

    Example:
        Input: arr = [40,10,20,30]
        Output: [4,1,2,3]
        Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

    https://leetcode.com/problems/rank-transform-of-an-array/
    """

    idxs = {k: v + 1 for v, k in enumerate(sorted(set(arr)))}
    
    return map(idxs.get, arr)

print array_rank_transform([40,10,20,30])

def test_array_rank_transform_1():
    assert [4,1,2,3] == array_rank_transform([40,10,20,30])

def test_array_rank_transform_2():
    assert [1,1,1] == array_rank_transform([100,100,100])

def test_array_rank_transform_3():
    assert [5,3,4,2,8,6,7,1,3] == array_rank_transform([37,12,28,9,100,56,80,5,12])