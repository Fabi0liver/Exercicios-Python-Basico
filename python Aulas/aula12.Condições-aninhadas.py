#                                     Condições Aninhadas

#  As condições aninhadas em Python permitem verificar múltiplas condições dentro de uma estrutura if/elif/else,
# proporcionando mais controle sobre o fluxo do programa. A sintaxe básica envolve a utilização de if,
# elif e else para realizar verificações e tomar decisões com base nas condições.

#   As condições aninhadas oferecem maior flexibilidade no controle do fluxo do programa

#  A utilização de if, elif e else permite a verificação de múltiplas condições e a tomada de decisões
# com base nos resultados.

#  Esses conceitos são fundamentais para a criação de programas Python que realizam verificações e comparações

#  O elif é a junção do comando ELSE+IF que é utilizado nas Estruturas Condicionais Aninhadas, que pode ser usado uma,
# ou varias vezes na mesma codição.

#exemplo:

print('Vamos brincar de matématica?')
num = int(input('Digite um número: '))
if num > 0:
    print(f'O {num} é um número positivo!')
elif num < 0:
    print(f'O {num} é um número negativo!')
else:
    print(f'O {num} é o número neutro!')

print('Você viu como sou bome de matematica!!')
