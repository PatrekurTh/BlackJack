
class Card:
    def __init__(self, suit, rank) -> None:
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
