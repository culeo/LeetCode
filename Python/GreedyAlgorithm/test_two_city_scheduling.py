# coding: utf-8

def two_city_sched_cost(costs):
    """
    1029. Two City Scheduling

    There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], 
    and the cost of flying the i-th person to city B is costs[i][1].
    Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

    Example :
        Input: [[10,20],[30,200],[400,50],[30,20]]
        Output: 110
        Explanation: 
            The first person goes to city A for a cost of 10.
            The second person goes to city A for a cost of 30.
            The third person goes to city B for a cost of 50.
            The fourth person goes to city B for a cost of 20.
            The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

    https://leetcode.com/problems/two-city-scheduling/
    """
    costs.sort(key = lambda x : x[0] - x[1])

    cost = 0

    for i in range(0, len(costs) / 2):
        cost += costs[i][0]
        
    for i in range(len(costs)/2, len(costs)):
        cost += costs[i][1]

    return cost


print two_city_sched_cost([[10,20],[30,200],[400,50],[30,20]])

def test_two_city_sched_cost_1():
    assert 110 == two_city_sched_cost([[10,20],[30,200],[400,50],[30,20]])