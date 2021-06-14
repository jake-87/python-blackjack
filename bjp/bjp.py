#!/usr/bin/env python3
import math
import os as os
import random
import time
import sys
import copy
try:
    from bjp.classes import *
except:
    from classes import *
def customsumas11(nums): # Custom sum assuming 11
    tmp = copy.copy(nums)
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
def turn(p1, dealer, deck): # Does math and stuff for one turn
    dealer.addcard(deck.getcard())
    print("\nDealer has :")
    dealer.printhand()
    print("\nSum : " + str(customsum(dealer.cards)))
    p1.addcard(deck.getcard())
    p1.addcard(deck.getcard())
    print("\nYou have : ")
    p1.printhand()
    print(" Sum : " + str(customsum(p1.cards)))
    print("\n How much do you want to bet? You have " + str(p1.money) + " peanuts.")
    bet = input(" >>> ")
    while 1:
        time.sleep(2)
        print("\nYou have : ")
        p1.printhand()
        print("\n Sum : " + str(customsum(p1.cards)))
        print("\nHit or Pass? (h/p)")
        hp = input(" >>> ")
        if hp == "h":
            p1.addcard(deck.getcard())
            if customsum(p1.cards) > 21:
                print("\nYou went over!")
                break
            continue
        else:
            break
    print("\nYour cards are:")
    p1.printhand()
    print("\n Sum is " + str(customsum(p1.cards)))
    x = customsum(p1.cards)
    while 1:
        time.sleep(2)
        print("\n Dealer has drawn:")
        dealer.addcard(deck.getcard())
        dealer.printhand()
        if customsum(dealer.cards) > 21:
            time.sleep(2)
            print("\n Dealer has gone over!")
            if x > 21:
                print("\nBut, so have you! You lose this round!")
                break
            else:
                print("\nYou win this round!")
                break
        elif customsum(dealer.cards) <= 14:
            time.sleep(2)
            continue
        else:
            break
    time.sleep(2)
    print("\nIn the end, you had:")
    p1.printhand()
    print("\nwhich sums up to " + str(x))
    time.sleep(2)
    print("\n The dealer had")
    dealer.printhand()
    print("\nwhich sums up to "  + str(customsum(dealer.cards)))
    time.sleep(2)
    win = int(int(bet) * random.randint(2,5))
    if x >= customsum(dealer.cards) and not x > 21:
        print("\nTherefor, you win this round! You won " + str(win) + " peanuts.")
        p1.addmoney(win)
    elif customsum(dealer.cards) > 21 and not x > 21:
        print("\nTherefor, you win this round! You won " + str(win) + " peanuts.")
    else:
        print("\nTherefor, you lose this round. You lost " + str(bet) + " peanuts.")
        p1.submoney(int(bet))
    time.sleep(2)
    if p1.money <= 0:
        print("You went broke! Do you want a loan? (y/n)")
        loan = input(" >>> ")
        if loan == "y":
            p1.money = 0
            p1.addmoney(10)
            print("You have been given 10 peanuts! Go on and win!")
        else:
            print("Bye then!")
            sys.exit()
def m(): # Main function
    d = deck()
    p1 = player(20,False)
    dealer = player(math.inf, True)
    print("\nHow many rounds?")
    rounds = input(" >>> ")
    print("Calculating...")
    time.sleep(int(rounds)) # funni lmao
    for i in range(int(rounds)):
        os.system("clear")
        print("Round " + str(i))
        p1.resethand()
        dealer.resethand()
        turn(p1, dealer, d)
        time.sleep(2)
    if p1.money > int(rounds) * 1.5 * 20:
        print("You Win! You have " + str(p1.money) + "Which is more than the " + str(int(rounds) * 1.5 * 20) + " you needed to win!")
    else:
        print("You lost. You needed " + str(int(rounds) * 1.5 * 20) + " to win, whereas you only had " + str(p1.money) )
if __name__ == "__main__":
    m()
