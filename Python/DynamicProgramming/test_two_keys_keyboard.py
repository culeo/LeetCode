# coding: utf-8

def min_steps(n):
    """
    650. 2 Keys Keyboard(两键盘)

    Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:
    Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
    Paste: You can paste the characters which are copied last time.
    Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. 
    Output the minimum number of steps to get n 'A'.

    Example 1:
        Input: 3
        Output: 3
        Explanation:
            Intitally, we have one character 'A'.
            In step 1, we use Copy All operation.
            In step 2, we use Paste operation to get 'AA'.
            In step 3, we use Paste operation to get 'AAA'.
    
    https://leetcode.com/problems/2-keys-keyboard/
    """
    f = list()
    f.append(0)
    f.append(0)
    for k in range(2, n+1):
        f.append(k)
        for i in range(1, k/2):
            if k % i == 0:
                f[k] = min(f[k], f[i] + k / i)
                
    return f[n]


def test_min_steps_1():
    assert 3 == min_steps(3)

def test_min_steps_6():
    assert 5 == min_steps(5)