# coding: utf-8

def longest_palindrome(s):
    """
    5. Longest Palindromic Substring(最长回文子串)

    Given a string s, find the longest palindromic substring in s. 
    You may assume that the maximum length of s is 1000.

    Example:
        Input: "babad"
        Output: "bab"

    Note: "aba" is also a valid answer.
    
    https://leetcode.com/problems/longest-palindromic-substring/
    """
    length = len(s)
    if length == 0: return ''
    if length == 1: return s[0]

    begin = 0
    end = 0

    f = [ [0] * length for i in range(length) ]
    for idx in range(length):
        f[idx][idx] = 1
        if idx < length - 1 and s[idx] == s[idx+1]:
            begin = idx
            end = idx + 1
            f[idx][idx+1] = 1

    for l in range(3, length + 1):
        for i in range(0, length - l + 1):
            j = l + i - 1
            if s[i] == s[j] and f[i+1][j-1] == 1:
                f[i][j] = 1
                begin = i
                end = j

    return s[begin: end+1]

def test_longest_palindrome_1():
    assert "aba" == longest_palindrome("babad")

def test_longest_palindrome_2():
    assert "bb" == longest_palindrome("cbbd")