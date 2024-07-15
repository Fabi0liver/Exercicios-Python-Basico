#Faça um algaritmo que leia o preço de produto,e mostre seu novo preço, com 5% de desconto.

p = float(input('Digite o valor do produto que você quer dá o desconto: R$'))
print('')
print('O seu produto custa: R${:.2f} \nCom desconto de 5% fica: R${:.2f}'.format(p, p-(5/100)*p))





