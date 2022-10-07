
class Card:
    _HIDDEN_IMAGE_PATH: str = "img/cards/card_back.png"

    def __init__(self, suit, rank) -> None:
        self.rank = rank
        self.suit = suit
        self.value: int = self._set_value()
        self.hidden: bool = False

    def get_image_path(self) -> str:
        if self.hidden:
            return self._HIDDEN_IMAGE_PATH
        else:
            image = f"img/cards/card_{self.suit.lower()}_{self.rank}.png"
            return image

    def _set_value(self) -> int:
        if self.rank == "A":
            return 11
        elif self.rank in ["J", "Q", "K"]:
            return 10
        else:
            return self.rank

    def flip(self):
        self.hidden = not self.hidden
        return self

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
