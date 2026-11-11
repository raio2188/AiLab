
import random
import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt

# Dados de treinamento
entradas = [1, 2, 3]
esperados = [4, 6, 8]

# Inicialização dos parâmetros
peso = random.uniform(-1, 1)
bias = random.uniform(-1, 1)

taxa = 0.01
historico = []

print(f"Peso inicial: {peso}")
print(f"Bias inicial: {bias}")

# Treinamento
for epoca in range(10000):
    erro_total = 0

    for i in range(len(entradas)):
        # Processamento
        saida = entradas[i] * peso + bias

        # Cálculo do erro
        erro = saida - esperados[i]

        # Acumular erro absoluto
        erro_total += abs(erro)

        # Atualização dos parâmetros
        peso = peso - (erro * entradas[i] * taxa)
        bias = bias - (erro * taxa)

    # Erro médio da época
    erro_medio = erro_total / len(entradas)
    historico.append(erro_medio)

# Resultado do treinamento
print(f"\nPeso final: {peso}")
print(f"Bias final: {bias}")

# Teste com valor não utilizado no treinamento
teste = 19813482

previsao = teste * peso + bias
esperado_teste = 2 * teste + 2
erro_teste = abs(previsao - esperado_teste)

print(f"\nEntrada de teste: {teste}")
print(f"Previsão: {previsao}")
print(f"Resultado esperado: {esperado_teste}")
print(f"Erro absoluto: {erro_teste}")

# Visualização do aprendizado
plt.plot(historico[:100])
plt.title("Aprendizado do Frankenstein")
plt.xlabel("Épocas")
plt.ylabel("Erro médio absoluto")
plt.grid(True)
plt.show()
