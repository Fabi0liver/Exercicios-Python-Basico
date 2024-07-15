#Crie um programa que leia duas notas de uma aluno e calcule sua média, mostrando uma mensagem no final,
#de acordo com a média atingida:
#média abaixo de 5.0: Reprovado
#média entre 5.0 e 6.9: recuperação
#média 7.0 ou superior: aprovado

print('Vamos calcular  média de notas do aluno(a)?')
print('')
n1 = float(input('Digite a primeira nota do aluno(a): '))
n2 = float(input('Digite a segunda nota do aluno(a): '))
m = (n1 + n2) / 2
print('')
if m < 5.0:
    print(f'A média deste aluno(a) é {m}, Com essa média ele(a) está: REPROVADO(A)!!')

elif (m >= 5.0) and (m <= 6.9):
    print(f'A média deste aluno(a) é {m}, Com esse média ele(a) está: RECURAÇÃO!!')

else:
    print(f'A média deste aluno(a) é {m}, com essa média ele(a) está: APROVADO(A)!!')


