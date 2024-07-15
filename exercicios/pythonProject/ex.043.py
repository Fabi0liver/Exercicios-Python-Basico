# Desenvolva Uma lógica que leia o peso e a altura de uma pessoa, calcule seu  IMC e mostre seu
# status de acordo com a tabela abaixo:
#Abaixo de 18.5: Anaixo do peso
#Entre 18.5 e 25: peso idial
#25 até 30: sobrepeso
#30 até 40: Obesidade
#acima de 40: obesidade mórbida


print('')
print('-' * 80)
print('                           Você sabe qual é o seu IMC?')
print('-' * 80)
print('''                  IMC é a sigla para Índice de Massa Corpórea,
Parâmetro adotado pela Organização Mundial de Saúde para calcular o peso ideal de cada pessoa.''')
print('')
print('Veja as categorias na tabela abaixo:')
print('')
print('''* Abaixo de 18.5: ABAIXO DO PESO
* De 18.5 até 25: PESO IDEAL
* De 25 até 30: SOBREPESO
* De 30 até 40: OBESIDADE
* Acima de 40: OBESIDADE MÓRBIDA''')
print('')
print('''                Sabendo disso, vamos calcular eu IMC?
                  Vou precisar só de duas coisas:''')
print('')
peso = float(input('Digite seu peso aqui: '))
print('')
altura = float(input('Agora digite sua altura aqui: '))
print('')
print('OK! Vamos agora calcura seu IMC!')
print('')
imc = peso / altura ** 2

if imc < 18.5:
    print(f'Seu IMC é {imc:.1f}! Então você está: ABAIXO DO PESO!!')
    print('É melhor você começar a se alimentar bem!!')
elif imc > 18.5 and imc <= 25:
    print(f'Seu IMC é {imc:.1f}! Então Você está com o PESO IDEAL!!')
    print('Continue assim!!')
elif imc > 25 and imc <= 30:
    print(f'Seu IMC é {imc:.1f}! Então Você está com SOBREPESO!!')
    print('É melhor começar a pratirar atividade fisicas e se alimentar melhor!')
elif imc > 30 and imc <= 40:
    print(f'Seu IMC é {imc:.1f}! Então Vocè está com OBESIDADE!!')
    print('É melhor Você procurar um médico, e cuida da sua saude!!')
else:
    print(f'Seu IMC é {imc:.1f}! Então você está com OBEDIDADE MÓRBIDA!!')
    print('PERIGO!! Seu corpo pode entrar em colapiso a qualquer momento!!')

print('')
print('-' * 80)
print('A sua saúde, e seu bem mais precioso! Então cuide bem dela!!')
print('-' * 80)



