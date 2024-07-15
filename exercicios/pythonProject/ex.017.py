#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
#calcule e mostre o comprimento da sua hipotenusa.

from math import sqrt,hypot

co = float(input('Qual e o comprimento do cateto oposto do seu triângulo:'))
ca = float(input('Qual e o comprimento do cateto adjacente do seu triângulo:'))
hp = sqrt((co ** 2) + (ca ** 2))
print('')
print('Um triângulo com {} de comprimento no cateto oposto,e {} de comprimento no cateto adjacente.'.format(co, ca))
print('Tem {:.2f} de comprimento na hipotenusa.'.format(hp))

print('')
print('Um triangulo de {}cm no cateto oposto e {}cm no cateto adjacente. Resulta ter {:.2f}cm na hipotenusa.'.format(co, ca, sqrt((co ** 2) + (ca ** 2))))

print('')
print('Um triangulo de {}cm no cateto oposto, e {}cm no cateto adjacente. Resulta ter {:.2f}cm na hipotenusa.'.format(co, ca, hypot(co, ca)))
