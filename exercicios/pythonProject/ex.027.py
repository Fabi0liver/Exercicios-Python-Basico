# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
#e o último separadamente.

nome = str(input('Digite o nome da pessoa completo: ')).strip()
lista= nome.split()
print('')
print(f'''O nome completo é: {nome} \n
          O primeiro nome é: {lista[0]}
 o ultimo nome(sobrenome) é: {lista[-1]} ''')
