#                                       Funções(1)

# Uma função é um bloco de código organizado e reutilizável que é capaz de realizar uma determinada
#aç ão. Funções nos ajudam a deixar o nosso código mais modular, trazendo a possibilidade de reusabilidade,
#conforme nosso programa fica cada vez maior, as funções o tornam mais organizado e gerenciável.

# Como vimos ao longo do guia, Python já nos traz várias funções pré-construídas,
#como por exemplo print() e range(), mas também é possível criarmos nossas próprias funções!

# Características das Funções

# * Possuem um nome
# * Possuem parâmetros (0 ou mais)
# * Possuem docstrings (opcional, porém recomendado)
# * Possuem um corpo
# * Retornam algo (opcional)


# Definindo uma Função

# Em Python devemos seguir a seguinte sintaxe para construirmos uma Função:

'''def nome_da_função(parametros):
    """docstrings"""
    <comandos>'''

# Para definir uma função é necessário que sigamos algumas regras:

# * Bloco de funções começam com a palavra-chave def seguido do nome da função e parenteses ().

# * O nome da função identifica exclusivamente a função.
#A nomenclatura de funções segue as mesmas regras de escrita de identificadores em Python.

# *Parâmetros de input ou argumentos (dados fornecidos por nós)
#devem ser colocados entre parenteses (). Eles são opcionais.

# * Dois pontos (:) para marcar o final do cabeçalho da função.

# * Opcionalmente podemos usar strings de documentação (docstrings)
#para descrever o que nossa função faz.

# *Uma ou mais instruções Python válidas que constituem o corpo da função.
#As declarações devem ter o mesmo nível de indentação (geralmente 4 espaços).

# *O comando opcional return (expressão) sai da função, opcionalmente passando um parâmetro para o chamador.
#O comando de retorno sem argumentos é o mesmo que return None.

#Por exemplo, vamos definir uma função capaz de converter uma temperatura em Fahrenheit para Celsius.


def fahr_to_celsius(temp):
    """
    Função que recebe como argumento uma temperatura
    em Fahrenheit e converte ela para Celsius
    """
    return ((temp - 32) * (5/9))


# Uma vez que temos a função definida, agora podemos usá-la. Se quisermos obter ajuda,
#podemos contar com o comando help() que nos trará o docstrings dessa função.

help(fahr_to_celsius) #fahr_to_celsius(temp)
                           #Função que recebe como argumento uma temperatura
                           #em Fahrenheit e converte ela para Celsius

# Para invocar a função, devemos passar um valor para ela como argumento:

print(fahr_to_celsius(91.76)) # 33.2
print(fahr_to_celsius(101.3)) # 38.5


# Como essa função tem valor de retorno, podemos armazenar o seu resultado em uma variável:

celsius = fahr_to_celsius(70.76)
print(f'{celsius:.2f}') # 21.53

# Também podemos definir uma função que não irá retornar um valor, por exemplo:

def cumprimentar(nome):
    """
    Essa função cumprimentará a pessoa passada por parâmetro
    """
    print("Olá {0} Seja bem-vindo".format(nome))

print('')
# A função foi criada e está definida, porém nada aconteceu.
#Para que ela possa funcionar precisamos invocá-la,
#para isso chamaremos ela por seu nome e passaremos os parâmetros requisitados por ela:

cumprimentar('Fabio') # Olá Fabio Seja bem-vindo

#Observe que esta função apenas nos imprime uma string, uma vez que ela não tem valor de retorno.







