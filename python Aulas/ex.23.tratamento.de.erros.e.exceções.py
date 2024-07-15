#                        Tratamento de Erros e Exceções

# Uma exceção é algo inesperado, fora do planejamento que ocorre durante a execução de um programa.
# Por exemplo, você quer realizar alguma operação aritmética (uma divisão) envolvendo dois números,
#mas acaba digitando uma letra no lugar de um dos números, o python irá gerar um erro na execução
#dessa operação(comando), chamado de exceção .

# Antes de mergulhar nas técnicas de tratamento de erros,
#é crucial entender os tipos comuns de erros em Python:

# SyntaxError: Erros de sintaxe ocorrem quando o código não segue a gramática da linguagem.

# NameError: Surge quando uma variável ou função não é reconhecida.

# TypeError: Acontece ao aplicar uma operação a um tipo inapropriado de objeto.

# IndexError e KeyError: Relacionados ao acesso de elementos em coleções,
#como listas e dicionários, com chaves ou índices inexistentes.

# ValueError: Ocorre quando uma função recebe um argumento correto em tipo, mas inadequado em valor.

# AttributeError: Surge ao tentar acessar um atributo ou método inexistente.

# ZeroDivisionError: Erro ao dividir um número por zero.

# EOFError: gerado quando a função input() atende à condição de fim de arquivo.

# ZeroDivisionError: gerado quando você divide um valor ou uma variável com zero.


#       Tratamento de exceções com try, except, else e finally


# Depois de aprender sobre erros e exceções, aprenderemos a lidar com eles usando os
#blocos try, except, else e finally.

# Então, o que queremos dizer com lidar com eles?
# Em circunstâncias normais, esses erros interromperão a execução do código e exibirão
#a mensagem de erro. Para criar sistemas estáveis, precisamos prever esses erros e apresentar
#soluções alternativas ou mensagens de aviso.

#    Declaração try e except

# O método mais básico em Python para o tratamento de exceções é o uso dos blocos try e except.
'''
try:
    # código potencialmente problemático

except TipoDeErro:
    # ação em caso de erro
'''

# Exemplo Prático:

'''
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Divisão por zero não permitida.")
'''

#   Tratando Múltiplas Exceções

# Para garantir que seu código esteja preparado para lidar com diferentes tipos de erros,
#você pode definir múltiplos blocos except.

'''
try:
    # código
except ZeroDivisionError:
    # tratamento para ZeroDivisionError
except TypeError:
    # tratamento para TypeError
'''

#   Blocos Else e Finally

# Else: Executado se nenhuma exceção for capturada no bloco try.

# Finally: Sempre executado, independentemente de uma exceção ocorrer ou não.

'''
try:
    # código
except TipoDeErro:
    # tratamento da exceção
else:
    # executado se não houver exceção
finally:
    # sempre executado
'''

#    Levantando Exceções

# Python permite que você também levante suas próprias exceções usando raise.

'''
if condicao_inadequada:
    raise ValueError("Descrição do erro")
'''

# Criando Exceções Personalizadas

# Para situações específicas, pode ser útil criar exceções personalizadas.

'''
class MinhaExcecao(Exception):
    pass

raise MinhaExcecao("Erro específico")
'''

# O tratamento adequado de erros e exceções em Python é essencial para o desenvolvimento de software de qualidade.
# Ao adotar estas práticas, você não só aumenta a robustez e a confiabilidade do seu código,
#mas também facilita a manutenção e a compreensão por outros desenvolvedores.
# Lembre-se, um código que trata exceções de forma eficaz é um marco de um bom desenvolvedor Python.


try:
    a = int(input('Digite o primeiro Valor: '))
    b = int(input('Digite o segundo Valor: '))
    s = a / b

except (ZeroDivisionError):
    print('O numero zero não poder ser usado nessa operação')

except (ValueError, TypeError):
    print('Talves a tipo de dado não pode ser usao nessa operação')

except (KeyboardInterrupt):
    print('Ops! O usuario não concluio a operação.')

except Exception as erro:
   print(f'Algo deu errado!! O erro foi {erro.__class__}')

else:
    print(f'A divisão do valor {a} com o valor {b} é : {s:.1f}')

finally:
    print('Muito obrigado!! Volte sempre!')

