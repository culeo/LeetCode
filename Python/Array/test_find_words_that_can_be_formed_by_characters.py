# coding: utf-8

import collections

def count_characters(words, chars):
    """
    1160. Find Words That Can Be Formed by Characters 

    You are given an array of strings words and a string chars.
    A string is good if it can be formed by characters from chars 
    (each character can only be used once).
    Return the sum of lengths of all good strings in words.

    Example:
        Input: words = ["cat","bt","hat","tree"], chars = "atach"
        Output: 6
        Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

    https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
    """
    cnts = collections.Counter(chars)
    ans = 0
    
    for word in words:
        find = True
        for c, cnt in collections.Counter(word).items():
            if cnts[c] < cnt:
                find = False
                break
        if find: ans += len(word)
    
    return ans

print count_characters(words = ["cat","bt","hat","tree"], chars = "atach")

def test_count_characters_1():
    assert 6 == count_characters(words = ["cat","bt","hat","tree"], chars = "atach")

def test_count_characters_2():
    assert 10 == count_characters(words = ["hello","world","leetcode"], chars = "welldonehoneyr")
