from utils import read_files, generate_population
from selection import Selection
from cross import Cross
from mutation import Mutation


if __name__ == '__main__':

    best_fitness = []
    best_perfomances = []
    best_risks = []
    best_population_chromosomes = []

    for thirty in range(30):
        generate_population.generate_input_population()
        population = read_files.read_population()  # original population
        #loop 100 generations
        for generation in range(100):
            # Selection
            selection = Selection(population)
            selection.cal_selection()
            original_rows = selection.rows

            # Cruce
            cross = Cross(original_rows)
            cross.cal_cross()
            crosses = []
            crosses = cross.return_crosses()

            # Mutation
            mutation = Mutation(crosses)
            mutation_fitness = mutation.cal_fitness()

            sustitution_chromosomes = []

            for i in range(0, len(mutation_fitness), 2):
                if (mutation_fitness[i] > mutation_fitness[i+1]):
                    sustitution_chromosomes.append(mutation_fitness[i])
                else:
                    sustitution_chromosomes.append(mutation_fitness[i+1])

            new_chromosomes = []
            for i in range(5):
                new_chromosomes.append(mutation.mutation_chromosomes[mutation_fitness.index(sustitution_chromosomes[i])])

            worst_indexes = selection.worst_fitness()

            for i in range(len(new_chromosomes)):
                population[worst_indexes[i]] = new_chromosomes[i]


        best_fitness.append(max(selection.fitness.fitness))
        best_perfomances.append(max(selection.fitness.performance))
        best_risks.append(max(selection.fitness.risk))
        idx = selection.fitness.fitness.index(max(selection.fitness.fitness))
        best_population_chromosomes.append(population[idx])

        f = open('./generation_population.txt', 'w')
        for value in population:
            f.write(','.join(map(str, value)))
            f.write('\n')
        f.close()

    #print(population)
    #print(len(population))
    print('Best Population Chromosomes ----------------- ', len(best_population_chromosomes))
    print(best_population_chromosomes)
    print('Best Fitness ------------------- ', len(best_fitness))
    print(best_fitness)
    print('Best Performance ------------------- ', len(best_perfomances))
    print(best_perfomances)
    print('Best Risk ------------------- ', len(best_risks))
    print(best_risks)

