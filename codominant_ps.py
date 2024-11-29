from punnett_square import PunnettSquare


class CodominantPS(PunnettSquare):
    def __init__(self, parent1, parent2, phenotypes, type="Codominant"):
        super().__init__(parent1, parent2, phenotypes, type)
    # TODO: Add methods to calculate codominant inheritance