# coding: utf-8

import collections

def group_the_people(groupSizes):
    """
    1282. Group the People Given the Group Size They Belong To

    There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. 
    Given the array groupSizes of length n telling the group size each person belongs to, 
    return the groups there are and the people's IDs each group includes.
    You can return any solution in any order and the same applies for IDs. 
    Also, it is guaranteed that there exists at least one solution. 

    Example:
        Input: groupSizes = [3,3,3,3,3,1,3]
        Output: [[5],[0,1,2],[3,4,6]]
        Explanation: 
            Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].

    https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
    """
    groups = collections.defaultdict(list)
    for ID, size in enumerate(groupSizes):
        groups[size].append(ID)

    ans = list()
    for size, ids in groups.items():
        for i in range(0, len(ids), size):
            ans.append(ids[i: i+size])

    return ans

print group_the_people([3,3,3,3,3,1,3])

def test_group_the_people_1():
    assert [[5],[0,1,2],[3,4,6]] == group_the_people([3,3,3,3,3,1,3])

def test_group_the_people_2():
    assert [[1],[0,5],[2,3,4]] == group_the_people([2,1,3,3,3,2])
