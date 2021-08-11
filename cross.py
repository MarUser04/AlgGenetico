import random


class Cross:
    cross1 = []
    cross2 = []
    cross3 = []
    cross4 = []
    pareja11 = []
    pareja12 = []
    pareja21 = []
    pareja22 = []
    point = 0
    point2 = 0
    prob_cross1 = 0
    prob_cross2 = 0

    def __init__(self, chromosomes):
        self.chromosomes = chromosomes
        self.generate_crosses()

    def generate_crosses(self):
        rands = random.sample(range(4), 4)
        aux_chromosomes = self.chromosomes
        self.pareja11 = aux_chromosomes[rands[0]]
        self.pareja12 = aux_chromosomes[rands[1]]
        self.pareja21 = aux_chromosomes[rands[2]]
        self.pareja22 = aux_chromosomes[rands[3]]

    def cal_cross(self):
        self.cross1 = []
        self.cross2 = []
        self.cross3 = []
        self.cross4 = []
        self.prob_cross1 = random.randint(0, 100)  # prob cruce 1
        self.prob_cross2 = random.randint(0, 100)  # prob cruce 2
        self.point = random.randint(1, 9)  # cruce primera pareja
        self.point2 = random.randint(1, 9)  # cruce segunda pareja

        if self.prob_cross1 <= 65:
            for i in range(11):
                if i < self.point:
                    self.cross1.append(self.pareja11[i])
                    self.cross2.append(self.pareja12[i])
                else:
                    self.cross1.append(self.pareja12[i])
                    self.cross2.append(self.pareja11[i])
        else:
            self.cross1 = self.pareja11
            self.cross2 = self.pareja12

        if self.prob_cross2 <= 65:
            for i in range(11):
                if i < self.point2:
                    self.cross3.append(self.pareja21[i])
                    self.cross4.append(self.pareja22[i])
                else:
                    self.cross3.append(self.pareja22[i])
                    self.cross4.append(self.pareja21[i])
        else:
            self.cross3 = self.pareja21
            self.cross4 = self.pareja22

        self.verify_row_total()

    def verify_row_total(self):
        total_1 = sum(self.cross1)
        total_2 = sum(self.cross2)
        total_3 = sum(self.cross3)
        total_4 = sum(self.cross4)

        for i in range(11):
            self.cross1[i] = self.cross1[i] / total_1
            self.cross2[i] = self.cross2[i] / total_2
            self.cross3[i] = self.cross3[i] / total_3
            self.cross4[i] = self.cross4[i] / total_4

    def return_crosses(self):
        return [
            self.cross1,
            self.cross2,
            self.cross3,
            self.cross4,
        ]

    def print_crosses(self):
        print('Pareja 1 ----------------------------')
        print(self.point)
        print(self.prob_cross1)
        print(self.pareja11)
        print(self.pareja12)
        print('--------------------------')
        print(self.cross1)
        print(self.cross2)
        print(' Pareja 2 ----------------------------')
        print(self.point2)
        print(self.prob_cross2)
        print(self.pareja21)
        print(self.pareja22)
        print('--------------------------')
        print(self.cross3)
        print(self.cross4)