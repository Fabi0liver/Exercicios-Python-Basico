#modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro
#a mais,informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
#desenvolvida no 108.

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
print(f' A metade do valor {moeda(p)} é {metade(p, True)}')
print('')
print(f' O dobro do valor {moeda(p)} é {dobro(p, True)}')
print('')
print(f' Aumentando {a}% do valor {moeda(p)} fica {aumentar(p, a, True)}')
print('')
print(f' Reduzindo {d}% do valor {moeda(p)} fica {diminuir(p, d, True)}')
print('')