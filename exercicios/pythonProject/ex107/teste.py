# Crie um módulo chamado moedas.py que tenha as funções incorporadas aumentar(), diminuir(),
# dobro(), e metade().
#Faça também um programa que importe esse módulo e use algumas dessas funções.

from moeda import *

print('$' * 40)
print('CALCULOS SOBRE PREÇO'.center(40))
print('$' * 40)
print('-' * 40)
p = float(input('  Digite o preço: R$'))
a = str(input('  Quantos % de aumento no preço: '))
d = str(input('  Quantos % de redução no preço: '))
print('-' * 40)
print('\033[7m')
print(f' A metade do valor R${p:.2f} é R${metade(p):.2f}')
print('')
print(f' O dobro do valor R${p:.2f} é R${dobro(p):.2f}')
print('')
print(f' Aumentando {a}% do valor R${p:.2f} fica R${aumentar(p, a):.2f}')
print('')
print(f' Reduzindo {d}% do valor R${p:.2f} fica R${diminuir(p, d):.2f}')
print('')
