from ativacao import ReLU

x1 = 2
x2 = 3
esperado = 5
peso1 = 0.7
peso2 = 0.4
bias_h1 = 1
bias_h2 = -1
w1_h1 = 0.5
w2_h1 = 0.8
w1_h2 = -0.3
w2_h2 = 0.6
taxa = 0.01
bias_y = 0.5



for epoca in range (1000):
    h1 = ReLU(w1_h1 * x1 + w2_h1 * x2 + bias_h1)
    print(f"h1: {h1}")
    h2 = ReLU(w1_h2 * x1 + w2_h2 * x2 + bias_h2)
    print(f"h2: {h2}")

    y = ( peso1 * h1 + peso2 * h2 + bias_y)
    print(f"Saída: {y}")

    erro = y - esperado
    print(f"Erro: {erro}")

    erroh1 = erro * peso1
    print(f"Erro h1: {erroh1}")

    erroh2 = erro * peso2
    print(f"Erro h2: {erroh2}")

    w1_h1 = w1_h1 - (erroh1 * x1 * taxa)
    print(f"w1_h1: {w1_h1}")

    w2_h1 = w2_h1 - (erroh1 * x2 * taxa)
    print(f"w2_h1: {w2_h1}")

    w1_h2 = w1_h2 - (erroh2 * x1 * taxa)
    print(f"w1_h2: {w1_h2}")

    w2_h2 = w2_h2 - (erroh2 * x2 * taxa)
    print(f"w2_h2: {w2_h2}")

    bias_h1 = bias_h1 - (erroh1 * taxa)   
    print(f"bias h1: {bias_h1}")

    bias_h2 = bias_h2 - (erroh2 * taxa)   
    print(f"bias h2: {bias_h2}")

    peso1 = peso1 - (erro * h1 * taxa)
    print(peso1)

    peso2 = peso2 - (erro * h2 * taxa)
    print(peso2)

    bias_y = bias_y - (erro * taxa)
    print(bias_y)

print(f"Saída final: {y}")
print(f"Erro final: {erro}")

