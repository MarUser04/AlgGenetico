from utils import read_files, generate_population
from selection import Selection
from cross import Cross
from mutation import Mutation


if __name__ == '__main__':

    generate_population.generate_input_population()
    population = read_files.read_population() #original population

    #loop
    for w in range(10):
        # Selection
        selection = Selection(25, population)
        selection.cal_selection()
        original_rows = list(selection.rows.values())

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


    print(population)
    f = open('./generation_population.txt', 'w')
    for value in population:
        f.write(','.join(map(str, value)))
        f.write('\n')
    f.close()
