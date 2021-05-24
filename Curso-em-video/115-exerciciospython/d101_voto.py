# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(d, m, a):
    from datetime import date
    dh = date.today().day
    mh = date.today().month
    ah = date.today().year
    if m < mh:
        i = ah - a
    elif m == mh:
        if d <= dh:
            i = ah - a
        else:
            i = ah - a - 1
    else:
        i = ah - a - 1
    if i >= 18:
        print("OBRIGATÓRIO")
    elif i >= 65 or 16 <= i < 18:
        print("OPCIONAL")
    else:
        print("NEGADO")


voto(21, 5, 2003)