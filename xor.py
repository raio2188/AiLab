import random
from ativacao import Identidade, Derivada_Identidade, leaky_relu, derivada_leaky_relu



entradas = [[0, 0], #should be 0
            [0, 1], #should be 1
            [1, 0], #should be 1
            [1, 1]  #should be 0
            ]
esperados = [0, 1, 1, 0]

peso1 = random.uniform(-1, 1)
peso2 = random.uniform(-1, 1)
bias_h1 = 1
bias_h2 = -0.5
w1_h1 = 0.5
w2_h1 = 1
w1_h2 = 1
w2_h2 = 0.6
taxa = 0.05
bias_y = 0.5

pares = list(zip(entradas, esperados))


def prever(x1, x2):
    z1 = leaky_relu(w1_h1 * x1 + w2_h1 * x2 + bias_h1)
    z2 = leaky_relu(w1_h2 * x1 + w2_h2 * x2 + bias_h2)

    return peso1 * z1 + peso2 * z2 + bias_y

for x1, x2 in entradas:
    z1 = w1_h1 * x1 + w2_h1 * x2 + bias_h1
    z2 = w1_h2 * x1 + w2_h2 * x2 + bias_h2
    print(x1, x2, round(z1, 2), round(z2, 2))

for epoca in range(10001):
    erro_total = 0
    random.shuffle(pares)

    for (x1, x2), esperado in pares:
        z1 = leaky_relu(w1_h1 * x1 + w2_h1 * x2 + bias_h1)
        z2 = leaky_relu(w1_h2 * x1 + w2_h2 * x2 + bias_h2)
    
        y = ( peso1 * z1 + peso2 * z2 + bias_y)

        erro = y - esperado
        erro_total += abs(erro)

        erroh1 = erro * peso1 * derivada_leaky_relu(z1)
        erroh2 = erro * peso2 * derivada_leaky_relu(z2)
  
        w1_h1 = w1_h1 - (erroh1 * x1 * taxa)
        w2_h1 = w2_h1 - (erroh1 * x2 * taxa)
  
        w1_h2 = w1_h2 - (erroh2 * x1 * taxa)
        w2_h2 = w2_h2 - (erroh2 * x2 * taxa)

        bias_h1 = bias_h1 - (erroh1 * taxa)   
        bias_h2 = bias_h2 - (erroh2 * taxa)   
    
        peso1 = peso1 - (erro * z1 * taxa)
        peso2 = peso2 - (erro * z2 * taxa)

        bias_y = bias_y - (erro * taxa)

        erro_medio = erro_total / len(entradas)
        
    if epoca % 1000 == 0:
        print(f"Época {epoca} | Erro médio: {erro_medio:.6f}")

for x1, x2 in entradas:
    z1 = w1_h1 * x1 + w2_h1 * x2 + bias_h1
    z2 = w1_h2 * x1 + w2_h2 * x2 + bias_h2
    print( "\n", x1, x2, round(z1, 2), round(z2, 2))

#print(f"Saída final: {y}")
#print(f"Erro final: {erro}\n")
#print(f"h1: {z1}")
#print(f"h2: {z2}")
#print(f"bias saida: {bias_y}")
#print(f"peso1: {peso1}")
#print(f"peso2: {peso2} \n")

for x1, x2 in entradas:
    print(f"entrada 1: {x1}\nentrada 2: {x2}\ny: {prever(x1, x2)}\n")

print(prever(0.5, 0.5))
print(prever(0, 0.5))
