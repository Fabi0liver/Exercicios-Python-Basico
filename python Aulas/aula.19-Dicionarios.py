#                       Dicionários

# Os dicionários são encontrados em outros linguagens de programação como "memórias associativas"
#ou "matrizes associativas". Ao contrário das seqüências, que são indexadas por um intervalo
#de números, os dicionários são indexados por chaves, que podem ser de qualquer tipo imutável.

# Eles são uma coleção não-ordenada de pares de chaves(keys) & valores(values)
#são normalmente usados quando temos uma grande quantidade de dados.

# Dicionários são otimizados para buscarmos dados e para isso, precisamos saber sua chave.

# Dicionários são definidos entre chaves "{}" onde cada item é um par na forma de chave:valor,
#separados por ",", sendo a chave e o valor podendo ser de qualquer tipo.


#    Construtor dict()

# Através do construtor "dict()" também é possível criarmos dicionários:

pessoa = dict(nome="Jesus", idade=33)
print(pessoa) # {'nome': 'Jesus', 'idade': 33}
print('')

#Uma outra maneira de atualizarmos os dados de um dicionário é com o uso do método update():

pessoa.update({'nome': 'Immanuel'})
print(pessoa) # {'nome': 'Immanuel', 'idade': 33}
print('')

#  Chaves(keys):

# Devem ser únicas
# Tipo imutável (int, float, string, tuple, bool) -
#Na verdade precisa de um objeto que seja hashable, mas imagine como imutável uma vez que
#todos os tipos imutáveis são hashable - Tenha cuidado com o tipo float como chave
# Nenhuma ordem para chaves ou valores


#   Valores(Values):

# Qualquer tipo (imutável e mutável)
# Pode ser duplicado
# Valores de dicionários podem ser listas, até mesmo outros dicionários

# Para compreendermos melhor o funcionamento dos dicionários, vamos definir alguns exemplos:

album = {'nome': 'A Night at the Opera', 'artista': 'Blind Guardian', 'lançamento': 2002}
print(type(album)) # <class 'dict'>
print(album) # {'nome': 'A Night at the Opera', 'artista': 'Blind Guardian', 'lançamento': 2002}
print(album['nome']) # A Night at the Opera
print(album['artista']) # Blind Guardian
print(album['lançamento']) # 2002
print('\n')

# Também podemos definir um dicionário dessa forma, o que torna ele mais legível:

elemento = {
   "nome": "Ouro",
   "símbolo": "Au",
   "número atômico": 79
}
print(elemento) # {'nome': 'Ouro', 'símbolo': 'Au', 'número atômico': 79}
print('')

#          Acessando e Manipulando Dados

# Para acessarmos os itens do dicionário, precisamos nos referir a sua chave, por exemplo:

print(elemento["nome"]) # Ouro
print('')

#É possível alterar os valores de um dicionário, podemos fazê-lo da seguinte maneira:

elemento["nome"] = "Prata"
elemento["símbolo"] = "Ag"
elemento["número atômico"] = 47
print(elemento) # {'nome': 'Prata', 'símbolo': 'Ag', 'número atômico': 47}
print('\n')


#     Imprimindo os Valores de um Dicionário

# Podemos usar o for loop para imprimir os elementos de um dicionário.

personagem = {
   "nome": "Gandalf",
   "classe": "Wizard",
   "ordem": "Istari"
}
print(personagem) # {'nome': 'Gandalf', 'classe': 'Wizard', 'ordem': 'Istari'}
print('')
for key in personagem: # Percorre os valores do dicionário
    print(personagem[key]) # Imprime os valores do dicionário
                           #Gandalf
                           #Wizard
                           #Istari
print('')

# Também podemos usar o método values() da seguinte forma:

for p in personagem.values(): # Percorre as chaves e os valores
    print(p) # Imprime os valores do dicionário
             #Gandalf
             #Wizard
             #Istari
print('')

#A lém disso é possível percorrer tanto as chaves como os valores, usando a função items():

for chave, valor in personagem.items(): # Percorre as chaves e os valores
    print(f'{chave}: {valor}') # Imprime as chaves e os valores
                               #nome: Gandalf
                               #classe: Wizard
                               #ordem: Istari
print('')


#      Adicionando Itens ao Dicionário

# Para adicionarmos um novo item em nosso dicionário usamos uma nova chave
#e atribuimos um valor a ela.

personagem['altura'] = 1.85
print(personagem) # {'nome': 'Gandalf', 'classe': 'Wizard', 'Ordem': 'Istari', 'altura': 1.85}
print('')


#    Removendo Itens do Dicionário

# É possível também, de várias formas, remover os itens de um dicionário.

# Usando o método pop(), nos será retornado o item removido:

personagem.pop('altura') # 1.85
print(personagem) # {'nome': 'Gandalf', 'classe': 'Wizard', 'Ordem': 'Istari'}
print('')

# Usando o método popitem(), remove o último par de chave-valores adicionado de personagem
#e o retorna como uma tupla:

personagem.popitem() # ('Ordem', 'Istari')
print(personagem) # {'nome': 'Gandalf', 'classe': 'Wizard'}
print('')

# A palavra-chave del remove um item com a chave especificada:

del personagem["Classe"] # 'classe: 'wizard'
print(personagem) # {'nome': 'Gandalf'}

# Além disso é possível deletar o dicionário por completo com del,
#tenha muita atenção, pois todos os dados serão perdidos.

del personagem
print(personagem) # NameError: name 'personagem' is not defined

#O método clear() nos permite esvaziar o dicionário por completo:

pessoa.clear()
print(pessoa) # {}

