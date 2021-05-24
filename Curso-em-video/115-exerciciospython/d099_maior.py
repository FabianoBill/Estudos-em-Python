# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* prmt):
    c = max = 0
    for valor in prmt:
        if c == 0:
            max = valor
        else:
            if valor > max:
                max = valor
        c += 1
    print(max)


maior(2, 5, 8, 3, 9)
maior(1, 3, 2, 7)

print(max(3, 2, 5))