from src.models.hand import Hand
from src.models.card import Card
from src.models.deck import Deck


class Dealer:
    def __init__(self) -> None:
        self.deck: Deck = Deck()
        self.hand: Hand = Hand()

    def new_deck(self) -> None:
        self.deck = Deck()
        self.deck.shuffle_deck()

    def deal(self) -> Card:
        return self.deck.draw_card()

    def hit(self, card: Card) -> None:
        self.hand.add(card)

    def clear_hand(self) -> None:
        self.hand.clear()

    def busted(self):
        return self.hand.value > 21
