peso = float(input('Seu peso: '))
altura = float(input('Sua altura: '))
imc = peso / altura ** 2
print('Seu imc é de {:.2f} e você está '.format(imc), end='')
if imc < 18.5:
    print('abaixo do peso.')
elif imc < 25:
    print('no peso ideal.')
elif imc < 30:
    print('com sobrepeso.')
elif imc < 40:
    print('com obesidade.')
else:
    print('com obesidade morbida.')
