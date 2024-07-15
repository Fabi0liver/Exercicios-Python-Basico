# Refaça o desafio 009, mostrando a tabuada de um número que o úsuárío escolher, só que agora
# utilizando um laço for.

print('=' * 30)
print('\t VAMOS FAZER TABUADA!')
print('=' * 30)
print('')
print('Vocês fala um número, e eu faço a tabuada dele! Ok?')
print('')
num = int(input('Diga um número: '))
print('')
print(f'\tA tabuada de {num} é:')
print('=' * 25)
for c in range(0, 11):
    print(f'\t {num:2} x {c:2} = {num * c}')
print('=' * 25)
print('')
print('Sou bom na matématica viu!!')






