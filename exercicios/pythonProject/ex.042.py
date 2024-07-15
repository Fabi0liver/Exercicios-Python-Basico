# Refaça o desafio 035 dos triângulos acrescentando o recurso de mostrar que tipo
#de triângulo será fomrado:
#Equilátero: todos os lados iguais
#Isósceres: dois lados igauis
#Escaleno: todos os lados diferentes

print('')
print('                      Vamos jogar um pouco?!')
print('')
print('''          Você vai me dizer o comprimento de três retas.
       E eu vou ti dizer se elas podem formar um triângulo.
             E que tipo de triângulo será formado!''')
print('')
print('                   Entendido?! Então vamos lá!!')
print('')
r1 = float(input('Diga o comprimento da primeira reta: '))
print('')
r2 = float(input('Diga o comprimento da segunda reta: '))
print('')
r3 = float(input('Diga o comprimento da terceira reta: '))
print('')
if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print('Com essas três retas, você conseguem formar um triângulo!!')
    if (r1 == r2) and (r1 == r3) and (r2 == r3):  # tbm pode ser : if r1 == r2 == r3
        print('E será um triângulo "Equilátero", já que todos os lados são iguais!')
    elif (r1 != r2) and (r1 != r3) and (r2 != r3):  # tbm pode ser if r1 != r2 != r3 != r1
        print('E será um tríângulo "Escaleno", já que todos os lados são diferentes!')
    else:
        print('E será um triângulo "Isósceles", já que somento dois lados são iguais!')
else:
    print('Com essas três retas, você não conseguem formar um triângulo!!')
print('')
print('''Engraçado como podemos aprender tanto com triângulos! 
      Espero que tenha gostado do jogo!!''')






