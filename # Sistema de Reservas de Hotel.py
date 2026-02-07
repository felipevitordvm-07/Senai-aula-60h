# Sistema de Reservas de Hotel

# Preços dos quartos
preco_simples = 100
preco_duplo = 150
preco_luxo = 250

# Listas para armazenar os dados
clientes = []
valores_totais = []

print("=== Sistema de Reservas do Hotel ===\n")

for i in range(1, 4):
    print(f"Cadastro do cliente {i}")

    nome = input("Nome do cliente: ")
    idade = int(input("Idade do cliente: "))

    print("\nTipos de quarto:")
    print("1 - Simples (R$ 100,00 por dia)")
    print("2 - Duplo (R$ 150,00 por dia)")
    print("3 - Luxo (R$ 250,00 por dia)")

    opcao = int(input("Escolha o tipo de quarto (1, 2 ou 3): "))
    dias = int(input("Quantos dias ficará no hotel? "))

    if opcao == 1:
        tipo_quarto = "Simples"
        valor_total = preco_simples * dias
    elif opcao == 2:
        tipo_quarto = "Duplo"
        valor_total = preco_duplo * dias
    elif opcao == 3:
        tipo_quarto = "Luxo"
        valor_total = preco_luxo * dias
    else:
        print("Opção inválida! Quarto Simples será aplicado.")
        tipo_quarto = "Simples"
        valor_total = preco_simples * dias

    clientes.append({
        "nome": nome,
        "idade": idade,
        "quarto": tipo_quarto,
        "dias": dias
    })

    valores_totais.append(valor_total)

    print(f"\nReserva feita para {nome}!")
    print(f"Valor total da estadia: R$ {valor_total:.2f}\n")
    print("-" * 40)

print("\n=== Resumo das Reservas ===")

for i in range(len(clientes)):
    print(f"\nCliente {i + 1}")
    print(f"Nome: {clientes[i]['nome']}")
    print(f"Idade: {clientes[i]['idade']} anos")
    print(f"Quarto: {clientes[i]['quarto']}")
    print(f"Dias: {clientes[i]['dias']}")
    print(f"Total a pagar: R$ {valores_totais[i]:.2f}")

print("\nObrigado por usar o sistema do hotel 🏨")
