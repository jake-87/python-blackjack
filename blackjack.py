from classes import *
import random
import array
def customsum(nums):
    tmp = nums
    for i in range(len(nums)):
        if tmp[i] > 10:
            tmp[i] = 10
    for i in range(len(tmp)):
        if tmp[i] == 1:
            print("Do you want this 1 to be one or eleven?")
            print("Total if one is " + str(sum(tmp)) + ", eleven is " + str(sum(tmp) + 10))
            x = input(" >>> ")
            if int(x) == 11:
                tmp[i] = 11
    print(tmp)
    total = 0
    for i in range(len(tmp)):
        total += tmp[i]
    return total
def playerturn(p1, deck, rn):
    print(" Your turn - round " + str(rn) + ", your have been delt is")
    p1.addcard(deck.getcard())
    p1.addcard(deck.getcard())
    p1.printhand()
def m():
    p1 = player(0,False)
    p1.addmoney(20)
    pai = [0 for i in range(10)]
    deck = deck()
    deck.shuffle()
    x, rounds = 0
    print("How many other players do you want? (More than 1, less than 11)")
    x = input(" >>> ")
    for i in range(0,x):
        pai[i] = player(20, True)
    print("How many rounds do you want to play? Less is harder.")
    rounds = input(" >>> ")
    print("Your objective is to get " + str((x * 20)) + " moneys to win.")
    for roundnum in range(rounds):
        p1turn(p1, deck, roundnum)
        aiturn(pai, deck, roundnum)
if __name__ == "__main__":
    nums = [1,2,3,4,13,143,15,1]
    print(customsum(nums))
