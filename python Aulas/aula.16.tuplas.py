#                          "Variáriveis compostas = Tuplas"


# As variáveis em Python são elementos fundamentais na programação.
# Elas são utilizadas para armazenar e representar valores, como números, textos, listas, entre outros.
# Uma variável é como uma caixa onde podemos guardar informações e dar um nome para acessá-las posteriormente.


#   "TUPLAS"

# Tuplas são uma sequência de objetos imutáveis, em outras palavras, uma vez criadas,
#tuplas não podem ser modificadas, normalmente são usadas para guardar dados protegidos.

#As tuplas são escritas entre parênteses ().

# Uma tupla em Python é semelhante a uma lista. A diferença entre os dois é que não podemos alterar
#os elementos de uma tupla depois de atribuída, enquanto podemos alterar os elementos de uma lista.



#    "Criando uma Tupla"


# Podemos definir uma tupla da seguinte maneira:

linguagens = ("Python", "Ruby", " Javascript", "Perl", "Haskell")
print(linguagens) # ('Python', 'Ruby', 'Javascript', 'Perl', 'Haskell')
print('')

# Com o método type() podemos confirmar que se trata de uma 'tuple':

print(type(linguagens))# <class 'tuple'>
print('')

# Com o método len() podemos saber quantos elementos tem dentro da dupla:

print(len(linguagens)) # 5
print('\n')

# O método count() nos retorna a quantidade de vezes que determinado valor ocorre em uma tupla:

print(linguagens.count('Ruby')) # 3
print()

#O método index() nos permite buscar por um determinado elemento e nos retorna o índice dele:

print(linguagens.index('Perl')) # 1
print()

# Somos capazes também de construir uma tupla com o uso do construtor tuple():

numeros = tuple(x for x in range(1,20,3))
print(numeros) # (1, 4, 7, 10, 13, 16, 19)
print('')


#   "Acessando Itens de uma Tupla"

# Os elementos da tupla são acessados através da posição do elemento na tupla(começando do O,1,2..).
# E a forma de acessar e atraves do nome da tupla e a posição do elemnto dentro de "[]".

# exemplos de como acessar os elementos da tupla 'linguagens':

print(linguagens[0]) # Python
print(linguagens[0:2]) # ('Python', 'Ruby')
print(linguagens[-1]) # Haskell
print(linguagens[:-2]) # ('Python', 'Ruby', 'Javascript')
print(linguagens[:]) # ('Python', 'Ruby', 'Javascript', 'Perl', 'Haskell')
print('')


#  "Imprimindo Elementos de uma Tupla"

# As tuplas são úteis para representar o que outras linguagens costumam chamar de registros,
#algumas informações relacionadas que pertencem entre si, como o registro de um estudante.
# Não há descrição do que significa cada um desses campos, mas podemos intuir.
# Uma tupla nos permite “agrupar” informações relacionadas e usá-las em uma única estrutura.

estudante = ('Miguel', 29, 1990, 'Brasil')

print(estudante) # ('Miguel',29, 1990,'Brasil')
print()

#Agora podemos utilizar um for loop para imprimir todos os elementos da tupla "estudante":


for e in estudante:  # Percorre os valores da tupla estudante
    print(e, end=' ') # Miguel 29 1991 Brasil
print('.')
print('')


# Também podemos facilmente converter esta tupla em uma lista usando a técnica list comprehension:

print([e for e in estudante]) # ['Miguel', 29, 1990, 'Brasil']
print('')

#  "Atualizando Tuplas"

# Lembrando que as tuplas são imutáveis, portanto se tentarmos modificá-la,
#nos será retornado um erro do tipo TypeError:

#linguagens[0] = "C++"
# TypeError: 'tuple' object does not support item assignment

# Como já mencionado, Tuplas são imutáveis, ou seja, não podemos alterar os seus elementos,
#porém podemos capturar porções de uma tupla e criar novas tuplas, por exemplo:

x = (1, 2)
y = (3, 4)
z = x + y
print(z) # (1, 2, 3, 4)
print('')

#    "Deletando a Tupla"

# Embora seja impossível remover itens da tupla, é possível deletá-la por completo com
#o uso da palavra-chave del. Observe que se tentarmos imprimir ela, ocorrerá um erro do tipo
#NameError, uma vez que a tupla não existe mais.

del linguagens
print(linguagens)
#NameError: name 'linguagens' is not defined