'''print('-' * 40)
print('')
for c in range(1, 10):
    print(c, end=' ')
print('Fim')

print('')
print('-' * 40)
print('')

c = 1
while c < 10:
    print(c, end=' ')
    c = c + 1
print('Fim')

print('')
print('-' * 40)
print('')

for c in range(1, 5):
    n = int(input(f'Digite o {c}º valor: '))
print('Fim')

print('')
print('-' * 40)
print('')

n = 1
while n != 0: #Vai continuar fazendo input enquanto o resposta não for 0
    n= int(input('Digite um valor: '))
print('Fim')

print('')
print('-' * 40)
print('')

r = 'S'
while r == 'S': #Vai continuar fazendo input enquanto a respota for 'S'. quando for 'N' ele para
    n1 = int(input('Digite uma  valor: '))
    r = str(input('Quer continuar? S/N: ')).upper()
print('Fim')'''

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print(f'Você digitou {par} números pares, \ne digitou {impar} números impares!!')



