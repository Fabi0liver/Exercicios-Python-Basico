# Estrutura de repeticão/laço de repetição

# O laço for em Python é uma estrutura de repetição poderosa e flexível.

#  Um laço em Python é uma estrutura de controle que permite executar um bloco de código várias vezes.
#  É uma forma eficiente de automatizar tarefas repetitivas, economizando tempo e esforço.
#  Em Python, existem diferentes tipos de laços que podem ser utilizados, dependendo das
# necessidades do programador.

# laço de repetição for

#  O laço for é utilizado quando se conhece o número exato de repetições que serão realizadas.
#  Ele percorre um conjunto de elementos, como uma lista ou uma sequência de números,
# e executa o bloco de código para cada elemento.

# por exemplo:

for i in range(5):
    print(i)

print('-' * 40)
#  Nesse exemplo, o laço for utiliza a função range() para gerar uma sequência de números de 1 a 9, com um passo de 2.
#  A cada iteração, a variável "i" assume um valor da sequência e é impressa na tela.

#  Nesse exemplo, o laço for percorre os números de 0 a 4 (pois o ultiomo número pedido neste exemplo o "5"
# é excluido da contagem) e imprime cada um deles.

# Utilizando a função range():

#  A função range() é uma ferramenta poderosa ao trabalhar com o laço for em Python.
#  Ela permite gerar uma sequência de números facilmente, especificando o início, o fim e o passo
# desejados.

# Veja o exemplo a seguir:

for i in range(1, 10, 2):
    print(i)

print('-" * 40')
#  Nesse exemplo, o laço for utiliza a função range() para gerar uma sequência de números de 1 a 9,
# com um passo de 2. A cada iteração, a variável "i" assume um valor da sequência e é impressa na tela.

# Percorrendo uma string:

#  Em Python, uma string é uma sequência de caracteres. Com o laço for,
# é possível percorrer cada caractere de uma string.

# Veja o exemplo a seguir:

texto = "Olá, mundo!"
for caractere in texto:
    print(caractere)

print('-' * 40)
#  Nesse exemplo, o laço for percorre a string "texto" e a variável "caractere" assume o valor de cada
# caractere da string em cada iteração. O bloco de código dentro do laço, nesse caso,
# imprime cada caractere na tela.

# Percorrendo uma listas,bibliotecas e tuplas:

#  O laço for é amplamente utilizado em Python devido à sua simplicidade e versatilidade.
#  Ele permite percorrer sequências, como listas,bibliotecas e tuplas, além de outros tipos de dados iteráveis.
#  Para utilizar o laço for, é necessário definir uma variável que irá armazenar cada elemento durante as repetições.

# A estrutura básica do laço for em Python é a seguinte:

# for elemento in sequencia:
#       bloco de código a ser executado

# Por exemplo, vamos percorrer uma lista de frutas e exibir cada uma delas:

frutas = ['maçã', 'banana', 'laranja']
for fruta in frutas:
    print(fruta)

print('-' * 40)
# Nesse exemplo, a variável "fruta" assume o valor de cada elemento da lista "frutas" em cada iteração do laço for.
# O bloco de código dentro do laço é executado uma vez para cada elemento.

