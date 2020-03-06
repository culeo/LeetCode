# coding: utf-8

def num_decodings(s):
    """
    639. Decode Ways II

    A message containing letters from A-Z is being encoded to numbers using the following mapping way:
    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
    Beyond that, now the encoded string can also contain the character '*', 
    which can be treated as one of the numbers from 1 to 9.
    Given the encoded message containing digits and the character '*', return the total number of ways to decode it.
    Also, since the answer may be very large, you should return the output mod 109 + 7.

    Example 1:
        Input: "*"
        Output: 9
        Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".

    https://leetcode.com/problems/decode-ways-ii/
    """
    if s == "0": return 0
    
    f = list()
    f.append(1)
    f.append(0 if s[0] == "0" else 9 if s[0] == "*" else 1)

    m = long(1e9 + 7)
    print m
    for i in range(2, len(s) + 1):
        f.append(0)
        if s[i-1] == "*": 
            f[i] = (f[i] + f[i-1] * 9) % m
            if s[i-2] == "*":
                f[i] = (f[i] + f[i-2] * 15) % m
            if s[i-2] == "1":
                f[i] = (f[i] + f[i-2] * 9) % m
            if s[i-2] == "2":
                f[i] = (f[i] + f[i-2] * 6) % m
        else:
            if s[i-1] != "0": 
                f[i] = (f[i] + f[i-1]) % m

            if s[i-2] == "*":
                if int(s[i-1]) < 7:
                    f[i] = (f[i] + f[i-2] * 2) % m
                else:
                    f[i] = (f[i] + f[i-2]) % m
            
            else:
                num = int(s[i-2:i])
                if num > 9 and num < 27:
                    f[i] = (f[i] + f[i-2]) % m

    print f
    return f[len(s)]

def test_num_decodings_1():
    assert 9 == num_decodings("*")

def test_num_decodings_2():
    assert 18 == num_decodings("1*")

def test_num_decodings_3():
    assert 96 == num_decodings("**")

def test_num_decodings_4():
    assert 0 == num_decodings("0")

def test_num_decodings_5():
    assert 0 == num_decodings("01")

def test_num_decodings_6():
    assert 1 == num_decodings("101")

def test_num_decodings_7():
    assert 1 == num_decodings("110")