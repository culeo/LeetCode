# coding: utf-8

def robot_sim(commands, obstacles):
    """
    874. Walking Robot Simulation
    
    A robot on an infinite grid starts at point (0, 0) and faces north.  
    The robot can receive one of three possible types of commands:
        -2: turn left 90 degrees
        -1: turn right 90 degrees
        1 <= x <= 9: move forward x units
    Some of the grid squares are obstacles. 
    The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])
    If the robot would try to move onto them, the robot stays on the previous grid square instead 
    (but still continues following the rest of the route.)
    Return the square of the maximum Euclidean distance that the robot will be from the origin.

    Example 1:
        Input: commands = [4,-1,3], obstacles = []
        Output: 25
        Explanation: robot will go to (3, 4)

    https://leetcode.com/problems/walking-robot-simulation/
    """
    x_offset = [0, 1, 0, -1]
    y_offset = [1, 0, -1, 0]

    direction = 0

    obstacleSet = set(map(tuple, obstacles))
    x, y = 0, 0
    ans = 0

    for command in commands:
        if command == -1:
            direction = (direction + 1) % 4
        elif command == -2:
            direction = (direction - 1) % 4
        else:
            for i in range(command):
                if (x + x_offset[direction], y + y_offset[direction]) in obstacleSet:
                    break

                x += x_offset[direction]
                y += y_offset[direction]
            ans = max(ans, x * x + y * y)
        
    return ans
    
print robot_sim(commands = [4,-1,4,-2,4], obstacles = [[2,4]])

def test_robot_sim_1():
    assert 25 == robot_sim(commands = [4,-1,3], obstacles = [])

def test_robot_sim_2():
    assert 65 == robot_sim(commands = [4,-1,4,-2,4], obstacles = [[2,4]])