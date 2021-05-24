# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input("Digite um número inteiro: "))
co = 0
for c in range(1, n + 1):
    if n % c == 0:
        co += 1
if co == 2:
    print(f"{n} é primo.")
else:
    print(f"{n} não é primo.")
