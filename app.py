import tkinter as tk
from title_frame import TitleFrame
from input_frame import InputFrame


class App:
    """Main application class."""
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(width=False, height=False)
        self.root.title("Punnett Square Calculator")
        self.root.grid()
        self.title_frame = TitleFrame(self.root)
        self.input_frame = InputFrame(self.root)

        self.title_frame.grid(row=0, column=0, sticky="nsew")
        self.input_frame.grid(row=1, column=0, sticky="nsew")

    def run(self):
        """Runs the application."""
        self.root.mainloop()