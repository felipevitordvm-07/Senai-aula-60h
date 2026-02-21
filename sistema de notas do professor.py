# Sistema de Notas de Alunos

senha_correta = "09876"
tentativas = 0
acesso = False

while tentativas < 3:
    senha = input("Digite a senha do professor: ")


    if senha == senha_correta:
        print("Acesso permitido ", 'seja bem vindo melhor professor do mundo')
        acesso = True
        break
    else:
        tentativas += 1
        print(f"Senha incorreta  | Tentativas restantes: {3 - tentativas}")

if not acesso:
    print("Conta bloqueada  (Senha incorreta 3x)")

    print('para de chutar a senha dos outros')
else:
    # Inserindo notas
    print("\n=== Inserir Notas ===")
    
    nota_matemática = float(input("Digite a nota de matemática: "))
    nota_português= float(input("Digite a nota de português: "))
    nota_inglês = float(input("Digite a nota de inglês: "))
    nota_educação_financeira = float(input("Digite a nota de educação financeira:"))

    media = (nota_matemática + nota_português + nota_inglês + nota_educação_financeira) / 4

    print(f"\nMédia do aluno: {media:.2f}")

    if media >= 7:
        print("Aluno APROVADO  ,  parabéns")
        print("voce é um orgulho da sua mae")
    elif media >= 5:
        print("Aluno em RECUPERAÇÃO , tente estudar mais um pouco ")
        print(" eu falei pra voce estudar mais um pouco")
    else:
        print("Aluno REPROVADO , voce nao foi bom o suficiente para passar de ano passar de ano ")
        print("infelizmente eu nao vou poder te ajudar")
           