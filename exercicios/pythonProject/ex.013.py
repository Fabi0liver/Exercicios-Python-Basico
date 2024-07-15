# Faça um algoritmo que leia o salário de um funcionário
#e mostre seu novo salário, com 15% de aumento.

#s = float(input('Digite o valor do salário, que vai receber o aumento: R$'))
#print('')
#print('O salário do seu funcionário é: R${:.2f} \nCom acrecimo de 15% ele passará á receber: R${:.2f}'.format(s, s+(15/100)*s))


produ = float(input('Qual o valor do produto: R$'))
avista = (produ - (10/100) * produ)
aprazo = (produ + (20/100) * produ)
atac = (produ - (40/100) * produ)

print(' A valor do produto é de R${:.2f}, mas  ficou por R${:.2f}, pois a vista tem um desconto de 10%!'.format(produ, avista))
print('O mesmo produto a prazo com o acrecismo de 20% de juros, ficaria por R${:.2f}.'.format(aprazo))
print('Tem a possibiliade de compra o produto pra em atacado para revender com o desconte de 40%. \nE o valor por unidade cai para R${:.2f}'.format(atac))
print('Achei muito legal!')
