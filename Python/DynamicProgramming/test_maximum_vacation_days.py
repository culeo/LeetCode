# coding: utf-8

def max_vacation_days(flights, days):
    """
    568	Maximum Vacation Days(最大假期天数)

    LintCode wants to give one of its best employees the option to travel among N cities to collect algorithm problems. 
    But all work and no play makes Jack a dull boy, you could take vacations in some particular cities and weeks. 
    Your job is to schedule the traveling to maximize the number of vacation days you could take, 
    but there are certain rules and restrictions you need to follow.

    Rules and restrictions:
        You can only travel among N cities, represented by indexes from 0 to N-1. Initially, 
        you are in the city indexed 0 on Monday.
        The cities are connected by flights. The flights are represented as a N*N matrix (not necessary symmetrical), 
        called flights representing the airline status from the city i to the city j. 
        If there is no flight from the city i to the city j, flights[i][j] = 0; Otherwise, flights[i][j] = 1. 
        Also, flights[i][i] = 0 for all i.
        You totally have K weeks (each week has 7 days) to travel. 
        You can only take flights at most once per day and can only take flights on each week's Monday morning. 
        Since flight time is so short, we don't consider the impact of flight time.
        For each city, you can only have restricted vacation days in different weeks, 
        given an N*K matrix called days representing this relationship. For the value of days[i][j], 
        it represents the maximum days you could take vacation in the city i in the week j+1.
        You're given the flights matrix and days matrix, 
        and you need to output the maximum vacation days you could take during K weeks.

    Example:
        Input：flights = [[0,1,1],[1,0,1],[1,1,0]]，days = [[1,3,1],[6,0,3],[3,3,3]]
        Output：12
        Explanation：
            Ans = 6 + 3 + 3 = 12. 
            One of the best strategies is:
            1st week : fly from city 0 to city 1 on Monday, and play 6 days and work 1 day. 
            (Although you start at city 0, we could also fly to and start at other cities since it is Monday.) 
            2nd week : fly from city 1 to city 2 on Monday, and play 3 days and work 4 days.
            3rd week : stay at city 2, and play 3 days and work 4 days.

    https://leetcode.com/problems/maximum-vacation-days
    https://www.lintcode.com/problem/maximum-vacation-days/description
    """
    if len(flights) == 0: return 0
    if len(days) == 0 or len(days[0]) == 0: return 0

    N = len(flights)
    K = len(days[0])
    f = [[-1] * N for i in range(K)]

    f[0][0] = days[0][0]
    for i in range(1, N):
        if flights[0][i]: f[0][i] = days[i][0]

    for k in range(1, K):
        for j in range(N):
            for i in range(N):
                if f[k-1][i] == -1: 
                    continue
                if j == i or flights[i][j] == 1:
                    f[k][j] = max(f[k][j], f[k-1][i]+days[j][k])

    return max(f[K-1])

print max_vacation_days([[0,1,1],[1,0,1],[1,1,0]], [[1,3,1],[6,0,3],[3,3,3]])

def test_max_vacation_days_1():
    assert 12 == max_vacation_days([[0,1,1],[1,0,1],[1,1,0]], [[1,3,1],[6,0,3],[3,3,3]])

def test_max_vacation_days_2():
    assert 3 == max_vacation_days([[0,0,0],[0,0,0],[0,0,0]], [[1,1,1],[7,7,7],[7,7,7]])