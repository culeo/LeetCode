# coding: utf-8

def is_match(s, p):
    """
    10. Regular Expression Matching(正则匹配)

    Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
        1. '.' Matches any single character.
        2. '*' Matches zero or more of the preceding element.
        3. The matching should cover the entire input string (not partial).
    Note:
        s could be empty and contains only lowercase letters a-z.
        p could be empty and contains only lowercase letters a-z, and characters like . or *.
    

    """

    n = len(s)
    m = len(p)

    f = [[False] * (m + 1) for i in range(n+1)]
    f[0][0] = True

    for j in range(2, m+1):
        f[0][j] = f[0][j-2] if p[j-1] == '*' else False

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == p[j-1] or p[j-1] == '.':
                f[i][j] = f[i-1][j-1]

            elif p[j-1] == '*':
                f[i][j] = f[i][j-2] or ((s[i-1] == p[j-2] or p[j-2] == '.') and f[i-1][j])
    print f
    return f[-1][-1]

print is_match("abc", ".*")

def test_is_match_1():
    assert True == is_match("aab", "c*a*b")

def test_is_match_2():
    assert False == is_match("a", ".*..a*")

def  test_is_match_3():
    assert False == is_match("ab", ".*c")