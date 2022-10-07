from tkinter.ttk import Frame, Button


class Menu(Frame):
    def __init__(self, root, controller):
        super().__init__(root)

        self.button = Button(
            self, text="Start Game", command=controller.new_game).grid(row=0, column=0, sticky="nsew")
