# Contains all classes used.
import random
import array
class deck:
    cards = [[0 for i in range(0,4)] for j in range(0,13)]
    def __init__(self):
        for i in range(0,4):
            for j in range(0,13):
                self.cards[j][i] = j
                self.check = self.cards
    def shuffle(self):
        for i in range(0,3):
            for j in range(0,13):
                r2 = random.randint(0,j) 
                r = random.randint(0,i)
                self.check[j][i], self.check[r2][r] = self.check[r2][r], self.check[j][i]
    def print(self):
        for i in range(0,4):
            for j in range(0,13):
                print("Card index " + str(i) + ' ' + str(j) + ":  ", end = '')
                print(self.check[j][i])
    def getcard(self):
        for i in range(0,4):
            suite = random.choice(self.check)
            if suite:
                card = random.choice(suite)
                break
            else:
                suite = -1
        if suite == -1:
            return -1
        for i in range(0,13):
            if self.check[i] == suite:
                self.check[i].remove(card)
                break
        return(card)    
    def reset(self):
        check = self
        check.shuffle()
if __name__ == "__main__":
    Mdeck = deck()
    Mdeck.shuffle()
    for i in range(0,52):
        x = Mdeck.getcard()
        print(x)
