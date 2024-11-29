from punnett_square import PunnettSquare


class BloodTypePS(PunnettSquare):
    def __init__(self, parent1, parent2, phenotypes, type="Blood"):
        super().__init__(parent1, parent2, phenotypes, type)
    # TODO: Add methods to calculate blood type inheritance