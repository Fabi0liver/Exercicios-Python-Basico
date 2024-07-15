#faça um progama que leia um número inteiro qualquer, e mostre na tela sua tabuada.

n = int(input('Digite um número:'))
print('Veja a tabuada do número digitado:')
a = n * 1
b = n * 2
c = n * 3
d = n * 4
e = n * 5
f = n * 6
g = n * 7
h = n * 8
i = n * 9
j = n * 10
z = n * 0
print('='*12)
print('{} x 0 = {} \n{} x 1 = {} \n{} x 2 = {} \n{} x 3 = {} \n{} x 4 = {} \n{} x 5 = {}'.format(n, z, n, a, n, b, n, c, n, d, n, e))
print('{} x 6 = {} \n{} x 7 = {} \n{} x 8 = {} \n{} x 9 = {} \n{} x 10 = {}'.format(n, f, n, g, n, h, n, i, n, j))
print('='*12)


num = int(input('Digite outro número:'))
print('=' * 12)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('=' * 12)