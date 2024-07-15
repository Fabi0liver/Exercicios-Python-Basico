                                #Manipulando  cadeia de texto/caractere

                   #Cadeia de caracteres, cadeia de textos ou string.
            #Para o python toda cadeia de texto está entre aspas simples ou duplas.



#     Como as cadeias de caracteres são uma sequência de caracteres, você pode acessá-las por meio
#          de fatiamento e indexação da mesma forma que faria com as listas ou tuplas do Python.
#  As cadeias de caracteres são indexadas em relação a cada caractere da cadeia e a indexação começa em 0:
# Também é possível acessar os caracteres na direção oposta a partir de -1, o que significa que você
#               também pode usar -1 como valor de índice para acessar  na cadeia de caracteres.

#                                      "Curso em vídeo Python"

#              0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20
#            | C | u | r | s | o |   | e | m |   | v | í | d | e | o |   | P | y | t | h | o | n |
#             -21 -20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1

   # fatiamento

 # O fatiamento é uma técnica em Python que permite que você use um elemento específico ou um subconjunto de
 #  elementos de um objeto contêiner usando seus valores de índice.

# exemplos apartir da frase "Curso em Vídeo Python" logo acima:

# frase[9] = na frase o 9 é o "V", que seria o mesmo que [-12] començando do ultímo caractere

# frase[9:13] = na frase seria "Víde", seria selecionado do 9 ao 12, pois no Python o ultimo caracte pedido e excluido.

# frase[9:21] = na frase seria  "Vídeo Python", como na frase não existe o 21 ela selecionarar até o ultimo caractere

# frase [9:21:2]= na frase seria "Vdopto", dessa maneira os caracter será selecionado pulando de dois em dois apartir do 9 até o 21

# frase[:5] = na frase seria " curso", dessa maneira com não está indicando o começo só o final,
# será selecionado desde o começo no caso do "0" e termina no "4" pois o ultimo pedido e excluido

# frase[15:] = na frase seria "Python", dessa maneira tem aonde começa mas não o final. Então seria selecionado
# até o começo na "15" indicado até o ultimo caracter que serio o "20".

# frase[9::3] =  na frase seria "VePh", dessa maneira só está indicando nada entre os "::", seria do primeiro
# caracter indicado até o ultimo, e o numero apos o "::" indica que sera selecionado os caracter pulando de 3 em 3.


   # Análise

 #  Análise seria pra saber sobre a string, que tamanho ela tem, que letra ela começa, qual ela termina , qual palavra inteira ...

# exemplos apartir da frase " Curso em Vídeo Python" logo acima

# len(frase) = seria usado pra saber o numero de caracteres da frase, que no exemplo da frase são "21".

# frase.count('o') = seria usado pra contar quantas vezes o "o" aparece na frase, que no caso da frase seria "3" vezes.
# frase.count('o',0,13)= seria usado para contar quantas vezes o "o" aparece na frase entre o 0 e 13(no caso 12, pois o ultimo e excluido)

# frase.find('deo') =  seria usado pra saber quando vezes encontra o "deo" na frase. O python vai dizer onde começou o que foi indicado
#que no caso da frase "deo" começa no "11".
# frase.find('Android')= nesse caso, como na nossa frase não há o "Android", o Python mostrará o "-1',
#que neste caso está dizendo que não encontrou essa string na frase.

# 'curso' in frase = seria usado pra saber se tem a string "curso" na frase, o Python responderá "True" que seria dizer que há essa palavra na frase.


   # Transformação

 # Uma lista de string é imutavel,mas podemos mexer nela atraves de alguns metodos

# exemplos apartur da frase "Curso em Vídeo Python" logo acima.

# frase.replace('Python,'Android') = seria pra trocar a string da frase pela outra palavra indicada. Nesse caso seria trocar onde há  "Python"
# pelo "Android". A frase ficaria " Curso em Vídeo Android".

# frase.upper() = seria usado pra transformar todas as letras minusculas da frase em maiusculas.

# frase.lower() = seria usado pra transformar todas as letras maiusculas da frase em minusculas.

# frase.capitalize() = Seria usado pra transformar toda as letras em minusculas de uma frase, só a primeira letra da frase em maiuscula.

# frase.title() = seria usado para transformar as primeira letras de todas as palavras da frase em maisculas.

# frase.strip() = seria usado pra remover espaços vazios inuteis  do começo e fim da string/frase.
# frase.rstrip() = seria usado pra remover  espaços vazios inuteis só do final da string/frase.
# frase.lstrip() = seria usado pra remover espaços vazios inuteis  só do inicio da string/frase.


   # Divisão e Junção

 #Como o nome já diz, é usado pra dividir e separar strings, e juntar os strings.

# exemplos apartir da frase "Curso em Vídeo Pythons" logo acima.

# frase.split() = seria usado pra separar um string em listas separadas.
# Como a frase "Curso de Vídeo Python" ficaria "Curso" "de" "Vídeo" "Python"

# '-'.join(frase)= seria usado para juntar listas separada com o que colocar no meio de ''.
#Como a frase separada "Curso" "de" "Vídeo" "Python" ficaria  assim " Curso-de-Vídeo-Python.



