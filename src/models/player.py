from typing import List
from src.models.card import Card


class Player:
    def __init__(self, name, credit) -> None:
        self.name: str = name
        self.credit: int = credit
        self.bet: int = 0
        self.hand: List[Card] = []

    def hit(self, card: Card) -> None:
        self.hand.append(card)
