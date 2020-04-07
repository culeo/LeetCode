# coding: utf-8

def remove_k_digits(num, k):
    """
    402. Remove K Digits

    Given a non-negative integer num represented as a string, remove k digits from the number so that the 
    new number is the smallest possible.
    Note:
        The length of num is less than 10002 and will be ≥ k.
        The given num does not contain any leading zero.
    
    Example:
        Input: num = "1432219", k = 3
        Output: "1219"
        Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
    
    https://leetcode.com/problems/remove-k-digits/
    """
    stack = []
    for digit in num:
        while k and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
            
    stack = stack[:-k] if k else stack

    return "".join(stack).lstrip('0') or "0"

print remove_k_digits(num = "9", k = 1)

def test_remove_k_digits_1():
    assert "1219" == remove_k_digits(num = "1432219", k = 3)

def test_remove_k_digits_2():
    assert "200" == remove_k_digits(num = "10200", k = 1)

def test_remove_k_digits_3():
    assert "0" == remove_k_digits(num = "10", k = 2)

def test_remove_k_digits_4():
    assert "0" == remove_k_digits(num = "9", k = 1)