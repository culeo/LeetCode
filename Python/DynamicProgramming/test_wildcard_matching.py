# coding: utf-8

def is_match(s, p):
    """
    44. Wildcard Matching(通配符匹配)

    Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
        1. '?' Matches any single character.
        2. '*' Matches any sequence of characters (including the empty sequence).

    The matching should cover the entire input string (not partial).
    Note:
        s could be empty and contains only lowercase letters a-z.
        p could be empty and contains only lowercase letters a-z, and characters like ? or *.

    Example 4:
        Input:
            s = "adceb"
            p = "*a*b"
        Output: true
        Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

    https://leetcode.com/problems/wildcard-matching/
    """
    n = len(s)
    m = len(p)

    f = [[False] * (m + 1) for i in range(n + 1)]
    f[0][0] = True

    for j in range(1, m + 1):
        f[0][j] = f[0][j-1] if p[j-1] == '*' else False
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i-1] == p[j-1] or p[j-1] == '?':
                f[i][j] = f[i-1][j-1]
            elif p[j-1] == '*':
                f[i][j] = f[i-1][j-1] or f[i][j-1] or f[i-1][j]
                
    return f[-1][-1]

print is_match("aab", "c*a*b")

def test_is_match_1():
    assert False == is_match("acdcb", "a*c?b")

def test_is_match_2():
    assert True == is_match("aa", "*")

def test_is_match_3():
    assert False == is_match("cb", "?a")

def test_is_match_4():
    assert True == is_match("adceb", "*a*b")

def test_is_match_5():
    assert False == is_match("aab", "c*a*b")