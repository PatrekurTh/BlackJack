
class Hand:
    def __init__(self) -> None:
        self.hand = []
        self.value = 0

    def add(self, card) -> None:
        self.hand.append(card)
        self.value += card.value

    def __iter__(self):
        return iter(self.hand)
