# coding: utf-8

def can_complete_circuit(gas, cost):
    """
    134. Gas Station
    
    There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
    You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to 
    its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
    Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, 
    otherwise return -1.
    
    Note:
        If there exists a solution, it is guaranteed to be unique.
        Both input arrays are non-empty and have the same length.
        Each element in the input arrays is a non-negative integer.

    Example:
        Input: 
            gas  = [1,2,3,4,5]
            cost = [3,4,5,1,2]
        Output: 3
        Explanation:
            Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
            Travel to station 4. Your tank = 4 - 1 + 5 = 8
            Travel to station 0. Your tank = 8 - 2 + 1 = 7
            Travel to station 1. Your tank = 7 - 3 + 2 = 6
            Travel to station 2. Your tank = 6 - 4 + 3 = 5
            Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
            Therefore, return 3 as the starting index.
        
    https://leetcode.com/problems/gas-station/
    """
    diff_sum = 0
    max_diff = 0
    start_idx = 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        diff_sum += diff
        if diff_sum <= max_diff: 
            start_idx = i
            max_diff = diff_sum

    start_idx = (start_idx + 1) % len(gas)

    return start_idx if sum(gas) >= sum(cost) else -1

print can_complete_circuit(gas = [3,1,1], cost = [1,2,2])

def test_can_complete_circuit_1():
    assert 3 == can_complete_circuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2])

def test_can_complete_circuit_2():
    assert -1 == can_complete_circuit(gas = [2,3,4], cost = [3,4,3])

def test_can_complete_circuit_3():
    assert 3 == can_complete_circuit(gas = [7,1,0,11,4], cost = [5,9,1,2,5])

def test_can_complete_circuit_4():
    assert 0 == can_complete_circuit(gas = [3,1,1], cost = [1,2,2])

    

