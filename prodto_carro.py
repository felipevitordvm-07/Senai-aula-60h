# Exercício 0
# Gerar e imprimir números pares de 2 a 20
for num in range(2, 21, 2):
    print(num)

print()  # linha em branco para organizar a saída

# Exercício 1
# Criar lista com números de 1 a 10
numeros = list(range(1, 11))
print(numeros)

# Exercício 2
# Imprimir o terceiro elemento da lista
print(numeros[2])

# Exercício 3
# Adicionar o número 9 à lista
numeros.append(9)
print(numeros)

# Exercício 4
# Remover o número 5 da lista
numeros.remove(5)
print(numeros)

# Exercício 5
# Criar lista de carros e concatenar com a lista numeros
carros = ["ferrari", "Uno", "prisma"]
lista_concatenada = numeros + carros
print(lista_concatenada)
