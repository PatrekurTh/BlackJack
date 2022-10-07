from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from src.views.game import Game
from src.views.menu import Menu


class View(Tk):
    def __init__(self, controller):
        super().__init__()
        self._configure()
        self.controller = controller
        self.menu: Menu = Menu(self, controller)
        self.menu.grid(row=0, column=0, sticky="nsew")
        self.game: Game = Game(self, controller)
        self.game.grid(row=0, column=0, sticky="nsew")
        self.game.rowconfigure(0, weight=1)
        self.game.rowconfigure(1, weight=1)
        self.game.columnconfigure(0, weight=1)

        self.bind("<Return>", lambda e: self.menu.start_game())
        self.bind("<Escape>", lambda e: self.destroy())
        self.bind("<s>", lambda e: self.game.stand())
        self.bind("<h>", lambda e: self.game.hit())

        self.show_menu()

    def _configure(self) -> Tk:
        self.title("Blackjack")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.geometry("400x400")

    def show_game(self):
        self.game.tkraise()

    def show_menu(self):
        self.menu.tkraise()

    def update_game(self, player, dealer):
        self.game.update(player, dealer)

    def show_message(self, message):
        messagebox.showinfo("", message)
