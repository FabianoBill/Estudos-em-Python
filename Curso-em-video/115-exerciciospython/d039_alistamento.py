from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - ano
if idade < 18:
    alist = 18 - idade
    print('Você tem ou vai fazer {} anos, faltam {} anos para se alistar.'.format(idade, alist))
elif idade == 18:
    print('Você deve se alistar.')
else:
    alist = idade - 18
    print('Você tem ou vai fazer {} anos. Já passaram {} anos do prazo do seu alistamento.'.format(idade, alist))
