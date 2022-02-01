import random
random.choice
from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
         'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
playing = True

# Creates the cards.
class Card:                                          
    def _init_(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def _str_(self):                              # Returns everything as a string.
        return self.rank + ' of ' + self.suit     # Returns suit and rank.

# Creates the deck of cards.
class Deck:
    def _init_(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

# Setting the card combination.
    def _str_(self):                                # Returns everything as a string.
        deck_combination = ''
        for card in self.deck:
            deck_combination += "\n " + card._str_()      # Creates new card and reasigns card value.
        return "The deck has: " + deck_combination        # Combination of the cards in the deck.
    
# Shuffles the deck.
    def shuffle(self):
        random.shuffle(self.deck)

# Deals a random card from the deck.
    def deal(self):
        single_card = self.deck.pop()
        return single_card

# This shows the cards both the dealer and the player have.
class Hands:
    def _init_(self):
        self.cards = []
        self.value = 0
        self.aces = 0                 # This keeps rack of all the aces.

# Adds a card to the dealer or players hand.
    def add_card(self, card):
        self.value += values[card.rank]
        if card.rank == 'Aces':
            self.aces += 1             # Adds 10 + 1 for aces = 11

    # This is for aces.
    def if_aces(self):
        while self.value > 21 and self.aces:       
            self.value -= 10                       # Keeps ace at 11 if well under 21.
            self.aces -= 1                         # Turns ace to 1 if too close to 21.

# Keeps track of your chips.
class Chips:
    def _init_(self):
        self.total_chips = 100                      # Total chips you start with.
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet                      # If you win bet.

    def lose_bet(self):
        self.total -= self.bet                      # If you lose bet.

# Taking the users bet.
    def Make_bet(Chips):    
         while True:
            try:
                Chips.bet  = int(input("What would you like to bet? "))   
            except:
                print("Sorry! Please enter the amount you would like to bet: ")
            else:
                if Chips.bet > Chips.total:
                    print("Your bet cannot exceed 100 Chips!")
                else:
                    break

# If you decide to take an extra card.
    def Hit(deck, hand):
        hand.add_card(deck.deal())
        hand.if_aces()

    def hit_or_stand(deck, hand):     # Askes if you want another card or if your ok with your hand.
        global playing                # Runs function first.
        while True:
            user_input = input("Would you like to hit or stand? Enter (H) for hit or (S) for stand : ")
            if user_input[0].lower == "H":
                Hit(deck, hand)    #<------------------Cant figure out where I went wrong
            elif user_input[0].lower() == "S":
                print("Player stands, Its the dealers turn.")
                playing = False
            else:
                print("Invalid selection. Please try again.")
                continue
            break
                

    pass

class Player:   #<------------------I forgot to seperate them into classes
    pass


class Dealer(Player):
    pass


class Human(Player):
    pass


class Game:
    pass


def main():
    pass


main()
