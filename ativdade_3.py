def exercicio3():
    lista = ["Python", "Java", "C++", "JavaScript"]

    try:
        indice = int(input("Digite o índice que deseja acessar (0 a 3): "))
        print(f"Elemento escolhido: {lista[indice]}")
    except IndexError:
        print("Erro: índice fora do tamanho da lista.")
    except ValueError:
        print("Erro: digite apenas números inteiros.")
    finally:
        print("Programa finalizado.")

exercicio3()