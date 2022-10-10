
from src.model import Model
from src.models.dealer import Dealer
from src.models.player import Player
from src.view import View
from tkinter import *


class Controller:
    def __init__(self) -> None:
        self.view: View = View(self)
        self.player: Player = Model.new_player("Player")
        self.dealer: Dealer = Model.new_dealer()

    def player_hit(self) -> None:
        self.player.hit(self.dealer.deal())
        self.view.refresh_view(self.player, self.dealer)
        if self.player.busted():
            self.end_round()

    def player_stand(self) -> None:
        self.dealer.show_card()
        self.view.refresh_view(self.player, self.dealer, dealer_animation=True)
        while (self.dealer.get_hand_value() < 17):
            print(self.dealer.get_hand_value())
            self.dealer.hit(self.dealer.deal())
            self.view.refresh_view(
                self.player, self.dealer, dealer_animation=True)
        self.end_round()

    def end_round(self) -> None:
        self.dealer.show_card()
        self.view.refresh_view(self.player, self.dealer, dealer_animation=True)
        if self.player.busted():
            self.dealer_wins()
        elif self.dealer.busted():
            self.player_wins()
        elif self.player.hand > self.dealer.hand:
            self.player_wins()
        elif self.player.hand < self.dealer.hand:
            self.dealer_wins()
        elif self.player.hand == self.dealer.hand:
            self.push()
        elif self.player.black_jack():
            self.player_wins(bj=True)
        else:
            self.view.show_message("Something went wrong!")
        self.init_game()

    def start(self) -> None:
        self.view.mainloop()

    def new_game(self) -> None:
        self.dealer.hit(self.dealer.deal())
        self.player.hit(self.dealer.deal())
        self.dealer.hit(self.dealer.deal().flip())
        self.player.hit(self.dealer.deal())
        self.view.refresh_view(self.player, self.dealer, dealer_animation=True)
        if self.player.black_jack():
            self.end_round()

    def player_wins(self, bj=False):
        if bj:
            self.player.credit += self.player.bet * 2.5
            self.view.show_message("Black Jack!")
        else:
            self.player.credit += self.player.bet * 2
            self.view.show_message("You win!")

    def dealer_wins(self):
        self.view.show_message("Dealer wins!")

    def push(self):
        self.view.show_message("Push!")

    def player_bet(self, bet):
        self.player.credit -= bet
        self.player.bet = bet
        self.new_game()

    def init_game(self):
        self.player.clear_hand()
        self.dealer.clear_hand()
        self.dealer.new_deck()
        self.view.refresh_view(self.player, self.dealer, dealer_animation=True)
