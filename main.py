# 1 - Crie um número aleatório de 5 a 10
import random


def numero_aleatorio_5_10():
    num = random.randint(5, 10)
    return num


# 2 - Crie 3 números aleatórios
def tres_numeros_aleatorios():
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    n3 = random.randint(1, 100)
    return n1, n2, n3


# 3 - Crie um número aleatório entre 10 e 30 usando range
def numero_aleatorio_10_30():
    lista = list(range(10, 31))
    num = random.choice(lista)
    return num


# 4 - Contagem regressiva simples
def contagem_regressiva():
    for i in range(10, 0, -1):
        print(i)
    print("Fogo!")


# 5 - Soma de números pares
def soma_pares(numero):
    soma = 0
    for i in range(2, numero + 1):
        if i % 2 == 0:
            soma += i
    return soma


# 6 - Tabuada de multiplicação
def tabuada(numero):
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)


# 7 - Números ímpares reversos
def impares_reversos():
    for i in range(99, 0, -2):
        print(i)


# Programa principal
print("Número aleatório entre 5 e 10:", numero_aleatorio_5_10())

print("Três números aleatórios:", tres_numeros_aleatorios())

print("Número aleatório entre 10 e 30:", numero_aleatorio_10_30())

print("\nContagem regressiva:")
contagem_regressiva()

num = int(input("\nDigite um número inteiro positivo: "))
print("Soma dos números pares:", soma_pares(num))

num2 = int(input("\nDigite um número para ver a tabuada: "))
tabuada(num2)

print("\nNúmeros ímpares reversos:")
impares_reversos()
