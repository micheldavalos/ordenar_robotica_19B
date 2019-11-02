import random

numeros = []

for i in range(0, 100):
    valor = random.randint(0, 1000)
    numeros.append(valor)

print(numeros)

numeros.sort(reverse=True)

print(numeros)