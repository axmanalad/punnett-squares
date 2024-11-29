class PunnettSquare:
    """A class to represent a Punnett Square"""
    def __init__(self, parent1, parent2, phenotypes, type="Monohybrid"):
        self.parent1 = parent1
        self.parent2 = parent2
        self.genotypes = []
        self.phenotypes = phenotypes # Phenotypes listed in descending order: dominant, recessive
        self.type = type
        self._possible_genotypes = []
        self._possible_phenotypes = []

    def _detect_zygosity(self, gene1: str, gene2: str):
        """Detects the zygosity of the gene pair
        
        Args:
            gene1 (str): The first gene
            gene2 (str): The second gene
        Returns:
            str: The zygosity of the gene pair
        """
        if gene1 == gene2:
            if gene1 == gene1.upper():
                return "Homozygous Dominant"
            else:
                return "Homozygous Recessive"
        else:
            return "Heterozygous"
        
    def _find_phenotype(self, zygosity: str):
        """Finds the phenotype of the offspring
        
        Args:
            zygosity (str): The zygosity of the gene pair
            
        Returns:
            str: The phenotype of the offspring
        """
        if zygosity == "Homozygous Dominant" or zygosity == "Heterozygous":
            return self.phenotypes[0]
        else:
            return self.phenotypes[1]

    def _set_parent_genotypes(self):
        """Sets the genotypes of the parents
        """
        allele = self.phenotypes[0][0]
        HOM_D = allele.upper() + allele.upper()
        HOM_R = allele.lower() + allele.lower()
        HET = allele.upper() + allele.lower()

        if self.parent1 == "Homozygous Dominant":
            self.genotypes.append(HOM_D)
        elif self.parent1 == "Homozygous Recessive":
            self.genotypes.append(HOM_R)
        else:
            self.genotypes.append(HET)

        if self.parent2 == "Homozygous Dominant":
            self.genotypes.append(HOM_D)
        elif self.parent2 == "Homozygous Recessive":
            self.genotypes.append(HOM_R)
        else:
            self.genotypes.append(HET)

    def _make_all_combinations(self):
        """Makes all possible combinations of genotypes."""
        allele = self.phenotypes[0][0]
        combinations = []
        combinations.append(f"{allele.upper()}{allele.upper()}")
        combinations.append(f"{allele.upper()}{allele.lower()}")
        combinations.append(f"{allele.lower()}{allele.lower()}")
        return combinations

    def generate(self):
        """Generates the possible genotypes and phenotypes of the offspring

        Returns:
            tuple: The possible genotypes and phenotypes of the offspring
        """
        self._set_parent_genotypes()
        for gene1 in self.genotypes[0]:
            for gene2 in self.genotypes[1]:
                genotype = gene1 + gene2 if gene1 < gene2 else gene2 + gene1
                self._possible_genotypes.append(genotype)
                zygosity = self._detect_zygosity(gene1, gene2)
                phenotype = self._find_phenotype(zygosity)
                self._possible_phenotypes.append(phenotype)

        # Only swaps the second and third genotypes/phenotypes if parents are dominant/recessive and heterozygous
        a1 = self._possible_genotypes[1]
        a2 = self._possible_genotypes[2]
        if self._detect_zygosity(a1[0], a1[1]) == "Homozygous Recessive" or self._detect_zygosity(a1[0], a1[1]) == "Homozygous Dominant" and \
            self._detect_zygosity(a2[0], a2[1]) == "Heterozygous" or self._detect_zygosity(a1[0], a1[1]) == "Heterozygous" and \
                self._detect_zygosity(a2[0], a2[1]) == "Homozygous Recessive" or self._detect_zygosity(a2[0], a2[1]) == "Homozygous Dominant":
            self._possible_genotypes[1], self._possible_genotypes[2] = self._possible_genotypes[2], self._possible_genotypes[1]
            self._possible_phenotypes[1], self._possible_phenotypes[2] = self._possible_phenotypes[2], self._possible_phenotypes[1]
        return self.get_possible_genotypes, self.get_possible_phenotypes

    def get_genotypic_ratio(self):
        """Gets the genotypic ratio of the offspring
        
        Returns:
            dict: The genotypic ratio of the offspring
        """
        combinations = self._make_all_combinations()
        genotypic_ratio = {combinations[i]:0 for i in range(len(combinations))}
        for genotype in self._possible_genotypes:
            genotypic_ratio[genotype] += 1
        # Simplify the genotypic ratio (Ex. 0:2:2 -> 0:1:1)
        if 0 in genotypic_ratio.values() and list(genotypic_ratio.values()).count(0) == 1:
            for key, value in genotypic_ratio.items():
                if value == 0:
                    continue
                if value % 2 == 0:
                    genotypic_ratio[key] = value // 2
        return genotypic_ratio
    
    def get_phenotypic_ratio(self):
        """Gets the phenotypic ratio of the offspring
        
        Returns:
            dict: The phenotypic ratio of the offspring
        """
        phenotypic_ratio = {self.phenotypes[i]:0 for i in range(len(self.phenotypes))}
        for phenotype in self._possible_phenotypes:
            phenotypic_ratio[phenotype] += 1
        # Simplify the phenotypic ratio (Ex. 2:2 -> 1:1)
        keys = list(phenotypic_ratio.keys())
        if phenotypic_ratio[keys[0]] == phenotypic_ratio[keys[1]]:
            for key, value in phenotypic_ratio.items():
                phenotypic_ratio[key] = value // 2
        return phenotypic_ratio
    
    def get_ratios(self):
        """Gets the genotypic and phenotypic ratios of the offspring
        
        Returns:
            dict: The genotypic and phenotypic ratios of the offspring
        """
        return {"genotypic_ratio": self.get_genotypic_ratio(), "phenotypic_ratio": self.get_phenotypic_ratio()}

    @property
    def get_possible_genotypes(self):
        return self._possible_genotypes
    
    @property
    def get_possible_phenotypes(self):
        return self._possible_phenotypes
