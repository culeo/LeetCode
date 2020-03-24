# coding: utf-8

import math

def minimum_swap(s1, s2):
    """
    1247. Minimum Swaps to Make Strings Equal

    You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. 
    Your task is to make these two strings equal to each other. 
    You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].
    Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

    Example:
        Input: s1 = "xx", s2 = "yy"
        Output: 1
        Explanation: 
            Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".
        
    https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/
    """
    xy_ctn= 0
    yx_ctn = 0
    
    for i in range(len(s1)):
        if s1[i] == 'x' and s2[i] == 'y':
            xy_ctn += 1
        elif s1[i] == 'y' and s2[i] == 'x':
            yx_ctn += 1

    if (xy_ctn + yx_ctn) & 1 == 1: return -1
    
    return int(math.ceil(xy_ctn/2.0) + math.ceil(yx_ctn/2.0))

print minimum_swap(s1 = "xx", s2 = "yy")

def test_minimum_swap_1():
    assert 1 == minimum_swap(s1 = "xx", s2 = "yy")

def test_minimum_swap_2():
    assert 2 == minimum_swap(s1 = "xy", s2 = "yx")

def test_minimum_swap_3():
    assert -1 == minimum_swap(s1 = "xx", s2 = "xy")

def test_minimum_swap_4():
    assert 4 == minimum_swap(s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx")