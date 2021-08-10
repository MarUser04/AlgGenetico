import random
from utils import read_files
from fitness import Fitness


class Selection:
    fitness = Fitness(read_files.read_population())
    population = {}
    rows = {}

    def __init__(self, divide):
        self.divide = divide
        self.percentage = int((self.divide * len(self.fitness.fitness)) / 100)
        for i in range(int(len(self.fitness.fitness) / self.percentage)):
            self.population["population_{}".format(i)] = []
            self.rows["rows_pop_{}".format(i)] = []

    def cal_selection(self):
        selecteds = []
        count = 0
        while count < int(len(self.fitness.fitness) / self.percentage):
            rand = random.choice(self.fitness.fitness)
            if rand not in selecteds:
                self.population['population_{}'.format(count)].append(rand)
                selecteds.append(rand)

            if len(self.population['population_{}'.format(count)]) == self.divide:
                count += 1

        for i in range(4):
            for j in range(11):
                self.rows['rows_pop_{}'.format(i)].append(self.fitness.population[self.fitness.fitness.index(max(self.population['population_{}'.format(i)]))][j])



