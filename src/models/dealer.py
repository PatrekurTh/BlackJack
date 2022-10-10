from src.models.player import Player
from src.models.hand import Hand
from src.models.card import Card
from src.models.deck import Deck


class Dealer(Player):
    def __init__(self) -> None:
        self.deck: Deck = Deck()
        self.hand: Hand = Hand()

    def new_deck(self) -> None:
        self.deck = Deck()
        self.deck.shuffle_deck()

    def deal(self) -> Card:
        return self.deck.draw_card()

    def show_card(self) -> None:
        self.hand.flip_cards()
