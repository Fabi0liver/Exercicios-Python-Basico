#                Estrutura de Repetição/laços de repetição while

# A estrutura de repetição é um recurso das linguagens de programação responsável por executar
#um bloco de código repetidas vezes enquanto determinada condição é atendida.
# No Python, possuímos dois tipos de estruturas de repetição: for e while.

# while

# O comando while faz com que um conjunto de instruções seja executado enquanto uma condição é atendida.
# Quando o resultado dessa condição passa a ser falso, a execução do loop é interrompida.

# Como mostra o exemplo a seguir:

contador = 0
while (contador < 100):
       print(contador)
       contador   = contador + 10

print('')
# Neste código, enquanto a variável contador, inicializada com 0, for menor do que 5,
#as instruções das linhas 3 e 4 serão executadas.

# Observe que o valor da variável contador, de forma que em algum momento seu valor igualará o
#número 100. Quando isso for verificado na linha 2, o laço será interrompido. Sem esse código,
#a condição de parada não será atingida, gerando o que é chamado de loop infinito.
# Evite que isso aconteça, pois leva ao congelamento e finalização da aplicação.

