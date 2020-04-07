# coding: utf-8

def min_time_to_visit_all_points(points):
    """
    1266. Minimum Time Visiting All Points
    
    On a plane there are n points with integer coordinates points[i] = [xi, yi]. 
    Your task is to find the minimum time in seconds to visit all points.
    You can move according to the next rules:
        1. In one second always you can either move vertically, horizontally by one unit or diagonally 
        (it means to move one unit vertically and one unit horizontally in one second).
        2. You have to visit the points in the same order as they appear in the array.
    
    Example:
        Input: points = [[1,1],[3,4],[-1,0]]
        Output: 7
        Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
            Time from [1,1] to [3,4] = 3 seconds 
            Time from [3,4] to [-1,0] = 4 seconds
            Total time = 7 seconds
    
    https://leetcode.com/problems/minimum-time-visiting-all-points/
    """
    ans = 0
    for i in range(len(points) - 1):
        curr_point = points[i]
        next_point = points[i+1]
        diff_x = abs(curr_point[0] - next_point[0])
        diff_y = abs(curr_point[1] - next_point[1])
        ans += max(diff_x, diff_y)
    return ans

print min_time_to_visit_all_points([[1,1],[3,4],[-1,0]])

def test_min_time_to_visit_all_points_1():
    assert 7 == min_time_to_visit_all_points([[1,1],[3,4],[-1,0]])

def test_min_time_to_visit_all_points_2():
    assert 5 == min_time_to_visit_all_points([[3,2],[-2,2]])
