#(Desafio4) Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações  possíveis  sobre ela.

#Forma meio errada

#x = input(' Digite algo:')
#print(x)
#v = (type(x))
#l = (x.isalpha())
#n = (x.isnumeric())
#M = (x.isupper())
#m = (x.islower())
#c = (x.isalnum())
#print('Os dados  do que  você digitou são')
#print('Que tipo primitivo é: {}'.format(v))
#print('É um numero inteiro: {}'.format(n))
#print('É uma letra: {}'.format(l))
#print('Está em letra maiuscula: {}'.format(M))
#print('Está em letra minuscula: {}'.format(m))
#print('É um numero ou letra: {}'.format(c)

#Forma de se fazer

a = input('Digite algo:')
print('O que você digital está em qual tipo primitivo? ', type(a))
print('O que você digitou tem só espaços? ', a.isspace())
print('O que você digitou é um número? ', a.isnumeric())
print('O que você digitou é uma letra? ', a.isalpha())
print('O que você digitou está em alfanúmerico? ', a.isalnum())
print('O que você digitou só está em letra maiuscula? ', a.isupper())
print('O que você digitou só está em letra minuscula? ', a.islower())
print('O que você digitou está capitalizado? ', a.istitle())





