#Faça um progra,a que leia  valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posiçãoes na lista.

valores = list()

print('=' * 45)
for valor in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {valor}ª da lista: ')))
print('=' * 45)
print('')
print(f'Você digitou os valores: {valores}')

maior = max(valores)
menor = min(valores)

print(f'O maior valor é o {max(valores)}, que está nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end=' ')
print('')
print(f'O menor valor é o {min(valores)}, que está nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end=' ')
print('')





