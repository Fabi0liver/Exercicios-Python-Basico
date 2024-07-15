#Faça um programa que leia o peso de 5 pessoas . No final, mostre qual foi o maior e o menor peso lidos.

print('')
print('\t\tVamos fazer um jogo rápido aqui?!')
print('')
print('\tVocê vai me dizer o peso de 5 pessoas.')
print('E eu vou ti dizer, qual e o com o maior peso, e o com menor! Ok?!')
print('')

maior = 0
menor = 999999
for p in range(1, 6):
    peso = float(input(f'Qual é o peso da {p}ª pessoa: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
            menor = peso

print('')
print(f'O maior peso lido é {maior}Kg!')
print(f'O menor peso lido é {menor}KG!')















