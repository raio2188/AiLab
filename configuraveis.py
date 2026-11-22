import random

from ativacao import leaky_relu as lr, derivada_leaky_relu as dlr

entradas = [1, 2]
pesos_oculta = [
    [0.5 , 1], 
    [1, 0.6]
]
bias_oculta = [1, -0.5]
saidas = []

def camada_oculta(entradas):
    saidas = []
    for i in range(len(pesos_oculta)):
        z = 0
        for j in range(len(entradas)):
            z += entradas[j] * pesos_oculta[i][j] 

        z += bias_oculta[i]
        saidas.append(lr(z))
    return saidas

print(camada_oculta([1, 2]))
print(camada_oculta([0, 0]))