# coding: utf-8

def longest_palindrome_subseq(s):
    """
    516. Longest Palindromic Subsequence(最长回文的子序列)

    Given a string s, find the longest palindromic subsequence's length in s.
    You may assume that the maximum length of s is 1000.

    Example 1:
        Input: "bbbab"
        Output: 4
        
    One possible longest palindromic subsequence is "bb".

    https://leetcode.com/problems/longest-palindromic-subsequence/
    """
    n = len(s)
    if n < 2: return n
    
    ml = 1

    f = [[0] * (n + 1) for i in range(n + 1)]

    for j in range(1, n):
        f[j][j] = 1
        for i in range(j - 1, -1, -1):
            if s[i] == s[j]:
                f[i][j] = f[i+1][j-1] + 2
            else:
                f[i][j] = max(f[i][j-1], f[i+1][j])

    return f[0][n-1]

def test_longest_palindrome_subseq_1():
    assert 4 == longest_palindrome_subseq("bbbab")

def test_longest_palindrome_subseq_2():
    assert 2 == longest_palindrome_subseq("cbbd")

def test_longest_palindrome_subseq_3():
    assert 7 == longest_palindrome_subseq("abcabcabcabc") 