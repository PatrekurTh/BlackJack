from time import sleep
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
        self.resizable(False, False)

    def show_game(self):
        """Show the game view"""
        self.game.tkraise()

    def show_menu(self) -> None:
        """Show the menu view"""
        self.menu.tkraise()

    def refresh_view(self, player, dealer, dealer_animation=False) -> None:
        """Update the view

        Args:
            player (Player): the player model
            dealer (Dealer): the dealer model
            dealer_animation (bool, optional): if the dealer should animate his moves. Defaults to False.
        """
        self.game.refresh_view(player, dealer, dealer_animation)

    def show_message(self, message) -> None:
        """Popup message box with the given message

        Args:
            message (str): message to show
        """
        messagebox.showinfo("", message)

    def delay(self, seconds) -> None:
        """Delay the UI for a given amount of seconds

        This is a blocking function, so it will not return until the delay is over

        Args:
            seconds (int): delay in seconds
        """
        try:
            time: int = seconds * 1000
            resume: BooleanVar = BooleanVar(value=False)
            self.after(time, lambda: resume.set(True))
            self.wait_variable(resume)
        except:
            pass
