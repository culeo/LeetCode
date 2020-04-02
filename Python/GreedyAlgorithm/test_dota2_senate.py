# coding: utf-8

import collections

def predict_party_victory(senate):
    """
    649. Dota2 Senate
    
    In the world of Dota2, there are two parties: the Radiant and the Dire.
    The Dota2 senate consists of senators coming from two parties. Now the senate wants to make a decision 
    about a change in the Dota2 game. The voting for this change is a round-based procedure. 
    In each round, each senator can exercise one of the two rights:
        1. Ban one senator's right:
           A senator can make another senator lose all his rights in this and all the following rounds.
        2. Announce the victory:
           If this senator found the senators who still have rights to vote are all from the same party, 
           he can announce the victory and make the decision about the change in the game.
    Given a string representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party 
    and the Dire party respectively. Then if there are n senators, the size of the given string will be n.
    The round-based procedure starts from the first senator to the last senator in the given order. 
    This procedure will last until the end of voting. All the senators who have lost their rights will be 
    skipped during the procedure.
    Suppose every senator is smart enough and will play the best strategy for his own party, 
    you need to predict which party will finally announce the victory and make the change in the Dota2 game. 
    The output should be Radiant or Dire.

    Example:
        Input: "RD"
        Output: "Radiant"
        Explanation: The first senator comes from Radiant and he can just ban the next senator's right in the round 1. 
            And the second senator can't exercise any rights any more since his right has been banned. 
            And in the round 2, the first senator can just announce the victory since he is the only guy in the senate 
            who can vote.

    https://leetcode.com/problems/dota2-senate/
    """
    queue = collections.deque()
    people = {'R': 0, 'D': 0}
    bans = {'R': 0, 'D': 0}

    for s in senate:
        people[s] += 1
        queue.append(s)

    while all(people.values()):
        s = queue.popleft()
        if bans[s] > 0:
            bans[s] -= 1
            people[s] -= 1
        else:
            bans['R' if s == 'D' else 'D'] += 1
            queue.append(s)

    return 'Radiant' if people['R'] else 'Dire'
    
print predict_party_victory('DDRRR')

def test_predict_party_victory_1():
    assert "Radiant" == predict_party_victory("RD")

def test_predict_party_victory_2():
    assert "Dire" == predict_party_victory("RDD")

def test_predict_party_victory_3():
    assert "Dire" == predict_party_victory("DDRRR")