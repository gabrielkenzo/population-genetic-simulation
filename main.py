from random import choice

class IndividuoHaploide:
    def __init__(self, alelo):
        self.locus = alelo


class IndividuoDiploide:
    def __init__(self, alelo_pai, alelo_mae):
        self.locus = [alelo_pai, alelo_mae]


class Populacao:
    def __init__(self, tipo):
        self.populacao = []
        # self.n = len(populacao)

        # self.heterozigotos =
        # self.heterozigose_observada = self.heterozigotos / self.n

        self.freq_a = 1
        self.freq_A = 0
        self.heterozigose_esperada = 2 * self.freq_a * self.freq_A

        match tipo:
            case "homozigoto":
                self.tipos_de_individuos = ["a", "A"]
            case "heterozigoto":
                self.tipos_de_individuos = ["aa", "aA", "Aa", "AA"]

    def insert_individuo(self, list_individuo, random=False, n=0):
        if random:
            list_individuo = []
            for k in range(n):
                list_individuo.append(choice(self.tipos_de_individuos))
        self.pop.append(list_individuo)

    def __str__(self):
        print("olar")
        return ""


# pop = Populacao("homozigoto")
# print(pop)


nAA = 298
nAa = 489
naa = 213
n_total = nAA + nAa + naa

observado = [nAA, nAa, naa]


def frequencias_alelicas(nAA, nAa, naa):
    n_total = nAA + nAa + naa

    fA = nAA + nAa / 2
    fA /= n_total

    fa = naa + nAa / 2
    fa /= n_total

    return fA, fa


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


esperado = frequencias_genotipicas(*frequencias_alelicas(nAA, nAa, naa))
esperado = list(esperado)
esperado = [f * n_total for f in esperado]

print(observado)
print(esperado)
print(chi_quadrado(observado, esperado))

heterozigotos = (esperado[1] - observado[1]) / esperado[1]
print()
print(heterozigotos)
print(heterozigotos**2)
print(n_total * heterozigotos**2)
sla = ((observado[1] - esperado[1]) ** 2) / esperado[1]
sla /= esperado[1] / n_total
print(sla)
+