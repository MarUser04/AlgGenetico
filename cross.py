import random


class Cross:
    crosses = []
    parejas = []
    points = []
    prob_crosses = []

    def __init__(self, chromosomes):
        self.chromosomes = chromosomes
        self.crosses = []
        self.points = []
        self.prob_crosses = []
        self.parejas = []
        self.generate_crosses()

    def generate_crosses(self):
        rands = random.sample(range(len(self.chromosomes)), len(self.chromosomes))
        aux_chromosomes = self.chromosomes
        self.parejas = []
        for i in range(len(self.chromosomes)):
            self.parejas.append(aux_chromosomes[rands[i]])

    def cal_cross(self):
        self.crosses = []
        self.prob_crosses = []
        self.points = []

        for i in range(int(len(self.chromosomes) / 2)):
            self.prob_crosses.append(random.randint(0, 100))
            self.points.append(random.randint(1, 9))

        cont = 0
        for i in range(0, len(self.chromosomes), 2):
            crosses_aux1 = []
            crosses_aux2 = []
            for j in range(11):
                if self.prob_crosses[cont] <= 65:
                    if j < self.points[cont]:
                        crosses_aux1.append(self.parejas[i][j])
                        crosses_aux2.append(self.parejas[i+1][j])
                    else:
                        crosses_aux2.append(self.parejas[i][j])
                        crosses_aux1.append(self.parejas[i+1][j])
                else:
                    crosses_aux1.append(self.parejas[i][j])
                    crosses_aux2.append(self.parejas[i + 1][j])

            self.crosses.append(crosses_aux1)
            self.crosses.append(crosses_aux2)
            cont += 1

        self.verify_row_total()

    def verify_row_total(self):
        totales = []
        for i in range(len(self.crosses)):
            totales.append(sum(self.crosses[i]))

        for i, value in enumerate(self.crosses):
            for j in range(len(value)):
                self.crosses[i][j] = self.crosses[i][j] / totales[i]

    def return_crosses(self):
        return self.crosses
