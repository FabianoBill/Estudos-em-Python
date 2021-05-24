vel = float(input('Qual a sua velocidade em km/h? '))
if vel >= 80:
    multa = (vel - 80)*7
    print('Você ultrapassou o limite de velocidade, sua multa será de R${:.2f}'.format(multa))
