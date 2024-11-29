import tkinter as tk


class TitleFrame(tk.Frame):
    """Frame for title."""
    def __init__(self, master=None):
        super().__init__(master, bg="peach puff", pady=3)
        self.create_widgets()

    def create_widgets(self):
        """Creates widgets for title."""
        BG_COLOR = "peach puff"
        self.title_label = tk.Label(self, text="Punnett Square Calculator", font=("Helvetica", 16, "bold"), bg=BG_COLOR)
        self.title_label.grid(row=0, column=0, columnspan=2)

        self.subtitle_label = tk.Label(self, text="Calculate the genotypes of \noffspring from two parent genotypes.", bg=BG_COLOR)
        self.subtitle_label.grid(row=1, column=0, columnspan=2)
        
        self.grid_anchor("center")