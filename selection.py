import random
from fitness import Fitness


class Selection:
    rows = []  # rows after division
    aux_population_selecteds = []  # aux population

    def __init__(self, population):
        self.aux_population_selecteds = []
        self.rows = []
        self.fitness = Fitness(population)  # get population

    def cal_selection(self):
        remaining = [*self.fitness.fitness]
        self.aux_population_selecteds = []
        self.rows = []
        for i in range(10):
            population_random = random.sample(remaining, 22)
            self.aux_population_selecteds.append(population_random)
            for element in population_random:
                remaining.remove(element)

        for i in range(10):
            aux_row = []
            for j in range(11):
                aux_row.append(self.fitness.population[self.fitness.fitness.index(max(self.aux_population_selecteds[i]))][j])
            self.rows.append(aux_row)

    def worst_fitness(self):
        indexes = []
        aux_fitness = self.fitness.fitness
        while len(indexes) < 5:
            indexes.append(aux_fitness.index(min(aux_fitness)))
            aux_fitness.remove(min(aux_fitness))
        return indexes



