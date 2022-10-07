
from src.models.dealer import Dealer
from src.models.player import Player


class Model:
    def new_player(self, name: str) -> Player:
        return Player(name=name, credit=1000)

    def new_dealer(self) -> Dealer:
        return Dealer()
