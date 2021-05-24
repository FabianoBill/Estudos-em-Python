n1 = float(input('Digite sua 1ª nota: '))
n2 = float(input('Digite sua 2ª nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Reprovado')
elif 5 <= m < 7:
    print('Recuperação')
else:
    print('Aprovado')
