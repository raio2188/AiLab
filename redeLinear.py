import random
from ativacao import Identidade, Derivada_Identidade

entradas = [
    [1, 2],
    [2, 3],
    [3, 4],
    [5, 6],
    [7, 2],
    [4, 9],
    [10, 10],
    [3, 15],
    [20, 5],
    [-5, 10],
    [-10, -20],
    [0, 0],
    [10, -15],
    [-20, 5]
]
esperados = [3, 5, 7, 11, 9, 13, 20, 18, 25, 5, -30, 0, -5, -15]

peso1 = 0.7
peso2 = 0.4
bias_h1 = 1
bias_h2 = -1
w1_h1 = 0.5
w2_h1 = 0.8
w1_h2 = -0.3
w2_h2 = 0.6
taxa = 0.0001
bias_y = 0.5

pares = list(zip(entradas, esperados))


def soma(x1, x2):
    h1 = Identidade(w1_h1 * x1 + w2_h1 * x2 + bias_h1)
    h2 = Identidade(w1_h2 * x1 + w2_h2 * x2 + bias_h2)

    y = peso1 * h1 + peso2 * h2 + bias_y
    print(f"teste {x1} + {x2}: {y}")

    print(f"h1: {h1}")
    print(f"h2: {h2}")
    print(f"bias saida: {bias_y}")
    print(f"peso1: {peso1}")
    print(f"peso2: {peso2}\n")

for epoca in range(10001):
    erro_total = 0
    random.shuffle(pares)

    for (x1, x2), esperado in pares:
        h1 = Identidade(w1_h1 * x1 + w2_h1 * x2 + bias_h1)
        h2 = Identidade(w1_h2 * x1 + w2_h2 * x2 + bias_h2)
    
        y = ( peso1 * h1 + peso2 * h2 + bias_y)

        erro = y - esperado
        erro_total += abs(erro)

        erroh1 = erro * peso1 * Derivada_Identidade(h1)
        erroh2 = erro * peso2 * Derivada_Identidade(h2)
  
        w1_h1 = w1_h1 - (erroh1 * x1 * taxa)
        w2_h1 = w2_h1 - (erroh1 * x2 * taxa)
  
        w1_h2 = w1_h2 - (erroh2 * x1 * taxa)
        w2_h2 = w2_h2 - (erroh2 * x2 * taxa)

        bias_h1 = bias_h1 - (erroh1 * taxa)   
        bias_h2 = bias_h2 - (erroh2 * taxa)   
    
        peso1 = peso1 - (erro * h1 * taxa)
        peso2 = peso2 - (erro * h2 * taxa)

        bias_y = bias_y - (erro * taxa)

        erro_medio = erro_total / len(entradas)
        
    if epoca % 1000 == 0:
        print(f"Época {epoca} | Erro médio: {erro_medio:.6f}")

soma(10, 21)
soma(50, 80)
soma(-30, -40)
soma(15, -25)
soma(0, 0)

print(f"Saída final: {y}")
print(f"Erro final: {erro}\n")
print(f"h1: {h1}")
print(f"h2: {h2}")
print(f"bias saida: {bias_y}")
print(f"peso1: {peso1}")
print(f"peso2: {peso2}")