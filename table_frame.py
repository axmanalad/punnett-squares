import tkinter as tk
from tkinter import ttk


class TableFrame(tk.Frame):
    """Frame for Punnett square table."""
    def __init__(self, master=None, ps=tuple, phenotypes=list, genotypes=list):
        super().__init__(master, bg="#4A9976", pady=3)
        self.table_label_frame = tk.Frame(self.master, bg="#4A9976")
        self.table_label_frame.grid(row=0, column=1)
        self.ps = ps
        self.phenotypes = phenotypes
        self.genotypes = genotypes
        self.create_widgets()

    def create_widgets(self):
        """Creates widgets for Punnett square table."""
        self.table_label = tk.Label(self.table_label_frame, text="Punnett Square Table", font=("Helvetica", 14, "bold"))
        self.table_label.grid(row=0, column=0)

        TABLE_HEIGHT = 3
        TABLE_WIDTH = 3
        k = 0
        for i in range(TABLE_HEIGHT):
            for j in range(TABLE_WIDTH):
                if i == 0 and j == 0:
                    label = tk.Label(self, text=" ", borderwidth=1, relief="solid", bg="black", font=("Helvetica", 16), width=5)
                elif i == 0:
                    label = tk.Label(self, text=f"{self.genotypes[0][j-1]}", borderwidth=1, relief="solid", bg="black", \
                                     fg="white", font=("Helvetica", 16), width=5)
                elif j == 0:
                    label = tk.Label(self, text=f"{self.genotypes[1][i-1]}", borderwidth=1, relief="solid", bg="black", \
                        fg="white", font=("Helvetica", 16), width=5)
                else:
                    label = tk.Label(self, text=f"{self.ps[0][k]}", borderwidth=1, relief="solid", font=("Helvetica", 16), width=5)
                    k += 1
                label.grid(row=i, column=j)
        self.grid_anchor("center")
        print(self.ps)