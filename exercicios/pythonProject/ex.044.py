# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
#preço normal e consição de pagamento:
#Á vista dinheiro/cheque: 10% de desconto
#Á vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% sw juros

print('')
vl = float(input('Qual Valor da compra:R$ '))
print('''
                                  Sabendo que:
        1:               Dinheiro ou Cheque: 10% de desconto!
        2:                Á vista no cartão: 5% de desconto!
        3:                     2x no cartão: Preço Normal!
        4:             3x no cartão ou mais: 20% de juros!''')

print('')
pg = int(input('Digite o número que será a forma de pagamento: '))
print('')
if pg == 1:
    print(f'''                o Valor da compra é R${vl:.2f}! 
Mas como o pagamento será á vista, terá 10% de desconto ficará R${ vl -(vl * (10 / 100)):.2f}!!''')
elif pg == 2:
    print(f'''                    o Valor da compra é R${vl:.2f}!
Mas como o pagamento será no cartão á vista, terá 5% de desconto e ficará R${vl - (vl * (5/100)):.2f}!!''')
elif pg == 3:
    print(f'''         O valor da compra é R${vl:.2f}!
Será dividido no cartão, você parará 2x de R${vl / 2 :.2f} SEM JUROS !!! ''')
elif pg == 4:
    div = int(input('Vai dividir a compra em quantas vezes: '))
    total = (vl + (vl * (20/100))) / div
    print(f'''         O valor da compra é R${vl:.2f}!
Mas como será dividido no cartão, você pagará com 20% de juros {div}x de R${total:.2f} !!''')
else:
    print('Não temos essa opção em forma de pagameno!')

print('\n')
print('   Agradecemos pela preferencia!!')
