# coding: utf-8

def erase_overlap_intervals(intervals):
    """
    435. Non-overlapping Intervals
    
    Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest 
    of the intervals non-overlapping.

    Example:
        Input: [[1,2],[2,3],[3,4],[1,3]]
        Output: 1
        Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

    https://leetcode.com/problems/non-overlapping-intervals/
    """
    if len(intervals) == 0: return 0

    intervals.sort()
    end_val = intervals[0][1]
    ans = 0

    for i in range(1, len(intervals)):
        if end_val > intervals[i][0]:
            ans += 1
            end_val = min(end_val, intervals[i][1])
        else:
            end_val = intervals[i][1]

    return ans

print erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]])

def test_erase_overlap_intervals_1():
    assert 1 == erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]])

def test_erase_overlap_intervals_2():
    assert 2== erase_overlap_intervals([[1,2],[1,2],[1,2]])

def test_erase_overlap_intervals_3():
    assert 0 == erase_overlap_intervals([[1,2],[2,3]])

