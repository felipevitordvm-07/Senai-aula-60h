#1: Verificando se o número é par ou ímpar

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é PAR")
else:
    print("O número é ÍMPAR")
    numero = float(input("Digite um número: "))


#2: Verificando se um número é positivo, negativo ou zero


if numero > 0:
    print("Número POSITIVO")
elif numero < 0:
    print("Número NEGATIVO")
else:
    print("O número é ZERO")

#Verificando se uma string é vazia ou não


texto = input("Digite algo: ")

if texto == "":
    print("A string está vazia")
else:
    print("A string NÃO está vazia")



#Verificando se um número é maior, menor ou igual a 10





    numero = int(input("Digite um número: "))

if numero > 10:
    print("Maior que 10")
elif numero < 10:
    print("Menor que 10")
else:
    print("Igual a 10")









#5Classificando idade em faixas etárias







idade = int(input("Digite a idade: "))

if  idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 35:
    print("Jovem")
elif idade <= 64:
    print("Adulto")
else:
    print("Idoso")


    