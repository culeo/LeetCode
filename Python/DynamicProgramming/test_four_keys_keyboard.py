# coding: utf-8

def max_a(n):
    """
    651. 4 Keys Keyboard(四键键盘)

    Imagine you have a special keyboard with the following keys:
    Key 1: (A): Print one 'A' on screen.
    Key 2: (Ctrl-A): Select the whole screen.
    Key 3: (Ctrl-C): Copy selection to buffer.
    Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.
    Now, you can only press the keyboard for N times (with the above four keys), 
    find out the maximum numbers of 'A' you can print on screen.

    Note:
        1 <= N <= 50
        Answers will be in the range of 32-bit signed integer.
    
    Example:
        Input: N = 3
        Output: 3
        Explanation: 
            We can at most get 3 A's on screen by pressing following key sequence:
            A, A, A

    https://leetcode.com/problem/4-keys-keyboard/
    https://www.lintcode.com/problem/4-keys-keyboard/description
    """
    f = list()
    f.append(0)
    f.append(1)
    f.append(2)
    f.append(3)

    for k in range(4, n + 1):
        f.append(k)
        for i in range(1, k - 3 + 1):
            f[k] = max(f[k], f[i] * (k - i - 1))
    print f
    return f[n]

def test_max_a_1():
    assert 9 == max_a(7)