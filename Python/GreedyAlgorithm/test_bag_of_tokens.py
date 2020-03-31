# coding: utf-8

def bag_of_tokens_score(tokens, P):
    """
    948. Bag of Tokens
    
    You have an initial power P, an initial score of 0 points, and a bag of tokens.
    Each token can be used at most once, has a value token[i], and has potentially two ways to use it.
        If we have at least token[i] power, we may play the token face up, losing token[i] power, 
        and gaining 1 point.
        If we have at least 1 point, we may play the token face down, gaining token[i] power, and losing 1 point.
    Return the largest number of points we can have after playing any number of tokens.

    Example:
        Input: tokens = [100,200,300,400], P = 200
        Output: 2
    
    https://leetcode.com/problems/bag-of-tokens/
    """
    tokens.sort()
    i, j = 0, len(tokens) - 1
    ans = 0

    while i <= j:
        if tokens[i] <= P:
            P -= tokens[i]
            i += 1
            ans += 1
        elif ans > 0 and i != j:
            P += tokens[j]
            j -= 1
            ans -= 1
        else:
            break

    return ans

print bag_of_tokens_score(tokens = [100,200,300,400], P = 200)

def test_bag_of_tokens_score_1():
    assert 0 == bag_of_tokens_score(tokens = [100], P = 50)

def test_bag_of_tokens_score_2():
    assert 1 == bag_of_tokens_score(tokens = [100,200], P = 150)

def test_bag_of_tokens_score_3():
    assert 2 == bag_of_tokens_score(tokens = [100,200,300,400], P = 200)
