d = float(input('Informe a distância da sua viagem em km: '))
if d <= 200:
    p = d * 0.5
    print('O custo da sua passagem será R$ {:.2f}'. format(p))
else:
    p = d * 0.45
    print('O custo da sua passagem será R$ {:.2f}'.format(p))
