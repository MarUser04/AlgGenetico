import random
from fitness import Fitness


class Selection:
    global_population = []
    rows = []  # rows after division
    aux_population_selecteds = []  # aux population

    def __init__(self, divide, population):
        self.divide = divide
        self.fitness = Fitness(population)  # get population
        self.global_population = population
        self.percentage = int((self.divide * len(self.fitness.fitness)) / 100)

    def get_population(self, population):
        self.global_population = population
        self.fitness = Fitness(population)

    def cal_selection(self):
        selecteds = []
        remaining = [*self.fitness.fitness]
        self.aux_population_selecteds = []
        for i in range(4):
            population_random = random.sample(remaining, 55)
            self.aux_population_selecteds.append(population_random)
            selecteds = [*selecteds, *population_random]
            for element in population_random:
                remaining.remove(element)

        for i in range(4):
            aux_row = []
            for j in range(11):
                aux_row.append(self.fitness.population[self.fitness.fitness.index(max(self.aux_population_selecteds[i]))][j])
            self.rows.append(aux_row)

    def worst_fitness(self):
        minimums = []
        for i in range(4):
            minimums.append(self.fitness.fitness.index(min(self.aux_population_selecteds[i])))
        min1 = min(minimums)
        minimums.remove(min1)
        min2 = min(minimums)
        minimums.remove(min2)

        return [min1, min2]



