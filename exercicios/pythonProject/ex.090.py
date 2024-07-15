#Faça Um programa que leia nome e média deum aluno, guardando também a situação em um diconário.
# no final, mostre o conteúdo da estrutura na tela.

print('')
aluno = dict()
aluno['Nome'] = str(input('Nome do aluno: '))
aluno['Média'] = float(input(f'Digite a média do {aluno['Nome']}: '))

if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
elif aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'

print('')
for k, v in aluno.items():
    print(f' -{k} é igual a {v}')
