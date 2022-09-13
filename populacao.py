import math
from random import choice
from prettytable import PrettyTable

class Individuo:
    def __init__(self, alelo_pai, alelo_mae):
        self.locus = [alelo_pai, alelo_mae]


class Populacao:
    def __init__(self, n):
        self.tipos_de_individuos = ["aa", "Aa", "AA"]
        self.populacao = []
        self.init_pop(n)

        self.freq_a = 1
        self.freq_A = 0
        self.heterozigose_esperada = 2 * self.freq_a * self.freq_A

    
    def init_pop(self, n):
        for k in range(n):
            self.populacao.append(choice(self.tipos_de_individuos))
    
    @property
    def n(self):
        return len(self.populacao)

    def insert_individuo(self, n=0, list_individuo=[], random=True):
        if random:
            list_individuo = []
            for k in range(n):
                list_individuo.append(choice(self.tipos_de_individuos))
        self.populacao.append(list_individuo)
    
    @property
    def AA(self):
        return self.populacao.count("AA")

    @property
    def Aa(self):
        return self.populacao.count("Aa")

    @property
    def aa(self):
        return self.populacao.count("aa")

    @property
    def fAA(self):
        return self.AA/self.n

    @property
    def fAa(self):
        return self.Aa/self.n

    @property
    def faa(self):
        return self.aa/self.n
    
    @property
    def fA(self):
        return self.fAA + self.fAa/2

    @property
    def fa(self):
        return self.faa + self.fAa/2

    def frequencias_genotipicas(fA, fa):
        fAA_esperado = fA**2
        fAa_esperado = 2 * fA * fa
        faa_esperado = fa**2
        return fAA_esperado, fAa_esperado, faa_esperado

    def chi_quadrado(observado, esperado):
        total = 0
        for index in range(len(observado)):
            total += ((observado[index] - esperado[index]) ** 2) / esperado[index]
        return total
    
    def __str__(self):
        def round_freq(n):
            return round(n, 3)

        t = PrettyTable(["", "AA", "Aa", "aa"])
        t.add_row(["n", self.AA, self.Aa, self.aa])
        row = [self.fAA, self.fAa, self.faa]
        row = [round_freq(x) for x in row]
        t.add_row(["freqs"] + row)
        # t.add_row(["freqs", self.fAA, self.fAa, self.faa])
        result =  str(t)

        t = PrettyTable(["", "A", "a"])
        t.add_row(["freqs", round_freq(self.fA), round_freq(self.fa)])
        result += str(t)
        return result


pop = Populacao(300)
print(pop)