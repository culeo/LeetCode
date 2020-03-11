# coding: utf-8

def lemonade_change(bills):
    """
    860. Lemonade Change

    At a lemonade stand, each lemonade costs $5. 
    Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).
    Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
    You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.
    Note that you don't have any change in hand at first.
    Return true if and only if you can provide every customer with correct change.

    Example:
        Input: [5,5,5,10,20]
        Output: true
        Explanation: 
            From the first 3 customers, we collect three $5 bills in order.
            From the fourth customer, we collect a $10 bill and give back a $5.
            From the fifth customer, we give a $10 bill and a $5 bill.
            Since all customers got correct change, we output true.
            
    https://leetcode.com/problems/lemonade-change/
    """
    coins = [0] * 21
    
    for bill in bills:
        coins[bill] += 1
        if bill > 5:
            change = bill - 5
            ten = change / 10
            five = (change % 10) / 5
            if coins[10] >= ten:
                coins[10] -= ten
            else:
                five += 2

            if coins[5] < five: return False
            
            coins[5] -= five
        
    return True

print lemonade_change([5,5,10,10,20])

def test_lemonade_change_1():
    assert True == lemonade_change([5,5,5,10,20])

def test_lemonade_change_2():
    assert True == lemonade_change([5,5,10])

def test_lemonade_change_3():
    assert False == lemonade_change([10,10])

def test_lemonade_change_4():
    assert False == lemonade_change([5,5,10,10,20])