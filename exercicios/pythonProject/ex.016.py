#crie um programa que leia um número real pelo teclado e mostre na tela na tela a sua porção inteira

from math import trunc,ceil,floor

num = float(input('Digite um número:'))
print('O numero {} tem a parte inteira de "{}".'.format(num, trunc(num)))
print('E "{}" "sendo sua parte inteira arredondada para cima.'.format(ceil(num)))
print('E "{}" sendo sua parte inteira arredondada para baixo.'.format(floor(num)))


'''num = float(input('Digite um uma valor: '))
print('O valor digitado foi {}, e a porção inteira é {}.'.format(num, int(num)))'''



