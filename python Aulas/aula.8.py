  #Trabalhando com módulos

#modúlos são pacotes que já podem vim na pré-definição do python , mas se precisar de mais funções
#que não tem no Python, pode se importa de fora outros modulos.

# Para se incluir essas funções no projeto/progrma se usa o comando "import"
# "import" e usado na primeira linha do programa pra importar modulos que será usado no projeto.
# import na frente com o nome do modulo apos ex.(import math), importa o modulo inteiro.
# colocando  o "from" primeiro após o nome do modulo, depois  o "import". Podemos escolher
#uma função ou mais do modulo ex.(from math import...).

#exemplo de um modulo muito usado no python

# math = esse modulo tras outras funções matematicas, que não tem no Python
#      ceil = essa função faz o arredondamento de um número flutuante(float), para cima
#     floor = essa função faz o arredondamento de um número flutuante(float), para baixo
#     trunc = essa função faz a eliminação da virgula pra frente nos números flutuantes, sem fazer arredondamento.
#       pow = essa função faz a potência de uma número, que é a mesma função do "**"
#      sqrt = essa função faz a raiz quadrada de um número.
# factorial = essa função faz o calculo fatorial de um número.

# então de eu quiser importa todo o modulo math eu devo usar: import math
# mas se eu quiser só uma função do modulo math eu devo usar: from math import sqrt
