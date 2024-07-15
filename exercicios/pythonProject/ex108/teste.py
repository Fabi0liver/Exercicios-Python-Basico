# adapte o código do desafio 107. criando uma função adicional chamada moedas()
#que consiga msotrar os valores como um valor monetário formatado.

from moeda import *

print('$' * 40)
print('CALCULOS SOBRE PREÇO'.center(40))
print('$' * 40)
print('-' * 40)
p = float(input('  Digite o preço: R$'))
a = int(input('  Quantos % de aumento no preço: '))
d = int(input('  Quantos % de redução no preço: '))
print('-' * 40)
print('\033[7m')
print(f' A metade do valor {moeda(p)} é {moeda(metade(p))}')
print('')
print(f' O dobro do valor {moeda(p)} é {moeda(dobro(p))}')
print('')
print(f' Aumentando {a}% do valor {moeda(p)} fica {moeda(aumentar(p, a))}')
print('')
print(f' Reduzindo {d}% do valor {moeda(p)} fica {moeda(diminuir(p, d))}')
print('')