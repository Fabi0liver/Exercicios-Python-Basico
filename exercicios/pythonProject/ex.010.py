#crie um programa que leia quanto dinheiro uma pessoa tem na carteira,
# e mostre quantos dolares ela pode comprar.  considere = U$$ 1,00 = R$ 3,27


#r = float(input('Digite o valor em Real que você quer converter em Dolar: R$'))
#print('')
#print(' Você tem: \n R$:{} \n Que são: \n U$$:{:.2f}'.format(r, r/3.27))

real = float(input('Diga quanto dinheiro você tem na carteira? R$:'))
dolar = real/ 5.35
euro = real / 5.25
pesoA = real / 0.0060
iene = real / 0.034
franco = real / 6.03
libra = real / 6.81
rublo = real / 0.060
rupia = real / 0.064

print('')
print('Então convertendo seus R${:.2f} , você tem:\n'' \nU$:{:.2f} (Dolar)\n'' \n€:{:.2f} (Euro)\n'' \n$:{:.2f} (Peso Argentino)\n'' \n¥:{:.2f} (Iene Japonês)\n'''.format(real, dolar, euro, pesoA, iene))
print('CHF:{:.2f} (Franco Suiço)\n'' \n£:{:.2f} (libra Esterlina)\n'' \n₽:{:.2f} (Rublo Russo)\n'' \n₹:{:.2f} (Rupia Indiana)'.format(franco, libra, rublo, rupia))



