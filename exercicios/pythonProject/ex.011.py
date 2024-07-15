# Faça um programa que leia a largura ea altura de uma parede em metros,
#calcule  sua área e a quantidade de tinta necessária para pintá-lá,
#sabendo que cada litros de tinta , pinta uma área de 2m².

print('')
l = float(input('Diga a largura de sua parede:'))
a = float(input('Diga a altura de sua parede:'))
print('')
print('Sua parede tem a dimensão de {} x {}, e a sua área é de {:.2f} m². \nVocê vai precisar de aproximadamente {:.2f} litros de tinta para pintar-la.'.format(l, a, l*a, (l*a)/2))



larg = float(input('Diga a Largura de sua parede:'))
alt =float(input('Diga a altura de sua parede:'))
área = larg * alt
tinta = área / 2
print('')
print('Sua parede tem as dimenções de {} x {}, e a área é de {}m².'.format(larg, alt, área))
print('Para pinta sua parede, você vai precisar de aproximadamente {}l de tinta.'.format(tinta))
