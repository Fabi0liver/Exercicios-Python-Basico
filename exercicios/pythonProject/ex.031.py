#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem , cobrando R$0.50 por km para viagem de até 200km
#e R$0.45 para viagem mais longas.

d = float(input('Digite em km a distância de sua viagem: '))
r1 = d * 0.50
r2 = d * 0.45
if d <= 200:
    print(f'A passagem da sua viagem de {d:.2f}km, custará R${r1:.2f}!')
else:
    print(f'A passagem da sua viagem de {d:.2f}km, custará R${r2:.2f}!')


if d <= 200:
    print(f'A passagem da sua viagem de {d:.2f}km, custará R${d * 0.50:.2f}!')
else:
    print(f'A passagem da sua viagem de {d:.2f}km, custará R${d * 0.45:.2f}!')




