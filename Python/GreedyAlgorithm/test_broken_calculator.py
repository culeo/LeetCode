# coding: utf-8

def broken_calc(X, Y):
    """
    991. Broken Calculator
    
    On a broken calculator that has a number showing on its display, we can perform two operations:
        Double: Multiply the number on the display by 2, or;
        Decrement: Subtract 1 from the number on the display.
    Initially, the calculator is displaying the number X.
    Return the minimum number of operations needed to display the number Y.

    Example:
        Input: X = 2, Y = 3
        Output: 2
        Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.

    https://leetcode.com/problems/broken-calculator/
    """
    ans = 0

    while X < Y:

        ans += 1
        if Y & 1 == 1:
            ans += 1
            Y += 1

        Y = Y / 2

    ans += (X - Y)

    return ans

print broken_calc(1, 1000000000)

def test_broken_calc_1():
    assert 2 == broken_calc(X = 2, Y = 3)

def test_broken_calc_2():
    assert 2 == broken_calc(X = 5, Y = 8)

def test_broken_calc_3():
    assert 3 == broken_calc(X = 3, Y = 10)

def test_broken_calc_4():
    assert 1023 == broken_calc(X = 1024, Y = 1)

def test_broken_calc_4():
    assert 39 == broken_calc(X = 1, Y = 1000000000)

