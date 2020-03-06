# coding: utf-8

def min_window(S, T):
    """
    727	Minimum Window Subsequence(最小的窗口子序列)

    Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.
    If there is no such window in S that covers all characters in T, return the empty string "". 
    If there are multiple such minimum-length windows, return the one with the smallest starting index.
        All the strings in the input will only contain lowercase letters.
        The length of S will be in the range [1, 20000].
        The length of T will be in the range [1, 100].
    
    Example:
        Input：S = "abcdebdde"， T = "bde"
        Output："bcde"
        Explanation："bcde" is the answer and "deb" is not a smaller window because the elements of T in the window must occur in order.

    https://leetcode.com/problems/minimum-window-subsequence
    https://www.lintcode.com/problem/minimum-window-subsequence/description
    """
    N = len(S)
    M = len(T)

    if N == 0: return ''
    if M == 0: return ''

    f = [[-1] * M for i in range(N)]

    for i in range(N): 
        if S[i] == T[0]:
            f[i][0] = i
        
    for j in range(1, M):
        k = -1
        for i in range(N):
            if k != -1 and S[i] == T[j]:
                f[i][j] = k
            if f[i][j-1] != -1:
                k = f[i][j-1]

    st, longest = -1, 0x7FFFFF
    for i in range(N):
        if f[i][M-1] != -1 and i -  f[i][M-1] + 1 < longest:
            longest = i -  f[i][M-1] + 1
            st = f[i][M-1]
    
    return S[st: st + longest] if st != -1 else ''

print min_window('cnhczmccqouqadqtmjjzl', 'mm')

def test_min_window_1():
    assert '' == min_window('jmeqksfrsdcmsiwvaovztaqenprpvnbstl', 'u')

def test_min_window_2():
    assert 'bcde'== min_window('abcdebdde', 'bde')

def test_min_window_3():
    assert 'mccqouqadqtm' == min_window('cnhczmccqouqadqtmjjzl', 'mm')