from tkinter import *
from tkinter import ttk


class Game(ttk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.bind("<s>", lambda e: self.stand())
        self.bind("<h>", lambda e: self.hit())

        # dealer
        dealer_fr = Frame(self, bg="green")
        dealer_fr.grid(row=0, column=0, sticky="nsew")
        dealer_fr.rowconfigure(0, weight=1)
        dealer_fr.columnconfigure(0, weight=1)

        self.dealer_hand_value = IntVar()
        self.dealer_hand_value.set(0)

        ttk.Label(dealer_fr, textvariable=self.dealer_hand_value, font=('Arial', 10, "bold"), anchor="center").grid(
            row=1, column=1, sticky="ew", ipadx=10, ipady=10)

        self.dealer_hand_fr = Frame(dealer_fr, bg="green")
        self.dealer_hand_fr.grid(row=0, column=0, sticky="nsew")

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
        stand_btn = ttk.Button(player_fr, text="Stand", command=self.stand)
        stand_btn.grid(row=0, column=2)

    def update_game(self, player, dealer) -> None:
        # clear hands
        for widget in self.player_hand_fr.winfo_children():
            widget.destroy()
        for widget in self.dealer_hand_fr.winfo_children():
            widget.destroy()

        # update hands
        for i, card in enumerate(player.hand):
            img = PhotoImage(file=card.get_image_path())
            l = ttk.Label(self.player_hand_fr, image=img)
            # for some reason tkinter garbage collects the image if we don't do this
            l.image = img
            l.grid(row=0, column=i)

        for i, card in enumerate(dealer.hand):
            img = PhotoImage(file=card.get_image_path())
            l = ttk.Label(self.dealer_hand_fr, image=img)
            # for some reason tkinter garbage collects the image if we don't do this
            l.image = img
            l.grid(row=0, column=i)

        # update hand values
        self.player_hand_value.set(player.hand.value)
        self.dealer_hand_value.set(
            sum([card.value for card in dealer.hand if not card.hidden]))

    def hit(self):
        self.controller.player_hit()

    def stand(self):
        self.controller.player_stand()
