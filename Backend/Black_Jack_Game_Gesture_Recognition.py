# between human player and a computer dealer
""""
player have a bank roll
player plays a bet

player starts with 2 cards face up and dealer starts with one card face up and one card face down

player goes first in game play

Aim : to get closer to a total value of 21 than the dealer does

Possible Actions :
Hit : recieve another card
Stay : stop recieving cards

When player's turn is over, dealer starts hitting until he beats the player or busts i.e. goes over 21

Game endings:
    1> If a player keeps hitting and busts and lose the bet
    2> If after player's turn, dealer hits and computer sum is higher than player sum and is still under 21 >> Dealer beats the Player and Computer wins
    3> If after player's turn, dealer hits and gets busted >> Player wins and his money double.

Special Rules :
    Face cards (Jack, King, Queen) count as a value of 10)
    Aces can count as either 1 or 11 whichever value is preferable to the player
"""
import random
import time
import sys
import datetime
import test

suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
ranks = (
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K",
    "A",
)
values = {"2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10,
    "A" : 11,
    }

class Card:
    """
    This is a card class whose objects will be type of card in the deck and will contain rank, value and suit of the card
    """
    def __init__(self, suit, rank):
        self.suit = suit.capitalize()
        self.rank = rank.capitalize()
        self.value = values[self.rank]

    def __str__(self):
        return self.rank + self.suit[0] + ".png"
    
class Deck:
    """
    This is a Deck class which will contain the deck of cards
    """
    def __init__(self) -> None:
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_one(self):
        
        return self.deck.pop()
    

class Player:
    def __init__(self, name):
        self.hands = []
        self.name = name
        self.sum = 0

    def add_cards(self,card):
        self.hands.append(card)
        if (card.rank != "A"):
            self.sum += card.value
        else:
            if(self.sum + card.value >21):
                self.sum += 1
            else:
                self.sum += card.value

    def stand_hit(self):
        print("Please! tell if you want to take a stand or a hit ")
        user_choice = test.capture()
        while(user_choice not in ["Hit","Stand"]):
            print("Not a valid input, Try again. . .")
            print("Please! tell if you want to take a stand or a hit ")
            user_choice = test.capture()
        return int(user_choice=="Hit")
    
    def display_player(self):
        print(f"\n{self.name}'s cards are : ")
        for i in range(0,len(self.hands)-1):
            print(self.hands[i],end=" + ")
        print(self.hands[len(self.hands)-1],"\n")


    def display_dealer(self):
        print(f"\n{self.name}'s cards are : ")
        print("red_back.png",end = " + ")
        for i in range(1,len(self.hands)-1):
            print(self.hands[i],end=" + ")
        print(self.hands[len(self.hands)-1],"\n")


# game logic
print("Welcome to Black Jack Game!!")
time.sleep(0.25)
dealer = Player("Ben Affleck")
player = Player("Player")
new_deck = Deck()
new_deck.shuffle_deck()

for i in range(2):
    # array in player.hands changes
    player.add_cards(new_deck.deal_one())
    # array in dealer.hands changes
    dealer.add_cards(new_deck.deal_one())
time.sleep(2)
player.display_player()
dealer.display_dealer()
time.sleep(5)

print(f"\nIt's {player.name}'s turn\n")
time.sleep(2.5)
while(player.sum<=21 ):
    if(player.stand_hit()):
        print(f"\n{player.name} will be taking a hit\n")
        # array in player.hands changes
        player.add_cards(new_deck.deal_one())
    else:
        print(f"\n{player.name} will be taking a stand\n")
        break
    player.display_player()
    dealer.display_dealer()
    time.sleep(2.5)

else:
    # Player gets busted and dealer wins
    print(f"\nOOPS! {player.name} got busted!!!!! \n")
    sys.exit()

# Turn changes from player to dealer
print("\nIt's now Dealer's turn\n")
time.sleep(1)
player.display_player()
dealer.display_player()
time.sleep(3)
while(dealer.sum<=21):
    if(dealer.sum<=player.sum):
        print("\nDealer will be taking a hit\n")
        time.sleep(2)
        # array in dealer.hands changes
        dealer.add_cards(new_deck.deal_one())
    else:
        # Dealer reached player and thus dealer wins
        print(f"\nDealer reached player, thus {player.name} looses!!!!\n")
        player.display_player()
        dealer.display_player()
        break
    player.display_player()
    dealer.display_player()
    time.sleep(5)
else:
    # Dealers got busted and Player wins
    print(f"\nOOPS! Dealer got busted!!!!! and {player.name} won the game \n")
    sys.exit()