# coding: utf-8

import collections

def count_largest_group(n):
    """
    1399. Count Largest Group
    
    Given an integer n. Each number from 1 to n is grouped according to the sum of its digits. 
    Return how many groups have the largest size.

    Example:
        Input: n = 13
        Output: 4
        Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
        [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.

    https://leetcode.com/problems/count-largest-group/
    """
    group = collections.defaultdict(int)
    largest = 0

    for i in range(1, n + 1):
        num = i
        count = 0
        while num >= 10:
            count += num % 10
            num //= 10
        count += num
        group[count] += 1
        largest = max(largest, group[count])
    
    return sum([x == largest for x in group.values()])

print count_largest_group(13)

def test_count_largest_group_1():
    assert 4 == count_largest_group(13)

def test_count_largest_group_2():
    assert 2 == count_largest_group(2)

def test_count_largest_group_3():
    assert 6 == count_largest_group(15)

def test_count_largest_group_4():
    assert 5 == count_largest_group(24)

