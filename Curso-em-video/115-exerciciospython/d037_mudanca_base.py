n = int(input('Digite um número inteio: '))
base = int(input('Pada mudar a base, escolha: 1 binário, 2 octal e 3 hexadecimal: '))
if base == 1:
    print(f'{n} na base 2 = {n:b}')
elif base == 2:
    print(f'{n} na base 8 = {n:o}')
else:
    print(f'{n} na bade 16 = {n:h}')

