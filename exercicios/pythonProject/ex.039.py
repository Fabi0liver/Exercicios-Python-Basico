#Faça um programa que leia o ano de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar.
#se é a hora de se alistar.
#Se já passou do tempo do alistamento


print('')
print('= * =' * 80)
print('     Olá jovem Homem Brasileiro!!! Como está sua situação com o seu ALISTAMENTO MILITAR?')
print('= * =' * 80)
print('')
print('''                  HUMM? Você não sabe o que é alistamento militar? 
  
      O alistamento militar deve ser realizado por todo brasileiro, do sexo masculino, 
      no período do primeiro dia útil de janeiro até o último dia útil do mês de junho
                        do ano em que o jovem completar 18 anos.''')
print('')
print('          Sabendo disso jovem, quer saber como está sua situação militar?!')
print('')
ano = int(input('Então vamos descobrir sua situação! Me diga o ano do seu nascimento: '))
idade = 2024 - (ano)
print('')
if idade < 18:
    print(f'''Você tem {idade} anos, ainda não tem a idade para se alistar! 
Falta {18 - idade} anos para seu momento de servir o país!!!''')
    print(f'    Seu alistamento será no ano {(18 - idade) + 2024}.')
elif idade == 18:
    print(f'''Você tem{idade} anos, está no momento certo pra se alistar!!
          Procure uma junta militar urgentemente!
    você só tem até o dia 30 de Junho pra se alistar!!''')
else:
    print(f'''Você tem {idade} anos, já passou {idade - 18} anos da idade do alistamento !!
              Procura agora mesmo um junta militar!
E regularize sua situação e evite pagar a  multa por atraso!''')
    print(f'          Seu alistamento foi no ano {2024 - (idade - 18)}.')


