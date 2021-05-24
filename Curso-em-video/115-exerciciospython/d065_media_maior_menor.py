# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

s = c = m = maior = menor = 0
cond = "S"
while cond in "Ss":
    n = int(input("Digite um número: "))
    s += n
    c += 1
    if n > maior:
        maior = n
    else:
        menor = n
    cond = input("Deseja continuar? [S/N] ").strip()[0]
m = s / c
print(f"A média dos {c} números digitados é {m}, o maior é {maior} e o menor é {menor}.")
