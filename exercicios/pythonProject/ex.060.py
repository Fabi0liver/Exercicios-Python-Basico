#Faça um programa que leia um número qualquer e mostre o seu fatorial.

from math import factorial
print('')
n = int(input('Digite um número para calcular seu factorial: '))
fatorial = factorial(n)
print(f'O fatorial de {n} é {fatorial}.')
print('')

print('')
print('-' * 50)
f = int(input('Digite um número para saber seu FATORIAL: '))
print('-' * 50)
print('')
fa = f
r = 1
print(f'Calculando {f}! = ', end='')
while fa > 0:
    r = fa * r
    print(f'{fa}', end='')
    print(' x ' if fa > 1 else ' = ', end='')
    fa = fa - 1
print(f'{r}')
print(f'O FATORIAL DE {f} É: {r}')
print('')
print('-' * 40)

fat = f
for c in range(1, f):
    fat = fat * c
print('')
print(f'O FATORIAL de {f}! é: {fat}')
print('')
