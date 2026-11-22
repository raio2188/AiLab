x = 10
w = 3
esperado = 3
taxa = 0.1

y = w * x

print(y)

erro = y - esperado

w = w - (erro * x * taxa)

y = w * x

print(y)
print(w)