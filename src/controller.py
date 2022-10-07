from src.model import Model
from src.models.dealer import Dealer
from src.models.player import Player
from src.view import View
from tkinter import *


class Controller:
    def __init__(self) -> None:
        self.view: View = View(self)
        self.model: Model = Model()
        self.player: Player = self.model.new_player("Player")
        self.dealer: Dealer = self.model.new_dealer()

    def hit(self):
        print("Hit")

    def stand(self):
        print("Stand")

    def start(self):
        self.view.mainloop()

    def new_game(self):
        self.dealer.new_deck()
        self.player.bet = 0
        print("New Game")
