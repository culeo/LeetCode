# coding: utf-8

def partition_labels(S):
    """
    763. Partition Labels

    A string S of lowercase letters is given. We want to partition this string into as 
    many parts as possible so that each letter appears in at most one part, 
    and return a list of integers representing the size of these parts.

    Example:
        Input: S = "ababcbacadefegdehijhklij"
        Output: [9,7,8]
        Explanation:
            The partition is "ababcbaca", "defegde", "hijhklij".
            This is a partition so that each letter appears in at most one part.
            A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
    
    https://leetcode.com/problems/partition-labels/
    """

    ans = list()
    begin = 0

    while begin < len(S):
        end = S.rfind(S[begin], begin + 1)
        if end == -1:
            ans.append(1)
            begin += 1
        else:
            mid = begin + 1
            while mid <= end:
                end = max(end, S.rfind(S[mid], mid + 1))
                mid += 1
            ans.append(end - begin + 1)
            begin = mid

    return ans

print partition_labels("ababcbacadefegdehijhklij")

def test_partition_labels_1():
    assert [9, 7, 8] == partition_labels("ababcbacadefegdehijhklij")