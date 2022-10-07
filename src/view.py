from tkinter import *
from tkinter import ttk

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

        self.menu.tkraise()

    def _configure(self) -> Tk:
        self.title("Blackjack")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.geometry("800x600")