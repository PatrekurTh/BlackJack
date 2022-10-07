from src.models.hand import Hand
from src.models.card import Card
from src.models.deck import Deck
from typing import List


class Dealer:
    def __init__(self) -> None:
        self.deck = Deck()
        self.hand = Hand()

    def new_deck(self):
        self.deck = Deck()
        self.deck.shuffle_deck()

    def deal(self) -> Card:
        return self.deck.draw_card()

    def hit(self, card: Card):
        self.hand.add(card)
