#Crie um programa que faça o computador jogar jokenpô com você.

from random import choice

print('')
print('-+-' * 30)
print('            VAMOS JOGAR?! Que tal Pedra, Papel e Tesoura?!')
print('-+-' * 30)
print('')
print('''            Você vai falar "Pedra", "Papel" ou "Tesoura". 
      E vai ver se ganha acertando o que eu estou pensando! 
                   OK?! Então vamos lá!!''')
print('')
jog = str(input('O que você vai jogar? ')).upper().strip()
lista = ['PAPEL', 'PEDRA', 'TESOURA']
pc = choice(lista)
print('')
print('*' * 30)
print(f''' Computador jogou {pc}!
   Jogador jogou  {jog}!''')
print('*' * 30)

if pc == 'PEDRA':
    if jog == 'PEDRA':
        print('Deu empate nessa!!')
    elif jog == 'PAPEL':
        print('Papel enbrulha a pedra!! Você ganhou nessa!!')
    elif jog == 'TESOURA':
        print('Pedra quebra tesoura! Ganhei Ganhei!!')
    else:
        print(f'Não existe {jog} neste jogo!')
elif pc == 'PAPEL':
    if jog == 'PAPEL':
        print('Deu empate nessa!!')
    elif jog == 'PEDRA':
        print('Papel enbrulha pedra!! Ganhei essa vez!! haha!')
    elif jog == 'TESOURA':
        print('Tesoura corta papel!! Você Ganha essa vez!')
    else:
        print(f'Não existe {jog} neste jogo!')
elif pc == 'TESOURA':
    if jog == 'TESOURA':
        print('Deu empate essa vez!')
    elif jog == 'PEDRA':
        print('Pedra quebra tesoura!! Ganhou em !')
    elif jog == 'PAPEL':
        print('Tesoura corta papel!! Venci !!')
    else:
        print(f'Não existe {jog} neste jogo!')








