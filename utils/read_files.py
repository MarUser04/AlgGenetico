def read_performance():
    f = open('perfomance.txt', 'r')
    perfomance = f.readlines()
    f.close()
    perfomance = [x.replace('\t', ' ').replace('\n', '') for x in perfomance]
    perfomance = [float(x) for x in perfomance]

    return perfomance


def read_population():
    f = open('input-population.txt', 'r')
    population_strings = f.readlines()
    f.close()

    population = []
    for line in population_strings:
        line = list(line.split(','))
        line = [x.replace('\n', '') for x in line]
        value_float = [float(x) for x in line]
        population.append(value_float)

    return population


def read_covar():
    f = open('covar.txt', 'r')
    covar_strings = f.readlines()
    f.close()
    covar_strings = [x.replace('\t', ' ').replace('\n', ' ') for x in covar_strings]

    covar_floats = []
    for line in covar_strings:
        line = list(line.split())
        value_float = [float(x) for x in line]
        covar_floats.append(value_float)

    return covar_floats