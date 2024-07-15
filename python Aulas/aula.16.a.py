
lanche = 'Hambúrguer'
print(lanche) # Hambúrguer
print('')

lanche = 'Hambúrguer'
lanche = 'Suco'
print(lanche) # suco
'''( 'Hambúrguer' estava atribuido ao  suco,
    mas como logo depois o 'Suco' foi atribuido,
 ele tomou o lugar do que estava atribuido a lanche)'''

print('')
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
#                          ou
lanche = 'Hambúrguer', 'suco', 'Pizza', 'Pudim'
print(lanche) #('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print('')
print(lanche[1]) # Suco
print(lanche[-3]) # suco
print(lanche[1:3]) # ('Suco', 'Pizza')
print(lanche[-3:-1]) # ('Suco', 'Pizza')
print(lanche[:2]) # ('Hambúrguer', 'Suco')
print(lanche[:-2]) # ('Hambúrguer', 'Suco')

'''Tuplas são imutáveis'''
#lanche[1] = 'Refrigerante'
#print(lanche[1]) #TypeError: 'tuple' object does not support item assignment'''
print('')

for comida in lanche:
    print(f'Eu vou comer {comida}!') #Eu vou comer Hambúrguer!
print('')                            #Eu vou comer suco!
                                     #Eu vou comer Pizza!
                                     #Eu vou comer Pudim!

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}!') #Eu vou comer Hambúrguer!
print('')                                  #Eu vou comer suco!
                                           #Eu vou comer Pizza!
                                           #Eu vou comer Pudim!

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}! ({comida} está na posição {pos} de lanche)')
print('')            #Eu vou comer Hambúrguer! (Hambúrguer está na posição 0 de lanche)
                     #Eu vou comer suco! (suco está na posição 1 de lanche)
                     #Eu vou comer Pizza! (Pizza está na posição 2 de lanche)
                     #Eu vou comer Pudim! (Pudim está na posição 3 de lanche)

for cont in range(len(lanche)):
    print(f'Eu vou comer {lanche[cont]}! ({lanche[cont]} está na posição {cont} de lanche)')
print('')            #Eu vou comer Hambúrguer! (Hambúrguer está na posição 0 de lanche)
                     #Eu vou comer suco! (suco está na posição 1 de lanche)
                     #Eu vou comer Pizza! (Pizza está na posição 2 de lanche)
                     #Eu vou comer Pudim! (Pudim está na posição 3 de lanche)


print(sorted(lanche)) #['Hambúrguer', 'Pizza', 'Pudim', 'suco']
'''O sorted(), coloca os elementos da tupla, em ordem e em uma "lista".'''
print('')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c) #(2, 5, 4, 5, 8, 1, 2)
d = b + a
print(d) #(5, 8, 1, 2, 2, 5, 4)
'''Tuplas é imataveis, mas podem ser juntas.'''
print('')

print(c.count(5)) # 2
'''c.count() mostra contras vezes um lementos(neste caso o "5")
           aparecem na tupla(neste caso a "c".'''
print('')

print(d) #(5, 8, 1, 2, 2, 5, 4)
print(d.index(8)) # 1
'''O .index() mostra em que posição o elemento(neste caso o "8")
        esta na tupla(neste caso a tupla "c")'''
print(d.index(5, 1))# 5
'''Neste caso mostra a posição do elemento apartir de uma posição
      (usado quando tem mais de um do mesmo número na tupla).'''
print('')

del(c)
print(c) # NameError: name 'c' is not defined
'''Embora seja impossível remover itens da tupla, é possível 
    deletá-la por completo com o uso da palavra-chave del'''














