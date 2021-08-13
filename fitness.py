from utils import read_files


class Fitness:
    performance = []
    risk = []
    fitness = []
    population = []

    def __init__(self, population):
        self.population = []
        self.fitness = []
        self.performance = []
        self.risk = []
        self.population = population
        self.calculate_fitness()

    def calculate_max(self):
        self.performance = []
        perfomance_file = read_files.read_performance()
        max = []
        for chromosome in self.population:
            acum = 0
            for idx, gen in enumerate(chromosome):
                acum += (float(gen) * perfomance_file[idx])
            max.append(acum)
        self.performance = max

    def calculate_min(self):
        self.risk = []
        covar = read_files.read_covar()
        min = []
        for chromosome in self.population:
            acum = 0
            for idx_i, gen_i in enumerate(chromosome):
                for idx_j, gen_j in enumerate(chromosome):
                    acum += (float(gen_i) * float(gen_j) * covar[idx_i][idx_j])
            min.append(acum)
        self.risk = min

    def calculate_fitness(self):
        self.calculate_min()
        self.calculate_max()
        self.fitness = []
        for idx, value in enumerate(self.performance):
            self.fitness.append(self.performance[idx] / self.risk[idx])




