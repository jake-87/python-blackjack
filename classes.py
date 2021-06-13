#!/usr/bin/env python3
# Contains all classes used.
import random
import array
class deck:
    debug = 0
    cards = [0 for i in range (52)]
    def __init__(self): # Init card array with 4 suites of 13 cards
        for i in range(0,4):
            for j in range(1,13):
                self.cards[(i * 13) + j - 1] = j
    def print(self): # Print card array
        for i in range(52):
            if self.cards[i] == -1:
                continue
    def getcard(self): # Get a card, eliminating that card from the possible cards
        if self.debug: print("IN GETCARD" + str(self.cards))
        s = random.choice(self.cards)
        self.cards.remove(s)
        if self.debug: print("SELECTED " + str(s))
        return s
    def reset(self): # Reset what cards can be gotten from getcard()
        self.cards = [0 for i in range(52)]
        for i in range(0,4):
            for j in range(1,13):
                self.cards[(i * 13) + j - 1] = j
        if self.debug: print("RESETCARDS")
class player: # The class for the player, contains an array for a hand of cards, and a money counter
    cards = [-1 for i in range(52)]
    money = 0
    cardcount = 0
    ai = False 
    debug = 0
    def __init__(self, money, ai): # Init new player
        self.money = money
        self.ai = ai
    
    def addmoney(self, money): # Add money to player
        self.money += money
    
    def submoney(self, money): # Subtract money from a player
        self.money -= money
    
    def addcard(self, card): # Add card to hand
        self.cards[self.cardcount] = card
        self.cardcount += 1
    def printhand(self): # Print hand
        for i in range(52):
            if self.cards[i] == -1:
                continue
            print(str(self.cards[i] + 1) + ",", end = '')
    def resethand(self): # Reset hand
        self.cards = [-1 for i in range(52)]
        self.cardcount = 0 
    def reset(self): # Reset player
        self.resethand()
        self.money = 0
if __name__ == "__main__": # If this program is not being run as a module, run some tests
    Mdeck = deck()
    Mdeck.shuffle()
    s = [0 for i in range(52)]
    for i in range(0,52):
        x = Mdeck.getcard()
        s[i] = x
    for j in range(52):
        assert s[i] != -1
