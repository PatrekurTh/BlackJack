from time import sleep
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

    def player_stand(self):
        while (self.dealer.hand.value < 17):
            self.dealer.hit(self.dealer.deal())
            self.view.update_game(self.player, self.dealer)
        self.summarize_round()

    def summarize_round(self):
        if self.player.hand.value > 21:
            self.view.show_message("You busted!")
        elif self.dealer.hand.value > 21:
            self.view.show_message("Dealer busted!")
        elif self.player.hand.value > self.dealer.hand.value:
            self.view.show_message("You win!")
        elif self.player.hand.value < self.dealer.hand.value:
            self.view.show_message("You lose!")
        else:
            self.view.show_message("Push!")
        self.new_game()

    def start(self):
        self.view.mainloop()

    def new_game(self):
        self.player.clear_hand()
        self.dealer.clear_hand()
        self.dealer.new_deck()
        self.player.bet = 0
        self.dealer.hit(self.dealer.deal())
        self.player.hit(self.dealer.deal())
        self.dealer.hit(self.dealer.deal())
        self.player.hit(self.dealer.deal())
        self.view.show_game()
        self.view.update_game(self.player, self.dealer)
