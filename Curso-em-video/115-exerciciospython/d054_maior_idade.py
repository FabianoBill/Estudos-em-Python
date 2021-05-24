# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    nasc = int(input("Em que ano você nasceu? "))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f"Temos {menor} menor(es) e {maior} maior(es). ")
