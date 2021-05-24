v = float(input('Valor da casa: R$'))
s = float(input('Salário: R$'))
a = int(input('Parcelado em quantos anos? '))
p = v / (12 * a)
if p <= s * 0.3:
    print('O valor da prestação mensal será de R$ \033[;31m{:.2f}.'.format(p))
else:
    print('Não será possível fazer o empréstimo.')
