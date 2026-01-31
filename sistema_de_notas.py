print ('siatema  de notas')
print ('...' *10)

nome_aluno  = input('nome do aluno:')
n1_port = float(input('nota de português: '))
n2_mat = float(input('nota de matemática: '))
n3_ing = float(input('nota de inglês: '))


media = (n1_port + n2_mat + n3_ing)/3

print ( 'situação do aluno:')
aprovado = media >=7
reprovado = media <5
recuperação = media >=5 and media <7
print(nome_aluno, 'aprovado? - ', aprovado)
print(nome_aluno, 'reprovado? - ', reprovado)
print(nome_aluno, 'recuperação? - ', recuperação)
