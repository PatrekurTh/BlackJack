from typing import List
from src.models.hand import Hand
from src.models.card import Card


class Player:
    def __init__(self, name, credit) -> None:
        self.name: str = name
        self.credit: int = credit
        self.bet: int = 0
        self.hand = Hand()

    def hit(self, card: Card) -> None:
        self.hand.add(card)

    def clear_hand(self) -> None:
        self.hand.clear()

    def busted(self):
        return self.hand.value > 21
