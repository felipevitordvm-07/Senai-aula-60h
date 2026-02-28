def exercicio1():
    try:
        numero = int(input("Digite um número inteiro: "))
        print(f"Você digitou o número {numero}")
    except ValueError:
        print("Erro: você não digitou um número inteiro válido.")
    finally:
        print("Programa finalizado.")

exercicio1()