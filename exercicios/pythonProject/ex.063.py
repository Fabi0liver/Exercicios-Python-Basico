# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os seus
#n primeiros elementos de uma sequência de fibonacci.

print('')
print('-' * 55)
print('\tVamos trabalhar com a Sequência de Fibonacci?')
print('-' * 55)
print('')
print('Você vai me falar um número N da Sequência de Fibonacci.')
print('\tE vou mostrar seus N primeiros elementos.')
print('')
n = int(input('Digite o número N inteiro: '))
print('')
print(f'Os primeiros elementos do {n}º número da Sequência de Finonacci são:')
print('')
f = 0
f1 = 1
f2 = 1
c = 1
print(f, end=', ')
while c < n:
    f2 = (f + f1)
    f = f1
    f1 = f2
    print(f, end=', ')
    c += 1
print('...')
print('')
print('É importante destacar que a sequência de Fibonacci é infinita!')







