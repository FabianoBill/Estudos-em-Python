n = input('Digite algo: ')
print('O tipo primitivo do que foi digitado é: ', type(n))
print('É um número?', n.isnumeric())
print('É apena alfabético?', n.isalpha())
print('É alfanumérico?', n.isalnum())
print('Está em maiúculas?', n.isupper())
print('Está capitalizado?', n.istitle())
