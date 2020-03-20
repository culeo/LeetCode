# coding: utf-8

def min_add_to_make_valid(S):
    """
    921. Minimum Add to Make Parentheses Valid

    Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', 
    and in any positions ) so that the resulting parentheses string is valid.
    Formally, a parentheses string is valid if and only if:
        It is the empty string, or
        It can be written as AB (A concatenated with B), where A and B are valid strings, or
        It can be written as (A), where A is a valid string.
    Given a parentheses string, return the minimum number of parentheses we must add to make the resulting 
    string valid.

    Example:
        Input: "())"
        Output: 1

    https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
    """
    dif = 0
    ans = 0
    
    for c in S:
        if c == '(':
            dif += 1
        else:
            dif -= 1
            if dif < 0:
                dif = 0
                ans += 1
                
    return ans + dif

print min_add_to_make_valid("())")

def test_min_add_to_make_valid_1():
    assert 1 == min_add_to_make_valid("())")

def test_min_add_to_make_valid_2():
    assert 3 == min_add_to_make_valid("(((")

def test_min_add_to_make_valid_3():
    assert 0 == min_add_to_make_valid("()")