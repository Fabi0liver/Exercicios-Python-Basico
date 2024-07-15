#Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um numero entre 0 e 10.
#Só que agora o jogador vai tenatr adivinhar ate acertar, mostrando no final quantos palpites formam
#necessáriospara acertar.

from random import randint

print('')
print('\t\tVAMOS JOGAR!!')
print('')
print('Vou pensar em um número entre 1 e 10. \n\t  Tente adivinhar!')
print('')

cp = randint(1, 10)
v = 0
acertou = False
while not acertou:
    v = v + 1
    jog = int(input('Em que número estou pensando? '))
    if jog == cp:
        print('')
        print(f'''\t  Eu estava pensando no número! {cp}!
            \33[33mVOCÊ ACERTOU !!!\33[m''')
        print('')
        acertou = True
    elif (jog != cp) and (jog >= 1 and jog <= 10):
        print('')
        print('\tNão é esse número que estou pensando!')
        if jog < cp:
            print('')
            print('\t\33[31mO número é maior... TENTE NOVAMENTE!\33[m')
        elif jog > cp:
            print('')
            print('\t\33[31mO número é menor...TENTE NOVAMENTE!\33[m')
        print('')
    elif jog > 10:
        print('')
        print('''\tVocê não entendeu o jogo?!
     \33[32mO número é entre 1 e 10!\33[m''')
        print('')

if v != 1:
    print(f'Você precisou de \33[35m{v} tentativas\33[m, para acerta o número!!')
else:
    print(f'Você precisou de \33[35m{v} vez\33[m , para acerta o número!!')


print('')
print('\tFoi legar jogar com Você! \n  Se quiser é só tentar de novo!')

