# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

#M = float(input('Digite a metragem :'))
#c = M * 100
#m = c * 10
#print('Sua metragem é {} metros. \nE essa metragem tem {:.0f} centímetros. \nE tem {:.0f} milímetros'.format(M, c, m))


me = float(input('Digite a medida em metros:'))
km = me/1000
hm = me/100
dam = me/10
m = me
dm = me*10
cm = me*100
mm = me* 1000
print('')
print('Uma distância em {}m, corresponde a: \n{}km \n{}hm  \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(m, km, hm, dam, dm, cm,mm))


