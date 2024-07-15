
num = [2, 5, 9, 1]
print(num) # [2, 5, 9, 1]

num[2] = 3
print(num) # [2, 5, 3, 1]

#num[4] = 7 #IndexError: list assignment index out of range
num.append(7)
print(num) # [2, 5, 3, 1, 7]

num.insert(2,0)
print(num) #[2, 5, 0, 3, 1, 7]

num.sort() #para colocar os números da lista em ordem crescente
print(num) #[0, 1, 2, 3, 5, 7]

num.sort(reverse=True) # para colocar os números da lista em ordem decrescente
print(num) # [7, 5, 3, 2, 1, 0]

print(f'Essa lista tem {len(num)} elementos.') # Essa lista tem 6 elementos.

lista = ['esmolas', 'assassinato', 'guerra', 'pinturas', 'condutor', 'ombros', 'embrulho', 'orangotango']

#lista.remove('pinturas')
#print(lista) #['esmolas', 'assassinato', 'guerra', 'condutor', 'ombros', 'embrulho', 'orangotango']

'''for c, p in enumerate(lista):
    print(f'Na posição {c} encontrei a palavra {p.upper()}!')
print('Fim da lista')

valores = []
for valor in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)

for c, valor in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {valor:2}.')
print('')
print('Fim da lista')

a = [1, 2, 6, 8]
b = a #forma errada de fazer uma copia da lista "a", 
print(f'Lista A: {a}')#Lista A: [1, 2, 6, 8]
print(f'Lista B: {b}')#Lista B: [1, 2, 6, 8]
b[2] = 8
print(f'Lista A: {a}') #Lista A: [1, 2, 8, 8] # se mudar a lista "b", muda a lista "a" tbm.
print(f'Lista B: {b}') #Lista B: [1, 2, 8, 8]'''

a = [1, 2, 6, 8]
b = a[:] # forma certa de fazer uma copia sem modificar a original
print(f'Lista A: {a}')# Lista A: [1, 2, 6, 8]
print(f'Lista B: {b}')# Lista B: [1, 2, 6, 8]
b[2] = 8
print(f'Lista A: {a}') # Lista A: [1, 2, 6, 8] # se mudar a lista "b", não muda a lista "a".
print(f'Lista B: {b}') # Lista B: [1, 2, 8, 8]



