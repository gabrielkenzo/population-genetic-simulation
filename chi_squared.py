#Nao funciona

def Exercicio():
    nAA = 298
    nAa = 489
    naa = 213
    n_total = nAA + nAa + naa

    observado = [nAA, nAa, naa]
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