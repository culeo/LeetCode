# coding: utf-8

def predict_the_winner(nums):
    """
    486. Predict the Winner
     
    Given an array of scores that are non-negative integers. 
    Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. 
    Each time a player picks a number, that number will not be available for the next player. 
    This continues until all the scores have been chosen. The player with the maximum score wins.
    Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

    Example:
        Input: [1, 5, 2]
        Output: False
        Explanation: Initially, player 1 can choose between 1 and 2. 
                     If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. 
                     If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
                     So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
                     Hence, player 1 will never be the winner and you need to return False.

    https://leetcode.com/problems/predict-the-winner/
    """
    N = len(nums)
    f = [[0] * N for i in range(N)]

    for i in range(N): f[i][i] = nums[i]
    for l in range(2, N+1):
        for i in range(N-l+1):
            j = i + l - 1
            f[i][j] = max(nums[i] - f[i+1][j], nums[j] - f[i][j-1])

    return f[0][N-1] >= 0

print predict_the_winner([1, 5, 233, 7])

def test_predict_the_winner_1():
    assert False == predict_the_winner([1,5,2])

def test_predict_the_winner_2():
    assert True == predict_the_winner([1,5,233,7])