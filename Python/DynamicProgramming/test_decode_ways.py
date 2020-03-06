# coding: utf-8

def num_decodings(s):
    """
    91. Decode Ways

    A message containing letters from A-Z is being encoded to numbers using the following mapping:
    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
    Given a non-empty string containing only digits, determine the total number of ways to decode it.

    Example 1:
        Input: "12"
        Output: 2
        Explanation: It could be decoded as "AB" (1 2) or "L" (12).

    https://leetcode.com/problems/decode-ways/
    """
    if s == "0": return 0
    
    f = list()
    f.append(1)
    f.append(0 if s[0] == "0" else 1)

    for i in range(2, len(s) + 1):
        f.append(0)
        if s[i-1] != "0":
            f[i] += f[i-1]

        num = int(s[i-2:i])
        if num > 9 and num < 27:
            f[i] += f[i-2]

    return f[len(s)]


def test_num_decodings_1():
    assert 2 == num_decodings("12")

def test_num_decodings_2():
    assert 3 == num_decodings("226")

def test_num_decodings_3():
    assert 1 == num_decodings("10")

def test_num_decodings_4():
    assert 0 == num_decodings("0")

def test_num_decodings_5():
    assert 0 == num_decodings("01")

def test_num_decodings_6():
    assert 1 == num_decodings("101")

def test_num_decodings_7():
    assert 1 == num_decodings("110")