#crie um pacote chamado utilidadecev que tenha dois módulos interno chamado moeda e dado.
#Tranfira todas as funções utilizadas nos desafios 107, 108e 109 pra o primeiro pacote e mantenha
#tudo funcionando.

from utilidadesCeV import moedas

p = float(input('Digite o preço: R$ '))
moedas.resumo(p, 35, 22)
