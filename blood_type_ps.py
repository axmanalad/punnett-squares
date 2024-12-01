from punnett_square import PunnettSquare


class BloodTypePS(PunnettSquare):
    def __init__(self, parent1, parent2, type="Blood"):
        phenotypes = [parent1[5:], parent2[5:]]
        super().__init__(parent1, parent2, phenotypes, type)
        
    def _set_parent_genotypes(self):
        """Sets the genotypes of the parents
        """
        TYPE_A = "A"
        TYPE_B = "B"
        TYPE_O = "O"

        if self.parent1 == "Type A":
            self.genotypes.append(TYPE_A + TYPE_A)
        elif self.parent1 == "Type B":
            self.genotypes.append(TYPE_B + TYPE_B)
        elif self.parent1 == "Type AB":
            self.genotypes.append(TYPE_A + TYPE_B)
        else:
            self.genotypes.append(TYPE_O + TYPE_O)

        if self.parent2 == "Type A":
            self.genotypes.append(TYPE_A + TYPE_A)
        elif self.parent2 == "Type B":
            self.genotypes.append(TYPE_B + TYPE_B)
        elif self.parent2 == "Type AB":
            self.genotypes.append(TYPE_A + TYPE_B)
        else:
            self.genotypes.append(TYPE_O + TYPE_O)

    
    def _detect_zygosity(self, gene1: str, gene2: str):
        raise NotImplementedError
    
    def _find_phenotype(self, zygosity: str):
        raise NotImplementedError

    def _find_phenotype(self, gene1: str, gene2: str):
        if (gene1 == "A" and gene2 == "A") or (gene1 == "A" and gene2 == "O"):
            return "Type A"
        elif (gene1 == "B" and gene2 == "B") or (gene1 == "B" and gene2 == "O"):
            return "Type B"
        elif gene1 == "A" and gene2 == "B":
            return "Type AB"
        else:
            return "Type O"
        
    def _swap_genotypes(self):
        if "AB" in self.genotypes:
            self._possible_genotypes[1], self._possible_genotypes[2] = self._possible_genotypes[2], self._possible_genotypes[1]
            self._possible_phenotypes[1], self._possible_phenotypes[2] = self._possible_phenotypes[2], self._possible_phenotypes[1]
        
    def _make_all_combinations(self):
        return ["AA", "AB", "BB", "AO", "BO", "OO"]

    def generate(self):
        """Generates the possible blood genotypes and phenotypes of the offspring.
        
        Returns:
            tuple: The possible blood genotypes and phenotypes of the offspring
        """
        self._set_parent_genotypes()
        for gene1 in self.genotypes[0]:
            for gene2 in self.genotypes[1]:
                genotype = gene1 + gene2 if gene1 < gene2 else gene2 + gene1
                self._possible_genotypes.append(genotype)
                phenotype = self._find_phenotype(genotype[0], genotype[1])
                self._possible_phenotypes.append(phenotype)
        self._swap_genotypes()
        return self.get_possible_genotypes, self.get_possible_phenotypes
    
    def get_genotypic_ratio(self):
        combinations = self._make_all_combinations()
        genotypic_ratio = {combinations[i]:0 for i in range(len(combinations))}
        for genotype in self._possible_genotypes:
            genotypic_ratio[genotype] += 1
        # Simplify the genotypic ratio
        if 0 in genotypic_ratio.values() and list(genotypic_ratio.values()).count(0) == 4:
            for key, value in genotypic_ratio.items():
                if value == 0:
                    continue
                if value % 2 == 0:
                    genotypic_ratio[key] = value // 2
        return genotypic_ratio

    def get_phenotypic_ratio(self):
        phenotypes = ["Type A", "Type B", "Type AB", "Type O"]
        phenotyipic_ratio = {phenotypes[i]: 0 for i in range(len(phenotypes))}
        for phenotype in self._possible_phenotypes:
            phenotyipic_ratio[phenotype] += 1
        # Simplify the phenotypic ratio (Ex. 2:2 -> 1:1)
        if 0 in phenotyipic_ratio.values() and list(phenotyipic_ratio.values()).count(0) == 2:
            for key, value in phenotyipic_ratio.items():
                if value == 0:
                    continue
                if value % 2 == 0:
                    phenotyipic_ratio[key] = value // 2
        return phenotyipic_ratio
    
