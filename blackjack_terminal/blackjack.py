# Imports and global variables
import random 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
        'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6,
        'Seven':7, 'Eight': 8, 'Nine':9, 'Ten': 10, 
        'Jack':10, 'Queen':10, 'King':10, 'Ace':10 }
playing = True

# Class Definitions

# Card class

class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'     

# class Deck

# store 52 card objects in the deck

class Deck():
    
    def __init__(self):
        self.deck = []   # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+ card.__str__()
        return f'The deck has {deck_comp}.'
                        
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

# print tests
test_deck = Deck()
test_deck.shuffle()
# print(test_deck)        

# Hand and Chip class
class Hand():
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        # card passed in from Deck() class and is deal() method (card,rank)
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        
        # IF the total value is greater than 21 and i still have an ace
            # change my ace to be a 1 instead of an 11 (any number can be tested as booleans except from 0)
        while self.value > 21 and self.aces:
            self.values -= 10
            self.aces -= 1

# tests -> creation of a player and give him a card 
test_deck2 = Deck()
test_deck2.shuffle()

# Player

test_player = Hand()
pulled_card = test_deck2.deal()
# print(pulled_card)
test_player.add_card(pulled_card)
# print(test_player.value)

test_player.add_card(test_deck2.deal())
# print(test_player.value)

class Chips():

    def __init__(self,total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet()


# FUNCTIONS

# functions for Gameplay
# bet : asks the user for a bet
def take_bet(chips):
    
    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry, please provide an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips ! Your current amount is : {}".format(Chips.total))
            else:
                break    

# hit : anytime a player requests a hit 
def hit(deck,hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:

        x = input('Hit or stand? Enter h or s ')

        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player Stands. Dealer is playing.")  
            playing = False     
        else:
            print("Sorry, do not understand that, please enter h or s only.")    
            continue
        break

# show some cards and all cards
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)    

# player and dealer cases
def player_busts(player,dealer,chips):
    print("BUST PLAYER!") 
    chips.lose_bet()   

def player_wins(player,dealer,chips):
    print("PLAYER WINS") 
    chips.win_bet()  

def dealer_busts(player,dealer,chips):
    print("DEALER BUSTED, PLAYER WINS")   
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("DEALER WINS, PLAYER BUSTED")   
    chips.lose_bet()   

def push(player,dealer):
    print('Dealer and player tie! PUSH')   

# MAIN 

# main logic of the game
while True:

    # opening statement
    print("Welcome to Blackjack Get as close to 21 as possible without going over! \n Dealer hist until she reaches 17. Aces count as 1 or 11.")

    # create & shuffle a deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # set up player's chips
    player_chips = Chips()

    # prompt the player for their bet
    take_bet(player_chips)

    # show cards
    show_some(player_hand,dealer_hand)

    while playing:

        #prompt the player ti hit or stand
        hit_or_stand(deck,player_hand)

        # show cards
        show_some(player_hand,dealer_hand)

        # check if player busts, run out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    # if the player has no busted, play Dealer's hand until Dealer reaches 17    

    if player_hand.value <= 21:

        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand)

        # show all cards
        show_all(player_hand,dealer_hand)
        
        # run different winning scenarios     
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    print('\n Player total chips are at :  {}'.format(player_chips.total))

    new_game = input('Would you like to play another hand? y or n')

    if new_game[0].lower == 'y':
        playing = True
        continue
    else:
        print('Thank you for playing.')
        break

