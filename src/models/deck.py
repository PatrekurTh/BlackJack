
from typing import List
from src.models.card import Card


class Deck:
    def __init__(self) -> None:
        self.ranks = ['A', 2, 3, 4, 5, 6, 7,
                      8, 9, 10, 'J', 'Q', 'K']
        self.suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        self.cards: List[Card] = self._create_new_deck()

    def _create_new_deck(self) -> List[Card]:
        deck: List = []
        for suit in self.suits:
            for rank in self.ranks:
                image = f"img/cards/card_{suit.lower()}_{rank}.png"
                deck.append(Card(suit, rank, image))
        return deck

    def shuffle_deck(self) -> None:
        import random
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop()
