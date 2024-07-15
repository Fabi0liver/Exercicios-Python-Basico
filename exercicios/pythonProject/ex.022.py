#crie um programa que leia o nome completo de uma pessoa e mostre:
  # O nome Com todas as Letras maiúsculas
  # O nome com todas as letras minúsculas
  # Quantas letras ao todo(sem considerar espaços)
  # Quantas letras tem o primeiro nome.


nome = str(input('Digite seu nome completo: ')).strip
lista = nome.split()
print('')
print('Vamos brincar com seu nome {}?'.format(lista[0]))
print('')
print('O seu nome completo com todas as letras maiúscuas fica: "{}"'.format(nome.upper()))
print('')
print('O Seu nome completo com todas as letras minúsculas fica: "{} "'.format(nome.lower()))
print('')
print('O seu nome completo sem espaços tem "{}" letras!'.format((len(''.join(lista)))))
print('')
print('E seu primeiro nome tem "{}" letras !'.format(len(lista[0])))


print(f'''Vamos brincar com seu nome {lista[0]}?'
         O seu nome completo com todas as letras maúsculas fica: "{nome.upper()}"
         O Seu some completo com todas as letras minúsculas fica: "{nome.lower()}"
         O seu nome completo sem espaços tem "{len(''.join(lista))}" letras!
         E seu primeiro nome  tem "{len(lista[0])}" letras!
         E se eu trocar seu primeiro nome por "José" como fica: "{nome.replace(lista[0], 'José')}"''')
