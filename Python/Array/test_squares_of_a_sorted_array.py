# coding: utf-8

def sorted_squares(A):
    """
    977. Squares of a Sorted Array
    
    Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, 
    also in sorted non-decreasing order.

    Example:
        Input: [-4,-1,0,3,10]
        Output: [0,1,9,16,100]

    https://leetcode.com/problems/squares-of-a-sorted-array/
    """
    return sorted([x * x for x in A])

print sorted_squares([-4,-1,0,3,10])

def test_sorted_squares_1():
    assert [0,1,9,16,100] == sorted_squares([-4,-1,0,3,10])

def test_sorted_squares_2():
    assert [4,9,9,49,121] == sorted_squares([-7,-3,2,3,11])

    