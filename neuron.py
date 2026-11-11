
# Nosso primeiro neurônio artificial

entrada = 3
peso = 3
bias = 2
esperado = 5
taxa = 0.5
erro = 1
contador = 0



while abs(erro) > 0.001 and contador < 1000:
    # Processamento
    saida = entrada * peso + bias

    # Calculo do erro
    erro = saida - esperado

    # Ajuste do peso
    peso = peso - (erro * entrada * taxa)

    # Processamento
    saida = entrada * peso + bias
    
    # Calculo do erro
    erro = saida - esperado

    contador += 1

    print(f"Resultado: {saida}")
    print(f"Erro: {erro} \n")

print(contador)