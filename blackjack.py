#!/usr/bin/env python3
from classes import *
import random
import array
def customsumas11(nums):
    tmp = nums
    for i in range(len(nums)):
        if tmp[i] > 9:
            tmp[i] = 9
        if tmp[i] == 0:
            tmp[i] = 10
    total = 0
    for i in range(len(tmp)):
        total += tmp[i]
    return total
def customsumas1(nums):
    tmp = nums
    for i in range(len(nums)):
        if tmp[i] > 9:
            tmp[i] = 9
    total = 0
    for i in range(len(tmp)):
        total += tmp[i] + 1
    return total
def customsum(nums):
    tmp = nums
    for i in range(len(nums)):
        if tmp[i] > 9:
            tmp[i] = 9
    for i in range(len(tmp)):
        if tmp[i] == 0:
            print("Do you want this 1 to be one or eleven?")
            print("Total if one is " + str(sum(tmp)) + ", eleven is " + str(sum(tmp) + 10))
            x = input(" >>> ")
            if int(x) == 1:
                tmp[i] = 10
    total = 0
    for i in range(len(tmp)):
        if tmp[i] == -1:
            continue
        total += tmp[i] + 1
    return total
def playerturn(p1,  deck, rn):
    print(" Your turn - round " + str(rn) + ", your have been delt is")
    p1.addcard(deck.getcard())
    p1.addcard(deck.getcard())
    p1.printhand()
    playerresult = [0,0]
    while 1:
        print(" ")
        print("Hit or pass? (h/p)")
        hp = input(" >>> ")
        if hp == 'p':
            break
        else:
            p1.addcard(deck.getcard())
            if customsum(p1.cards) > 21:
                print("You went over!")
                break
            print("Your hand:")
            p1.printhand()
    playerresult = customsum(p1.cards)
    return playerresult
def aiturn(pai, ainum, deck, roundnum):
    airesults = [0 for i in range(int(ainum))]
    for i in range(int(ainum)):
        pai[i].addcard(deck.getcard())
        pai[i].addcard(deck.getcard())
        if customsumas11(pai[i].cards) == 21:
            airesults[i] = 21
            
        else:
            x = customsumas1(pai[i].cards)
            while x < 16:
                pai[i].addcard(deck.getcard())
                x = customsumas1(pai[i].cards)
            if x == 16 or 17:
                pai[i].addcard(deck.getcard())
            airesults[i] = customsumas1(pai[i].cards)
    return airesults
def m():
    p1 = player(0,False)
    p1.addmoney(20)
    pai = [0 for i in range(10)]
    d = deck()
    print("How many other players do you want? (More than 1, less than 11)")
    x = input(" >>> ")
    for i in range(0,int(x)):
        pai[i] = player(20, True)
    print("How many rounds do you want to play? Less is harder.")
    rounds = input(" >>> ")
    print("Your objective is to get " + str((x * 20)) + " moneys to win.")
    for roundnum in range(int(rounds)):
        d.reset()
        presult = playerturn(p1, d, roundnum)
        p1.resethand()
        airesult = aiturn(pai, x, d, roundnum)
        for i in range(int(x)):
            pai[i].resethand()
if __name__ == "__main__":
    m()
