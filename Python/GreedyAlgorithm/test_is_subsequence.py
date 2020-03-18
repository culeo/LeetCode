# coding: utf-8

def is_subsequence(s, t):
    """
    392. Is Subsequence
    Given a string s and a string t, check if s is subsequence of t.
    You may assume that there is only lower case English letters in both s and t. 
    t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
    A subsequence of a string is a new string which is formed from the original string by deleting some 
    (can be none) of the characters without disturbing the relative positions of the remaining characters. 
    (ie, "ace" is a subsequence of "abcde" while "aec" is not).

    Example:
        s = "abc", t = "ahbgdc"
        Return true.

    https://leetcode.com/problems/is-subsequence/
    """
    sl = len(s)
    tl = len(t)
    
    i = 0
    j = 0
    while i < sl and j < tl:
        if s[i] == t[j]:
            i += 1
        j += 1
    
    return i == len(s)

print is_subsequence(s = "abc", t = "ahbgdc")

def test_is_subsequence_1():
    assert True == is_subsequence(s = "abc", t = "ahbgdc")

def test_is_subsequence_2():
    assert False == is_subsequence(s = "axc", t = "ahbgdc")