# Contains all classes used.
import random
import array
class deck:
    cards = [[0 for i in range(0,4)] for j in range(0,13)]
    
    def __init__(self): # Init card array with 4 suites of 13 cards
        for i in range(0,4):
            for j in range(0,13):
                self.cards[j][i] = j
                self.check = self.cards 
    
    def shuffle(self): # Shuffle cards
        for i in range(0,3):
            for j in range(0,13):
                r2 = random.randint(0,j) 
                r = random.randint(0,i)
                self.check[j][i], self.check[r2][r] = self.check[r2][r], self.check[j][i]
    
    def print(self): # Print card array
        for i in range(0,4):
            for j in range(0,13):
                print("Card index " + str(i) + ' ' + str(j) + ":  ", end = '')
                print(self.check[j][i])
    
    def getcard(self): # Get a card, eliminating that card from the possible cards
        sarr = [0,1,2,3,4,5,6,7,8,9,10,11,12]
        for i in range(0,13):
            s = random.choice(sarr)
            suite = self.check[s]
            if suite:
                card = random.choice(suite)
                break
            else:
                suite = -1
                sarr.remove(s)
        if suite == -1:
            return -1
        for i in range(0,13):
            if self.check[i] == suite:
                self.check[i].remove(card)
                break
        return(card)    
    
    def reset(self): # Reset what cards can be gotten from getcard()
        self.check = self.cards
        self.shuffle()
class player: # The class for the player, contains an array for a hand of cards, and a money counter
    cards = [0 for i in range(52)]
    money = 0
    cardcount = 0
    ai = False    
    def __init__(self, money, ai): # Init new player
        self.money = money
        self.ai = ai
    
    def addmoney(self, money): # Add money to player
        self.money += money
    
    def submoney(self, money): # Subtract money from a player
        self.money -= money
    
    def addcard(self, card): # Add card to hand
        self.cards[cardcount] = card
        cardcount += 1
    
    def printhand(self): # Print hand
        print(self.cards)
    
    def resethand(self): # Reset hand
        cards = [0 for i in range(52)]
        cardcount = 0
    
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
