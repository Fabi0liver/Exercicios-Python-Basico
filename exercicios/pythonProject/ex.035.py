#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
#podem formar um triângulo.

r1 = float(input('Digite o comprimento de uma reta em cm: '))
r2 = float(input('Digite o comprimento de uma segunda reta: '))
r3 = float(input('Digite o comprimento de uma terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com essas três retas você conseguem formar um triagulo!!')
else:
    print('Com essas três retas você não consegue formar um triângulo !!')

