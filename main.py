from selection import Selection
from cross import Cross
from mutation import Mutation

if __name__ == '__main__':
    # Selection
    selection = Selection(25)
    selection.cal_selection()
    original_rows = list(selection.rows.values())
    #print(original_rows)
    # for value in riginal_rows:
    #     print(value)

    # Cruce
    cross = Cross(list(selection.rows.values()))
    cross.cal_cross()
    crosses = cross.return_crosses()

    # for value in crosses:
    #    print(value)
    #    print(sum(value))

    # Mutation
    mutation = Mutation(crosses)
    #print(mutation.mutation_chromosomes)
    # for value in mutation.mutation_chromosomes:
    #     print(sum(value))