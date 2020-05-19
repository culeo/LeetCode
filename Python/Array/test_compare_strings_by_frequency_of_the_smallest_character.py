# coding: utf-8

import bisect

def num_smaller_by_frequency(queries, words):
    """
    1170. Compare Strings by Frequency of the Smallest Character

    Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s.
    For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.
    Now, given string arrays queries and words, return an integer array answer, 
    where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

    Example 1:
        Input: queries = ["cbd"], words = ["zaaaz"]
        Output: [1]
        Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").

    https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/
    """

    word_ctn = sorted([word.count(min(word)) for word in words])
    ret= [len(word_ctn) - bisect.bisect(word_ctn, querie.count(min(querie))) for querie in queries]
        
    return ret

print num_smaller_by_frequency(queries = ["cbd"], words = ["zaaaz"])

def test_num_smaller_by_frequency_1():
    assert [1] == num_smaller_by_frequency(queries = ["cbd"], words = ["zaaaz"])

def test_num_smaller_by_frequency_2():
    assert [1, 2] == num_smaller_by_frequency(queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"])