
from src.models.dealer import Dealer
from src.models.player import Player


class Model:
    @staticmethod
    def new_player(name: str) -> Player:
        return Player(name=name, credit=1000)

    @staticmethod
    def new_dealer() -> Dealer:
        return Dealer()
