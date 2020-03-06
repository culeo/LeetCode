# coding: utf-8

def word_break(s, wordDict):
    """
    139. Word Break(单词分解问题)

    Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
    determine if s can be segmented into a space-separated sequence of one or more dictionary words.

    Note:
        The same word in the dictionary may be reused multiple times in the segmentation.
        You may assume the dictionary does not contain duplicate words.
    
    Example :
        Input: s = "leetcode", wordDict = ["leet", "code"]
        Output: true
        Explanation: Return true because "leetcode" can be segmented as "leet code".

    https://leetcode.com/problems/word-break/
    """

    f = [False] * len(s)

    for i in range(len(s)):
        f[i] = s[0:i+1] in wordDict
        if f[i]: continue

        for k in range(1, i+1):
            f[i] = f[k-1] and (s[k:i+1] in wordDict)
            if f[i]: break

    return f[len(s) - 1]

def test_word_break_1():
    assert True == word_break("leet", ["leet", "code"])

def test_word_break_2():
    assert True == word_break("applepen", ["apple", "pen"])

def test_word_break_3():
    assert False == word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])