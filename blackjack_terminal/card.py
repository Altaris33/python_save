#class Deck : a deck of 52 cards in blackjack

class Card():

    
    faceup = False
    facedown = True

    def __init__(self,value,suit):
        self.value = value
        self.suit = suit 
        

    def __str__(self):
        return f'{self.value} is {self.suit} type.'

    suits = ['spade', 'heart', 'diamond', 'club']
    values = ['2','3','4','5','6','7','8','9','10','jack','queen','king','ace']

    deck = [Card(value, suit) for value in range(1, 14) for suit in suits]    

        