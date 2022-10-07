from tkinter import *
from tkinter import ttk


class Game(ttk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller

        # dealer
        dealer_fr = Frame(self, bg="green")
        dealer_fr.grid(row=0, column=0, sticky="nsew")
        dealer_fr.rowconfigure(0, weight=1)
        dealer_fr.columnconfigure(0, weight=1)
        ttk.Label(dealer_fr, text="Dealer Goes Here").grid(
            row=0, column=0)

        # player
        player_fr = Frame(self, bg="blue")
        player_fr.grid(row=1, column=0, sticky="nsew")
        player_fr.rowconfigure(0, weight=1)
        player_fr.columnconfigure(0, weight=1)
        player_fr.columnconfigure(1, weight=2)
        player_fr.columnconfigure(2, weight=1)

        self.player_hand_fr = Frame(player_fr, bg="red")
        self.player_hand_fr.grid(row=0, column=1, sticky="nsew")

        hit_btn = ttk.Button(player_fr, text="Hit", command=self.hit)
        hit_btn.grid(row=0, column=0)
        self.player_hand_value = IntVar()
        self.player_hand_value.set(0)
        ttk.Label(player_fr, textvariable=self.player_hand_value, font=('Arial', 10, "bold"), anchor="center").grid(
            row=1, column=1, sticky="ew", ipadx=10, ipady=10)
        stand_btn = ttk.Button(player_fr, text="Stand")
        stand_btn.grid(row=0, column=2)

    def update(self, player, dealer) -> None:
        # clear player hand
        for widget in self.player_hand_fr.winfo_children():
            widget.destroy()

        # update player hand
        for card in player.hand:
            img = PhotoImage(file=card.image)
            l = ttk.Label(self.player_hand_fr, image=img)
            # for some reason tkinter garbage collects the image if we don't do this
            l.image = img
            l.grid()

        # update player hand value
        self.player_hand_value.set(player.hand.value)

    def hit(self):
        self.controller.player_hit()
