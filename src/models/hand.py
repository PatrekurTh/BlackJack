
from typing import List


class Hand:
    def __init__(self) -> None:
        self.hand: List = []
        self.value: int = 0

    def add(self, card) -> None:
        self.hand.append(card)
        self.value += card.value

    def clear(self) -> None:
        self.hand = []
        self.value = 0

    def show_card(self) -> None:
        for card in self.hand:
            if card.hidden:
                card.flip()

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
