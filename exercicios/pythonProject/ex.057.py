#Faça um programa que leia o sexo de uma pessoa , mas só aceite os valores "M" ou "F".
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

nome = str(input('Digite o nome: ')).strip().capitalize()
idade = int(input('Digite a idade: '))
sexo = str(input('Digite o sexo M/F:')).upper().strip()[0]
print('')
while sexo not in 'MF':
    print(f'O Sexo {sexo}, é inválido para esse cadastro!')
    sexo = str(input('\tDigite o sexo novamente M/F: ')).upper().strip()[0]

if sexo == 'M':
    sexo = 'Masculino'
elif sexo == 'F':
    sexo = 'Feminino'

print('')
print('*' * 20)
print('CADASTRO CONFIRMADO!')
print('*' * 20)
print('')
print('Informações:')
print(f'''[NOME] {nome}
[IDADE] {idade} anos
[SEXO] {sexo}''')
