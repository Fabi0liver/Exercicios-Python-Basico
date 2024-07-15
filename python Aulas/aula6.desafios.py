#(Desafio3) Crie um programa que leia dois números e mostre a soma entre eles.
#n = int(input('Diga um número:'))
#n1 = int(input('Diga outro número:'))
#s = (n+n1)
#print('A soma entre {} e {}, deu a valor de {}. Está correto?'.format(n,n1,s))

#(Desafio4) Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações  possíveis  sobre ela.
x = input ('Digite algo:')
print(x)
v=(type(x))
n=(x.isnumeric())
l=(x.isalpha())
m=(x.isupper())
print('O que você escreveu e do tipo primitivo {}, o que você escreveu {} número, e {} letra ,se for uma letra, {} letra maiscula.'.format(v,n,l,m))
