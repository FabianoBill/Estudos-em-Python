'''n = int(input('Digite um número de 0 à 9999: '))
print('Unidade: ', n%10)
print('Dezena: ', n%100//10)
print('Centena: ', n%1000//100)
print('Milhar: ', n%10000//1000)'''

n = input('Digite um número de 0 à 9999: ')
print('Unidade: ', n[3])
print('Dezena: ', n[2])
print('Centena: ', n[1])
print('Milhar: ', n[0])