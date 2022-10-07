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

    def player_hit(self):
        self.player.hit(self.dealer.deal())
        self.view.update_game(self.player, self.dealer)

    def stand(self):
        print("Stand")

    def start(self):
        self.view.mainloop()

    def new_game(self):
        self.dealer.new_deck()
        self.player.bet = 0
        self.dealer.hit(self.dealer.deal())
        self.player.hit(self.dealer.deal())
        self.dealer.hit(self.dealer.deal())
        self.player.hit(self.dealer.deal())
        self.view.show_game()
        self.view.update_game(self.player, self.dealer)
