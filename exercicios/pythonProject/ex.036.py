#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.Oprograma vai
#perguntar o valor da casa, o sálário do comprador e em quantos anos ele vai pagar.

#Calcule o valor da prestação mensal, sabendo ela não pode exceder 30% do salário ou então o empréstimo
#será negado.

print('*' * 60)
print('Olá, Vamos fazer uma simulação de financiamento para sua casa?')
print('*' * 60)
print('')
v = float(input('Qual o  valor a ser pago pela casa: R$ '))
s = float(input('Qual o salário do comprador da casa: R$ '))
a = int(input('Em quantos anos o comprador quer dividir o emprestimo: '))
p = v / (12 * a)
e = (30/100) * s
print('')
if p <= e:
    print(f'''Valor do financiamento mensal é: R${p:.2f}  
    \n   Parabéns seu emprestimo foi aprovado!!''')
elif p > e:
    print(f'''O valor do financiamento mensal é: R${p:.2f}
    \n  Lamento!! Seu emprestimo foi negado. 
   Tente outro forma de parcelamento!''')
print('')
print('*' * 60)
print('O nossa equiper Agradece a sua  preferencia !!')
print('*' * 60)

