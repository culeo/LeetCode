# coding: utf-8

def max_depth_after_split(seq):
    """
    1111. Maximum Nesting Depth of Two Valid Parentheses Strings

    A string is a valid parentheses string (denoted VPS) if and only if it consists of "(" and ")" 
    characters only, and:
        It is the empty string, or
        It can be written as AB (A concatenated with B), where A and B are VPS's, or
        It can be written as (A), where A is a VPS.
    We can similarly define the nesting depth depth(S) of any VPS S as follows:
        depth("") = 0
        depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's
        depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
    For example,  "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), 
    and ")(" and "(()" are not VPS's.
    Given a VPS seq, split it into two disjoint subsequences A and B, such that A and B are VPS's 
    (and A.length + B.length = seq.length).
    Now choose any such A and B such that max(depth(A), depth(B)) is the minimum possible value.
    Return an answer array (of length seq.length) that encodes such a choice of A and B:  
        answer[i] = 0 if seq[i] is part of A, else answer[i] = 1.  
        Note that even though multiple answers may exist, you may return any of them.

    Example:
        Input: seq = "(()())"
        Output: [0,1,1,1,1,0]

    https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
    """
    ans = [0] * len(seq)

    for i, c in enumerate(seq):
        if c == '(':
            ans[i] = i & 1
        else:
            ans[i] = 1 - (i & 1)

    return ans

print max_depth_after_split("()(())()")

def test_max_depth_after_split_1():
    assert [0,1,1,1,1,0] == max_depth_after_split("(()())")

def test_max_depth_after_split_2():
    assert [0,0,0,1,1,0,0,0] == max_depth_after_split("()(())()")


