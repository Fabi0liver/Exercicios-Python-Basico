print('')
teste = list()
teste.append('Fabio')
teste.append(33)
print(teste) #['Fabio', 33]

'''galera = list()
galera.append(teste)
print(galera) #[['Fabio', 33]]

teste[0] = 'Maria'                #forma errada
teste[1] = 65                     
galera.append(teste)
print(galera) #[['Maria', 65], ['Maria', 65]]'''

galera = list()
galera.append(teste[:])
print(galera) #[['Fabio', 33]]

teste[0] = 'Maria'
teste[1] = 65
galera.append(teste[:])
print(galera) #[['Fabio', 33], ['Maria', 65]]
print('')

irmaos = [['Fabio', 33], ['Aline', 35], ['Igor', 29], ['Matheus', 25]]
print(irmaos) #[['Fabio', 33], ['Aline', 35], ['Igor', 29], ['Matheus', 25]]
print(irmaos[0]) #['Fabio', 33]
print(irmaos[0][0]) #Fabio
print(irmaos[3]) #['Matheus', 25]
print(irmaos[2][0]) #Igor
print(irmaos[2][1]) #29
for i in irmaos:
    print(i)#['Fabio', 33]
            #['Aline', 35]
            #['Igor', 29]
            #['Matheus', 25]
print('')
for i in irmaos:
    print(i[0])#Fabio
               #Aline
               #Igor
               #Matheus
print('')
for i in irmaos:
    print(f'{i[0]:.<10}{i[1]} anos')#Fabio.....33 anos
                                    #Aline.....35 anos
                                    #Igor......29 anos
                                    #Matheus...25 anos
print('')

dados = list()
familia = list()
maior = menor = 0
for c in range(0, 9):
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite a idade: ')))
    familia.append(dados[:])
    dados.clear()
print(familia)
p = 0
for pessoa in familia:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade. Pois tem {pessoa[1]} anos de idade.')
        maior += 1
    else:
        print(f'{pessoa[0]} é mesnor de idade. Pois tem {pessoa[1]} anos de idade.')
        menor += 1
print(f'Está familia tem {maior} maiores de idade, e {menor} menores de idade.')








