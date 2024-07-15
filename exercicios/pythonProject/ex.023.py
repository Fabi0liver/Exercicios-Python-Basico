# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# Ex: Digite um numero: 1834

#              unidade: 4
#               dezena: 3
#              centena: 8
#               milhar: 1


#n = str(input('Digite um número que esteja entre 0 e 9999: '))
#print('')
#print(f'''O número que você digitou foi {n}? \n
     #   A unidade desse número é: {n[3]}
      #   A dezena desse número é: {n[2]}
      #  A centena desse nÚmero é: {n[1]}
       #  A milhar desse número é: {n[0]}''')

num = int(input('Digite um número que esteja entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('')
print(f'''O número que você digitou foi: {num} \n
          A unidade desse número é: {u}
           A dezena desse número é: {d}
          A centena desse número é: {c}
           O milhar dessa número é: {m}''')


