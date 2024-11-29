import tkinter as tk
from tkinter import ttk
from punnett_square import PunnettSquare
from table_frame import TableFrame
from stats_frame import StatsFrame


class InputFrame(tk.Frame):
    """Frame for user input."""
    def __init__(self, master=None):
        super().__init__(master, bg="antique white", pady=3)
        self.root = master
        self.create_widgets()

    def create_widgets(self):
        """Creates widgets for user input."""
        zygosity = ["Homozygous Dominant", "Homozygous Recessive", "Heterozygous"]
        CB_WIDTH = 25
        BG_COLOR = "antique white"
    
        self.label = tk.Label(self, text="Enter parent genotypes:", bg=BG_COLOR)
        self.label.grid(row=0, column=0, columnspan=2)

        self.parent1_label = tk.Label(self, text="Parent 1:", anchor="center", bg=BG_COLOR)
        self.parent1_label.grid(row=1, column=0)
        self.parent1_cb = ttk.Combobox(self, values=zygosity, state="readonly", width=CB_WIDTH, background=BG_COLOR)
        self.parent1_cb.grid(row=1, column=1)

        self.parent2_label = tk.Label(self, text="Parent 2:", anchor="center", bg=BG_COLOR)
        self.parent2_label.grid(row=2, column=0)
        self.parent2_cb = ttk.Combobox(self, values=zygosity, state="readonly", width=CB_WIDTH)
        self.parent2_cb.grid(row=2, column=1)

        # Dominant and Recessive Phenotypes for the gene
        self.phenotypes_label = tk.Label(self, text="Enter dominant and recessive phenotypes:", bg=BG_COLOR)
        self.phenotypes_label.grid(row=3, column=0, columnspan=2)
        # Dominant
        self.dominant_label = tk.Label(self, text="Dominant:", bg=BG_COLOR)
        self.dominant_label.grid(row=4, column=0)
        self.dominant_entry = tk.Entry(self, validate="key", validatecommand=(self.register(lambda x: x.isalpha()), "%S"))
        self.dominant_entry.grid(row=4, column=1)
        # Recessive
        self.recessive_label = tk.Label(self, text="Recessive:", bg=BG_COLOR)
        self.recessive_label.grid(row=5, column=0)
        self.recessive_entry = tk.Entry(self, validate="key", validatecommand=(self.register(lambda x: x.isalpha()), "%S"))
        self.recessive_entry.grid(row=5, column=1)

        self.calculate_button = tk.Button(self, text="Calculate", command=lambda: self.calculate())
        self.calculate_button.grid(row=6, column=0, columnspan=2)

        # Configure rows and columns to expand
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def calculate(self):
        """Calculates the genotypic and phenotypic ratios of the offspring."""
        self._validate()
        self.phenotypes = [self.dominant_entry.get(), self.recessive_entry.get()]
        parent1 = self.parent1_cb.get()
        parent2 = self.parent2_cb.get()
        self.ps = PunnettSquare(parent1, parent2, self.phenotypes)
        self.ps_table = self.ps.generate()
        self.genotypes = self.ps.genotypes
        # Table Frame
        self.table_frame = TableFrame(self.root, self.ps_table, self.phenotypes, self.genotypes)
        self.table_frame.grid(row=1, column=1, sticky="nsew")
        # Stats Frame
        self.stats_frame = StatsFrame(self.root, self.ps.get_ratios(), self.phenotypes, self.ps.type)
        self.stats_frame.grid(row=2, column=0, sticky="nsew", columnspan=2)

    def _validate(self):
        """Check if the user has entered a dominant and recessive phenotype."""
        if len(self.dominant_entry.get()) < 1 or len(self.recessive_entry.get()) < 1:
            self._error("Please enter a dominant and recessive phenotype.")
            raise ValueError("Please enter a dominant and recessive phenotype.")
        elif self.dominant_entry.get() == self.recessive_entry.get():
            self._error("Dominant and recessive phenotypes cannot be the same.")
            raise ValueError("Dominant and recessive phenotypes cannot be the same.")
        else:
            try:
                self.error_label.destroy()
            except AttributeError:
                pass

    def _error(self, message: str):
        """Displays an error message."""
        if hasattr(self, "error_label"):
            self.error_label.destroy()
        self.error_label = tk.Label(self, text=message, fg="red")
        self.error_label.grid(row=7, column=0, columnspan=2)
    