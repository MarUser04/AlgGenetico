import random
from fitness import Fitness


class Selection:
    global_population = []
    rows = []  # rows after division
    aux_population_selecteds = []  # aux population

    def __init__(self, population):
        self.fitness = Fitness(population)  # get population
        self.global_population = population

    def get_population(self, population):
        self.global_population = population
        self.fitness = Fitness(population)

    def cal_selection(self):
        selecteds = []
        remaining = [*self.fitness.fitness]
        self.aux_population_selecteds = []
        self.rows = []
        for i in range(10):
            population_random = random.sample(remaining, 22)
            self.aux_population_selecteds.append(population_random)
            selecteds = [*selecteds, *population_random]
            for element in population_random:
                remaining.remove(element)

        for i in range(10):
            aux_row = []
            for j in range(11):
                aux_row.append(self.fitness.population[self.fitness.fitness.index(max(self.aux_population_selecteds[i]))][j])
            self.rows.append(aux_row)

    def worst_fitness(self):
        minimums = []
        indexes = []
        for i in range(5):
            minimums.append(self.fitness.fitness.index(min(self.aux_population_selecteds[i])))
        for i in range(len(minimums)):
            indexes.append(min(minimums))
        return indexes



