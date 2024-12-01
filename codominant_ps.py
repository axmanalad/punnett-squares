from punnett_square import PunnettSquare


class CodominantPS(PunnettSquare):
    def __init__(self, parent1, parent2, phenotypes, type="Codominant"):
        super().__init__(parent1, parent2, phenotypes, type)
    # TODO: Add methods to calculate codominant inheritance

    def _find_phenotype(self, zygosity: str):
        if zygosity == "Homozygous Dominant":
            return self.phenotypes[0]
        elif zygosity == "Homozygous Recessive":
            return self.phenotypes[1]
        else:
            return self.phenotypes[2]
        
    def get_phenotypic_ratio(self):
        phenotyipic_ratio = {self.phenotypes[i]: 0 for i in range(len(self.phenotypes))}
        for phenotype in self._possible_phenotypes:
            phenotyipic_ratio[phenotype] += 1
        # Simplify the phenotypic ratio (Ex. 2:2 -> 1:1)
        if 0 in phenotyipic_ratio.values() and list(phenotyipic_ratio.values()).count(0) == 1:
            for key, value in phenotyipic_ratio.items():
                if value == 0:
                    continue
                if value % 2 == 0:
                    phenotyipic_ratio[key] = value // 2
        return phenotyipic_ratio