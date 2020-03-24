# coding: utf-8

def check_valid_string(s):
    """
    678. Valid Parenthesis String(验证括号字符串)

    Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this 
    string is valid. We define the validity of a string by these rules:
        1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
        2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
        3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
        4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
        5. An empty string is also valid.

    Example:
        Input: "(*))"
        Output: True
    
    https://leetcode.com/problems/valid-parenthesis-string/
    """
    
    n = len(s)

    if n == 0: return True
    if n == 1: return True if s[0] == '*' else False

    f = list([set([0])])
   
    for i in range(1, n + 1):
        c = s[i-1]
        if c == '(':
            f.append(set([v+1 for v in f[i-1]]))
        elif c == ')':
            f.append(set([v-1 for v in f[i-1] if v > 0]))
        elif c == '*':
            f.append(set([v+1 for v in f[i-1]]) |
                     set([v-1 for v in f[i-1] if v > 0]) |
                     f[i-1])

    return 0 in f[n]

print check_valid_string('(((******))')

def test_check_valid_string_1():
    assert False == check_valid_string(')()')

def test_check_valid_string_2():
    assert True == check_valid_string('()')

def test_check_valid_string_3():
    assert True == check_valid_string('(*))')

def test_check_valid_string_4():
    assert True == check_valid_string('(*)')

def test_check_valid_string_5():
    assert True == check_valid_string('(((******))')