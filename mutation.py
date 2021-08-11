import random
from fitness import Fitness


class Mutation:
    mutation_chromosomes = []

    def __init__(self, crosses):
        self.mutation_chromosomes = []
        self.crosses = []
        self.crosses = crosses
        self.cal_mutation()

    def cal_mutation(self):
        prob_mutation = random.randint(0, 100)
        for value in self.crosses:
            if prob_mutation <= 2:
                rands = random.sample(range(11), 2)
                sum_values = value[rands[0]] + value[rands[1]]
                upd1 = random.uniform(0, sum_values)
                upd2 = sum_values - upd1

                value[rands[0]] = upd1
                value[rands[1]] = upd2
            self.mutation_chromosomes.append(value)

    def cal_fitness(self):
        fitness = Fitness(self.mutation_chromosomes)
        return fitness.fitness
