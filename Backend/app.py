# from flask import Flask
# import Black_Jack_Game_Gesture_Recognition
# import json
# from Black_Jack_Game_Gesture_Recognition import Player
# app = Flask(__name__)

# @app.route("/",methods = ['GET'])
# def func():
    
        

# if __name__ == "__main__":
#     app.run(debug=True, port=5000)
from flask import Flask, jsonify
import random
from flask_cors import CORS


app = Flask(__name__)

CORS(app, origins='http://localhost:3000')


# Define global variables
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11,
}

# Define classes
class Card:
    def __init__(self, suit, rank):
        self.suit = suit.capitalize()
        self.rank = rank.capitalize()
        self.value = values[self.rank]

    def __str__(self):
        return self.rank + self.suit[0] + ".png"

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_one(self):
        return self.deck.pop()

class Player:
    def __init__(self, name):
        self.hands = []
        self.name = name
        self.sum = 0

    def add_cards(self, card):
        self.hands.append(card)
        if card.rank != "A":
            self.sum += card.value
        else:
            if self.sum + card.value > 21:
                self.sum += 1
            else:
                self.sum += card.value

    def display_player(self):
        # cards = [str(card) for card in self.hands]
        return self.hands
  


# Flask routes
@app.route("/deck", methods=['GET'])
def func():
    dealer_lst = []
    player_lst = []
    # Create a new deck and shuffle it
    new_deck = Deck()

    # Create a Player instance (you may need to provide the player's name)
    player = Player("Player Name")
    dealer = Player("Dealer Name")

    # Deal cards to the player's hand
    player.add_cards(new_deck.deal_one())
    dealer.add_cards(new_deck.deal_one())

    # Display player's card information and return it in JSON format
    player_card_info = [str(card) for card in player.display_player()]
    dealer_card_info = [str(card) for card in dealer.display_player()]
    
    return jsonify(player_cards=player_card_info, dealer_cards = dealer_card_info)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
