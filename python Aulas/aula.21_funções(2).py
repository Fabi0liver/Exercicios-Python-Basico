#                                       Funções(2)


#    Função Help

# Em Python, a help()função é uma função interna que fornece informações sobre módulos, classes, funções e módulos.

# A função de ajuda do Python é usada para exibir a documentação de módulos,
#funções, classes, palavras-chave, etc. Ela fornece informações sobre módulos, classes,
#funções e métodos. É uma ferramenta útil para obter documentação e assistência sobre vários aspectos do Python.

#Sintaxe : help([objeto])

# Parâmetros (opcional): qualquer objeto para o qual queremos alguma ajuda ou informação.

#Se a função de ajuda for passada sem um argumento, o utilitário de ajuda interativo será iniciado no console.

# exemplo:

help(abs) # abs(x, /)
             #  Return the absolute value of the argument.

# Docstring

# A primeira string depois do cabeçalho da função é chamada de docstring,
#é uma string usada para especificar a funcionalidade da nossa função, e embora seja opcional,
#vos lembro que documentar é uma importante prática de programação, uma vez que possivelmente outras
#pessoas estarão lendo nosso código, inclusive é importante até mesmo para você lembrar o que você fez!

def contador(i, f, p):
    '''
    Esse fução e usada pra fazer um contagem com parametros :
    'i' como o número de  inicio da contagem,
    'f' como o número do final da contagem,
    'p' como o números de quantos numeros em quentos numeros vão ser contados.
    '''
    for c in range(i, f, f):
        c = i
        while c <= f:
            print(c, end=' ')
            c += p
        print('FIM!')


help(contador) # contador(i, f, p)
                   # Esse fução e usada pra fazer um contagem com parametros :
                   # 'i' como o número de  inicio da contagem,
                   # 'f' como o número do final da contagem,
                   # 'p' como o números de quantos numeros em quentos numeros vão ser contados.


# Caso queiramos ver o docstring de uma função, podemos acessar o atributo __doc__:

print(contador.__doc__) # Esse fução e usada pra fazer um contagem com parametros :
                        # 'i' como o número de  inicio da contagem,
                        # 'f' como o número do final da contagem,
                        # 'p' como o números de quantos numeros em quentos numeros vão ser contados.

print(abs.__doc__) # Return the absolute value of the argument.


#     Parâmetros Opcionais

# Podemos definir parâmetros padrão para caso a função seja invocada sem nenhum argumento passado,
#estes preencherão as opções.:

def somar(a, b, c=0):
    s = a + b + c
    print(f'A soma é {s}')

# O primeiro, e o segundo  parâmetros são  necessários ; o terceiro  é opcional.
# O valor padrão do terceiro ('c') é 0.

# Se fornecer os três um argumento:

somar(3, 5, 4)  # A soma é 12

# O 'C' recebe o valor do argumento passado .
# Em outras palavras, o argumento opcional ignora o valor padrão.

# Se você só fornecer dois  argumento:

somar (3, 5) #A soma é 8
print('\n')
# O 'C' recebe o valor padrão passado, que é '0'.

# Se uma função tem ambos os parâmetros obrigatório e opcional,
# todos os parâmetros necessários têm que vir primeiro, seguidos pelos opcionais.


#       Escopo de Variáveis

# O escopo de uma variável se refere ao local onde uma variável é definida e onde ela pode ser acessada.
# Em Python, existem quatro tipos de escopos: local, global, enclosing e built-in.

# _______________________________________ #

#   * Escopo Local: Uma variável definida dentro de uma função é chamada de variável local.
#Ela só pode ser acessada dentro dessa função.


def funcao_local():
  x = 10  # Variável local
  print(f'Na função, x vale {x}')
  print(f'Na função, n vale {n}')


# programa principal
n = 2
# print(f'No programa principal, x vale {x}') # NameError: name 'x' is not defined
print(f'No programa principal, n vale {n}') # No programa principal, n vale 2
funcao_local()  # Na função, x vale 10
          # Na função, n vale 2

# Conseguimos imprimir a variável "x" na função "funcao_local"
# Porém, ao tentar acessar e imprimir a mesma variável de fora da função, foi gerado um NameError.
# Isso ocorre porque o argumento "x" é "local" para a função - portanto, não pode ser acessado de fora do corpo da função.

# _______________________________________ #

#   * Escopo Global: Uma variável definida fora de todas as funções é uma variável global
#e pode ser acessada em qualquer lugar do programa.

x = 10
n = 2

def funcao_global():
    print(f'Na função, x vale {x}')
    print(f'Na função, n vale {n}')


# programa principal
print(f'No programa principal, x vale {x}') # No programa principal, x vale 10
print(f'No programa principal, n vale {n}') # No programa principal, n vale 2
funcao_global() # Na função, x vale 10
                # Na função, n vale 2

# _______________________________________ #

#   * Escopo Enclosing: Se uma função está dentro de outra função (função aninhada),
#a função interna tem acesso às variáveis da função externa. Este é o escopo enclosing.


def funcao_externa():
    A = 10  # Variável da função externa
    print(f'Na funcao_externa, A vale {A}')
  # print(f' Na funcao_externa, B vale {B}')

    def funcao_interna():
        B = 2
        print(f'Na funcao_interna, A vale {A}')
        print(f'Na funcao_interna, B vale {B}')
    funcao_interna()


funcao_externa() # Na funcao_externa, A vale 10
                 # NameError: name 'B' is not defined
                 # Na funcao_interna, A vale 10
                 # Na funcao_interna, B vale 2


# Ocorreu um erro?
# Isso ocorre porque não é possível acessar "B" em "funcao_externa". Ele não é definido nessa função.
# No entanto, você pode acessar "A" porque o seu escopo é maior,pois está em "funcao_externa".
# As variáveis de 'funcao_externa" têm um escopo maior e podem ser acessadas a partir
#da função anexa "funcao_interna"..

# _______________________________________ #

#   * Escopo Built-in: São nomes pré-definidos no módulo builtins do Python. Eles são sempre acessíveis.

print(len('Python'))  # 6

print(abs(- 85)) # 85


#    Comando return


# O comando return é uma parte integral de funções em Python.
# Ele não só marca o fim da execução de uma função mas também permite que valores sejam retornados
#para onde a função foi chamada. As estruturas de dados em Python são usadas para armazenar coleções
#de dados, que podem ser retornadas a partir das funções.


def somar(a=0, b=0, c=0):
    s = a + b + c
  # print(f'A soma vale {s}')
    return s


# programa principal

# Sem return:

somar(3, 3, 5) # A soma vale 11
somar(2,2)  # A soma vale 4
somar(6) # A soma vale 6

# Com return:

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2}, {r3}') # Os resultados foram 10, 4, 6

