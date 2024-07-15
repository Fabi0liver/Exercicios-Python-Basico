#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre:
#A média de idade do grupo.
#Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

print('')
print('Me diga as informações de 4 pessoas, eu ti passo algumas dados!')
print('')
somaidade = 0
media_idade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
for p in range(1,5):
    print('-' * 18, f'{p}ª', '-' * 18)
    nome = str(input('Qual o nome: ')).strip().capitalize()
    idade = int(input('Qual a idade: '))
    sexo = str(input('Qual o sexo [M/F]: ')).strip().upper()
    print('-' * 40)
    somaidade = somaidade + idade
    if p == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
        if sexo in 'F' and idade < 20:
            totmulher += 1

media_idade = somaidade / 4

print('')
print(f'A média da idade desse grupo de pessoas é {media_idade} anos.')
print(f'O {nomevelho} é o homem mais velho com {maioridadehomem} anos.')
print(f'Neste grupo de pessoas á {totmulher} com menos de 20 anos.')





