# coding: utf-8

def str_without_3a3b(A, B):
    """
    984. String Without AAA or BBB

    Given two integers A and B, return any string S such that:
    S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
        1. The substring 'aaa' does not occur in S;
        2. The substring 'bbb' does not occur in S.

    Example:
        Input: A = 1, B = 2
        Output: "abb"
        Explanation: "abb", "bab" and "bba" are all correct answers.

    https://leetcode.com/problems/string-without-aaa-or-bbb/
    """
    a, b = 'a', 'b'
    if B > A:
        A, B = B, A
        a, b = b, a
    
    ans = ""
    while A > 0 or B > 0:
        if A > 0:
            ans += a
            A -= 1
        if A > B:
            ans += a
            A -= 1
        if B > 0:
            ans += b
            B -= 1

    return ans

print str_without_3a3b(A = 3, B = 3)

def test_str_without_3a3b_1():
    assert 'bab' == str_without_3a3b(A = 1, B = 2)

def test_str_without_3a3b_2():
    assert 'aabaa' == str_without_3a3b(A = 4, B = 1)

def test_str_without_3a3b_3():
    assert 'bbabbab' == str_without_3a3b(A = 2, B = 5)