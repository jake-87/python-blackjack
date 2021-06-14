#!/usr/bin/env python3
try:
    from blackjack.classes import *
except:
    from classes import *
import random
import array
import time
from os import system
import copy
debug = 0
def customsumas11(nums): # Custom sum assuming 11
    tmp = copy.copy(nums)
    if debug: print("AS11 : " + str(nums))
    for i in range(len(nums)):
        if tmp[i] > 9:
            tmp[i] = 9
    total = 0
    for i in range(len(tmp)):
        total += tmp[i] + 1
        if tmp[i] == 0:
            total += 10
    return total
def customsumas1(nums): # Custom sum assuming 1
    tmp = copy.copy(nums)
    if debug: print("AS1 : " + str(nums))
    for i in range(len(nums)):
        if tmp[i] > 9:
            tmp[i] = 9
    total = 0
    for i in range(len(tmp)):
        total += tmp[i] + 1
    return total
def customsum(nums): # Checks best combination
    if customsumas11(nums) > 21:
        total = customsumas1(nums)
    else:
        total = customsumas11(nums)
    return total
def playerturn(p1,  deck, rn): # Handles the players turn
    print(" Your turn - round " + str(rn) + ", your have been delt is")
    p1.addcard(deck.getcard())
    p1.addcard(deck.getcard())
    p1.printhand()
    print(" ")
    print("Sum is " + str(customsum(p1.cards)))
    playerresult = [0,0]
    while 1:
        time.sleep(2)
        print(" ")
        print("How many peanuts do you want to bet? You have " + str(p1.money))
        pbet = input(" >>> ")
        if int(pbet) <= p1.money:
            break
        else:
            print("Too much money!")
    p1.submoney(int(pbet))
    playerresult[1] = int(pbet)
    while 1:
        time.sleep(2)
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
            time.sleep(2)
            print("Your hand:")
            p1.printhand()
            print("Sum is " + str(customsum(p1.cards)))
    playerresult[0] = customsum(p1.cards)
    return playerresult
def aiturn(pai, ainum, deck, roundnum): # Handles the AI's turns
    airesults = [0 for i in range(int(ainum))]
    for i in range(int(ainum)):
        if debug: print("AINUM is " + str(i))
        pai[i].addcard(deck.getcard())
        pai[i].addcard(deck.getcard())
        if customsumas11(pai[i].cards) == 21:
            airesults[i] = 21
            
        else:
            x = customsumas1(pai[i].cards)
            while x < 15:
                pai[i].addcard(deck.getcard())
                x = customsumas1(pai[i].cards)
            if x == 15:
                pai[i].addcard(deck.getcard())
            airesults[i] = customsumas1(pai[i].cards)
        if customsumas1(pai[i].cards) > 21:
            airesults[i] = 0
    return airesults
def m(): # Main function
    system("clear")
    p1 = player(0,False)
    p1.addmoney(20)
    pai = [0 for i in range(10)]
    d = deck()
    print("Enable Debug? (1/0) (If in doubt, pick 0)")
    debug = input (" >>> ")
    if int(debug) == 1: p1.debug = 1
    print("How many other players do you want? (More than 1, less than 11)")
    x = input(" >>> ")
    for i in range(0,int(x)):
        pai[i] = player(20, True)
        if debug: pai[i].debug = 1
    print("How many rounds do you want to play? Less is harder.")
    rounds = input(" >>> ")
    print("Your objective is to get " + str((int(x) * 40)) + " peanuts to win.")
    for roundnum in range(int(rounds)):
        time.sleep(2)
        system("clear")
        d.reset()
        presult = playerturn(p1, d, roundnum)
        p1.resethand()
        print("AI is thinking...")
        time.sleep(2)
        airesult = aiturn(pai, x, d, roundnum)
        for i in range(int(x)):
            pai[i].resethand()
        win = True
        print("AI's results are " +  str(airesult) + ", 0 means they went over")
        for i in range(int(x)):
            if presult[0] < airesult[i] or presult[0] > 21:
                win = False
        time.sleep(2)
        if win ==  True:
            y = int(random.randint(1,10) * int(x) / random.randint(1,10) * presult[1] / int(x)) + presult[1]
            print("You won round " + str(roundnum) + "! You won " + str(y) + " peanuts.")
            p1.addmoney(int(y))
        else:
            print("You lost round " + str(roundnum) + ".")
            if p1.money == 0:
                print("You went broke! You have no peanuts left! Do you want a small loan to keep going? (y/n)")
                loan = input(" >>> ")
                if loan == 'y':
                    p1.addmoney(10)
                else:
                    break
        time.sleep(2)
    if p1.money > (int(x) * 40):
        print("You won!")
    else:
        print("You lost.")
    time.sleep(2)
    print("Bye!")
    return 0
if __name__ == "__main__": # If this is not being run as a submodule, run the main function.
    m()
