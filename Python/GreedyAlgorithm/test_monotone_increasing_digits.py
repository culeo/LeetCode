# coding: utf-8

def monotone_increasing_digits(N):
    """
    738. Monotone Increasing Digits(单调递增数字)
    
    Given a non-negative integer N, find the largest number that is less than or equal to 
    N with monotone increasing digits.
    (Recall that an integer has monotone increasing digits if and only if each pair of 
    adjacent digits x and y satisfy x <= y.)
        
    Example 1:
        Input: N = 10
        Output: 9

    https://leetcode.com/problems/monotone-increasing-digits/
    """
    st = str(N)

    j = len(st)
    for i in range(len(st) - 1, 0, -1):
        if int(st[i]) < int(st[i-1]):
            st = st[:i-1] + str(int(st[i-1]) - 1) + st[i:]
            j = i

    res = st[:j]
    for i in range(j, len(st)):
        res += '9'
        
    return int(res)

print monotone_increasing_digits(332)

def test_monotone_increasing_digits_1():
    assert 9 == monotone_increasing_digits(10)

def test_monotone_increasing_digits_2():
    assert 1234 == monotone_increasing_digits(1234)

def test_monotone_increasing_digits_3():
    assert 299 == monotone_increasing_digits(332)