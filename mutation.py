import random


class Mutation:
    mutation_chromosomes = []

    def __init__(self, crosses):
        self.crosses = crosses
        self.cal_mutation()

    def cal_mutation(self):
        for value in self.crosses:
            rands = random.sample(range(11), 2)
            sum_values = value[rands[0]] + value[rands[1]]
            upd1 = random.uniform(0, sum_values)
            upd2 = sum_values - upd1

            value[rands[0]] = upd1
            value[rands[1]] = upd2
            self.mutation_chromosomes.append(value)
