import tkinter as tk


class StatsFrame(tk.Frame):
    """Frame for displaying stats."""
    def __init__(self, master=None, stats=dict, phenotypes=list, type="Monohybrid"):
        super().__init__(master, bg="gray25", pady=3, highlightthickness=3, highlightbackground="#ffffff")
        self.stats = stats
        self.phenotypes = phenotypes
        self.type = type
        self.create_widgets()
    
    def create_widgets(self):
        """Creates widgets for displaying stats."""
        LABEL_FONT = ("Helvetica", 12, "bold")
        VALUE_FONT = ("Helvetica", 12)
        BG_COLOR = "gray25"
        G_COLOR = "spring green"
        P_COLOR = "deep pink"
        self.stats_label = tk.Label(self, text="Statistical Data", font=("Helvetica", 14, "bold", "underline"), bg=BG_COLOR, fg="cyan")
        self.stats_label.grid(row=0, column=0, columnspan=3)
        self.stats_label.grid_anchor("center")

        # Genotype
        self.genotypic_ratio_label = tk.Label(self, text=f"Genotypic Ratio: ", font=LABEL_FONT, bg=BG_COLOR, fg=G_COLOR)
        self.genotypic_ratio_label.grid(row=1, column=0, columnspan=2)
        self.genotypic_ratio_value = tk.Label(self, text=f"{self.format_stats().get('genotypic_ratio')}", font=VALUE_FONT, bg=BG_COLOR, fg="white")
        self.genotypic_ratio_value.grid(row=2, column=0, columnspan=2)
        # Percentage of each genotype
        self.genotypic_percentage_label = tk.Label(self, text=f"Genotypic Percentage(s): ", font=LABEL_FONT, bg=BG_COLOR, fg=G_COLOR)
        self.genotypic_percentage_label.grid(row=1, column=1, columnspan=2)
        self.genotypic_percentage_value = tk.Label(self, text=f"{self.format_percentage().get('genotypic_percentage')}", font=VALUE_FONT, \
                                                   bg=BG_COLOR, fg="white")
        self.genotypic_percentage_value.grid(row=2, column=1, columnspan=2)

        # Phenotype
        self.phenotypic_ratio_label = tk.Label(self, text=f"Phenotypic Ratio: ", font=LABEL_FONT, bg=BG_COLOR, fg=P_COLOR)
        self.phenotypic_ratio_label.grid(row=3, column=0)
        self.phenotypic_ratio_value = tk.Label(self, text=f"{self.format_stats().get('phenotypic_ratio')}", font=VALUE_FONT, \
                                               bg=BG_COLOR, fg="white")
        self.phenotypic_ratio_value.grid(row=4, column=0)
        # Percentage of each phenotype
        self.phenotypic_percentage_label = tk.Label(self, text=f"Phenotypic Percentage(s): ", font=LABEL_FONT, bg=BG_COLOR, fg=P_COLOR)
        self.phenotypic_percentage_label.grid(row=3, column=2)
        self.phenotypic_percentage_value = tk.Label(self, text=f"{self.format_percentage().get('phenotypic_percentage')}", font=VALUE_FONT, \
                                                    bg=BG_COLOR, fg="white")
        self.phenotypic_percentage_value.grid(row=4, column=2)

        self.grid_anchor("center")
    
    def format_stats(self):
        """Formats stats for display."""
        genotypic_ratio = self.stats.get("genotypic_ratio")
        phenotypic_ratio = self.stats.get("phenotypic_ratio")
        genotypic_ratio = self._format_ratio(genotypic_ratio, "genotypic")
        phenotypic_ratio = self._format_ratio(phenotypic_ratio, "phenotypic")
        return {"genotypic_ratio": genotypic_ratio, "phenotypic_ratio": phenotypic_ratio}
    
    def format_percentage(self):
        """Formats percentage for display."""
        genotypic_ratio = self.stats.get("genotypic_ratio")
        phenotypic_ratio = self.stats.get("phenotypic_ratio")
        genotypic_percentage = self._format_percentage(genotypic_ratio, "genotypic")
        phenotypic_percentage = self._format_percentage(phenotypic_ratio, "phenotypic")
        return {"genotypic_percentage": genotypic_percentage, "phenotypic_percentage": phenotypic_percentage}
    
    def _format_ratio(self, ratio: dict, type: str):
        """Formats ratios for display."""
        formatted_ratio = ""
        if type == "genotypic":
            keys = list(ratio.keys())
            return ":".join([str(ratio.get(key)) for key in keys[:len(ratio)]])
        elif type == "phenotypic":
            for value in ratio.values():
                formatted_ratio += f"{value}:"
        return formatted_ratio[:-1]
    
    def _format_percentage(self, ratio: dict, type: str):
        """Formats monohybrid percentages for display."""
        formatted_percentage = ""
        if type == "genotypic":
            total = sum(ratio.values())
            for key, value in ratio.items():
                formatted_percentage += f"{key}: {(value / total) * 100:.2f}%\n"
        elif type == "phenotypic":
            total = sum(ratio.values())
            for key, value in ratio.items():
                formatted_percentage += f"{key}: {(value / total) * 100:.2f}%\n"
        return formatted_percentage.rsplit("\n", 1)[0]
    