#                                        LISTAS(1)

# Em Python, a função list[] é uma maneira conveniente de criar uma lista a partir de um iterável,
#como uma string, uma tupla ou até mesmo outra lista.
# Essa função retorna uma nova lista contendo os elementos do iterável.

#  Fundamentos Básicos de Listas

#Para melhor entendermos o conceito de Listas, vamos definir a nossa primeira lista que
#será chamada de L e irá conter as letras das palavras "Monty Python":

L = ['M','o','n','t','y',' ','P','y','t','h','o','n']

# Veja que podemos imprimir o conteúdo da lista com o comando print():

print(L) # ['M', 'o', 'n', 't', 'y', ' ', 'P', 'y', 't', 'h', 'o', 'n']
print('')

# Com o comando len() podemos verificar o tamanho (número de itens) da lista:

print(len(L)) # 12
print('')

#Podemos acessar apenas determinados itens da lista utilizando o conceito de fatiamento:

print(L[6:10]) # ['P', 'y', 't', 'h']
print(L[-12:-7]) # ['M', 'o', 'n', 't', 'y']
print('')

#Observe esta lista que definimos é uma lista de caracteres, se quisermos uní-los para formar as palavras,
#podemos usar o método join() da seguinte forma:

nome = ''.join(L)
print(nome) # Monty Python
print('')

#                Alterando Elementos de uma Lista

#A lista é um tipo de dados mutável. Assim que uma lista for criada:

# Elementos podem ser modificados
# Valores individuais podem ser substituídos
# A ordem dos elementos pode ser alterada.

#Para compreendermos melhor as mutações de listas, vamos executar alterações em nossas listas.

#Iniciaremos alterando os elementos da lista ciencias:

ciencias = ['física', 'química', 'matemática']

#    Adicionando Itens a uma Lista

# Iniciaremos alterando o primeiro elemento da lista ciencias:

print(ciencias) #['física', 'química', 'matemática']
print(ciencias[0]) #física

ciencias[0] = "computação" # o primeiro elemento da lista.

print(ciencias) # ['computação', 'química', 'matemática']
print(ciencias[0]) # computação
print('')

# Vamos agora incrementar mais ciências a nossa lista ciencias:

ciencias += ['astronomia','biologia']
print(ciencias)#['computação', 'química', 'matemática', 'astronomia', 'biologia']
print('')
''' os elementos que estavam numa lista se juntaram a lista que ja existia. '''

# Uma outra maneira de adicionarmos mais itens a uma lista
#é com o uso do método append(), por exemplo:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros.append(11)
print(numeros) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print('')
'''Um elemento do appende será adicionada no final da lista.'''

# Se você precisarmos anexar vários itens à mesma lista, o método extend() será útil.
# Precisamos simplesmente passar a lista de itens para anexar ao método extend,
#conforme o exemplo abaixo:

numeros.extend([12, 13])
print(numeros) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print('')

# Podemos também usar o método insert() para inserirmos itens em uma posição específica:

numeros.insert(5, 5.5)
print(numeros) # [1, 2, 3, 4, 5, 5.5, 6, 7, 8, 9, 10, 11, 12, 13]
print('')

# Passamos como argumento o número 5 e o número float "5,5",
#indicando que desejamos inserir essa string na quinta posição da lista.

#       Removendo Itens de uma Lista

#   Uma tarefa muito comum é a de remoção de itens de uma lista, podemos por exemplo:

# * Deletar um elemento em um índice específico com #del(lista[indice])#
# * Remover elementos no fim da lista com "lista.pop()", retornará o elemento removido
# * Remover um elemento específico com "lista.remove(elemento)"
#Busca pelo elemento e remove ele - Se o elemento ocorre múltiplas vezes na lista,
#remove a primeira ocorrência - Se o elemento não estiver presente na lista, ocorrerá um erro

# Definiremos então uma nova lista para trabalharmos com essas operações de remoção:

lista = [2, 1, 3, 6, 3, 7, 0]
print(lista) #[2, 1, 3, 6, 3, 7, 0]

lista.remove(2)
print(lista)# [1, 3, 6, 3, 7, 0]

lista.remove(3)
print(lista)# [1, 6, 3, 7, 0]

del(lista[1])
print(lista)# [1, 3, 7, 0]

lista.pop() # retorna 0
print(lista)# [1, 3, 7]
print('')

#Fique atento, pois caso não seja especificado um índice, "del" vai eliminar sua lista por completo!

#O método pop() remove o último elemento da lista e nos retorna ele

#lista.pop()
#print(lista) #[1, 3]

# Se tentarmos remover um elemento que já foi removida de lista. Aparecera um erro:

lista.remove(7)# ValueError: list.remove(x): x not in list

# A alternativa para remover um elemento, que não sabe se está na lista e usando o 'if':

if 7 in lista:
    lista.remove(7)

# se o elemento estiver na lista será removido.

#Finalmente, o método "clear()" esvazia a lista por completo:

lista.clear()
print(lista) # []
print('')

#  Construindo uma Lista com list()

#Também é possível construirmos listas através do método construtor list(), veja:

par = list((2, 4, 6, 8, 10))
print(par) #[2, 4, 6, 8, 10]
print('')

#também pode se criar uma lista de  valores atraves do range():

impar = list(range(1, 10, 2))
print(impar)#[1, 3, 5, 7, 9]




