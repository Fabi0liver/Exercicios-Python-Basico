#Dentro do pacote utilidadeCev que criamos no desafio 111, temos um módulo chamado dado.
#Crie uma função chmada leiaDinheiro() Que seja capaz de funcionar como a função input(),
#mas com uma validação de dados para aceitar apenas valores que sejam monetários.

from utilidadeCeV import dado
from utilidadeCeV.moeda import resumo


p = dado.leiaDinheiro('Digite o preço: R$ ')
resumo(p, 10, 13)
