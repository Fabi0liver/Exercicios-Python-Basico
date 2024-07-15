#                      Interrompendo repetições while

# Em Python, o laço while é uma estrutura de repetição que executa um bloco de código enquanto
#uma condição de teste for verdadeira. A sintaxe básica do while é:

#   while condição:
#       bloco de código

# A condição é verificada antes da execução do bloco de código. Se a condição for verdadeira,
#o bloco de código é executado. Após a execução do bloco de código, a condição é verificada novamente.
# Se a condição ainda for verdadeira, o bloco de código é executado novamente.

# Esse processo se repete até que a condição seja avaliada como falsa, e neste momento o laço é encerrado (sai do while)

# Por exemplo, o código a seguir imprime os números de 1 a 5 utilizando o laço while:

i = 1
while i <= 5:
    print(i)
    i += 1

# Neste exemplo, a variável i é inicializada com o valor 1. O laço while é executado enquanto i for menor ou igual a 5.
# A cada iteração do laço, o valor de i é incrementado em 1 e o número é impresso na tela.

#A lém disso, é possível utilizar a instrução break dentro de um laço while para interromper
#a execução do laço antes que a condição seja avaliada como falsa.

#Por exemplo, o código a seguir executa o laço while até que o usuário digite a palavra “sair”:

while True:
    resposta = input("Digite 'sair' para encerrar o programa: ")
    if resposta == 'sair':
        break
    else:
        print("Resposta inválida.")

# Neste exemplo, o laço while é executado indefinidamente, já que a condição é sempre verdadeira (True).
# Dentro do laço, o programa solicita que o usuário digite a palavra “sair”. Se o usuário digitar “sair”,
#o laço é interrompido utilizando a instrução break. Caso contrário, o programa exibe uma mensagem de erro.

# Em resumo, o laço while é uma estrutura de repetição que executa um bloco de código enquanto uma condição
#for verdadeira. A instrução break pode ser utilizada para interromper a execução do laço antes que a
#condição seja avaliada como falsa.

# É importante ter cuidado ao utilizar a instrução break, já que ela pode resultar em um código
#mais difícil de entender e depurar.