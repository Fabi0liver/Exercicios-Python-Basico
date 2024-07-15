#crie um programa que leia o nome de uma cidade é diga se ela começa ou não com o nome "santo"

cidade = str(input('Digite um nome de cidade: ')).strip()
capit = cidade.capitalize()
lista = capit.split()
print('')
print('Você digitou "{}"! \nÉ "{}" que essa cidade  tem "Santo" no nome!'''.format(cidade, 'Santo' in lista[0]))

print('')
print(f'''Você digitou "{cidade}"! '
É "{'Santo' in lista[0]}" que essa cidade  tem "Santo" no nome''')


print('\n')
cid = str(input(' Digite uma cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')
