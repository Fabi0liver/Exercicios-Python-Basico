#A confederação  Nascinal de Natação precisa de um programa que leia o ano de nascimento
#de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: Mirim
#Até 14 anos: Infantil
#Até 19 anos: Junior
#Até 25 anos: sênior
#Acima: Master

import datetime


print('')
print('*' * 80)
print('          OLÁ!! ATLETA DA NOSSA CONFEDERAÇÃO NACIONAL DE NATAÇÃO!!')
print('*' * 80)
print('')
print('''           Venho Atraves dessa mensagem informa-lo,
      que estamos cadastrando nos atletas participante,
           numa base de dados apartir de categorias.
     Não fiquei assustado! Essa é uma forma de sabemos
              e premiarmos melhor nossos atletas!''')
print('')
print('Nossa forma de categorizar nossos atletas, será primeiramente apartir da faixa de idade.')
print('')
print('       Você pode ver nossas categorias nesta lista logo abaixo:')
print('_' * 80)
print('')
print('''                   Até 9 anos: MIRIM
                  Até 14 anos: INFANTIL
                  Até 19 anos: JUNIOR
                  Até 20 anos: SÊNIOR
                        Acima: MASTER''')
print('')
print('_' * 80)
print('')
print('              Espero que tenha entendido!')
print('\n')
ano = int(input('''Para cadastra-lo no nosso banco de dados,e sabermos sua categoria. 
        Preciso que digite aqui o seu ano de nascimento: '''))
atual = datetime.date.today().year
idade = atual - ano
print('')
if idade <= 9:
    print(f'Você tem {idade} anos! Então entra na categoria: "MIRIM"!!')
elif idade <= 14:
    print(f'Você tem {idade} anos! Então entra na categoria: "INFANTIL"!!')
elif idade <= 19:
    print(f'Você tem {idade} anos! Então entra na categoria: "JUNIOR"!!')
elif idade <= 25:
    print(f'Você tem {idade} anos! Então entra na categoria: "SÊNIOR"!!')
else:
    print(f'Você tem {idade} anos! Então entra na categoria: "MASTER"!!')

print('')
print('''Agora você está cadastrado no nosso banco de dados!!
E já sabe qual sua categoria!! Espero que ti ajude Atleta!''')




