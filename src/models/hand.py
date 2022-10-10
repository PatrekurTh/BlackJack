
from typing import List


class Hand:
    def __init__(self) -> None:
        self.hand: List = []
        self.value: int = 0

    def add(self, card) -> None:
        self.hand.append(card)
        if not card.hidden:
            self.value += card.value
        if self.value > 21:
            if self.ace():
                self.value -= 10

    def get_value(self):
        return self.value

    def ace(self) -> bool:
        for card in self.hand:
            if card.rank == "A":
                return True
        return False

    def clear(self) -> None:
        self.hand = []
        self.value = 0

    def flip_cards(self) -> None:
        for card in self.hand:
            if card.hidden:
                card.flip()
                self.value += card.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def __len__(self):
        return len(self.hand)

    def __iter__(self):
        return iter(self.hand)
