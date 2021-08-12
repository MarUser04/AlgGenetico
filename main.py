from utils import read_files, generate_population
from selection import Selection
from cross import Cross
from mutation import Mutation


if __name__ == '__main__':

    best_fitness = []
    best_population_chromosomes = []

    for thirty in range(30):
        generate_population.generate_input_population()
        population = read_files.read_population()  # original population
        #loop 100 generations
        for generation in range(100):
            # Selection
            selection = Selection(25, population)
            selection.cal_selection()
            original_rows = selection.rows

            # Cruce
            cross = Cross(original_rows)
            cross.cal_cross()
            crosses = cross.return_crosses()

            # Mutation
            mutation = Mutation(crosses)
            mutation_fitness = mutation.cal_fitness()
            mutation_child_1 = mutation_fitness[0] if mutation_fitness[0] >= mutation_fitness[1] else mutation_fitness[1]
            mutation_child_2 = mutation_fitness[2] if mutation_fitness[2] >= mutation_fitness[3] else mutation_fitness[3]

            new_chromosome_1 = []
            new_chromosome_2 = []

            for i in range(11):
                new_chromosome_1.append(mutation.mutation_chromosomes[mutation_fitness.index(mutation_child_1)][i])
                new_chromosome_2.append(mutation.mutation_chromosomes[mutation_fitness.index(mutation_child_2)][i])

            worst_indexes = selection.worst_fitness()
            population[worst_indexes[0]] = new_chromosome_1
            population[worst_indexes[1]] = new_chromosome_2

            if(generation == 99):
                best_fitness.append(max(selection.fitness.fitness))
                idx = selection.fitness.fitness.index(max(selection.fitness.fitness))
                best_population_chromosomes.append(population[idx])

            f = open('./generation_population.txt', 'w')
            for value in population:
                f.write(','.join(map(str, value)))
                f.write('\n')
            f.close()

    #print(population)
    #print(len(population))
    print('Best Fitness ------------------- ', len(best_fitness))
    print(best_fitness)
    print('Best Population Chromosomes ----------------- ', len(best_population_chromosomes))
    print(best_population_chromosomes)

