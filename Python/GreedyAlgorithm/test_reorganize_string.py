# coding: utf-8

import collections
import heapq

def reorganize_string(S):
    """
    767. Reorganize String

    Given a string S, check if the letters can be rearranged so that two characters that are adjacent 
    to each other are not the same.
    If possible, output any possible result.  If not possible, return the empty string.

    Example:
        Input: S = "aab"
        Output: "aba"

    https://leetcode.com/problems/reorganize-string/
    """
    pq = [(-S.count(x), x) for x in set(S)]
    max_cnt = (len(S) + 1) / 2
    
    if any(-cnt > max_cnt for cnt, _ in pq): return ""

    ans = ""
    heapq.heapify(pq)

    while len(pq) > 1:
        cnt1, c1 = heapq.heappop(pq)
        cnt2, c2 = heapq.heappop(pq)
        ans += c1
        ans += c2
        if cnt1 < -1: heapq.heappush(pq, (cnt1 + 1, c1))
        if cnt2 < -1: heapq.heappush(pq, (cnt2 + 1, c2))

    return ans + (pq[0][1] if pq else "")

print reorganize_string("abbabbaaab")

def test_reorganize_string_1():
    assert "aba" == reorganize_string("aab")

def test_reorganize_string_2():
    assert "" == reorganize_string("aaab")

def test_reorganize_string_3():
    assert "ababababab" == reorganize_string("abbabbaaab")