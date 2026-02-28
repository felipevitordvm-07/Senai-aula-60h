def exercicio2():
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = n1 / n2
        print(f"Resultado da divisão: {resultado}")
    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero.")
    except ValueError:
        print("Erro: você digitou um valor inválido.")
    else:
        print("Divisão realizada com sucesso!")
    finally:
        print("Programa encerrado.")

exercicio2()