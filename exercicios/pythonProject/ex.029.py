#Escreva um programa que leia a velocidade de uma carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado .
#A multa vai custar R$7,00 por cada km acima do limite.


v = float(input('Em que velocidade o seu carro está: '))
multa = (v - 80) * 7.00
if v > 81:
    print(f'''Você está há {v:.2f}km/h. E ultrapassou a velocidade permitida de  80km/h!'
Como infração de excesso de velocidade, você sera multado em R${multa:.2f}!''')
else:
    print(f'''Você está há {v:.2f}km/h. 
Mantenha a velocidade permitida de 80km/h!''')
