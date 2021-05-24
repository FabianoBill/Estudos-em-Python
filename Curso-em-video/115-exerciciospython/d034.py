sal = float(input('Qual o valor do seu salário? R$ '))
if sal <= 1250:
    print('Seu salário com o aumento será R$ {:.2f}'.format(sal * 1.15))
else:
    print('Seu salário com aumento será R$ {:.2f}.'.format(sal * 1.1))
