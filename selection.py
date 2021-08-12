import random
from fitness import Fitness


class Selection:
    global_population = []
    aux_population = {}  # aux population
    rows = {}  # aux rows after division

    def __init__(self, divide, population):
        self.divide = divide
        self.fitness = Fitness(population)  # get population
        self.global_population = population
        self.percentage = int((self.divide * len(self.fitness.fitness)) / 100)
        for i in range(int(len(self.fitness.fitness) / self.percentage)):
            self.aux_population['population_{}'.format(i)] = []
            self.rows["rows_pop_{}".format(i)] = []

    def get_population(self, population):
        self.global_population = population
        self.fitness = Fitness(population)

    def cal_selection(self):
        selecteds = []
        remaining = [*self.fitness.fitness]
        for i in range(4):
            population_random = random.sample(remaining, min(len(remaining), 55))
            self.aux_population['population_{}'.format(i)] = population_random
            selecteds = [*selecteds, *population_random]
            remaining = list(set(remaining) - set(selecteds))

        for i in range(4):
            for j in range(11):
                self.rows['rows_pop_{}'.format(i)].append(self.fitness.population[self.fitness.fitness.index(max(self.aux_population['population_{}'.format(i)]))][j])

    def worst_fitness(self):
        minimums = []
        for i in range(4):
            minimums.append(self.fitness.fitness.index(min(self.aux_population['population_{}'.format(i)])))
        min1 = min(minimums)
        minimums.remove(min1)
        min2 = min(minimums)
        minimums.remove(min2)

        return [min1, min2]



