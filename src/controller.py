
from src.model import Model
from src.models.dealer import Dealer
from src.models.player import Player
from src.view import View
from tkinter import *


class Controller:
    def __init__(self) -> None:
        self.view: View = View(self)
        self.player: Player = Model.new_player("Player")
        print("Player: ", self.player)
        self.dealer: Dealer = Model.new_dealer()

    def player_hit(self) -> None:
        self.player.hit(self.dealer.deal())
        if self.player.busted():
            self.summarize_round()
        else:
            self.view.update_game(self.player, self.dealer)

    def player_stand(self) -> None:
        self.dealer.hand.show_card()
        self.view.update_game(self.player, self.dealer)
        while (self.dealer.hand.value < 17):
            self.dealer.hit(self.dealer.deal())
            self.view.update_game(self.player, self.dealer)
        self.summarize_round()

    def summarize_round(self) -> None:
        if self.player.busted():
            self.dealer_wins()
        elif self.dealer.busted():
            self.player_wins()
        elif self.player.hand.compareTo(self.dealer.hand) > 1:
            self.player_wins()
        elif self.player.hand.compareTo(self.dealer.hand) < 1:
            self.dealer_wins()
        else:
            self.push()
        self.init_game()

    def start(self) -> None:
        self.view.mainloop()

    def new_game(self) -> None:
        self.player.clear_hand()
        self.dealer.clear_hand()
        self.dealer.new_deck()
        self.dealer.hit(self.dealer.deal())
        self.player.hit(self.dealer.deal())
        self.dealer.hit(self.dealer.deal().flip())
        self.player.hit(self.dealer.deal())
        self.view.update_game(self.player, self.dealer)

    def player_wins(self):
        self.player.credit += self.player.bet * 2
        self.view.show_message("You win!")

    def dealer_wins(self):
        self.view.show_message("Dealer wins!")

    def push(self):
        self.view.show_message("Push!")

    def player_bet(self, bet):
        self.player.bet = bet
        self.player.credit -= bet
        self.new_game()

    def init_game(self):
        self.view.update_game(self.player, self.dealer)
