#                              Modularização

# Em termos simples, modularização é a prática de dividir um programa em módulos independentes e interconectados.
# Um módulo em Python é um arquivo contendo código Python, geralmente contendo funções, classes e variáveis.
# Essa abordagem ajuda a organizar o código de maneira mais lógica e eficiente.


#    Vantagens da Modularização

# * Legibilidade:
# Dividir um programa em módulos torna o código mais legível. Cada módulo pode ser tratado
#como uma unidade funcional separada, facilitando a compreensão do código.

# * Reusabilidade:
# Módulos podem ser reutilizados em diferentes partes de um projeto ou em projetos distintos.
# Isso economiza tempo e esforço, especialmente ao lidar com funcionalidades comuns.

# * Manutenção Simples:
# Ao isolar diferentes partes do código, as atualizações e correções podem ser aplicadas de forma mais direta.
# Isso reduz a complexidade e o risco de introduzir erros indesejados.


#   Como Modularizar em Python

# - Funções e Classes:
# Agrupe funcionalidades relacionadas em funções ou classes.
# Isso permite a reutilização e a fácil compreensão do código.

# - Imports:
# Use imports para incluir módulos externos ou seus próprios módulos no código.
# Isso facilita a organização e a manutenção do projeto.

# - Divisão Lógica:
# Separe o código de acordo com a lógica de negócios.
# Crie módulos específicos para lidar com entrada/saída, lógica de processamento, interfaces de usuário, etc.


#   Exemplo Prático

# Vamos pensar no modo comum de programar.
# Por exemplo, tenho uma função chamada “soma” que recebe dois parâmetros, ‘a’ e ‘b’, e retorna a soma deles.
# É uma função simples. Poderia tê-la aqui e, quando precisasse usá-la, bastaria chamar, passando os valores, como 2 e 3.
# Dessa forma, ao executar esse trecho de código, o resultado seria 5, pois é a soma de três com dois.


''' calculo.py

def soma(a, b):
    return int(a) + int(b)


print(soma(2, 3))'''


# À medida que nossa aplicação cresce, torna-se impraticável programar tudo em um único arquivo Python.
# Além de ser extremamente bagunçado, isso torna nosso código imenso e de difícil leitura.
# A situação fica caótica, e a legibilidade desaparece. Não conseguimos separar e testar adequadamente.
# Para resolver esse problema, é crucial compreender que não se pode programar em um único arquivo.
# É necessário dominar o conceito de modularização.

#Então vamos incrementar a nossa programação.
#Vou colocar a função soma em um outro arquivo chamado operacoes_matematicas.py


'''operações matemáticas


def soma(a, b):
    return int(a) + int(b)'''


# Como referenciar essa função no arquivo calculo.py?
# A palavrinha mágica é a palavra reservada import


'''calculo.py

import operacoes_matematicas

print(operacoes_matematicas.soma(2, 3))'''


# Quando utilizamos o import dessa maneira, trazemos TUDO que está no módulo operacoes_matematicas
#e dependendo do tamanho do módulo isso pode criar problemas de desempenho no script.

#Vamos incrementar o nosso módulo operacoes_matematicas acrescentando uma funcao de subtração.


'''operações matemáticas

def soma(a,b):
    return int(a) + int(b)

def subtracao(a,b):
    return int(a) - int(b)'''


# Vamos supor que você não precise mais do método de soma.
# Como carregar apenas o método de subtração no módulo calculo.py?


'''from operacoes_matematicas import subtracao

print(subtracao(3,2))'''


# Note que nesse caso, não foi preciso mencionar o nome do módulo para chamar a função subtracao.

# Agora vamos incrementar ainda mais o módulo operacoes_matematicas,
#desta vez acrescentando as funções de multiplicação e divisão.


'''operações matemáticas


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b
 
 
def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    return a / b'''


#E supondo que eu queira trazer apenas as funções de soma e multiplicação para o módulo calculo.py.
# Como fazer isso?


'''from operacoes_matematicas import soma, multiplicacao

print(soma(3,2))
print(multiplicacao(3,2))'''


# Neste caso, se você tentar referenciar a função subtração ou divisão, o Python vai gerar um erro.


'''$ python calculo.py
5
Traceback (most recent call last):
  File "C:\Users\quali\OneDrive\Documentos\modularizacao\calculo.py", 
line 4, in <module>
    print(subracao(3,2))
          ^^^^^^^^
NameError: name 'subracao' is not defined'''


# Uma outra forma de referenciar todos os pacotes é utilizando o caracter asterisco(*).
# Note que neste caso não precisamos referenciar o nome do módulo.

'''from operacoes_matematicas import *

print(soma(3,2))
print(subtracao(3,2))'''



#                     Empacotamento

# O empacotamento de Python refere-se ao processo de criar pacotes ou bibliotecas reutilizáveis
#em Python. Um pacote é um conjunto de módulos, que são arquivos contendo código Python,
#que podem ser facilmente importados e usados em diferentes projetos.
# Esses pacotes são empacotados em uma estrutura hierárquica de diretórios que facilita sua
# distribuição e instalação.
'''
projeto/
└── uteis/
    └── modulo/
        ├── __init__.py
        └── operações matematicas.py
                           '''

#    Por Que o Empacotamento de Python é Importante?

# O empacotamento de Python é importante por diversos motivos.
# Abaixo, listamos algumas razões pelas quais essa prática é essencial para os desenvolvedores Python:

#  1. Reutilização de código:
# Ao criar pacotes, os desenvolvedores podem compartilhar código e funcionalidades com outros projetos.
# Isso permite uma maior eficiência no desenvolvimento, pois não é necessário reinventar a roda a cada novo projeto.

#  2. Modularidade:
# O empacotamento de Python promove a modularidade do código. Ao organizar o código em pacotes e módulos,
#é possível separar funcionalidades específicas em componentes individuais.
# Isso facilita a manutenção e o entendimento do código, tornando-o mais legível e escalável.

#  3. Facilidade de distribuição e instalação:
# Ao empacotar um código em Python, é possível distribuí-lo de forma fácil e rápida.
# Os pacotes podem ser disponibilizados em repositórios públicos, como o PyPI (Python Package Index),
# e instalados usando ferramentas como o pip.
# Isso facilita a disseminação do código e permite que outros desenvolvedores o utilizem com apenas alguns comandos.

#  4. Colaboração:
# O empacotamento de Python incentiva a colaboração entre desenvolvedores.
# Ao criar pacotes, é possível compartilhar o trabalho com outros membros da comunidade,
#que podem contribuir para sua melhoria e correção de bugs.
# Isso cria um ambiente de colaboração e aprendizado mútuo.


#               Como Criar e Empacotar um Pacote em Python

# A criação e o empacotamento de um pacote em Python envolvem algumas etapas essenciais.
# Vamos abordar cada uma delas de forma resumida:


#  1. Estrutura do pacote:

#  primeira etapa é organizar a estrutura de diretórios do pacote.
# Geralmente, os pacotes em Python seguem uma estrutura padrão, com um diretório principal
#que leva o nome do pacote e contém os módulos e subpacotes.

#  2. Definição de módulos:

# Em seguida, é necessário definir os módulos que farão parte do pacote.
# Cada módulo é um arquivo Python que contém o código correspondente a uma funcionalidade específica.

# 3. Arquivo de configuração:

# Um arquivo de configuração, como o setup.py, é necessário para definir
#metadados sobre o pacote, como nome, versão e dependências.
# Esse arquivo também é responsável por especificar as instruções de instalação do pacote.

# 4. Empacotamento e distribuição:

# Depois de definir a estrutura do pacote e configurar o arquivo de configuração, é possível empacotar
#o pacote e distribuí-lo.
# Isso pode ser feito gerando um arquivo de distribuição, como um arquivo .tar.gz ou .whl,
#que pode ser instalado em outros projetos.



