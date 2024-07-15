#Faça um programa que leia um ângulo qualquer e mostre na tela o valor
#do seno cosseno e tangente desse ângulo.

from math import sin, tan, cos, radians

a = int(input('Defina o ângulo para saber o seno cosseno e tangente:'))
se = sin(radians(a))
co = cos(radians(a))
ta = tan(radians(a))
print('Apartir do ângulo {}° você tem um triângulo com: \n {:.2f} de seno \n {:.2f} de cosseno \n {:.2f} de tangente'.format(a, sin(radians(a)), cos(radians(a)), tan(radians(a))))

print('')
print('Apartir do ângulo {}° você tem em radiano  um triângulo com : \n {:.2f} de seno \n {:.2f} de cosseno \n {:.2f} de tangente'.format(a, se, co, ta))





