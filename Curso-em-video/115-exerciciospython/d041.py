from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
if idade < 9:
    print('Mirim')
elif idade < 14:
    print('Infantil')
elif idade < 19:
    print('Júnior')
elif idade < 25:
    print('Sênior')
else:
    print('Master')
