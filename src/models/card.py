
class Card:
    def __init__(self, suit, rank, image) -> None:
        self.rank = rank
        self.suit = suit
        self.value = self._get_value()
        self.image = image

    def _get_value(self):
        if self.rank == "A":
            return 11
        elif self.rank in ["J", "Q", "K"]:
            return 10
        else:
            return self.rank

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
