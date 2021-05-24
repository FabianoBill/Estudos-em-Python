# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

ac = 0
co = 0
for c in range(1, 7):
    n = int(input(f"Digite o {c}º número inteiro: "))
    if n % 2 == 0:
        ac += n
        co += 1
print(f"A soma dos {co} números pares escolhidos é ", ac)
