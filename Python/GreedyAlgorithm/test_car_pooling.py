# coding: utf-8

def car_pooling(trips, capacity):
    """
    1094. Car Pooling

    You are driving a vehicle that has capacity empty seats initially available for passengers.  
    The vehicle only drives east (ie. it cannot turn around and drive west.)
    Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about 
    the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and 
    drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial 
    location.
    Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

    Example:
        Input: trips = [[2,1,5],[3,3,7]], capacity = 4
        Output: false

    https://leetcode.com/problems/car-pooling/
    """
    nums = [0] * 10001
    for trip in trips:
        nums[trip[1]] += trip[0]
        nums[trip[2]] -= trip[0]

    for num in nums:
        capacity -= num
        if capacity < 0: return False
    
    return True


print car_pooling(trips = [[9,3,4],[9,1,7],[4,2,4],[7,4,5]], capacity = 23)

def test_car_pooling_1():
    assert False == car_pooling(trips = [[2,1,5],[3,3,7]], capacity = 4)

def test_car_pooling_2():
    assert True == car_pooling(trips = [[2,1,5],[3,3,7]], capacity = 5)

def test_car_pooling_3():
    assert True == car_pooling(trips = [[2,1,5],[3,5,7]], capacity = 3)

def test_car_pooling_4():
    assert True == car_pooling(trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11)

def test_car_pooling_5():
    assert False == car_pooling(trips = [[9,3,6],[8,1,7],[6,6,8],[8,4,9],[4,2,9]], capacity = 28)

def test_car_pooling_6():
    assert True == car_pooling(trips = [[9,3,4],[9,1,7],[4,2,4],[7,4,5]], capacity = 23)
