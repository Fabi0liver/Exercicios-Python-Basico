nome = str(input('Qual é o seu nome? '))
if nome == 'Fábio':
    print('Que nome legal! ')
print(f'Bom dia, {nome}!')

print('\n')

nome1 = str(input('Qual seu nome? '))
if nome1 == 'Fábio':
    print('Gostei do seu nome!;)')
else:
    print('Que nome legal !')
print(f'Bom dia, {nome1}!')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'Sua média é: {m:.1f}')
if m >= 6.0:
    print('Sua média está boa')
else:
    print('Sua média está baixa')

print('Parabéns' if m >= 6.0 else 'Estude mais!')









