# coding: utf-8

def distance_between_bus_stops(distance, start, destination):
    """
    1184. Distance Between Bus Stops

    A bus has n stops numbered from 0 to n - 1 that form a circle. 
    We know the distance between all pairs of neighboring stops where distance[i] is the 
    distance between the stops number i and (i + 1) % n.
    The bus goes along both directions i.e. clockwise and counterclockwise.
    Return the shortest distance between the given start and destination stops.

    Example:
        Input: distance = [1,2,3,4], start = 0, destination = 1
        Output: 1
        Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.

    https://leetcode.com/problems/distance-between-bus-stops/
    """

    if start > destination:
        start, destination = destination, start
    
    ret = sum(distance[start: destination])
    ret = min(ret, sum(distance) - ret)
    
    return ret

print distance_between_bus_stops([7,10,1,12,11,14,5,0], 7, 2)

def test_distance_between_bus_stops_1():
    assert 1 == distance_between_bus_stops(distance = [1,2,3,4], start = 0, destination = 1)

def test_distance_between_bus_stops_2():
    assert 3 == distance_between_bus_stops(distance = [1,2,3,4], start = 0, destination = 2)

def test_distance_between_bus_stops_3():
    assert 4 == distance_between_bus_stops(distance = [1,2,3,4], start = 0, destination = 3)

def test_distance_between_bus_stops_4():
    assert 17 == distance_between_bus_stops(distance = [7,10,1,12,11,14,5,0], start = 7, destination = 2)