# Desenvolva um programa que leia o primeiro termo e a razão de uma pa.
#no final, mostre os 10 primeiros termos dessa progressão.
print('')
print('#=#' * 15)
print('\tVAMOS FAZER PROGRESSÃO ARITMÉTICA?!')
print('#=#' * 15)
print('')
print('Você vai me dizer o primeiro termo e a razão dessa P.A. \n\tE eu vou mostrar os 10 primeiro termo dela.')
print('')
p = int(input('Então me diga o primeiro termo dessa P.A: '))
r = int(input('Agora me diga a razão dessa P.A: '))
n = p + (10 - 1) * r
print('')
print(f'\t\t\tNa Progressão Aritmética que: \no primeiro termo é "{p}", o n-ésimo termo é "{n}" e a razão é "{r}".')
print('\tOs 10 primeiros termos desta progressão são:')
print('-' * 50)
for i in range(p, n+1, r):
    print( i, end=' -> ')
print('Acabou')
print('-' * 50)
print('Mas as vezes matematica é bem interessante né?')

