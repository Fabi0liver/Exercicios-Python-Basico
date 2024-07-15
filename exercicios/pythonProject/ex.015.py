#  Escreva um programa que pergunte a quantidade de km pecorridos por um carro alugado,
#e a quantidade de dias pelos quais ele foi alugado.
#  Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.

km = float(input('Quantos quilômetros você rodou com o carro:'))
dia = int(input('Quantos dias você fico com o carro:'))
pck = km * 0.15
pcd = dia * 60
preco = pck + pcd
print('')
print('O carro ficou alugado por {} dias, resultou no valor de R${:.2f} a pagar pelos dias usados.'.format(dia, pcd))
print('E o carro rodou por {:.0f}km, resultando no valos de R${:.2f} a pagar pela quilômetragem rodada.'.format(km, pck))
print('O total do pagamento do aluguel do carro é R${:.2F}. Obrigado pela preferencia!'.format(preco))


print('')
print('')

Dia = int(input('Quantos dias você ficou com o carro:'))
Km = float(input('Quantos quilômetros você rodou com o carro:'))
prc= ((Dia * 60) + (Km * 0.15))
print('')
print('Você alugou o carro por {} dias. E pecorreu com ele {:.0f}km.'.format(Dia, Km))
print('O valor total  do aluguel do carro a ser pago é de R${:.2f}'.format(prc))


