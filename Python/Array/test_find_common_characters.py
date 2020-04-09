# coding: utf-8

def common_chars(A):
    """
    1002. Find Common Characters
    
    Given an array A of strings made only from lowercase letters, 
    return a list of all characters that show up in all strings within the list (including duplicates).  
    For example, if a character occurs 3 times in all strings but not 4 times, 
    you need to include that character three times in the final answer.
    You may return the answer in any order.

    Example 1:
        Input: ["bella","label","roller"]
        Output: ["e","l","l"]

    https://leetcode.com/problems/find-common-characters
    """

    return reduce(lambda x, y: x + y, [[c] * min(string.count(c) for string in A) for c in set(A[0])])
        
print common_chars(["bella","label","roller"])

def test_common_chars_1():
    assert ["e","l","l"] == common_chars(["bella","label","roller"])

def test_common_chars_2():
    assert ["c","o"] == common_chars(["cool","lock","cook"])
