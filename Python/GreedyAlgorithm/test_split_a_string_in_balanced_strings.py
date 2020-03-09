# coding: utf-8

def balanced_string_split(s):
    """
    1221. Split a String in Balanced Strings

    Balanced strings are those who have equal quantity of 'L' and 'R' characters.
    Given a balanced string s split it in the maximum amount of balanced strings.
    Return the maximum amount of splitted balanced strings.

    Example 1:
        Input: s = "RLRRLLRLRL"
        Output: 4
        Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

    https://leetcode.com/problems/split-a-string-in-balanced-strings/
    """
    split = 0
    length  = 0

    for c in s:
        if c == 'L':
            length += 1
        else:
            length -= 1
        if length == 0:
            split += 1
    
    return split

print balanced_string_split("RLRRRLLRLL")

def test_balanced_string_split_1():
    assert 4 == balanced_string_split("RLRRLLRLRL")

def test_balanced_string_split_2():
    assert 3 == balanced_string_split("RLLLLRRRLR")

def test_balanced_string_split_3():
    assert 1 == balanced_string_split("LLLLRRRR")

def test_balanced_string_split_4():
    assert 2 == balanced_string_split("RLRRRLLRLL")