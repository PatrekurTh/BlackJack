from tkinter.ttk import Frame, Button


class Menu(Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller

        self.button = Button(
            self, text="Start Game", command=self.start_game).grid(row=0, column=0, sticky="nsew")

    def start_game(self):
        self.controller.new_game()
